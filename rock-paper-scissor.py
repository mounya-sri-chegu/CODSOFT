from tkinter import *
from PIL import Image,ImageTk
from random import randint
root=Tk()
root.title("Rock-Paper-Scissor")
root.configure(background="#8ADA1D")

rock_img=ImageTk.PhotoImage(Image.open("rock-user.jpg"))
paper_img=ImageTk.PhotoImage(Image.open("paper-user.jpg"))
scissor_img=ImageTk.PhotoImage(Image.open("scissors-user.jpg"))
rock_img_comp=ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_img_comp=ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_img_comp=ImageTk.PhotoImage(Image.open("scissors.jpg"))

user_label=Label(root,image=scissor_img,bg="#8ADA1D")
comp_label=Label(root,image=scissor_img_comp,bg="#8ADA1D")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

playerscore=Label(root,text=0,font=100,bg="#8ADA1D",fg="black")
computerscore=Label(root,text=0,font=100,bg="#8ADA1D",fg="black")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

user_indicator=Label(root,font=50,text="USER",bg="#8ADA1D",fg="black")
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#8ADA1D",fg="black")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

msg=Label(root,font=50,bg="#8ADA1D",fg="black")
msg.grid(row=3,column=2)

def updatemessage(x):
    msg['text']=x

def updateuserscore():
    score=int(playerscore["text"])
    score+=1
    playerscore["text"]=str(score)

def updatecompscore():
    score=int(computerscore["text"])
    score+=1
    computerscore["text"]=str(score)

def checkwin(player,computer):
    if player==computer:
        updatemessage("Its a tie!!")
    elif player=="rock":
        if computer=="paper":
            updatemessage("you loose")
            updatecompscore()
        else:
            updatemessage("you win")
            updateuserscore()
    elif player=="paper":
        if computer=="scissor":
            updatemessage("you loose")
            updatecompscore()
        else:
            updatemessage("you win")
            updateuserscore()
    elif player=="scissor":
        if computer=="rock":
            updatemessage("you loose")
            updatecompscore()
        else:
            updatemessage("you win")
            updateuserscore()
    else:
        pass



choices=["rock","paper","scissor"]

def updateChoice(x):
    compchoice=choices[randint(0,2)]
    if compchoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif compchoice=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkwin(x,compchoice)

rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="black",command=lambda:updateChoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="black",command=lambda:updateChoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="black",command=lambda:updateChoice("scissor")).grid(row=2,column=3)

root.mainloop()
