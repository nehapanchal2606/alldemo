from tkinter import *
from cv2 import *

ci = Tk()
ci.title("Criminal Identification")
ci.geometry("1400x800")
ci.configure(bg="#202d42")

pid=0

def regFIR():
    global RGf, pid
    RGf = Frame(ci)
    RGf.pack()
    RGf.configure(bg="#202d42")

    pid = 3

    F_title = StringVar()
    F_reg_date = StringVar()
    F_cr_datetime = StringVar()
    F_cr_place = StringVar()
    F_cr_detail = StringVar()
    F_Victim_name = StringVar()
    F_victim_dob = StringVar()
    F_victim_gender = StringVar()
    F_victim_address = StringVar()
    F_cr_reg_name = StringVar()
    F_cr_reg_mno = IntVar()
    F_sus_name = StringVar()
    F_sus_dob = StringVar()
    F_sus_gender = StringVar()
    F_sus_address = StringVar()
    F_sus_photo = StringVar()
    F_sus_group = StringVar()
    F_cr_type = StringVar()
    F_cr_area = StringVar()
    F_p_station = StringVar()

    Label(RGf, bg="#202d42", text="ENTER FIR DETAILS!", fg="white", font=('arial 18 bold'), pady=15).grid(row=1,columnspan=2,pady=5)
    RGf.configure(bg="#202d42")
    lbl_ftitle = Label(RGf, bg="#202d42", fg="white", text="FIR title:", font=('arial', 14))
    lbl_ftitle.grid(row=2)
    lbl_fdate = Label(RGf, bg="#202d42", fg="white", text="FIR Registered date:", font=('arial', 14))
    lbl_fdate.grid(row=3)
    lbl_cdatetime = Label(RGf, bg="#202d42", fg="white", text="Date and time of crime:", font=('arial', 14))
    lbl_cdatetime.grid(row=4)
    lbl_cplace = Label(RGf, bg="#202d42", fg="white", text="Place of crime:", font=('arial', 14))
    lbl_cplace.grid(row=5)
    lbl_cdetails = Label(RGf, bg="#202d42", fg="white", text="Details of crime:", font=('arial', 14))
    lbl_cdetails.grid(row=6)
    lbl_vname = Label(RGf, bg="#202d42", fg="white", text="Victim's name:", font=('arial', 14))
    lbl_vname.grid(row=7)
    lbl_vdob = Label(RGf, bg="#202d42", fg="white", text="Victim's Date of Birth:", font=('arial', 14))
    lbl_vdob.grid(row=8)
    lbl_vgender = Label(RGf, bg="#202d42", fg="white", text="Victim's gender:", font=('arial', 14))
    lbl_vgender.grid(row=9)
    lbl_vaddress = Label(RGf, bg="#202d42", fg="white", text="Victim's Address:", font=('arial', 14))
    lbl_vaddress.grid(row=10)
    lbl_frgname = Label(RGf, bg="#202d42", fg="white", text="FIR Registerer's name:", font=('arial', 14))
    lbl_frgname.grid(row=11)
    lbl_frgno = Label(RGf, bg="#202d42", fg="white", text="FIR Registerrer's phone no:", font=('arial', 14))
    lbl_frgno.grid(row=12)
    lbl_sname = Label(RGf, bg="#202d42", fg="white", text="Suspect's name:", font=('arial', 14))
    lbl_sname.grid(row=13)
    lbl_sdob = Label(RGf, bg="#202d42", fg="white", text="Suspect's Date of Birth:", font=('arial', 14))
    lbl_sdob.grid(row=14)
    lbl_sgender = Label(RGf, bg="#202d42", fg="white", text="Suspect's gender:", font=('arial', 14))
    lbl_sgender.grid(row=15)
    lbl_saddress = Label(RGf, bg="#202d42", fg="white", text="Suspect's Address:", font=('arial', 14))
    lbl_saddress.grid(row=16)
    lbl_sgroup = Label(RGf, bg="#202d42", fg="white", text="How many suspects where involvede:", font=('arial', 14))
    lbl_sgroup.grid(row=17)
    lbl_ctype = Label(RGf, bg="#202d42", fg="white", text="Type of crime:", font=('arial', 14))
    lbl_ctype.grid(row=18)
    lbl_sphoto = Label(RGf, bg="#202d42", fg="white", text="Suspect's photo:", font=('arial', 14))
    lbl_sphoto.grid(row=19)
    lbl_carea = Label(RGf, bg="#202d42", fg="white", text="Area where the crime happened:", font=('arial', 14))
    lbl_carea.grid(row=20)
    lbl_pstation = Label(RGf, bg="#202d42", fg="white", text="police station name(where FIR registred):", font=('arial', 14))
    lbl_pstation.grid(row=21)

    Ftitle = Entry(RGf, font=('arial', 10), textvariable=F_title, width=30)
    Ftitle.grid(row=2, column=1)
    rdate= Entry(RGf, font=('arial', 10), textvariable=F_reg_date, width=30)
    rdate.grid(row=3, column=1)
    cdatetime= Entry(RGf, font=('arial', 10), textvariable=F_cr_datetime, width=30)
    cdatetime.grid(row=4, column=1)
    cplace= Entry(RGf, font=('arial', 10), textvariable=F_cr_place, width=30)
    cplace.grid(row=5, column=1)
    cdetail= Entry(RGf, font=('arial', 10), textvariable=F_cr_detail ,width=30)
    cdetail.grid(row=6, column=1)
    vname= Entry(RGf, font=('arial', 10), textvariable=F_Victim_name, width=30)
    vname.grid(row=7, column=1)
    vdob= Entry(RGf, font=('arial', 10), textvariable=F_victim_dob, width=30)
    vdob.grid(row=8, column=1)
    vgender= Entry(RGf, font=('arial', 10), textvariable=F_victim_gender, width=30)
    vgender.grid(row=9, column=1)
    vaddress= Entry(RGf, font=('arial', 10), textvariable=F_victim_address, width=30)
    vaddress.grid(row=10, column=1)
    crgname= Entry(RGf, font=('arial', 10), textvariable=F_cr_reg_name, width=30)
    crgname.grid(row=11, column=1)
    crgno= Entry(RGf, font=('arial', 10), textvariable=F_cr_reg_mno, width=30)
    crgno.grid(row=12, column=1)
    sname= Entry(RGf, font=('arial', 10), textvariable=F_sus_name, width=30)
    sname.grid(row=13, column=1)
    sdob= Entry(RGf, font=('arial', 10), textvariable=F_sus_dob, width=30)
    sdob.grid(row=14, column=1)
    sgender= Entry(RGf, font=('arial', 10), textvariable=F_sus_gender, width=30)
    sgender.grid(row=15, column=1)
    saddress= Entry(RGf, font=('arial', 10), textvariable=F_sus_address, width=30)
    saddress.grid(row=16, column=1)
    sgroup= Entry(RGf, font=('arial', 10), textvariable=F_sus_group, width=30)
    sgroup.grid(row=17, column=1)
    ctype= Entry(RGf, font=('arial', 10), textvariable=F_cr_type, width=30)
    ctype.grid(row=18, column=1)
    carea= Entry(RGf, font=('arial', 10), textvariable=F_cr_area, width=30)
    carea.grid(row=20, column=1)
    pstation= Entry(RGf, font=('arial', 10), textvariable=F_p_station, width=30)
    pstation.grid(row=21, column=1)

    btn_regFIR = Button(RGf, text="Register", font=('arial', 12), width=35, activeforeground="blue",
                       activebackground="yellow")
    btn_regFIR.grid(row=23, columnspan=2, pady=20)

