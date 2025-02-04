import json
import requests
import sys
import locale

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
# print(json.dumps(response.json(), indent = 2))

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argmuent is not a number")
    else:
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        except requests.RequestsException:
            sys.exit()

        all = response.json()
        bpi = all["bpi"]
        usd = bpi["USD"]
        rate = usd["rate"]
        result = n * locale.atof(rate)
        result = "{:,.4f}".format(result)
        print(f"${result}")
