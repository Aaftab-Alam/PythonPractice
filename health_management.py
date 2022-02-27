def getdate():
	import datetime
	return datetime.datetime.now()
	
lock_write1=input("What do you want to do write aur retrieve?\n")
lock_write=lock_write1.lower()


name1=input("Choose one:-\nHarry\nCarry\nRohan\n")
name=name1.lower()
try:
	new_file=open(name+".txt","x")
	new_file.close()
except:
	pass


if lock_write=="write":
	f=open(name+".txt" ,"a")
	f.write("\n"+"["+str(getdate())+"]"+" "+input("\nWrite your meal\n"))
	f.close()
		
elif lock_write=="retrieve":
	try:
		f=open(name+".txt" ,"r")
		print(f.read())
		f.close()
	except Exception as e:
		print("No such directory found")

else:
	print("invalid syntax")