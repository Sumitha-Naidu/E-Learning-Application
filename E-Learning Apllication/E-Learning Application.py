from tkinter import *
import pygame
import pyttsx3
from PIL import Image,ImageTk

pygame.init()
engine = pyttsx3.init()
root = Tk()
root.title('Alphabet Tutorial Application')
root.geometry('1425x715')
root.config(background='white')

str1 = StringVar()
str1.set('Welcome to Sumitha`s Academy!!!')
frame1 = Frame(root,bg='White')
frame1.pack(fill=BOTH)

Disp = Canvas(frame1, width=160, height=120, bg='white', bd=0)
Disp.grid(row=1,column=3)
img=ImageTk.PhotoImage(Image.open("icon.png").resize((85,62)))
image=Disp.create_image(85, 62, image=img)

img1 = ImageTk.PhotoImage(Image.open("apple.png").resize((100,100)))
def Alphabet_A():
    Disp.delete("all")
    str1.set('A for Apple')
    Disp.create_image(85,62,image=img1)
    engine.say("A for Apple")
    engine.runAndWait()
    
img2 = ImageTk.PhotoImage(Image.open("ball.png").resize((100,100)))
def Alphabet_B():
    Disp.delete("all")
    str1.set('B for Ball')
    Disp.create_image(85,62,image=img2)
    engine.say("B for Ball")
    engine.runAndWait()
    
img3 = ImageTk.PhotoImage(Image.open("cat.png").resize((100,100)))
def Alphabet_C():
    Disp.delete("all")
    str1.set('C for Cat')
    Disp.create_image(85,62,image=img3)
    engine.say("C for Cat")
    engine.runAndWait()
    
img4 = ImageTk.PhotoImage(Image.open("dog.png").resize((100,100)))
def Alphabet_D():
    Disp.delete("all")
    str1.set('D for Dog')
    Disp.create_image(85,62,image=img4)
    engine.say("D for Dog")
    engine.runAndWait()

img5 = ImageTk.PhotoImage(Image.open("elephant.png").resize((100,100)))
def Alphabet_E():
    Disp.delete("all")
    str1.set('E for Elephant')
    Disp.create_image(85,62,image=img5)
    engine.say("E for Elephant")
    engine.runAndWait()
    
img6 = ImageTk.PhotoImage(Image.open("fish.png").resize((100,100)))
def Alphabet_F():
    Disp.delete("all")
    str1.set('F for Fish')
    Disp.create_image(85,62,image=img6)
    engine.say("F for Fish")
    engine.runAndWait()
    
img7 = ImageTk.PhotoImage(Image.open("grapes.png").resize((100,100)))
def Alphabet_G():
    Disp.delete("all")
    str1.set('G for Grapes')
    Disp.create_image(85,62,image=img7)
    engine.say("G for Grapes")
    engine.runAndWait()
    
img8 = ImageTk.PhotoImage(Image.open("house.png").resize((100,100)))
def Alphabet_H():
    Disp.delete("all")
    str1.set('H for House')
    Disp.create_image(85,62,image=img8)
    engine.say("H for House")
    engine.runAndWait()
    
img9 = ImageTk.PhotoImage(Image.open("iglo.png").resize((100,100)))
def Alphabet_I():
    Disp.delete("all")
    str1.set('I for Igloo')
    Disp.create_image(85,62,image=img9)
    engine.say("I for Igloo")
    engine.runAndWait()
    
img10 = ImageTk.PhotoImage(Image.open("joker.png").resize((100,100)))
def Alphabet_J():
    Disp.delete("all")
    str1.set('J for Joker')
    Disp.create_image(85,62,image=img10)
    engine.say("J for Joker")
    engine.runAndWait()

img11 = ImageTk.PhotoImage(Image.open("kite.png").resize((100,100)))
def Alphabet_K():
    Disp.delete("all")
    str1.set('K for Kite')
    Disp.create_image(85,62,image=img11)
    engine.say("K for Kite")
    engine.runAndWait()
    
img12 = ImageTk.PhotoImage(Image.open("iglo.png").resize((100,100)))
def Alphabet_L():
    Disp.delete("all")
    str1.set('L for Lion')
    Disp.create_image(85,62,image=img12)
    engine.say("L for Lion")
    engine.runAndWait()

img13 = ImageTk.PhotoImage(Image.open("mango.png").resize((100,100)))
def Alphabet_M():
    Disp.delete("all")
    str1.set('M for Mango')
    Disp.create_image(85,62,image=img13)
    engine.say("M for Mango")
    engine.runAndWait()
    
img14 = ImageTk.PhotoImage(Image.open("nest.png").resize((100,100)))
def Alphabet_N():
    Disp.delete("all")
    str1.set('N for Nest')
    Disp.create_image(85,62,image=img14)
    engine.say("N for Nest")
    engine.runAndWait()
    
