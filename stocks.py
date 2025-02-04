# source 
# https://medium.com/@albertoglvz25/predicting-stock-prices-with-an-lstm-model-in-python-26c7377b8ecb#:~:text=In%20the%20realm%20of%20financial,for%20predicting%20financial%20time%20series.
# https://medium.com/@deepml1818/implementing-time-series-stock-price-prediction-with-lstm-and-yfinance-in-python-a769a3fe9a7b

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import yfinance as yf   # For retreiving stock data
import pandas as pd     # For data manipulation
import numpy as np      # For numerical computations
import matplotlib.pyplot as plt     # For plotting graphs
from sklearn.preprocessing import MinMaxScaler      # For normalizing data
from sklearn.metrics import  mean_squared_error     # For mesauring the model's performance 
from tensorflow.keras.models import Sequential      # For defining a neural network model
from tensorflow.keras.layers import Dense, LSTM, Input, Dropout     # For adjusting the neural network
from tensorflow.keras.callbacks import EarlyStopping        # For stopping training if performance degrades
from easygui import * 


# Function to create the dataset for LSTM
# Returns an array of input features and target values
def create_lstm_data(data, time_step = 1):
    X, Y = [], []
    for i in range(len(data) - time_step - 1):
        a = data[i:(i+time_step), 0]
        X.append(a)
        Y.append(data[i + time_step, 0])
    return np.array(X), np.array(Y)




if __name__ == '__main__':
    
    fields = ["Stock Name Abbreviation", " Start Date(YYYY-MM-DD)", "End Date(YYYY-MM-DD)"]
  
    user_input = multenterbox("Enter the details below:", 
                              "Stock Prediction Input",
                              fields)
 
    if user_input:
        stock_name = user_input[0]
        start_date = user_input[1]
        end_date = user_input[2]
    else:
        print("Error")
    #Download Data
    #stock_name = input('Enter the abbreviation of the Stock you want the prediction of: ')  # Get the stock name
    #start_date = "2020-01-01"   # Set start date
    #end_date = "2023-01-01"     # Set end date
    stock = yf.download (str(stock_name), start_date, end_date) # Retrieves Stock data

    #print(stock)
    # Preprocessing data
    data = stock.copy()     # Creates a copy of the stock  
    data = data.reset_index()   # Resets the index to ensure that 'Date' is a column
    data['Date'] = pd.to_datetime(data['Date']) # Convert 'Date' to datetime format
    data.set_index('Date', inplace = True)  # Set 'Date' as the index
    data = data['Close'].to_frame()    # Keep only the 'Close' column
    #print(data)

    scaler = MinMaxScaler(feature_range = (0,1))    # Initalizes the MinMaxScaler for normalization
    close_prices_scaled = scaler.fit_transform(data)    # Scales the data 
    #print(data)
    
    
    # Split data intot train and test sets
    training_size = int(len(close_prices_scaled) * 0.7) # Defines the size of training and test sets
    train_data, test_data = close_prices_scaled[:training_size], close_prices_scaled[training_size:]   # Splits the data into training and test sets 
    
    # Prepare data for LSTM
    time_steps = 25     # Sets the number of time steps for LSTM
    x_train, y_train = create_lstm_data(train_data, time_steps)     # Creates trainng data with time steps
    x_test, y_test = create_lstm_data(test_data, time_steps)        # Creates test data with time steps

    x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], 1)    # Reshapes x_train to the shape requried by LSTM (samples, tim_steps, features)
    x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1)        # Same for x_test
    
    # Build the LSTM
    model = Sequential()    # Initializes the Sequential model
    model.add(Input(shape = (time_steps, 1)))   # Adds an Input layer
    model.add(LSTM(units = 50, return_sequences = True))   # Adds an LSTM layer with 50 units
    model.add(LSTM(units = 50, return_sequences = False))
    #model.add(Dropout(0.3))     # Add a Dropout layer with a 30% dropuout rate to reduce overfitting
    model.add(Dense(units = 50))
    model.add(Dense(units = 1))     # Adds a Dense layer with 1 unit to predict next value
    
    # Compile the model
    #optimizer = Adam(learning_rate = 0.001)
    model.compile(optimizer = 'adam', loss = 'mean_squared_error')
    
    
    #early_stopping = EarlyStopping(monitor = 'val_loss', patience = 10, restore_best_weights = True)     # Defines early stopping to prevent overfitting
    
    # Train the model
    model.fit(x_train, y_train, epochs = 100, batch_size = 4, validation_data = (x_test, y_test))   #, callbacks = [early_stopping]
    
    # Make predictions
    train_predict = model.predict(x_train)      # Prediction on training data
    test_predict = model.predict(x_test)        # Prediction on testing data


    # Invert scaling to get original values
    train_predict = scaler.inverse_transform(train_predict)
    y_train = scaler.inverse_transform(y_train.reshape(-1,1))
    test_predict = scaler.inverse_transform(test_predict)
    y_test = scaler.inverse_transform(y_test.reshape(-1,1,))
        
        
       
    # Calculates and prints MSE for training data
    train_mse = mean_squared_error(y_train, train_predict)
    print(f"Train MSE: {train_mse}")

    # Calculates and prints MSE for testing data    
    test_mse = mean_squared_error(y_test, test_predict)
    print(f'Test MSE: {test_mse}')
    
    # Visualize the Data
    plt.figure(figsize=(12,6))
    
    # Plot Actual Stock Prices
    plt.plot(data.index, data['Close'], label = 'Actual Stock Prices', color = 'blue')
    
    # PLot Training Predicted Stock Price
    train_plot = np.empty_like(data)
    train_plot[:] = np.nan
    train_plot[time_steps:len(train_predict) + time_steps] = train_predict
    
    # Plot Test Predictions
    test_plot = np.empty_like(data)
    test_plot[:] = np.nan
    shift = len(train_predict) + (time_steps * 2)
    test_plot[shift:shift + len(test_predict)] = test_predict
    
    # PLot training and test predictions
    plt.plot(data.index, train_plot, label = 'Train Predictions')
    plt.plot(data.index, test_plot, label = 'test Predictions')
    
    # Sets parameter for the Graph 
    plt.title(f'LSTM Predictions vs Actual Prices for {stock_name}')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend(loc = 'best')
    plt.show()
 
    
    # Calculate the Fourier Transform and plot 
    data_FT = data[['Close']]
    close_fft = np.fft.fft(np.asarray(data_FT['Close'].tolist()))
    fft_df = pd.DataFrame({'fft':close_fft})
    fft_df['absolute'] = fft_df['fft'].apply(lambda x: np.abs(x))
    fft_df['angle'] = fft_df['fft'].apply(lambda x: np.angle(x))
    
    
    # Plot the Fourier Transform
    plt.figure(figsize = (14, 7))
    plt.plot(np.asarray(data_FT['Close'].tolist()), label = 'Real')
    for num_ in [3, 6, 9]:
        fft_list_m10 = np.copy(close_fft); fft_list_m10[num_:-num_] = 0
        plt.plot(np.fft.ifft(fft_list_m10), label = f'Fourier transform with {num_} components')
    
    plt.xlabel('Days')
    plt.ylabel('USD')
    plt.title('Fourier transforms')
    plt.legend()
    plt.show()

   
    
    
    
    
    