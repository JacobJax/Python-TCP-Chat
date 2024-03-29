import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()), 1111))
s.listen(8)

clients = []

# broadcast message
def broadcast(message):
   for client in clients:
      client.send(message)

# handle client
def handle(client):
   while True:
      try:
         message = client.recv(1024)
         broadcast(message)
      except:
         clients.remove(client)
         client.close()
         break

# receive clients
def receive():
   while True:

      # accept connection
      client, adress = s.accept()
      print(f"{adress} joined chat")

      # inform client
      clients.append(client)
      client.send("Connected to server \n".encode())

      # broadcast to all clients
      broadcast("\nAnother fag joined the chat!\n".encode())

      # create handle thread
      h_thread = threading.Thread(target=handle, args=(client,))
      h_thread.start()

print("Server is listening...")
receive()
