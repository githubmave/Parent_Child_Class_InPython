# This is the child class of parent class of Cart
from cart import Cart
class CartOne(Cart):
    # given empty shopping cart
    def _init_(self,label, unitprice):
        super()._init_(self, label, unitprice)
# add dove soap in cart
cartOne=CartOne('Dove',39.99)
cartOne.add_to_cart(5)
    
print(f'after adding 5 Dove ,the total is {cartOne.totalPrice}')
# test the constructor
assert cartOne.label=="Dove"
assert cartOne.unitprice==39.99
# test add_to_cart function
assert cartOne.totalPrice==199.95