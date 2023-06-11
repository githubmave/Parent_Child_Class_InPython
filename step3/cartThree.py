# This is the child class of parent class of Cart
from cart import Cart
class CartThree(Cart):
    # given empty shopping cart
    def _init_(self,label, unitprice):
        super()._init_(self, label, unitprice)
    def add_sale_rate(self,rate):
        self.totalPrice=self.totalPrice+self.totalPrice*rate
        self.totalPrice=round(self.totalPrice,2)
# add dove soap in cart
cartThree=CartThree('Dove',39.99)
cartThree.add_to_cart(2)
cartThree.add_sale_rate(0.125)
print(f'after adding 2 Dove ,the total is {cartThree.totalPrice}')
# add Axe deos in cart
cartThree=CartThree('Axe',99.99)
cartThree.add_to_cart(2)
cartThree.add_sale_rate(0.125)
print(f'after adding 2 Axe ,the total is {cartThree.totalPrice}')
# test the constructor
assert cartThree.label=="Axe"
assert cartThree.unitprice==99.99
# test add_to_cart function
assert cartThree.totalPrice==314.95