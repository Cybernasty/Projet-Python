import time
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import threading 
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Menu, simpledialog
from PIL import Image, ImageTk
#from fonctions import *




# def set_name():
#     pass 

# def send():
#     pass
# def exit():
#     pass

def hello():
     pass

# def runTimer():
#     pass

# def receive():
#     pass

#***********************************************************************************************************************************************
#**********************************************************************************************************************************************

def receive():
    """Traite les messages entrants"""
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf8")
            msg_split = msg.split("@")
            print(msg_split)
            if len(msg_split) > 1:
                destino = msg_split[1]
                print(destino)
                if destino == Sender.get():
                    print(msg_split)
                    msg_list.insert(tkinter.END, "Sender: " + msg_split[0])
                    msg_list.insert(tkinter.END, "Subject: " + msg_split[2])
                    msg_list.insert(tkinter.END, "Message: " + msg_split[3])
                    msg_list.insert(tkinter.END, " ")

            if len(msg_split) == 1:
                msg_list.insert(tkinter.END, msg)
                print(msg)

        except OSError:  # Le client a peut-être quitté le chat.
            break

def select():
    recipient.set("")
    #l_Sender.config(text = e_listbox.get(ANCHOR))
    #recipient = e_listbox.get(ANCHOR)
    e_recipient.insert(0, e_listbox.get(ANCHOR))

    


def set_name():  # event is passed by binders.
    """Gère la réception du nom de l'expéditeur."""
    msg = Sender.get()
    print(msg)
    client_socket.send(bytes(msg, "utf8"))


def send():
    """Gère l'envoi de messages."""
    #recipient.set(e_listbox.get(ANCHOR))  # effacer le champ destinataire
    e_recipient.insert(0, e_listbox.get(ANCHOR))
    if recipient.get() != "" and Message.get() != "":
        #msg = "@" + recipient.get() + "@" + Subject.get() + "@" + Message.get()
        msg = "@" + recipient.get() + "@" + Subject.get() + "@" + Message.get()
        recipient.set("")  # effacer le champ destinataire
        Subject.set("")
        Message.set("")  # effacer le champ de message
        client_socket.send(bytes(msg, "utf8"))

def exit():
    """fermer la connexion"""
    msg = "quit"
    client_socket.send(bytes(msg, "utf8"))
    client_socket.close()
    window.quit()


def close():
    """Cette fonction est appelée lorsque la fenêtre est fermée."""
    Message.set("quit")
    send()





#**************function countdown*************************
def runTimer():
    try:
        clockTime = int(hourString.get())*3600 + int(minuteString.get())*60 + int(secondString.get())
    except:
        print("Incorrect values")

    while(clockTime > -1):
        
        totalMinutes, totalSeconds = divmod(clockTime, 60)

        totalHours = 0
        if(totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)

        hourString.set("{0:2d}".format(totalHours))
        minuteString.set("{0:2d}".format(totalMinutes))
        secondString.set("{0:2d}".format(totalSeconds))

        ### Update the interface
        window.update()
        time.sleep(1)

        ### Let the user know if the timer has expired
        if(clockTime == 0):
            messagebox.showinfo("", "Your time has expired!")
            secondString.set("40")
        clockTime -= 1


# setTimeButton = Button(window, text='Set Time', bd='5', command=runTimer)
# setTimeButton.place(relx=0.5, rely=0.5, anchor=CENTER)
# runTimer()

# receive_thread = threading.Thread(target= receive)
# receive_thread.start()
# start_thread = threading.Thread(target= runTimer)
# start_thread.start()



# #**************End function countdown**********************

#*****************************************************************************************************************************************
#*****************************************************************************************************************************************
window = tkinter.Tk()
window.title("AHKILESS")
window.configure(bg="#ffffff")
#window.geometry("+450+10")  # taille et placement
window.geometry("850x700+350+10")  # taille et placement

#declaration des variables
Sender = tkinter.StringVar()  # déclarer le type du champ expéditeur
hourString = tkinter.StringVar()
minuteString = tkinter.StringVar()
secondString = tkinter.StringVar()

Sender = tkinter.StringVar()  # déclarer le type du champ expéditeur
recipient = tkinter.StringVar()   # déclarer le type du champ destinataire
Subject = tkinter.StringVar()   # Déclarer le type du champ sujet
Message = tkinter.StringVar()  # Déclarer le type du champ message

### Set strings to default value
hourString.set("00")
minuteString.set("00")
secondString.set("40")
#affichage icon 
window.iconbitmap('logo.ico')

# create all of the main containers
top_frame = Frame(window, bg='#D58881', width=850, height=100, pady=3)
center = Frame(window, bg='#9990DA', width=850, height=40, padx=3, pady=3)
txt_frame = Frame(window, bg='#9990DA', width=850, height=45, pady=3)
btm_frame = Frame(window, bg='#9990DA', width=850, height=60, pady=3)
# affichage des container
top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
txt_frame.grid(row=3, sticky="ew")
btm_frame.grid(row=4, sticky="ew")

#create the container of the center container(frame)
ctr_left = Frame(center, bg='#9990DA', width=350, height=500)
#ctr_mid = Frame(center, bg='#9990DA', width=250, height=190, padx=3, pady=3)
ctr_right = Frame(center, bg="#9990DA", width=5000, height=190, padx=3, pady=3)
# affichage des container of the center
ctr_left.grid(row=0, column=0, sticky="ns")
#ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")



# layout all of the main containers
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)


# widget of the top_frame conyainer