def rgftoggle():
    if pid == 0:
        pass
    elif pid==1:
        RGu.destroy()
    elif pid==2:
        RGc.destroy()
    elif pid==3:
        RGf.destroy()
    regFIR()

def regcriminal():

    global RGc, pid
    RGc = Frame(ci)
    RGc.pack()
    RGc.configure(bg="#202d42")

    pid = 2

    Name = StringVar()
    DOB = StringVar()
    Gender = StringVar()
    Address = StringVar()
    Ctype = StringVar
    MO = StringVar()
    Adhar = IntVar()
    Photo = StringVar()

    Label(RGc, bg="#202d42", text="ENTER CRIMINAL'S DETAILS!", fg="white", font=('arial 23 bold'), pady=20).grid(row=1,columnspan=2,pady=5)
    RGc.configure(bg="#202d42")
    lbl_name = Label(RGc, bg="#202d42", fg="white", text="Name:", font=('arial', 20))
    lbl_name.grid(row=2)
    lbl_dob = Label(RGc, bg="#202d42", fg="white", text="Date Of Birth:", font=('arial', 20))
    lbl_dob.grid(row=3)
    lbl_gender = Label(RGc, bg="#202d42", fg="white", text="gender:", font=('arial', 20))
    lbl_gender.grid(row=4)
    lbl_address = Label(RGc, bg="#202d42", fg="white", text="Address:", font=('arial', 20))
    lbl_address.grid(row=5)
    lbl_ctype = Label(RGc, bg="#202d42", fg="white", text="Crime type:", font=('arial', 20))
    lbl_ctype.grid(row=6)
    lbl_mo = Label(RGc, bg="#202d42", fg="white", text="operating Method(MO):", font=('arial', 20))
    lbl_mo.grid(row=7)
    lbl_adhar = Label(RGc, bg="#202d42", fg="white", text="AdharCard Number:", font=('arial', 20))
    lbl_adhar.grid(row=8)
    lbl_photo = Label(RGc, bg="#202d42", fg="white", text="Photo:", font=('arial', 20))
    lbl_photo.grid(row=9)

    Name = Entry(RGc, font=('arial', 10), textvariable=Name, width=20)
    Name.grid(row=2, column=1)
    DOB = Entry(RGc, font=('arial', 10), textvariable=DOB, width=20)
    DOB.grid(row=3, column=1)
    Gender = Entry(RGc, font=('arial', 10), textvariable=Gender, width=20)
    Gender.grid(row=4, column=1)
    Address = Entry(RGc, font=('arial', 10), textvariable=Address, width=20)
    Address.grid(row=5, column=1)
    Ctype = Entry(RGc, font=('arial', 10), textvariable=Ctype, width=20)
    Ctype.grid(row=6, column=1)
    MO = Entry(RGc, font=('arial', 10), textvariable=MO, width=20)
    MO.grid(row=7, column=1)
    Adhar = Entry(RGc, font=('arial', 10), textvariable=Adhar, width=20)
    Adhar.grid(row=8, column=1)

    btn_rgc = Button(RGc, text="Register", font=('arial', 12), width=35, activeforeground="blue",
                       activebackground="yellow")
    btn_rgc.grid(row=10, columnspan=2, pady=20)

