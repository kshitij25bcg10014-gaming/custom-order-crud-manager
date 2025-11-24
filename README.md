*Customer Order CRUD Manager*
#Project Overview
	This project is a simple console-based Customer Order Manager built using Python. It allows managing customer orders with 	essential Create, Read, Update, and Delete (CRUD) operations. Orders are stored persistently in a JSON file for easy retrieval and 	modification.

#Features
	1)Add new customer orders with order ID, customer name, product, and quantity

	2)List all existing orders in a clear format

	3)Update specific order details by order ID

	4)Delete an order by its ID, with order IDs auto-adjusting after deletions

	5)Data persistence using JSON file (orders.json)

	6)Simple menu-driven interface for ease of use

#Tools
	1)Python 3.x (no external dependencies)

	2)Built-in json module

	3)Standard console I/O

#Installation and Usage
	1)Make sure Python 3 is installed on your system.

	2)Copy the project file (orders_manager.py or whatever name you give) into a folder.

	3)Open a terminal or command prompt and navigate to the project folder.

Run the project using:

	text
		**python CRUD.py**
	Use the on-screen menu to create, view, update, or delete orders.

#Testing Instructions
	1)Start by creating a few orders through the “Create order” option.

	2)Verify orders by listing all orders using the “List orders” option.

	3)Test updating any order’s details using the “Update order” option.

	4)Try deleting an order and check if the list updates correctly and IDs shift.

	5)Exit and relaunch the program to ensure all data is saved and loaded properly from orders.json.