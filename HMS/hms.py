#Define the menu of resturant
menu ={
    'momo':150,
    'Pizza':200,
    'Burger':100,
    'Chowmean0':140,
    'Coffe':80,
    'Salad':70,
}


#WELCOME

print("Welcome to My Restro")
print("momo:      Rs.150\nPizza:     Rs.200\nBurger:    Rs.100\nChowmean0: Rs140\nCoffe:     Rs.80\nSalad:     Rs.70")

order_total = 0

item_1 = input("Enter the name of item you want to order :")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your Item Has Been Added To Your Order")

else:
    print(f"Ordered item {item_1} is not available now!")

aru_order = input("Do You Want To Add Another Item? : (yes/no)")

if aru_order == "yes":
    item_2 = input("Enter The Name Of Second Item :")
    if item_2 in menu:
        order_total += menu[item_2]
    else:
          print(f"Ordered item {item_2} is not available now!")  

print(f"The Total Amount of Items to pay is {order_total}")     
print("Thank You!!!!!!")      