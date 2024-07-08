from tkinter import*

from turtle import heading
class Qr_Generator:
    def __init__(self, root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator | Developed By sanjana and saloni")
        self.root.resizable(False,False)
        
        
        title=Label(self.root,text="   Qr Code Generator", font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1) 

        #====Employee Details window=========
        #===Variable======
        self.var_std_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_Enrollment_No=StringVar()
        self.var_Mobile_No=StringVar()

        std_Frame=Frame(self.root,bd=2,relief=RIDGE)
        std_Frame.place(x=50,y=100,width=500,height=380)

        std_title=Label(std_Frame,text="  Student Details", font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1) 

        lbl_std_code=Label(std_Frame,text="  Student ID", font=("times new roman",15,'bold'),bg='white').place(x=20,y=60) 
        lbl_name=Label(std_Frame,text="  Name", font=("times new roman",15,'bold'),bg='white').place(x=20,y=100) 
        lbl_department=Label(std_Frame,text="  Department", font=("times new roman",15,'bold'),bg='white').place(x=20,y=140) 
        lbl_Enrollment_No=Label(std_Frame,text="  Enrollment_No", font=("times new roman",15,'bold'),bg='white').place(x=20,y=180) 
        lbl_Mobile_No=Label(std_Frame,text="  Mobile_No", font=("times new roman",15,'bold'),bg='white').place(x=20,y=220) 


        txt_std_code=Entry (std_Frame, font=("times new roman", 15),textvariable=self.var_std_code, bg='lightyellow').place(x=200,y=60) 
        txt_name=Entry (std_Frame, font=("times new roman", 15),textvariable=self.var_name, bg='lightyellow').place(x=200, y=100) 
        txt_department=Entry (std_Frame, font=("times new roman", 15),textvariable=self.var_department, bg='lightyellow').place(x=200,y=140)
        txt_Enrollment_No=Entry(std_Frame, font=("times new roman", 15),textvariable=self.var_Enrollment_No, bg='lightyellow').place(x=200,y=180)  
        txt_Mobile_No=Entry(std_Frame, font=("times new roman",15),textvariable=self.var_Mobile_No,bg='lightyellow').place(x=200,y=220) 

        btn_generation=Button(std_Frame,text='QR Generation',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=180,height=30)
        btn_clear=Button(std_Frame,text='Clear',command=self.clear, font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=290,y=250,width=180,height=30)

        self.msg=''
        self.lbl_msg=Label(std_Frame,text=self.msg, font=("times new roman",20,'bold'),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1) 

        #====Employee QR Code window=========
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE)
        qr_Frame.place(x=600,y=100,width=250,height=380)

        std_title=Label(qr_Frame,text="  Student QR Code", font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1) 

        
        self.qr_code=Label(qr_Frame,text='No Qr\nAvailable',font=('times to roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)
    
    
    def clear(self):
        self.var_std_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_Enrollment_No.set('')
        self.var_Mobile_No.set('')
        self.msg=' '
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')


    def generate(self):
        if self.var_Enrollment_No.get()=='' or self.var_std_code.get()=='' or self.var_department.get()=='' or self.var_name.get()=='' or self.var_Mobile_No.get()=='':
           self.msg='All Fields are Required!!! '
           self.lbl_msg.config(text=self.msg,fg='red')
        else:
             qr_data=(f"Student ID: {self.var_std_code.get()}\nStudent Name:{self.var_name.get()}\nDepartment:{self.var_department.get()}\nEnrollment_No:{self.var_Enrollment_No.get()}\nMobile_No:{self.var_Mobile_No.get()}")
             qr_code=qrcode.make(qr_data)
            # print(qr_code)
             qr_code=resizeimage.resize_cover(qr_code,[180,180])
             qr_code.save("Student_QR/std_"+str(self.var_std_code.get())+'.png')
            #=====QR Code Image Update========
             self.im=ImageTk.PhotoImage(file="Student_QR/std_"+str(self.var_std_code.get())+'.png')
             self.qr_code.config(image=self.im)
            #======updating  Notification=========
             self.msg='QR Generated Successfully!!!'
             self.lbl_msg.config(text=self.msg,fg='green')
            
root=Tk()
obj =Qr_Generator(root)
root.mainloop()
