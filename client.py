from dotenv import load_dotenv
import os
import socket
import threading

load_dotenv()

HOST = os.getenv("HOST_IP")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, 1111))

call_sign = input("CALL SIGN: ")

def receive():
   while True:
      try:
         message = client.recv(1024)
         print(message.decode())
      except:
         print("An error ocurred!")
         client.close()
         break

def send():
   while True:
      message = f"{call_sign}: {input('')}"
      client.send(message.encode())

recv_thread = threading.Thread(target=send)
recv_thread.start()

send_thread = threading.Thread(target=receive)
send_thread.start()
