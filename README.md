# Parent_Child_Class_InPython
OOP methodology:  identify common features pattern, and make them "Parent class", all Child classes inherit all methods of parents





Version number of this submission: 72cf4fe47f85c39779267d0ecee07655a354e623


Requirements for running my code:

•	Editor:  VSCode
•	Runtime: > Python3.8

	
How to run cartThree.py


Open VSCode:
    
	1. Go to File /     Open Folder, browser to find: ShoppingCard
	2. Go to Terminal / New Terminal
	3. Create python virtual environment: > python3 -m even env (press enter)
										 env>Scripts/Activate  (press enter)
										 
	3. run cartThree.py 
	> python cartThree.py (press enter)

Output file:

•	bytecode file after interpreting code: _pycache
•	virtual environment folder: env
•	unit test has been included in cartThree.py, unit test starts with "assert...", 
•	test contructor and every function
•	Successful Output  screen dump file:  StepThree-OutPut-SreenDump.doc
  
 Code design following OOP methodology :
   
•	The idea of OOP programming is to reuse code. 
  	Parent class: Cart
	Child class:  CartOne, CartTwo, CartThree

o	Therefore, I create Class Cart for parent class

o	parent class : Class Cart
o	function: add_to_cart
	
	Then in Step three, class cartThree can initialize an instance of Cart (parent class), in which inherit  add_to_cart function
	Step three also initialize Class Cart to inherit the add_to_cart, 
	
	In the above design pattern, the property and methods of Class Cart  can be reused in its child classes