img15 = ImageTk.PhotoImage(Image.open("orange.png").resize((100,100)))
def Alphabet_O():
    Disp.delete("all")
    str1.set('O for Orange')
    Disp.create_image(85,62,image=img15)
    engine.say("O for Orange")
    engine.runAndWait()
    
img16 = ImageTk.PhotoImage(Image.open("parrot.png").resize((100,100)))
def Alphabet_P():
    Disp.delete("all")
    str1.set('P for Parrot')
    Disp.create_image(85,62,image=img16)
    engine.say("P for Parrot")
    engine.runAndWait()

img17 = ImageTk.PhotoImage(Image.open("queen.png").resize((100,100)))
def Alphabet_Q():
    Disp.delete("all")
    str1.set('Q for Queen')
    Disp.create_image(85,62,image=img17)
    engine.say("Q for Queen")
    engine.runAndWait()
    
img18 = ImageTk.PhotoImage(Image.open("rainbow.png").resize((100,100)))
def Alphabet_R():
    Disp.delete("all")
    str1.set('R for Rainbow')
    Disp.create_image(85,62,image=img18)
    engine.say("R for Rainbow")
    engine.runAndWait()
    
img19 = ImageTk.PhotoImage(Image.open("sun.png").resize((100,100)))
def Alphabet_S():
    Disp.delete("all")
    str1.set('S for Sun')
    Disp.create_image(85,62,image=img19)
    engine.say("S for Sun")
    engine.runAndWait()
    
img20 = ImageTk.PhotoImage(Image.open("tree.png").resize((100,100)))
def Alphabet_T():
    Disp.delete("all")
    str1.set('T for Tree')
    Disp.create_image(85,62,image=img20)
    engine.say("T for Tree")
    engine.runAndWait()
    
img21 = ImageTk.PhotoImage(Image.open("umbrella.png").resize((100,100)))
def Alphabet_U():
    str1.set('U for Umbrella')
    Disp.create_image(85,62,image=img21)
    engine.say("U for Umbrella")
    engine.runAndWait()
    
img22 = ImageTk.PhotoImage(Image.open("violin.png").resize((100,100)))
def Alphabet_V():
    Disp.delete("all")
    str1.set('V for Violin')
    Disp.create_image(85,62,image=img22)
    engine.say("V for Violin")
    engine.runAndWait()

img23 = ImageTk.PhotoImage(Image.open("watermelon.png").resize((100,100)))
def Alphabet_W():
    Disp.delete("all")
    str1.set('W for Watermelon')
    Disp.create_image(85,62,image=img23)
    engine.say("W for Watermelon")
    engine.runAndWait()
    
img24 = ImageTk.PhotoImage(Image.open("xmastree.png").resize((100,100)))
def Alphabet_X():
    Disp.delete("all")
    str1.set('X for X-Mas Tree')
    Disp.create_image(85,62,image=img24)
    engine.say("X for X-Mas Tree")
    engine.runAndWait()
    
img25 = ImageTk.PhotoImage(Image.open("yellow.png").resize((100,100)))
def Alphabet_Y():
    Disp.delete("all")
    str1.set('Y for Yellow')
    Disp.create_image(85,62,image=img25)
    engine.say("Y for Yellow")
    engine.runAndWait()

img26 = ImageTk.PhotoImage(Image.open("zebra.png").resize((100,100)))
def Alphabet_Z():
    Disp.delete("all")
    str1.set('Z for Zebra')
    Disp.create_image(85,62,image=img26)
    engine.say("Z for Zebra")
    engine.runAndWait()
    
img27 = ImageTk.PhotoImage(Image.open("icon.png").resize((100,100)))
def Alphabet_Clear():
    Disp.delete("all")
    str1.set('Welcome to Sumitha`s Academy!!!')
    Disp.create_image(85,62,image=img27)
    engine.say("Welcome to Sumithas Academy!!!")
    engine.runAndWait()
    
#===========Main Screen==================

Display = Entry(frame1, textvariable=str1, font=("arial",44,"bold"), bg="blue",fg="white",bd=34,width=39,justify=CENTER)
Display.grid(row=0,column=0,columnspan=7,pady=1)

btn1 = Button(frame1,pady=1,bd=4, command=Alphabet_A, font=("arial",24,"bold"),width=10,height=3,text="A",bg="orange",fg="white").grid(row=1,column=0)
btn2 = Button(frame1,pady=1,bd=4, command=Alphabet_B, font=("arial",24,"bold"),width=10,height=3,text="B",bg="orange",fg="white").grid(row=1,column=1)
btn3 = Button(frame1,pady=1,bd=4, command=Alphabet_C, font=("arial",24,"bold"),width=10,height=3,text="C",bg="orange",fg="white").grid(row=1,column=2)
btn4 = Button(frame1,pady=1,bd=4, command=Alphabet_D, font=("arial",24,"bold"),width=10,height=3,text="D",bg="orange",fg="white").grid(row=1,column=4)
btn5 = Button(frame1,pady=1,bd=4, command=Alphabet_E, font=("arial",24,"bold"),width=10,height=3,text="E",bg="orange",fg="white").grid(row=1,column=5)
btn6 = Button(frame1,pady=1,bd=4, command=Alphabet_F, font=("arial",24,"bold"),width=10,height=3,text="F",bg="orange",fg="white").grid(row=1,column=6)

