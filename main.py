import data

def main():
	print("Welcome to the data management system")
	print("1. Add data")
	print("2. Read data")
	print("3. Update data")
	print("4. Delete data")
	print("5. Display all data")
	print("6. Reset data")
	print("7. Exit")
	while True:
		choice = input("Enter your choice: ")
		if choice == "1":
			data.add_data()
		elif choice == "2":
			data.read_data()
		elif choice == "3":
			data.update_data()
		elif choice == "4":
			data.delete_data()
		elif choice == "5":
			data.displayall()
		elif choice == "6":
			data.data_reset()
		elif choice == "7":
			print("Thank you for using the data management system")
			break
		else:
			print("Invalid choice")


main()