def rgctoggle():
    if pid==0:
        pass
    elif pid==1:
        RGu.destroy()
    elif pid==2:
        RGc.destroy()
    elif pid==3:
        RGf.destroy()

    #uh.destroy()
    regcriminal()

def user_uregister():

    global RGu, pid
    pid = 1
    RGu = Frame(ci)
    RGu.pack(side=TOP, pady=40)
    RGu.configure(bg="#202d42")



    Fname = StringVar()
    Lname = StringVar()
    Bno = IntVar()
    Post = StringVar()
    Dob = StringVar()
    Gender = StringVar()
    Email = StringVar()
    Pno = IntVar()
    Address = StringVar()
    Dtime = StringVar()
    Parea = StringVar()

    ## header ##



    ## register form ##

    Label(RGu, bg="#202d42", text="ENTER USER'S DETAILS!",fg="white", font=('arial 23 bold')).grid(row=2, columnspan=2, pady=5)
    RGu.configure(bg="#202d42")
    lbl_firstname = Label(RGu, bg="#202d42",fg="white", text="First name:", font=('arial', 20))
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RGu, bg="#202d42",fg="white", text="Last name:", font=('arial', 20))
    lbl_lastname.grid(row=4)
    lbl_batchno = Label(RGu, bg="#202d42",fg="white", text="Batch no:", font=('arial', 20))
    lbl_batchno.grid(row=5)
    lbl_post = Label(RGu, bg="#202d42",fg="white", text="post:", font=("arial", 20))
    lbl_post.grid(row=6)
    lbl_dob = Label(RGu, bg="#202d42",fg="white", text="Date of birth:", font=('arial', 20))
    lbl_dob.grid(row=7)
    lbl_gender = Label(RGu, bg="#202d42",fg="white", text="Gender:", font=('arial', 20))
    lbl_gender.grid(row=8)
    lbl_email = Label(RGu, text="Email:",fg="white", bg="#202d42", font=('arial', 20))
    lbl_email.grid(row=9)
    lbl_pno = Label(RGu, bg="#202d42",fg="white", text="Phone number:", font=('arial', 20))
    lbl_pno.grid(row=10)
    lbl_adrs = Label(RGu, bg="#202d42",fg="white", text="Residential Address:", font=('arial', 20))
    lbl_adrs.grid(row=11)
    lbl_dtime = Label(RGu, bg="#202d42",fg="white", text="Duty time:", font=('arial', 20))
    lbl_dtime.grid(row=12)
    lbl_parea = Label(RGu, bg="#202d42",fg="white", text="Posting area:", font=('arial', 20))
    lbl_parea.grid(row=13)
    lbl_photo = Label(RGu, bg="#202d42",fg="white", text="Photo:", font=('arial', 20))
    lbl_photo.grid(row=14)

    Fname = Entry(RGu, font=('arial', 10), textvariable=Fname, width=20)
    Fname.grid(row=3, column=1)
    Lname = Entry(RGu, font=('arial', 10), textvariable=Lname, width=20)
    Lname.grid(row=4, column=1)
    Batchno = Entry(RGu, font=('arial', 10), textvariable=Bno, width=20)
    Batchno.grid(row=5, column=1)
    Post = Entry(RGu, font=('arial', 10), textvariable=Post, width=20)
    Post.grid(row=6, column=1)
    Dob = Entry(RGu, font=('arial', 10), textvariable=Dob, width=20)
    Dob.grid(row=7, column=1)
    Gender = Entry(RGu, font=('arial', 10), textvariable=Gender, width=20)
    Gender.grid(row=8, column=1)
    Email = Entry(RGu, font=('arial', 10), textvariable=Email, width=20)
    Email.grid(row=9, column=1)
    Phoneno = Entry(RGu, font=('arial', 10), textvariable=Pno, width=20)
    Phoneno.grid(row=10, column=1)
    Address = Entry(RGu, font=('arial', 10), textvariable=Address, width=20)
    Address.grid(row=11, column=1)
    Dutytime = Entry(RGu, font=('arial', 10), textvariable=Dtime, width=20)
    Dutytime.grid(row=12, column=1)
    Postingarea = Entry(RGu, font=('arial', 10), textvariable=Parea, width=20)
    Postingarea.grid(row=13, column=1)


    btn_login = Button(RGu, text="Register", font=('arial', 12), width=35, activeforeground="blue",activebackground="yellow")
    btn_login.grid(row=16, columnspan=2, pady=20)

