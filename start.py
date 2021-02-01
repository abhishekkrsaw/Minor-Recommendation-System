from tkinter import *
from tkinter import messagebox

def about():
    msg['text']='''Minors which is offered to you are:\n\n 1. Machine Learning \n 2. Data Science\n 3. Cyber Security
 4. Mean Stack Development\n 5. Software Methodology & Testing'''
    msg['bg']='saddle brown'
    msg['fg']='white'

def connection():
    window.destroy()
    import quiz
window=Tk()
window.configure(background='lemon chiffon')
window.title('Minor Recommendation')
window.geometry('1000x680')
frame1=Frame(window)
frame1.pack()
label1=Label(window,text='Minor Recommendation System',font=('forte',30,'underline'),bg='white',fg='purple')
label1.place(x=0,y=0,relwidth=1,height=190)
img=PhotoImage(file='2.png')
img=img.subsample(3)
img1=PhotoImage(file='3.png')
img1=img1.subsample(3)
label2=Label(window,image=img,bg='white')
label2.place(x=100,y=0)
label3=Label(window,image=img1,bg='white')
label3.place(x=800,y=0)

msg1=Label(window, text="Welcome to Minor Recommendation System !!",
          font=('times new roman',17,'bold'),fg='black',bg='yellow')
msg1.place(x=0,y=190,relwidth=1)

about=Button(window,text='Available Minors',font=('arial',10),activebackground='brown',
             cursor='hand2',command=about)
about.place(x=175,y=320,height=60,width=320)

msg=Label(window,text='We are here to help you with\n minor selection !!!!',
            bg='light cyan',fg='green',font=('arial',15),justify='left')
msg.place(x=620,y=221,height=456,width=380)

conn=Button(window,text='Start Your Journey',font=('arial',10),activebackground='red',
             cursor='hand2',command=connection)
conn.place(x=160,y=420,height=80,width=350)
