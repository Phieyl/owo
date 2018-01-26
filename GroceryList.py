Grocery_List = []
while True:
    variable = input('What do you want for food yo? ')
    Grocery_List.append(variable)
    if variable == ' ':
        Grocery_List.pop(len(Grocery_List)-1)
        break
for num, item in enumerate(Grocery_List):
  print(str(num+1)+':', item)
