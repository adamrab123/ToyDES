import socket
import des
import sys
from time import sleep
import library


def Main():
        host = "127.0.0.1"
        port = 5000
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        
        message = input("Enter the message you want to encrypt -> ")

        finalEncryptedMessage = library.encrypt(message)
        print("Encrypted message = " + finalEncryptedMessage)


        while message != 'q':

                library.sending()

                finalEncryptedMessage = library.encrypt(message)
            
                mySocket.send(finalEncryptedMessage.encode())
                data = mySocket.recv(1024).decode()
                print("Received from server = " + data)
                
                decryptedMessage = library.decrypt(data)

                if not data:
                        break
                print ("Decrypted Message = " + str(decryptedMessage))

                print("\n")
                 
                message = input("Enter the message you want to encrypt -> ")

                finalEncryptedMessage = library.encrypt(message)
                print("Encrypted message = " + finalEncryptedMessage)
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