btn7 = Button(frame1,pady=1,bd=4, command=Alphabet_G, font=("arial",24,"bold"),width=10,height=3,text="G",bg="orange",fg="white").grid(row=2,column=0)
btn8 = Button(frame1,pady=1,bd=4, command=Alphabet_H, font=("arial",24,"bold"),width=10,height=3,text="H",bg="blue",fg="white").grid(row=2,column=1)
btn9 = Button(frame1,pady=1,bd=4, command=Alphabet_I, font=("arial",24,"bold"),width=10,height=3,text="I",bg="blue",fg="white").grid(row=2,column=2)
btn10= Button(frame1,pady=1,bd=4, command=Alphabet_J, font=("arial",24,"bold"),width=10,height=3,text="J",bg="blue",fg="white").grid(row=2,column=3)
btn11 = Button(frame1,pady=1,bd=4, command=Alphabet_K, font=("arial",24,"bold"),width=10,height=3,text="K",bg="blue",fg="white").grid(row=2,column=4)
btn12 = Button(frame1,pady=1,bd=4, command=Alphabet_L, font=("arial",24,"bold"),width=10,height=3,text="L",bg="blue",fg="white").grid(row=2,column=5)
btn13 = Button(frame1,pady=1,bd=4, command=Alphabet_M, font=("arial",24,"bold"),width=10,height=3,text="M",bg="orange",fg="white").grid(row=2,column=6)

btn14 = Button(frame1,pady=1,bd=4, command=Alphabet_N, font=("arial",24,"bold"),width=10,height=3,text="N",bg="orange",fg="white").grid(row=3,column=0)
btn15 = Button(frame1,pady=1,bd=4, command=Alphabet_O, font=("arial",24,"bold"),width=10,height=3,text="O",bg="blue",fg="white").grid(row=3,column=1)
btn16 = Button(frame1,pady=1,bd=4, command=Alphabet_P, font=("arial",24,"bold"),width=10,height=3,text="P",bg="blue",fg="white").grid(row=3,column=2)
btn17 = Button(frame1,pady=1,bd=4, command=Alphabet_Q, font=("arial",24,"bold"),width=10,height=3,text="Q",bg="blue",fg="white").grid(row=3,column=3)
btn18 = Button(frame1,pady=1,bd=4, command=Alphabet_R, font=("arial",24,"bold"),width=10,height=3,text="R",bg="blue",fg="white").grid(row=3,column=4)
btn19 = Button(frame1,pady=1,bd=4, command=Alphabet_S, font=("arial",24,"bold"),width=10,height=3,text="S",bg="blue",fg="white").grid(row=3,column=5)
btn20 = Button(frame1,pady=1,bd=4, command=Alphabet_T, font=("arial",24,"bold"),width=10,height=3,text="T",bg="orange",fg="white").grid(row=3,column=6)

btn21 = Button(frame1,pady=1,bd=4, command=Alphabet_U, font=("arial",24,"bold"),width=10,height=3,text="U",bg="orange",fg="white").grid(row=4,column=0)
btn22 = Button(frame1,pady=1,bd=4, command=Alphabet_V, font=("arial",24,"bold"),width=10,height=3,text="V",bg="blue",fg="white").grid(row=4,column=1)
btn23 = Button(frame1,pady=1,bd=4, command=Alphabet_W, font=("arial",24,"bold"),width=10,height=3,text="W",bg="blue",fg="white").grid(row=4,column=2)
btn24 = Button(frame1,pady=1,bd=4, command=Alphabet_X, font=("arial",24,"bold"),width=10,height=3,text="X",bg="blue",fg="white").grid(row=4,column=3)
btn25 = Button(frame1,pady=1,bd=4, command=Alphabet_Y, font=("arial",24,"bold"),width=10,height=3,text="Y",bg="blue",fg="white").grid(row=4,column=4)
btn26 = Button(frame1,pady=1,bd=4, command=Alphabet_Z, font=("arial",24,"bold"),width=10,height=3,text="Z",bg="blue",fg="white").grid(row=4,column=5)
btn27 = Button(frame1,pady=1,bd=4, command=Alphabet_Clear, font=("arial",24,"bold"),width=10,height=3,text="Clear",bg="white").grid(row=4,column=6)



root.mainloop()
