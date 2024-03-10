#Calculator
from tkinter import*

root=Tk()
root.title("Calculator")
e=Entry(root,width=45, borderwidth=5)
e.grid(row=0,column=0, columnspan=4, padx=20,pady=20)
def Button_click(n):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(n))

def Add():
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str("+"))

def Sub():
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str("-"))

def Mul():
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str("*"))

def Div():
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str("/"))

def Clr():
    e.delete(0,END)

def eq():
    
    st=e.get()
    if("+" in st):
          numbers = st.split("+")
          if (len(numbers) == 2):
              result = int(numbers[0]) + int(numbers[1])
              e.delete(0, END)
              e.insert(0, str(result))
    elif("-" in st):
        numbers = st.split("-")
        if (len(numbers) == 2):
              result = int(numbers[0]) - int(numbers[1])
              e.delete(0, END)
              e.insert(0, str(result))
    elif("*" in st):
        numbers = st.split("*")
        if (len(numbers) == 2):
              result = int(numbers[0]) * int(numbers[1])
              e.delete(0, END)
              e.insert(0, str(result))
    elif("/" in st):
        numbers = st.split("/")
        if (len(numbers) == 2):
              result = int(numbers[0]) / int(numbers[1])
              e.delete(0, END)
              e.insert(0, str(result))
    else:
        e.insert(0, str(st))

b1=Button(root,text="1",width=8, height=4, command=lambda:Button_click(1))
b2=Button(root,text="2",width=8, height=4, command=lambda:Button_click(2))
b3=Button(root,text="3",width=8, height=4, command=lambda:Button_click(3))
b4=Button(root,text="4",width=8, height=4, command=lambda:Button_click(4))
b5=Button(root,text="5",width=8, height=4, command=lambda:Button_click(5))
b6=Button(root,text="6",width=8, height=4, command=lambda:Button_click(6))
b7=Button(root,text="7",width=8, height=4, command=lambda:Button_click(7))
b8=Button(root,text="8",width=8, height=4, command=lambda:Button_click(8))
b9=Button(root,text="9",width=8, height=4, command=lambda:Button_click(9))
b0=Button(root,text="0",width=8, height=4, command=lambda:Button_click(0))
b_clr=Button(root,text="CLR", width=8, height=4, command=lambda:Clr())
b_add=Button(root,text="+", width=8, height=4, command=lambda:Add())
b_sub=Button(root,text="-", width=8, height=4, command=lambda:Sub())
b_mul=Button(root,text="*", width=8, height=4, command=lambda:Mul())
b_div=Button(root,text="/", width=8, height=4, command=lambda:Div())
b_eq=Button(root,text="=",width=8, height=4, command=lambda:eq())

b1.grid(row=1, column=0, padx=5, pady=5)
b2.grid(row=1, column=1, padx=5, pady=5)
b3.grid(row=1, column=2, padx=5, pady=5)
b_add.grid(row=1, column=3, padx=5, pady=5)

b4.grid(row=2, column=0, padx=5, pady=5)
b5.grid(row=2, column=1, padx=5, pady=5)
b6.grid(row=2, column=2, padx=5, pady=5)
b_sub.grid(row=2, column=3, padx=5, pady=5)

b7.grid(row=3, column=0, padx=5, pady=5)
b8.grid(row=3, column=1, padx=5, pady=5)
b9.grid(row=3, column=2, padx=5, pady=5)
b_mul.grid(row=3, column=3, padx=5, pady=5)

b0.grid(row=4, column=0, padx=5, pady=5)
b_clr.grid(row=4, column=1, padx=5, pady=5)
b_eq.grid(row=4, column=2, padx=5, pady=5)
b_div.grid(row=4, column=3, padx=5, pady=5)


root.mainloop()
