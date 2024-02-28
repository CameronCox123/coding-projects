# File: HW8
# Author: Cameron Cox
# UT EID: cpc2526
# Course: cs303E
#
# Date: 11/13/2023

# Description of program: 
# Creates 2 classes, one for items and one for a 'cart' of item objects. Then uses their functions to do some stuff

# Scource Citing:
# Looked at lecture notes. Looked online at python library. Coding Challenge 4 also helped me connect a few
# concepts and helped me get it made

import random

class ItemToPurchase:

    def __init__(self, name, price, quantity):
        """
        Initializes variables 

        :name: String. name of the item
        :price: float. the price of the item
        :quantity: the number of items
        :return: No Return
        """  
        self.name = name
        self.price = price
        self.__quantity = quantity

    def get_quantity(self):
        """
        Accesses the private variable self.__quantity to give the value to the user

        :return: int. the quantity of whatever item this method is called on
        """  
        return self.__quantity

    def set_quantity(self, newQuantity):
        """
        Replaces the quanity of a specific item with another value

        :newQuantity: the new quantity of whatever item this method is called on
        :return: No Return
        """  
        self.__quantity = newQuantity
    
    def __str__ (self):
        """
        Used to avoid weird print statements. Gives a formatted string when asked to print an item. 

        :return: String. formatted f string with all the information of an item. 
        """ 
        return (f'{self.name}: {self.__quantity} @ ${self.price:.2f} = ${self.__quantity * self.price:.2f}')
    
class ShoppingCart:

    def __init__(self, customer_ID):
        """
        Initializes variables

        :self.customer_ID: String. The ID displayed when printing out the shopping cart
        :return: No Return
        """
        self.customer_ID = customer_ID
        self.cart_items = []

    def add_item(self, item):
        """
        Adds an item (ItemToPurchase object) to cart_items list. 

        :item: Object. item added to cart_items
        :return: No Return
        """
        self.cart_items.append(item)

    def remove_item(self, item):
        """
        Removes an item (ItemToPurchase object) from cart_items list. 

        :item: Object. item removed from cart_items
        :return: No Return
        """
        self.cart_items.remove(item)

    def change_quantity(self, item, quantity):
        """
        Loops through cart_items list and finds specific item and changes the quantity. 

        :item: Object. item searched for in cart_items
        :quantity: int. the quantity that replaces the previous quantity of items.
        :return: No Return
        """
        # Makes sure we actually have the product first before changing the quantity
        for product in self.cart_items:
            if item == product:
                item.set_quantity(quantity)
    
    def print_cart(self):
        """
        Takes each object and adds it to a string before printing a formatted statement displaying the cart

        :return: No Return
        """    
        printStatement = ''    
        printStatement += (f'Shopping Cart for Customer: {self.customer_ID} \n') # Header for our final print

        # Appends a call to __str__ method for each item. __str__ displays information about each item
        for item in self.cart_items:      
            printStatement += (f'{item.__str__()} \n')

        #Calculating total price by adding each object's quantity times the price to a total
        total_price = 0
        for item in self.cart_items:      
            total_price += item.price * item.get_quantity()


        printStatement += (f'TOTAL: ${total_price:.2f}') # Ending for our final print
        print(printStatement)

def main():
    # Create our items
    first_item = ItemToPurchase('Potato Chips', 3.49, 1)
    first_item.set_quantity(2)
    second_item = ItemToPurchase('Soda', 1.50, 1)

    # the assignment asks us to comment them out but I'm gonna keep them here just in case
    # print(first_item)
    # print(second_item)

    # Create a shopping cart object and add our items
    my_shopping_cart = ShoppingCart(987654)
    my_shopping_cart.add_item(first_item)
    my_shopping_cart.add_item(second_item)


    # Printing the carts in between a few changes
    my_shopping_cart.print_cart()
    my_shopping_cart.remove_item(first_item)

    print()

    my_shopping_cart.print_cart()
    my_shopping_cart.change_quantity(second_item, 3)

    print()

    my_shopping_cart.print_cart()


if __name__ == '__main__':
    main()