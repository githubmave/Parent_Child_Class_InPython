# This program is to process orders with shopping cart program
# This class is the parent class for the other class in this project
class Cart:
    # given empty shopping cart
    totalPrice=0
    def __init__(self,label,unitprice):
        self.label=label
        self.unitprice=unitprice
# implement add to cart action
    def add_to_cart(self,m):
        subTotal=round(self.unitprice*m,2)
        print({self.label})
        print(f'{self.unitprice} x {m}')
        print(f'subTotal = {subTotal}')
        # Cart.cartItems.append({'label':self.label,'UnitPrice':self.unitprice,'Quantity':m})
        # calculate the total price for cart items
        Cart.totalPrice=Cart.totalPrice+subTotal
        Cart.totalPrice=round(Cart.totalPrice,2)