def rgutoggle():
    if pid==0:
        pass
    elif pid==1:
        RGu.destroy()
    elif pid==2:
        RGc.destroy()
    elif pid==3:
        RGf.destroy()
    #uh.destroy()
    user_uregister()

def uhome():
    global uh
    uh = Frame(ci)
    uh.pack()
    uh.configure(bg="#202d42")

    mreg = Menubutton(uh ,fg="white", text="Register", bg="#202d42", font="Arial 20")
    mreg.grid(row=1,column=1)

    mreg.menu = Menu(mreg, tearoff=0)
    mreg["menu"] = mreg.menu


    mreg.menu.add_checkbutton(label="Add user",command = rgutoggle)
    mreg.menu.add_checkbutton(label="Add FIR", command= rgftoggle)
    mreg.menu.add_checkbutton(label="Add Criminal", command = rgctoggle)

    Label(uh, text="|",font="Arial 20",bg="#202d42").grid(row=1,column=2)

    mlst = Menubutton(uh, fg="white",font="Arial 20",text="List", bg="#202d42")
    mlst.grid(row=1, column=3)

    mlst.menu = Menu(mlst, tearoff=0)
    mlst["menu"] = mlst.menu

    mlst.menu.add_checkbutton(label="User List")
    mlst.menu.add_checkbutton(label="FIR List")
    mlst.menu.add_checkbutton(label="Criminal List")

    Label(uh, text="|", font="Arial 20", bg="#202d42").grid(row=1, column=4)

    dect = Menubutton(uh, fg="white", font="Arial 20", text="Detection", bg="#202d42")
    dect.grid(row=1, column=5)

    dect.menu = Menu(dect, tearoff=0)
    dect["menu"] = dect.menu

    dect.menu.add_checkbutton(label="Face Detection")
    dect.menu.add_checkbutton(label="MO detetction")

    Label(uh, text="|",font="Arial 20",bg="#202d42").grid(row=1,column=6)
    lo = Button(uh ,fg="white", text="LOG OUT!", bg="#202d42")
    lo.grid(row=1, column=7)

def Toggleuh(event=None):
    UL.destroy()
    uhome()

