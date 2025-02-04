name = input('Enter a variable name: ')

result = ''

for i in range(len(name)):
    if name[i].isupper():
        result = result + '_'
        result = result + name[i].lower()
    else:
        result = result + name[i]

print(result)