def main():
    menu = {
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
            }
    total = 0
    while True:
        try:
            item = input('Item:')
            item = item.title()
            cost = round(menu[item],2)
        except KeyError:
            pass
        except EOFError:
            print()
            break
        else:
            total += cost
            print(f'${total:.2f}')


main()