def user_login():
    global UL
    UL = Frame(ci)
    UL.pack(side=TOP, pady=80)
    UL.configure(bg="#202d42")



    USERNAME = StringVar()
    PASSWORD = StringVar()


    lbl1 = Label(UL, text="Enter your details!", bg="#202d42",fg="white", font=('arial 25 bold'), bd=20)
    lbl1.grid(row=1, columnspan=2)
    lbl_username = Label(UL, text="Username:",fg="white", bg="#202d42", font=('arial', 25), bd=18)
    lbl_username.grid(row=2)
    lbl_password = Label(UL, text="Password:",fg="white", bg="#202d42", font=('arial', 25), bd=18)
    lbl_password.grid(row=3)
    lbl_reg = Label(UL, text="Register here!",bg="#202d42",fg="Blue" , font=('arial', 15), bd=18)
    lbl_reg.grid(row=4)
    lbl_result1 = Label(UL, text="", bg="#202d42", font=('arial', 18))
    lbl_result1.grid(row=5, columnspan=2)
    username = Entry(UL, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=2, column=1)
    password = Entry(UL, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)
    btn_login = Button(UL, text="Login", font=('arial', 18), width=35, activeforeground="blue",
                       activebackground="yellow" , command = Toggleuh)
    btn_login.grid(row=6, columnspan=2, pady=20)
    lbl_reg.bind('<Button-1>', ToggleToRegister)

def ToggleToLogin(event=None ):
    RG.destroy()
    user_login()


def ToggleToRegister(event=None):
    UL.destroy()
    user_register()

def user_register():
    global RG
    RG = Frame(ci)
    RG.pack(side=TOP, pady=40)
    RG.configure(bg="#202d42")


    Fname = StringVar()
    Lname = StringVar()
    Bno = IntVar()
    Post = StringVar()
    Dob = StringVar()
    Gender = StringVar()
    Email = StringVar()
    Pno = IntVar()
    password = StringVar()
    cpassword = StringVar()
    Parea = StringVar()

    Label(RG, bg="#202d42", text="ENTER YOUR DETAILS!",fg="white", font=('arial 23 bold'), pady=20).grid(row=1, columnspan=2, pady=5)
    RG.configure(bg="#202d42")
    lbl_firstname = Label(RG, bg="#202d42",fg="white", text="First name:", font=('arial', 20))
    lbl_firstname.grid(row=2)
    lbl_lastname = Label(RG, bg="#202d42",fg="white", text="Last name:", font=('arial', 20))
    lbl_lastname.grid(row=3)
    lbl_batchno = Label(RG, bg="#202d42",fg="white", text="Batch no:", font=('arial', 20))
    lbl_batchno.grid(row=4)
    lbl_post = Label(RG, bg="#202d42",fg="white", text="post:", font=("arial", 20))
    lbl_post.grid(row=5)
    lbl_dob = Label(RG, bg="#202d42",fg="white", text="Date of birth:", font=('arial', 20))
    lbl_dob.grid(row=6)
    lbl_gender = Label(RG, bg="#202d42",fg="white", text="Gender:", font=('arial', 20))
    lbl_gender.grid(row=7)
    lbl_email = Label(RG, text="Email:",fg="white", bg="#202d42", font=('arial', 20))
    lbl_email.grid(row=8)
    lbl_password = Label(RG, text="Password:", fg="white", bg="#202d42", font=('arial', 20))
    lbl_password.grid(row=9)
    lbl_cpassword = Label(RG, text="Confirm Password:", fg="white", bg="#202d42", font=('arial', 20))
    lbl_cpassword.grid(row=10)
    lbl_pno = Label(RG, bg="#202d42",fg="white", text="Phone number:", font=('arial', 20))
    lbl_pno.grid(row=11)
    lbl_parea = Label(RG, bg="#202d42",fg="white", text="Posting area:", font=('arial', 20))
    lbl_parea.grid(row=12)
    lbl_photo = Label(RG, bg="#202d42",fg="white", text="Photo:", font=('arial', 20))
    lbl_photo.grid(row=13)

    Fname = Entry(RG, font=('arial', 10), textvariable=Fname, width=20)
    Fname.grid(row=2, column=1)
    Lname = Entry(RG, font=('arial', 10), textvariable=Lname, width=20)
    Lname.grid(row=3, column=1)
    Batchno = Entry(RG, font=('arial', 10), textvariable=Bno, width=20)
    Batchno.grid(row=4, column=1)
    #Post = Entry(RG, font=('arial', 10), textvariable=Post, width=20)
    #Post.grid(row=5, column=1)

    choices = {'DSP', 'SP', 'Head Constable', 'constable'}
    Post.set('Not defined')  # set the default option

    popupMenu = OptionMenu(RG, Post, *choices,)
    popupMenu.grid(row=5, column=1)
    popupMenu.configure(font=('arial', 10), width=15)

    # on change dropdown value
    def change_dropdown(*args):
        print(Post.get())

    # link function to change dropdown
    Post.trace('w', change_dropdown)


    Dob = Entry(RG, font=('arial', 10), textvariable=Dob, width=20)
    Dob.grid(row=6, column=1)

    Gender = Entry(RG, font=('arial', 10), textvariable=Gender, width=20)
    Gender.grid(row=7, column=1)
    Email = Entry(RG, font=('arial', 10), textvariable=Email, width=20)
    Email.grid(row=8, column=1)
    password = Entry(RG, font=('arial', 10), textvariable=password, width=20)
    password.grid(row=9, column=1)
    cpassword = Entry(RG, font=('arial', 10), textvariable=cpassword, width=20)
    cpassword.grid(row=10, column=1)
    Phoneno = Entry(RG, font=('arial', 10), textvariable=Pno, width=20)
    Phoneno.grid(row=11, column=1)
    #Postingarea = Entry(RG, font=('arial', 10), textvariable=Parea, width=20)
    #Postingarea.grid(row=10, column=1)

    choices1 = {'naroda', 'maninagar', 'isckon', 'krishna nagar'}
    Parea.set('Not defined')  # set the default option

    popupMenu1 = OptionMenu(RG, Parea, *choices1)
    popupMenu1.grid(row=12, column=1)
    popupMenu1.configure(font=('arial', 10), width=15)

    # on change dropdown value
    def change_dropdown1(*args):
        print(Parea.get())

    # link function to change dropdown
    Post.trace('w', change_dropdown1)

    lbl_login = Label(RG, text="Login!", bg="#202d42", fg="Blue", font=('arial', 15))
    lbl_login.grid(row=14)
    lbl_login.bind('<Button-1>', ToggleToLogin)

    btn_reg = Button(RG, text="Register", font=('arial', 12), width=35, activeforeground="blue",
                       activebackground="yellow")
    btn_reg.grid(row=15, columnspan=2, pady=20)


