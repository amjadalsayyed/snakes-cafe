orders ={}
def order():
     food = input("What would you like to order ?")
     while food!='quit':    
        if food in orders:
           orders[food] +=1
           print(f"** {orders[food]} order of {food} has been added to your meal **")
           food = input("Do you want anything more ?")
        else:
           orders[food] = 1
           print(f"** {orders[food]} order of {food} has been added to your meal **")
           food = input("Do you want anything more ?")
     if food == 'quit' and len(orders) > 0:
         for x in orders:
             print(f"you have ordered {orders[x]} {x}")
       
if __name__=="__main__":
   
    print("""           **************************************
           **    Welcome to the Snakes Cafe!   **
           **    Please see our menu below.    **
           **
           ** To quit at any time, type "quit" **
           **************************************

            Appetizers
            ----------
           Wings
           Cookies
           Spring Rolls

           Entrees
           -------
           Salmon
           Steak
           Meat Tornado
           A  Literal Garden

           Desserts
           --------
           Ice Cream
           Cake
           Pie

           Drinks
           ------
           Coffee
           Tea
           Unicorn Tears""")
    answer = input("would you like to order? (yes,no)")

    if answer != 'no' and answer != 'n':
        order()
    else:
        print("You just missed the best meal of your life!")

        