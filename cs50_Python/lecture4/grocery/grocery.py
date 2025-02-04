def main():
    groceryList = []
    while True:
        try:
            item = input()
            groceryList += [item.upper()]
        except EOFError:
            break
    grocerySet = list(set(groceryList))
    grocerySet.sort()
    #print(grocerySet, groceryList)
    for i in range(len(grocerySet)):
        print(groceryList.count(list(grocerySet)[i]), list(grocerySet)[i])









main()
