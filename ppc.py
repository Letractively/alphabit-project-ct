from tkinter import *
import socket
from time import strftime
from threading import Thread

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
#
# NOTICE: Before running the program please configure the port number and ip addresses
#
# Type the address of your computer
UDP_IP_LOCAL="192.168.56.1"
# Type the address of the computer you want to comunicate with
UDP_IP_REMOTE="192.168.56.130"
# This port does not work on win7 recommended is 6000, on winXP and Linux it works
UDP_PORT=5005
# -----------------------------------------------------------------------------



# A small server (listening procedure)
def read_msg():
        while True:
                sock_local = socket.socket( socket.AF_INET, socket.SOCK_DGRAM ) # UDP
                sock_local.bind( (UDP_IP_LOCAL,UDP_PORT) )
                data, addr = sock_local.recvfrom( 1024 ) # buffer size is 1024 bytes
                text.insert(INSERT,"Remote(" + strftime("%Y-%m-%d %H:%M:%S") + "):\n")
                text.insert(INSERT,data)
                text.insert(INSERT,"\n")
                print("Received message:")
                print(strftime("%Y-%m-%d %H:%M:%S") + " -----> ", data)
                text.see(END)

root = Tk()
root.title("Primitive chat client - PCC")

text = Text(root, bg="black", fg="white")

t = Thread(target=read_msg)
t.start()

text1 = Text()

text1.config(width=15, height=5)



def button1():
        text.insert(INSERT,"You(" + strftime("%Y-%m-%d %H:%M:%S") + "):\n")
        text.insert(INSERT, text1.get("0.0",END))
        # Sending the massage does not have to be in a while loop
        MESSAGE=text1.get("0.0",END)
        sock_remote = socket.socket( socket.AF_INET, socket.SOCK_DGRAM ) # UDP
        sock_remote.sendto(bytes(MESSAGE, 'UTF-8'), (UDP_IP_REMOTE, UDP_PORT))
        print(strftime("%Y-%m-%d %H:%M:%S"))
        print(MESSAGE)
        
        text1.delete("0.0",END)
        text.see(END)
        
def key_enter(event):
        print("Enter pressed!")
        if chk_var.get() != 0:
                button1()
        
        
        
text1.bind("<Return>", key_enter)            
def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)
    
    
b = Button(root, text="Send", width=10, height=2, command=button1)


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text.config(width=60, height=15)
text.pack(side=LEFT, fill=Y)
text1.pack()
chk_var=IntVar()
chk=Checkbutton(root, text='Insert text after enter has been pressed', variable=chk_var).pack(side=LEFT, padx=5)
b.pack()
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
frame = Frame(root, width=100, height=100)

frame.bind("<Button-1>", callback)
frame.pack()
text.focus_set()
print(chk_var.get())




root.mainloop()
