import time
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import threading 
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Menu, simpledialog



        
    # msg1 = tkinter.Tk()
    # msg1.withdraw
    # sender = simpledialog.askstring("Pseudo","Veuillez choisir un pseudonyme", parent=msg1)
    # gui_done = False
    # running = True 




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



def set_name():  # event is passed by binders.
    """Gère la réception du nom de l'expéditeur."""
    msg = Sender.get()
    print(msg)
    client_socket.send(bytes(msg, "utf8"))


def send():
    """Gère l'envoi de messages."""
    if recipient.get() != "" and Message.get() != "":
       # msg = "@" + recipient.get() + "@" + Subject.get() + "@" + Message.get()
        msg = "@" + recipient.get() + "@"  + "@" + Message.get()
        recipient.set("")  # effacer le champ destinataire
        #Subject.set("")
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



#**************End function countdown**********************


window = tkinter.Tk()
window.title("AHKILESS")
window.configure(bg="#ffffff")
window.geometry("+450+10")  # taille et placement

champ_Conversationtion = tkinter.Frame(window)
Sender = tkinter.StringVar()  # déclarer le type du champ expéditeur
recipient = tkinter.StringVar()   # déclarer le type du champ destinataire
Subject = tkinter.StringVar()   # Déclarer le type du champ sujet
Message = tkinter.StringVar()  # Déclarer le type du champ message

#**********************************************
hourString = tkinter.StringVar()
minuteString = tkinter.StringVar()
secondString = tkinter.StringVar()

### Set strings to default value
hourString.set("00")
minuteString.set("00")
secondString.set("40")

### Get user input
hourTextbox = Entry(window, width=3, font=("Calibri", 20, ""), textvariable=hourString)
minuteTextbox = Entry(window, width=3, font=("Calibri", 20, ""), textvariable=minuteString)
secondTextbox = Entry(window, width=3, font=("Calibri", 20, ""), textvariable=secondString)

### Center textboxes
hourTextbox.place(x=170, y=180)
minuteTextbox.place(x=220, y=180)
secondTextbox.place(x=270, y=180)

#**********************************************


scrollbar = tkinter.Scrollbar(champ_Conversationtion)
scrollbar2 = tkinter.Scrollbar(champ_Conversationtion)

l_Sender = tkinter.Label(window, text="   Sender:", font="Ubuntu 14", width=11, height=2, bg="#ffffff")
l_recipient = tkinter.Label(window, text=" destinataire:", font="Ubuntu 14", width=11, height=2, bg="#ffffff")
#l_Subject = tkinter.Label(window, text="       Subject:", font="Ubuntu 14", width=11, height=2, bg="#ffffff")
l_Message = tkinter.Label(window, text="   Message:", font="Ubuntu 14", width=11, height=2, bg="#ffffff")

l_Conversation = tkinter.Label(window, text=" Conversation: ", font="Ubuntu 14", height=2, bg="#ffffff")

msg_list = tkinter.Listbox(window, height=11, width=38, font="Ubuntu 12 bold", fg="#483659", border=2,
                           yscrollcommand=scrollbar.set)

e_Sender = tkinter.Entry(window, font="Ubuntu 12 bold", fg="#483659", textvariable=Sender)
e_Sender.bind("<Return>", )
e_recipient = tkinter.Entry(window, font="Ubuntu 12 bold", fg="#483659", textvariable=recipient)
e_recipient.bind("<Return>", )
e_Subject = tkinter.Entry(window, font="verdana 12 bold", fg="#483659", textvariable=Subject)
e_Subject.bind("<Return>", )
e_Message = tkinter.Entry(window, font="Ubuntu 12 bold", fg="#483659", width=65, textvariable=Message)
e_Message.bind("<Return>", )

window.protocol("WM_DELETE_WINDOW", close)

b_Envoyer_Sender = tkinter.Button(window, text="    Envoyer    ", font="Ubuntu 14 bold", height=1, border=3,
                                    relief="groove", fg="#483659", command=set_name)
b_Envoyer = tkinter.Button(window, text="Envoyer Message", font="Ubuntu 14 bold", height=1, border=3,
                          relief="groove", fg="#483659", command=send)
b_sair = tkinter.Button(window, text="Exit", font="Ubuntu 14 bold", fg="red", border=3, relief='groove',
                        command=exit)

setTimeButton = Button(window, text='Set Time', bd='5', command=runTimer)

scrollbar.grid()
msg_list.grid(row=2, column=3)
champ_Conversationtion.grid(column=3)

l_Sender.grid(row=1, column=1, sticky="n")
l_recipient.grid(row=2, column=1)
#l_Subject.grid(row=3, column=1)
l_Message.grid(row=4, column=1)
l_Conversation.grid(row=1, column=3)

e_Sender.grid(row=1, column=2)
e_recipient.grid(row=2, column=2)
e_Subject.grid(row=3, column=2)
e_Message.grid(row=4, column=2, columnspan=6)

b_Envoyer.grid(row=5, column=2, sticky="n")
setTimeButton.grid(row=5, column=5)
b_Envoyer_Sender.grid(row=2, column=2, sticky="n")
b_sair.grid(row=5, column=3)

HOST = "localhost"
PORT = 50000
if not PORT:
    PORT = 50000
else:
    PORT = int(PORT)

ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
"""début d'exécution de l'interface"""

# def start_thread():
#     t=Thread(target=runTimer)
#     t.runTimer()
#runTimer()
window.mainloop()
