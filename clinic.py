from tkinter import *
space=Tk()
space.title("*Clinic Roj*")
space.geometry("600x400")
space.resizable(width=False, height=False)
Label(space, text="کلینیک فوق تخصصی", font=("thoma",20),bg="green",fg="white").pack()
Label(space, text=":اسم خود را وارد کنید").pack()
name=Entry(space)
name.pack()
def sing():
    welcom.config(text="*به کلینیک روژ خوش آمدید*")
sing=Button(space, text="ورود",font=("thoma",10),activebackground="green",activeforeground="white",bd=5, command=sing)
sing.pack()
welcom=Label(space,text="")
welcom.pack()
def time():
    welcom.config(text="لطفاً سر ساعت تشریف بیاورید.")
time_var=IntVar()
Checkbutton(space, text="16:00", variable=time_var).pack()
def time():
    welcom.config(text="لطفاً سر ساعت تشریف بیاورید.")
time_var=IntVar()
Checkbutton(space, text="16:00", variable=time_var).pack()
Button(space, text="رزرو", command=time).pack()
space.mainloop()