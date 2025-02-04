def main():
    while True:
        date = input('Date: ')

        # Check if the input contains a '/' character
        if '/' in date:
            date_parts = date.split('/')
            if len(date_parts) == 3:
                if is_valid_date(date_parts[0], date_parts[1], date_parts[2]):
                    formatted_date = f'{date_parts[2]}-{int(date_parts[0]):02d}-{int(date_parts[1]):02d}'
                    print(formatted_date)
                    break
        else:
            month_list = [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ]
            for month in month_list:
                if month in date:
                    date_parts = date.split(' ')
                    if len(date_parts) == 3:
                        month_index = month_list.index(month) + 1
                        formatted_date = f'{date_parts[2]}-{month_index:02d}-{int(date_parts[1][:-1]):02d}'
                        print(formatted_date)
                        break
            break

def is_valid_date(month, day, year):
    try:
        month = int(month)
        day = int(day)
        year = int(year)
        if 1 <= month <= 12 and 1 <= day <= 31:
            return True
    except ValueError:
        pass
    return False

if __name__ == "__main__":
    main()