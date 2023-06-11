# This is the child class of parent class of Cart
from cart import Cart
class CartTwo(Cart):
    # given empty shopping cart
    def _init_(self,label, unitprice):
        super()._init_(self, label, unitprice)
        
# add dove soap in cart
cartTwo=CartTwo('Dove',39.99)
# test the constructor
assert cartTwo.label=="Dove"
assert cartTwo.unitprice==39.99
cartTwo.add_to_cart(5)
# test add_to_cart function
assert cartTwo.totalPrice==199.95
print(f'after adding 5 Dove ,the total is {cartTwo.totalPrice}')
# add 3 more dove soaps to carts
cartTwo.add_to_cart(3)
print(f'after adding 3 more Dove ,the total is {cartTwo.totalPrice}')

