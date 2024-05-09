import json
import time
from time import sleep

# data_reset function


def data_reset():
	data= {}
	with open("data.json",'w') as file:
		file.write('{}')
		sleep(1)
		print("Data reset sucefully")



# add_data function


def add_data():
	with open("data.json",'r') as file:
		data = json.load(file)
		Key = input("Key: ")
		Val = input("Val: ")
		if (Key in data) or (Val in data):
			sleep(2)
			print("Key or value already exists")
			return
		else:
			data[Key] = Val
			with open("data.json",'w') as file:
				json.dump(data,file,indent=4)
				sleep(2)
				print("Data added Suceessfully")



# read_data function


def read_data():
	with open("data.json",'r') as file:
		data = json.load(file)
		key = input("key: ")
		if key in data:
			sleep(2)
			print(data[key])
		else:
			sleep(2)
			print("Key not found")


# update_data function


def update_data():
	with open("data.json",'r') as file:
		data = json.load(file)
		key = input("key: ")
		if key in data:
			val = input("val: ")
			data[key] = val
			with open("data.json",'w') as file:
				json.dump(data,file,indent=4)
				sleep(2)
				print("Data updated Suceessfully")
		else:
			sleep(2)
			print("Key not found")


def displayall():
	with open("data.json",'r') as file:
		data = json.load(file)
		for key,val in data.items():
			print(key,":",val)
		if data == {}:
			print("No data found")


# delete_data function


def delete_data():
	with open("data.json",'r') as file:
		data = json.load(file)
		key = input("key: ")
		if key in data:
			del data[key]
			with open("data.json",'w') as file:
				json.dump(data,file,indent=4)
				sleep(2)
				print("Data deleted Suceessfully")
		else:
			sleep(2)
			print("Key not found")
