from tkinter import *
import sqlite3
import time
import datetime
import random
from tkinter import messagebox
import subprocess as s
from datetime import date 

class Application():
    
    def __init__(self, master):
        self.master=master


        #heading for the main window
        self.heading = Label(master, text="Welcome to Hospital Managment System", font=('arial 40 bold'), bg='#49E3CE')
        self.heading.place(x=25, y=0)

        self.bottom = Label(master, text="DEVELOPED BY ZKP", font=('arial 7 '), bg='#49E3CE')
        self.bottom.place(x=480, y=500)
 
      
        #button to perform
        self.appoinment = Button(master, text="Patients", width=20, height=3, command=self.patient, bg='#3D6DEE',font=('arial 15 bold')).place(x=400, y=100)
        
        
        self.doctor = Button(master, text="Doctors", width=20, height=3, command=self.doctor, bg='#1DC550',font=('arial 15 bold')).place(x=400, y=200)
        
        self.staff = Button(master, text="Staffs", width=20, height=3,command=self.staff,  bg='#EE3D3D',font=('arial 15 bold')).place(x=400, y=300)






       
    def patient(self):
        class Stan(Text):
            def __init__(self, fram):
                Text.__init__(self, fram)
                self.hd = Label(fram, text="Patient", font=('arial 25 bold'), fg='steelblue')
                self.hd.place(x=0, y=0)

                        
                self.name = Label(fram, text="Name ", font=('arial 15'))
                self.name.place(x=0, y=60)

                self.address = Label(fram, text="Address", font=('arial 15'))
                self.address.place(x=0, y=100)

                self.phone = Label(fram, text="Mobile Number", font=('arial 15'))
                self.phone.place(x=0, y=140)                   
                self.diseases = Label(fram, text="Diseases", font=('arial 15 '))
                self.diseases.place(x=0, y=180)                                

                self.issue = time.strftime("%x")
                self.date_1 = date.today()
                self.end_date = datetime.datetime.now().time()


                self.dla = Label(fram, text=("Apoinment Date: " + "                        "+ str(self.date_1)), font=('arial 15'))
                self.dla.place(x=0, y=220)

                                            
                self.end = Label(fram, text=("Apoinment Time: " +"                     " +str(self.end_date)), font=('arial 15'))
                self.end.place(x=0, y=260)
                        
                self.email = Label(fram, text="Email Address", font=('arial 15'))
                self.email.place(x=0, y=300)
                
                
                

                
                
                
                
                
                
                
                self.name2 = Entry(fram, width=30)
                self.name2.place(x=280, y=60)
                self.address2 = Entry(fram, width=30)
                self.address2.place(x=280, y=100)
                self.phone2 = Entry(fram, width=30)
                self.phone2.place(x=280, y=180)
                self.diseases2 = Entry(fram, width=30)
                self.diseases2.place(x=280, y=140)
                self.email2 = Entry(fram, width=30)
                self.email2.place(x=280, y=300)
                
                        #button to make issue right

                self.iss = Button(fram, text="Add", width=20, height=2, command=self.issues, bg='#1DC550').place(x=0, y=340)
                self.xt = Button(fram, text="Exit", width=20, height=2, command=fram.destroy, bg='#EE3D3D').place(x=400, y=340)
                self.search = Button(fram, text="search", width=20, height=2,command=self.search_root,  bg='#1DC550').place(x=200, y=340)

                self.box = Text(fram, height=15, width=45)
                self.box.place(x=550, y=60)
                
                
               
                    
            def issues(self):
                self.name3 = self.name2.get()
                self.address3 = self.address2.get()
                self.phone3 = self.phone2.get()
                self.diseases3= self.diseases2.get()
                self.email3 = self.email2.get()
                
                if self.name3 == '' or self.address3 == '' or self.phone3 == '' or self.diseases3 == '' :
                    messagebox.showwarning("Error", "Please Fill The Missing Boxes")
                else:
                    c.execute("CREATE TABLE IF NOT EXISTS patient(name TEXT, address TEXT, mobile TEXT, diseases TEXT, email TEXT)")
                    c.execute("INSERT INTO patient (name,address, mobile, diseases, email) VALUES (?, ?,?, ?, ?)",(self.name3,self.address3,self.phone3,self.diseases3, self.email3))
                    conn.commit()
                    self.box.insert(END, ('Successfuly Added '+'\n'+'Name: ' +self.name3 +'\n'+'Address: '+ self.address3 +'\n' +'Mobile Number: '+ self.diseases3 +'\n' +'Deseases: '  +self.phone3+'\n'+'Email: '+self.email3))
                    messagebox.showinfo("Success", "Successfully added to the database")
            
            
            def search_root(self):
                class Search(Text):
                    def __init__(self, faster):
                        Text.__init__(self, faster)

                #labels for window
                        self.heading = Label(faster, text="Search patient name", font=('arial 25 bold'), bg='#F0AE59')
                        self.heading.place(x=0, y=0)
                        
                        self.name = Label(faster, text="Patient ", bg='#F0AE59')
                        self.name.place(x=0, y=60)
        
                        #self.entrybox
        
                        self.ent = Entry(faster, width=30)
                        self.ent.place(x=150, y=60)
        
                        self.sbox = Text(faster, height=15, width=60, bg="white")
                        self.sbox.place(x=50, y=130)
                        self.sbox.focus_set()
        


                #button to perform search
                        self.bt = Button(faster,text="Search",command=self.get_it ,width=20, height=2, bg='#3D6DEE')
                        self.bt.place(x=390, y=50)
        
                        
        
                        #button to quit
                        self.qt = Button(faster,text="Exit",command=faster.destroy ,width=20, height=2, bg='#EE3D3D').place(x=600, y=350)
        
                   	#destroy button
                    def master_exit(self):
                    	master.destroy()
                    
                    #button to book books
        
                    

                    def get_it(self):
            
                        conn = sqlite3.connect('hospital.db')
                        c = conn.cursor()                
                        c.execute("CREATE TABLE IF NOT EXISTS patient(name TEXT, address TEXT, mobile TEXT, diseases TEXT, email TEXT)")
                        free = self.ent.get()
                        full_proof = '%' + free + '%'
                        c.execute("SELECT * FROM patient WHERE name LIKE ?", (free,))
                            #data = c.fetchall()
                            #print(data)
                        for self.row in c.fetchall():
                                if self.row == None:
                                    messagebox.showinfo("Not Found", "Sorry, No such name found.")
                                    self.sbox.insert(END, "No Such name found in the database.")
                                else:
            
                                    self.sbox.insert(END, ('Name:'+self.row[0] +"\n"+'Address:'+ self.row[1]) +"\n"+'Mobile Number:'+self.row[3]+'\n'+'Diseases:'+self.row[2]+'\n'+'Email:'+ self.row[4] )
                            #dynamic_data_entry()
                        c.close
                        conn.close()


                window = Tk()
                window.geometry('900x400')
                window.resizable(False, False)
                window.config(background='#F0AE59')
                c = Search(window)
                window.mainloop()

            
                        
                

        dw = Tk()
        dw.geometry('1100x600')
        dw.resizable(False, False)
                
        d= Stan(dw)
        dw.mainloop()
        
        
        
        
    def doctor(self):
        class Stan(Text):
            def __init__(self, fram):
                Text.__init__(self, fram)
                self.hd = Label(fram, text="Doctor", font=('arial 25 bold'), fg='steelblue')
                self.hd.place(x=0, y=0)

                        
                self.name = Label(fram, text="Name ", font=('arial 15'))
                self.name.place(x=0, y=60)

                self.address = Label(fram, text="Address", font=('arial 15'))
                self.address.place(x=0, y=100)

                self.phone = Label(fram, text="Mobile Number", font=('arial 15'))
                self.phone.place(x=0, y=140)                   
                self.specialist = Label(fram, text="Specialist", font=('arial 15'))
                self.specialist.place(x=0, y=180)  
                
                self.email = Label(fram, text="Email Address", font=('aial 15'))
                self.email.place(x=0, y=300)

                       
                self.name2 = Entry(fram, width=30)
                self.name2.place(x=280, y=60)
                self.address2= Entry(fram, width=30)
                self.address2.place(x=280, y=100)
                self.phone2= Entry(fram, width=30)
                self.phone2.place(x=280, y=140)
                self.specialist2= Entry(fram, width=30)
                self.specialist2.place(x=280, y=180)
                
                self.email2 = Entry(fram, width=30)
                self.email2.place(x=280, y=300)
                self.issue = time.strftime("%x")
                self.date_1 = date.today()
                self.end_date = datetime.datetime.now().time()


                self.dla = Label(fram, text=("Apoinment Date: " + "                        "+ str(self.date_1)), font=('arial 15'))
                self.dla.place(x=0, y=220)

                                            
                self.end = Label(fram, text=("Apoinment Time: " +"                     " +str(self.end_date)), font=('arial 15'))
                self.end.place(x=0, y=260)
                        

                self.iss = Button(fram, text="Add", width=20, height=2, command=self.issues, bg='#1DC550').place(x=0, y=340)
                self.xt = Button(fram, text="Exit", width=20, height=2, command=fram.destroy, bg='#EE3D3D').place(x=400, y=340)
                self.search = Button(fram, text="search", width=20, height=2,command=self.search_root,  bg='#1DC550').place(x=200, y=340)

                self.mty = Text(fram, height=15, width=45)
                self.mty.place(x=550, y=60)

                    
            def issues(self):
                self.name3 = self.name2.get()
                self.address3 = self.address2.get()
                self.phone3= self.phone2.get()
                self.specialist3= self.specialist2.get()
                self.email3= self.email2.get()
                if self.name3 == '' or self.address3 == '' or self.phone3 == '' or self.specialist3 == '' :
                    messagebox.showwarning("Error", "Please Fill The Missing Boxes")
                else:
                     c.execute("CREATE TABLE IF NOT EXISTS doctor(name TEXT, address TEXT, mobile TEXT, specialist TEXT, email TEXT)")
                     c.execute("INSERT INTO doctor (name,address, mobile, specialist, email) VALUES (?, ?,?, ?, ?)",(self.name3,self.address3,self.phone3,self.specialist3, self.email3))
                     conn.commit()
                     self.mty.insert(END, ('Successfuly Added ' +self.name3.upper()+'\n'  ))
                    
                     messagebox.showinfo("Success", "Successfully added to the database")

            
            
            
            
            
            def search_root(self):
                class Search(Text):
                    def __init__(self, faster):
                        Text.__init__(self, faster)

                #labels for window
                        self.heading = Label(faster, text="Search doctor name:", font=('arial 25 bold'), bg='#F0AE59')
                        self.heading.place(x=0, y=0)
                        
                        self.name = Label(faster, text="Doctor ", bg='#F0AE59')
                        self.name.place(x=0, y=60)
        
                        #self.entrybox
        
                        self.ent = Entry(faster, width=30)
                        self.ent.place(x=150, y=60)
        
                        self.sbox = Text(faster, height=15, width=60, bg="white")
                        self.sbox.place(x=50, y=130)
                        self.sbox.focus_set()
        


                #button to perform search
                        self.bt = Button(faster,text="Search",command=self.get_it ,width=20, height=2, bg='#3D6DEE')
                        self.bt.place(x=390, y=50)
        
                       
                        #button to quit
                        self.qt = Button(faster,text="Exit",command=faster.destroy ,width=20, height=2, bg='#EE3D3D').place(x=600, y=300)
        
                   	#destroy button
                    def master_exit(self):
                    	master.destroy()
                    
                    #button to book books
        
                    

                    def get_it(self):
            
                        conn = sqlite3.connect('hospital.db')
                        c = conn.cursor()                
                        c.execute("CREATE TABLE IF NOT EXISTS doctor(name TEXT, address TEXT, mobile TEXT, specialist TEXT, email TEXT)")
                        free = self.ent.get()
                        full_proof = '%' + free + '%'
                        c.execute("SELECT * FROM doctor WHERE name LIKE ?", (free,))
                            #data = c.fetchall()
                            #print(data)
                        for self.row in c.fetchall():
                                if self.row == None:
                                    messagebox.showinfo("Not Found", "Sorry, No name found.")
                                    self.sbox.insert(END, "No Such name found in the database.")
                                else:
            
                                    self.sbox.insert(END, ('Name:'+self.row[0] +"\n"+'Address:'+ self.row[1]) +"\n" +'Mobile Number:'+ self.row[2]+'\n'+'Specialist:'+self.row[3]+'\n'+'Email:'+self.row[4] )
                            #dynamic_data_entry()
                        c.close
                        conn.close()


                window = Tk()
                window.geometry('900x400')
                window.resizable(False, False)
                window.config(background='#F0AE59')
                c = Search(window)
                window.mainloop()

            
                        
                

        dw = Tk()
        dw.geometry('1100x600')
        dw.resizable(False, False)
                
        d= Stan(dw)
        dw.mainloop()
        
                         

        
        
        
    def staff(self):
        class Stan(Text):
            def __init__(self, fram):
                Text.__init__(self, fram)
                self.hd = Label(fram, text="Staff", font=('arial 25 bold'), fg='steelblue')
                self.hd.place(x=0, y=0)

                        
                self.name = Label(fram, text="Name ", font=('arial 15'))
                self.name.place(x=0, y=60)

                self.address = Label(fram, text="Address", font=('arial 15'))
                self.address.place(x=0, y=100)

                self.phone= Label(fram, text="Mobile Number", font=('arial 15'))
                self.phone.place(x=0, y=140)                   
                self.post = Label(fram, text="Post", font=('arial 15 '))
                self.post.place(x=0, y=180)                                

                
                self.email = Label(fram, text="Email Address", font=('aial 15'))
                self.email.place(x=0, y=300)
                self.issue = time.strftime("%x")
                self.date_1 = date.today()
                self.end_date = datetime.datetime.now().time()


                self.dla = Label(fram, text=("Apoinment Date: " + "                        "+ str(self.date_1)), font=('arial 15'))
                self.dla.place(x=0, y=220)

                                            
                self.end = Label(fram, text=("Apoinment Time: " +"                     " +str(self.end_date)), font=('arial 15'))
                self.end.place(x=0, y=260)
                        
                self.name2= Entry(fram, width=30)
                self.name2.place(x=280, y=60)
                self.address2 = Entry(fram, width=30)
                self.address2.place(x=280, y=100)
                self.phone2 = Entry(fram, width=30)
                self.phone2.place(x=280, y=180)
                self.post2= Entry(fram, width=30)
                self.post2.place(x=280, y=140)
                self.email2 = Entry(fram, width=30)
                self.email2.place(x=280, y=300)

                        

                self.iss = Button(fram, text="Add", width=20, height=2, command=self.issues, bg='#1DC550').place(x=0, y=340)
                self.xt = Button(fram, text="Exit", width=20, height=2, command=fram.destroy, bg='#EE3D3D').place(x=400, y=340)
                self.search = Button(fram, text="search", width=20, height=2,command=self.search_root,  bg='#1DC550').place(x=200, y=340)

                self.mty = Text(fram, height=15, width=45)
                self.mty.place(x=550, y=60)

                    
            def issues(self):
                self.name3 = self.name2.get()
                self.address3 = self.address2.get()
                self.phone3= self.phone2.get()
                self.post3= self.post2.get()
                self.email3= self.email2.get()
                if self.name3 == '' or self.address3 == '' or self.phone3 == '' or self.post3 == '' :
                    messagebox.showwarning("Error", "Please Fill The Missing Boxes")
                else:

                     c.execute("CREATE TABLE IF NOT EXISTS staffs(name TEXT, address TEXT, mobile TEXT, post TEXT, email TEXT)")
                     c.execute("INSERT INTO staffs (name,address, mobile, post, email) VALUES (?, ?,?, ?, ?)",(self.name3,self.address3,self.phone3,self.post3, self.email3))
                     conn.commit()
                     self.mty.insert(END, ('Successfuly Added ' +self.name3.upper()+'\n'  ))
                     messagebox.showinfo("Success", "Successfully added to the database")


            



            def search_root(self):
                class Search(Text):
                    def __init__(self, faster):
                        Text.__init__(self, faster)

                #labels for window
                        self.heading = Label(faster, text="Search staff name:", font=('arial 25 bold'), bg='#F0AE59')
                        self.heading.place(x=0, y=0)
                        
                        self.name = Label(faster, text="Staff ", bg='#F0AE59')
                        self.name.place(x=0, y=60)
        
                        #self.entrybox
        
                        self.ent = Entry(faster, width=30)
                        self.ent.place(x=150, y=60)
        
                        self.sbox = Text(faster, height=15, width=60, bg="white")
                        self.sbox.place(x=50, y=130)
                        self.sbox.focus_set()
        


                #button to perform search
                        self.bt = Button(faster,text="Search",command=self.get_it ,width=20, height=2, bg='#3D6DEE')
                        self.bt.place(x=390, y=50)
        
                        
        
                        #button to quit
                        self.qt = Button(faster,text="Exit",command=faster.destroy ,width=20, height=2, bg='#EE3D3D').place(x=600, y=300)
        
                   	#destroy button
                    def master_exit(self):
                    	master.destroy()
                    
                    #button to book books
        
                    

                    def get_it(self):
            
                        conn = sqlite3.connect('hospital.db')
                        c = conn.cursor()                
                        c.execute("CREATE TABLE IF NOT EXISTS staffs(name TEXT, address TEXT, mobile TEXT, post TEXT, email TEXT)")
                        free = self.ent.get()
                        full_proof = '%' + free + '%'
                        c.execute("SELECT * FROM staffs WHERE name LIKE ?", (free,))
                            #data = c.fetchall()
                            #print(data)
                        for self.row in c.fetchall():
                                if self.row == None:
                                    messagebox.showinfo("Not Found", "Sorry, No name found.")
                                    self.sbox.insert(END, "No Such name found in the database.")
                                else:
            
                                    self.sbox.insert(END, ('Name:'+self.row[0] +"\n"+'Address:'+ self.row[1]) +"\n" +'Mobile Number:'+ self.row[3]+'\n'+'Post:'+self.row[2]+'\n'+'Email:'+self.row[4] )
                            #dynamic_data_entry()
                        c.close
                        conn.close()


                window = Tk()
                window.geometry('900x400')
                window.resizable(False, False)
                window.config(background='#F0AE59')
                c = Search(window)
                window.mainloop()

            
                        
                

        dw = Tk()
        dw.geometry('1100x600')
        dw.resizable(False, False)
                
        d= Stan(dw)
        dw.mainloop()
        

              
        
    global conn
    global c   
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()        
    
    
    

root = Tk()
root.geometry('1100x600')
root.resizable(True, True)
root.config(background='#49E3CE')

b = Application(root)
root.mainloop()
