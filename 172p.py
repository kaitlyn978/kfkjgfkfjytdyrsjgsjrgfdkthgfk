from tkinter import*
root=Tk()
root.title("username")
root.geometry("600x600")
u=Label(root,text="Username: ")
u.place(relx=0.3,rely=0.5,anchor=CENTER)
eu=Entry(root)
eu.place(relx=0.9,rely=0.5,anchor=CENTER)
l2=Label(root,text="Email Id: ")
l2.place(relx=0.3,rely=0.2,anchor=CENTER)
le=Entry(root)
le.place(relx=0.9,rely=0.2,anchor=CENTER)
l=Label(root)
dictionary={}
class Users():
    def addUser():
        global dictionary
        dictionary[key]=value
        l["text"]=dictionary
class getUser():
    def gg():
        root.mainloop()
        e=eu.get()
        ee=le.get()
        Users.addUsers(e,ee)
users=getUser()
btn=Button(root,text="add user details",command=users.gg)
btn.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()
        