def home():
    global hm
    hm = Frame(ci)
    hm.pack()
    hm.configure(bg="#202d42")

    Label(hm, text="Criminal Identification System", fg="white", bg="#202d42", font="Arial 35 bold", pady=20).pack()

    btn_frame1 = Frame(hm, bg="#202d42", pady=15)
    btn_frame1.pack()

    def ToggleL(event=None):
        hm.destroy()
        user_login()

    def ToggleR(event=None):
        hm.destroy()
        user_register()

    Button(btn_frame1, text="Login", command = ToggleL)
    Button(btn_frame1, text="Register", command = ToggleR)
    for btn in btn_frame1.winfo_children():
        btn.configure(font="Arial 15", width=17, bg="#2196f3", fg="white",pady=10, bd=0, highlightthickness=0, activebackground="#091428", activeforeground="white")
        btn.pack(pady=10)

def welcome():
    global wl
    wl= Frame(ci)
    wl.pack()
    wl.configure(bg="#202d42")
    Label(wl, text="Criminal Identification", fg="white", bg="#202d42", font="Arial 35 bold", pady=7).pack()
    logo1 = PhotoImage(file="user.png")
    lbl_p = Label(wl, image=logo1, bg="#202d42")
    lbl_p.image = logo1
    lbl_p.pack()

    btn_frame1 = Frame(wl, bg="#202d42", pady=22)
    btn_frame1.pack()

    def ToggleH(event=None):
        wl.destroy()
        home()

    Button(btn_frame1, text="let's start!" ,command = ToggleH)
    for btn in btn_frame1.winfo_children():
        btn.configure(font="Arial 15", width=17, bg="#2196f3", fg="white",pady=10, bd=0, highlightthickness=0, activebackground="#091428", activeforeground="white")
        btn.pack(pady=10)
welcome()

if __name__ == '__main__':
    ci.mainloop()