# affichage de l'image
# image = Image.open("logo1.png") 
image = tkinter.PhotoImage(file="logo1.png") 
#photo = ImageTk.PhotoImage(image) 
canvas = tkinter.Canvas(top_frame, width = 80, height = 80) 
canvas.create_image(0,0, anchor = tkinter.NW, image=image)
canvas.grid(row=1, column=1)

#affichage tu titre le l'application 
l_titre = tkinter.Label(top_frame, text="AHKILESS", font="Ubuntu 25", width=11, height=2, bg="#D58881")
l_titre.grid(row=1, column=2, sticky="n")

# widget of the center_frame conyainer
# widget of the ctr_left container of center_frame conyainer
l_Sender = tkinter.Label(ctr_left, text="   Sender:", font="Ubuntu 14", width=11, height=2, fg="white", bg="#9990DA")
l_recipient = tkinter.Label(ctr_left, text=" destinataire:", font="Ubuntu 14", fg="white", width=11, height=2, bg="#9990DA")
e_Subject = tkinter.Entry(window, font="verdana 12 bold", fg="#483659", textvariable=Subject)
e_Sender = tkinter.Entry(ctr_left, font="Ubuntu 12 bold", fg="#483659", bg="#9990DA",textvariable=Sender)
e_listbox=tkinter.Listbox(ctr_left)
b_Envoyer_Sender = tkinter.Button(ctr_left, text="    Envoyer    ", font="Ubuntu 14 bold", height=1, border=3,
                                    relief="groove", fg="#483659", bg="#9990DA", command=set_name)
e_recipient = tkinter.Entry(window, font="Ubuntu 12 bold", fg="#483659",bg="#9990DA", textvariable=recipient)

### Get user input
hourTextbox = Entry(ctr_left, width=3, bg="#483659",font=("Calibri", 20, ""), textvariable=hourString)
minuteTextbox = Entry(ctr_left, width=3,bg="#483659", font=("Calibri", 20, ""), textvariable=minuteString)
secondTextbox = Entry(ctr_left, width=3,bg="#483659", font=("Calibri", 20, ""), textvariable=secondString)

# ### Center textboxes
hourTextbox.place(x=170, y=420)
minuteTextbox.place(x=220, y=420)
secondTextbox.place(x=270, y=420)


l_Sender.grid(row=1, column=1, sticky="n")
l_recipient.grid(row=3, column=1)
e_Sender.grid(row=1, column=2)
e_listbox.grid(row=4, column=2)
b_Envoyer_Sender.grid(row=2, column=2, sticky="n")

#affichage 

# widget of the ctr_right container of center_frame conyainer
scrollbar = tkinter.Scrollbar(ctr_right)
scrollbar2 = tkinter.Scrollbar(ctr_right)

msg_list = tkinter.Listbox(ctr_right, height=20, width=50, font="Ubuntu 12 bold", fg="#483659", border=2,
                        yscrollcommand=scrollbar.set)
l_Conversation = tkinter.Label(ctr_right, text=" Conversation: ", font="Ubuntu 14", height=2, bg="#9990DA")
msg_list.grid(row=2, column=3)
l_Conversation.grid(row=1, column=3)
scrollbar.grid()
champ_Conversationtion = tkinter.Frame(window)
champ_Conversationtion.grid(column=3)

window.protocol("WM_DELETE_WINDOW", close)
# widget of the txt_frame conyainer (3ime frame)
l_Message = tkinter.Label(txt_frame, text="   Message:", font="Ubuntu 14", width=11, height=2, bg="#9990DA")
l_Message.grid(row=0, column=1)
e_Message = tkinter.Entry(txt_frame, font="Ubuntu 12 bold", fg="#483659", width=40, textvariable=Message)
e_Message.grid(row=0, column=2, columnspan=6)


# widget of the btm_frame conyainer (3ime frame)

b_Envoyer = tkinter.Button(btm_frame, text="Envoyer Message", font="Ubuntu 14 bold", height=1, border=3,
                        relief="groove", fg="#483659", bg="#9990DA" ,command=send)
setTimeButton = Button(ctr_left, text='Set Time', bd='5', command=runTimer)
#b_sair = tkinter.Button(btm_frame, text="Exit", font="Ubuntu 14 bold", fg="red", border=3, relief='groove', command=exit)
                        
b_Envoyer.grid(row=0, column=1)
#setTimeButton.grid(row=5, column=2)
setTimeButton.place(x=100, y = 420)
#b_sair.grid(row=0, column=5, sticky="e")



# créer un menu
menubar = Menu(window)
# créer un sous-menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=hello)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
menubar.add_cascade(label="File", menu=filemenu)

menubar.add_command(label="A Propos", command=window.quit)
sarramenu = Menu(menubar, tearoff=0)
sarramenu.add_command(label="New", command=hello)
sarramenu.add_command(label="Open", command=hello)
sarramenu.add_command(label="Save", command=hello)
menubar.add_cascade(label="sarra", menu=sarramenu)

menubar.add_command(label="Quit!", command=exit)
menubar.add_command(label="Help", command=window.quit)
# afficher le menu
window.config(menu=menubar)

#remplir le listbox
e_listbox.insert(END,"nabil")
e_listbox.insert(END,"sarra")
e_listbox.insert(END,"meriem")


HOST = "localhost"
#HOST = '192.168.1.108'
PORT = 50000
if not PORT:
    PORT = 50000
else:
    PORT = int(PORT)

ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
#client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()

window.mainloop()
