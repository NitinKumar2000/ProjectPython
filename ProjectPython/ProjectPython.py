
import PySimpleGUI as sg
import pymongo
from random import randint

#database
NITIN = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = NITIN["VRCARD"]
mycol = mydb["student"]
mycol2= mydb["Card"]

#function for the Credit card  window 
def Credit():
    layout1 = [[sg.Image(r'C:\Users\nitin\Desktop\ProjectPython\ProjectPython\W.png')],
          [sg.Text('Welcome to CPCM students Virtual Credit  Account    '+student_id)],
           [sg.Text('Click on credit to get your Credit Card Number')],
          [sg.Button('Credit')]
           ]
    win1 = sg.Window(' Welcome CPCM vertual Account', layout1)
    win2_active=False
    while True:
        ev1, vals1 = win1.read(timeout=1000)
        if ev1 == sg.WIN_CLOSED :
              break
          ### function for random credit card numbers
        def random_with_N_digits(n):    
                range_start = 10**(n-1)
                range_end = (10**n)-1
                return randint(range_start, range_end)
        
           
        random = random_with_N_digits(12)
        mydict = { "StudentId": student_id,"Credit Card Number ":random}
        y = mycol2.insert_one(mydict)

        if ev1 == 'Credit'  and not win2_active:
            win2_active = True
            win1.Hide()
            
            mydoc = mycol2.find(mydict)
            for x in mydoc:
                if x is not None:
                    pass
            z=str(random)                                      
            layout2 = [[sg.Text('Your randomly genrated credit card number is '+z)],    ##will be different every time and stored in database   
                       
                       [sg.Button('Show Balance'),sg.Button('Reload the Card'),sg.Button('Exit')]]

            
           

                



            win2 = sg.Window('Window 2', layout2)
            while True:
                ev2, vals2 = win2.read()
                if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
                    win2.close()
                    win2_active = False
                    win1.UnHide()
                    break
                elif ev2=='Show Balance':
                    sg.popup('Your Initial Bamance is  $5')
                elif ev2=='Reload the Card' :  
                     sg.popup('Please Contact school admisnistrative survices')
    
    
    




# Project   


sg.theme('DarkAmber')  

layout1 = [[sg.Image(r'C:\Users\nitin\Desktop\ProjectPython\ProjectPython\download.png')],
          [sg.Text('Welcome to CPCM students Vertual Credit  Account')],
          [sg.Button('Login'),sg.Button('Signup')],
           ]

win1 = sg.Window('CPCM vertual Account', layout1)










win2_active=False
while True:
    ev1, vals1 = win1.read(timeout=10000)
    if ev1 == sg.WIN_CLOSED:
        break
    

    if ev1 == 'Signup'  and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Welcome to the Signup Page')],       # note must create a layout from scratch every time. No reuse
                   [sg.Text('First Name', size=(15, 1)),sg.Input()],
                   [sg.Text('Last Name', size=(15, 1)),sg.Input()],
                   [sg.Text('Student Id', size=(15, 1)),sg.Input()],
                   [sg.Text('Phone Number', size=(15, 1)),sg.Input()],
                   [sg.Text('Address', size=(15, 1)),sg.Input()],
                   [sg.Text('Password', size=(15, 1)),sg.Input()],


                   [sg.Button('Signup'),sg.Button('Exit')]]
        
                            

        win2 = sg.Window('Signup', layout2)
        while True:
            ev2, vals2 = win2.read()
           
            first_name = vals2[0] 
            last_name = vals2[1] 
            student_id = vals2[2] 
            phoneNumber = vals2[3] 
            address= vals2[4] 
            Password = vals2[5]

            if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
                     win2.close()   
                     win2_active = False
                     win1.UnHide()
                     break
             
            elif first_name=="" or last_name==""or student_id=="" or phoneNumber=="" or address=="" or Password=="":
                    sg.popup("All Feilds are recquired")
            else:

                if ev2 =='Signup':
               
                
                    mydict = { "First name ": first_name, "Last name": last_name,"Student ID":student_id,"phone number":phoneNumber,"Address":address,"password":Password }
                    x = mycol.insert_one(mydict)
                    sg.popup(first_name,'You are now successfully registered in our student credit card service')
                
                                     
                
           
                

    
            
    elif ev1 == 'Login'  and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Welcome to the Login Page')],       # note must create a layout from scratch every time. No reuse
                   
                   [sg.Text('Student Id', size=(15, 1)),sg.Input()],
                   
                   
                   [sg.Text('password', size=(15, 1)),sg.Input()],


                   [sg.Button('Login'),sg.Button('Exit')]]

        win2 = sg.Window('Login', layout2)
        while True:
            ev2, vals2 = win2.read()
            if ev2 =='Login':
                student_id= vals2[0] 
                Password= vals2[1] 
                if student_id=="" or Password=="":
                    sg.popup("please enter Your student id and password")
                    
                    global s
                    s=student_id
                    
                else:
                    mydict = { "Student ID":student_id,"password":Password }

                    mydoc = mycol.find(mydict)

                    for x in mydoc:
                        if x is not None:
                            Credit()
                            break
                
                    else :  
                            sg.popup("sorry Id and Password doesn't match")
                
                                     
            elif ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
                 win2.close()   
                 win2_active = False
                 win1.UnHide()
                 break



