from tkinter import *


#Window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Login Signup')

signupButton = Button(tkWindow, text="Signup" ).grid(row=4, column=1)
loginButton = Button(tkWindow, text="Login").grid(row=4, column=0)

tkWindow.mainloop()









import pymongo



print("Enter name")
name = input()
print("Enter Programm")
Programm = input()

print("Enter City")
City = input()

mydict = { "Student_name ": name, "programm": Programm,"City":City  }





print("Select C to insert, U to update, R to read, D to Delete")

func = input()



if func=="C":
    
    x = mycol.insert_one(mydict)

elif func=="U":
    
   
    print("Enter name")
    name = input()
    print("Enter Programm")
    Programm = input()

    print("Enter City")
    City = input()

    newValue={  "$set":{"Student_name ": name, "programm": Programm,"City":City  }}
    x = mycol.update_one(mydict,newValue)

elif func=="R":
     
     for x in mycol.find({},{ "_id": 0, "name": input('enter the student name you are looking for '), "address": 1  }):
         print(x)

elif func=="D":

    print("Enter the student name you want to delete")
    name = input()
    myquery = { "name": name }
    x = mycol.delete_many(myquery)

else:
    print('Wrong .. ')
    

