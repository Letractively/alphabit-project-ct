from tkinter import *
import socket
from time import strftime
from threading import Thread
import shelve

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

class Agent(object):

    
    def __init__(self, number):
        self.number = number
        print('I am ' + number)
        def messageWindow(self):
# create child window
            win = Toplevel()
# display message
            message = self.number
            Label(win, text=message).pack()
# quit child window and return to root window
# the button is optional here, simply use the corner x of the child window
            Button(win, text='OK', command=win.destroy).pack()

        self.t=Thread(messageWindow(self))
    
    x = 1
    
    def sets(self,var):
        self.x=var
    def gets(self):
        print(self.x)
      
    #def run(self):
     #   t.start()
    

    
        

def read_msg():
        while True:
                sock_local = socket.socket( socket.AF_INET, socket.SOCK_DGRAM ) # UDP
                sock_local.bind( (UDP_IP_LOCAL,UDP_PORT) )
                data, addr = sock_local.recvfrom( 1024 ) # buffer size is 1024 bytes
                print("Received message:")
                print(strftime("%Y-%m-%d %H:%M:%S") + " -----> ", data)



print("==============================")
print("  Distributed Agent Platform")
print("  Version: 0.1")
print("==============================")
print("\n")
# GUI start
root = Tk()
root.title("Dispatcher")

listbox = Listbox(root)
listbox.pack()

#listbox.insert(END, "a list entry")

agent=""
agent_database=shelve.open('agents.dat')
agent_no=0
agents = []

def new_agent():
    e=""
    winA = Toplevel()
    message="Type the agents name"
    Label(winA, text=message).pack()
    entryWidget = Entry(winA)
    
    entryWidget["width"] = 50
    entryWidget.pack(side=LEFT)
    def gett():
        e=entryWidget.get()
        winA.destroy()
    Button(winA, text='OK', command=gett()).pack()

    
    
    #e = input("Agent name >")
    listbox.insert(END,e)
    agents.append(Agent(e))
    print(agents)
    

def list_sel(event):
    print(listbox.get(listbox.curselection()[0]))
    agent=listbox.get(listbox.curselection()[0])

def transfer():
    print("Tool transfated!")
    print(listbox.get(listbox.curselection()[0]))
    agent=listbox.get(listbox.curselection()[0])

    
b_t = Button(root, text="Transfer", command=transfer)
b_t.pack()

b_n = Button(root, text="New agent", command=new_agent)
b_n.pack()

#for item in ["one", "two", "three", "four"]:
#    listbox.insert(END, item)

listbox.bind("<<ListboxSelect>>", list_sel)




# GUI end
root.mainloop()
