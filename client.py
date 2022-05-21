import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1111))

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
