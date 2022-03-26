from vidstream import *
import tkinter as tk
import socket
import threading

local_ip_adress = socket.gethostbyname(socket.gethostname())

server = StreamingServer(local_ip_adress,9999)
receiver = AudioReceiver(local_ip_adress,8888)

def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)
    t1.start()
    t2.start()
    print('erreur')


def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0),7777)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

def start_screen_sharing():
    screen_client = CameraClient(text_target_ip.get(1.0),7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()


def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0),6666)
    t5 = threading.Thread(target=audio_sender.start_stream)
    t5.start()








window = tk.Tk()
window.title("Audio call 0.0.1")
window.geometry('300x200')
label_target_ip = tk.Label(window , text="Target IP:")
label_target_ip.pack()
text_target_ip = tk.Text(window,height = 1)
text_target_ip.pack()


btn_listen = tk.Button(window , text="Start listening" , width = 50,command=start_listening)
btn_listen.pack(anchor=tk.CENTER,expand=True)

btn_camera = tk.Button(window , text="Start Video Call" , width = 50,command = start_camera_stream)
btn_camera.pack(anchor=tk.CENTER,expand=True)

btn_screen = tk.Button(window , text="Start screen sharing" , width = 50,command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER,expand=True)

btn_audio = tk.Button(window , text="Start audio call" , width = 50,command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER,expand=True)

window.mainloop ()