import socket
import des
import library

def Main():
    host = "127.0.0.1"
    port = 5000
     
    mySocket = socket.socket()
    mySocket.bind((host,port))

    print("Waiting for connection.....")
     
    mySocket.listen(2)

    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))

    
    while True:
            data = conn.recv(1024).decode()
            
            print("Received from client = " + data)
            
            decryptedMessage = library.decrypt(data)

            if not data:
                    break
            print ("Decrypted Message = " + str(decryptedMessage))

            print("\n")
            
            message = input("Enter the message you want to encrypt -> ")
            finalEncryptedMessage = library.encrypt(message)
            print("Encrypted message = " + finalEncryptedMessage)

            library.sending()
            conn.send(finalEncryptedMessage.encode())

             
    conn.close()
     
if __name__ == '__main__':
    Main()





