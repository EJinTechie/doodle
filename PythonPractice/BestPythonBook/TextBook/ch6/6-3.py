#1
menu={'Americano' : 3000, 'Cappuccino': 3500,'Cafe Latte':4000 , 'Espresso':3600}
print(f"Americano Price :{menu['Americano']}")
print(f"Cappuccino Price :{menu['Cappuccino']}")
print(f"Cafe Latte Price :{menu['Cafe Latte']}")
print(f"Espresso Price :{menu['Espresso']}")
print('\n')

#2
menu1=input("choose from above menu : ")
price=menu[menu1]
print(f"{menu1} is {price}. To go?")