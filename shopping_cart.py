# shopping_cart.py
import os
import datetime #to display the date and time on the receipt

import dotenv 
dotenv.load_dotenv()  #setting up an environment variable

tax = os.getenv("TAX_RATE", default=0.0875) #defining a variable relating to the environment variable

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

#print(products)
print("Enter every item with its identifier. Once done, type the word done in all lowercase.")
total_price= 0 #setting up a variable for price
id_list= []
purchased_products= [] #establishing a list to store the product identifiers in
now= datetime.datetime.now() #defining a variable to display the date and time
#user inputs
for x in products:
    id_list.append(str(x["id"])) #to create a current list of all product ID's in the system for data validation purposes
while True:
    selected_id= input("Please input a product identifier: ")
    if selected_id == "done":
        break #escaping the loop once cashier is done
    elif selected_id in id_list:
        purchased_products.append(selected_id)
    else: #dealing with invalid inputs
        print("Make sure you have a valid identifier, and try again!") 


#printing the receipt

print("---------------------------------")
print("McDonough Store of Buyables")
print("www.mcdonoughstore.com")
print("---------------------------------")
print("Checkout at:", now.strftime("%Y-%m-%d %I:%M %p")) #current date and time
print("---------------------------------")
print("Selected Products:")

for selected_id in purchased_products:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)] #making sure that the data types are the same
    matching_product = matching_products[0]
    total_price= total_price + matching_product["price"] #iteratively adding the total price
    print("+", matching_product["name"] + " ... " + (str(to_usd(matching_product["price"]))))

print("---------------------------------")
print("Subtotal:", to_usd(total_price))
print ("Tax:", to_usd(total_price*float(tax))) #using the environment variable to have a flexible tax rate
print("Total Price:", to_usd(total_price*(1+float(tax))))
print("---------------------------------")
print("Thank you, have a great day!")
print("---------------------------------")