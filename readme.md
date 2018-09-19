# Toy DES Implementation for CSCI 4230

This simplified DES implementation works on 8-bit blocks and uses a 10-bit key, with 2 rounds used for it's encryption.

This implementation is not "secure" with respect to current standards, but demonstrates the core logic and algorithms behind DES.

### The Code

This code was written in Python 3. There are 4 Python files in this repository:

* des.py: this file contains the DES class which runs our Toy DES implementation and can encrypt and descrypt an 8-bit message inputted
* library.py: this file contains the macro functions for maintaining the interactions between the user and the DES class (e.g. turning user input into blocks that can be passed into the DES class, and converting ascii to binary (and back)).
* server.py: this file sets up the server for sending information back and forth between two users. The server will also serve as one of the users, and will have the capability of decrypting incoming messages that are encrypted, as well as encrypting messages before sending them back.
* client.py: this file will connect to the server created by server.py and will serve as a user that can communicate with the user from server.py.

### Running The Code

First you must cd in the DES folder

To run the code, first run the server.py file 

```
python server.py
```

The code declares the host IP and port with the following two lines:

> host = "127.0.0.1"
> port = 5000

These can be changed to any value.

**NOTE: these must match across server.py and client.py**

The code will display the following in the terminal until a user connects:

> "Waiting for connection....." 

Now, run the client.py file

```
python client.py
```

This will display the following in the terminal for client.py:

> Enter the message you want to encrypt -> 



The terminal for server.py will now show the following:

> Connection from: ('127.0.0.1', 54008)

The IP and the address will vary depending on the user.

### Using The Server And DES

Now that you have set up the server and client, you can start encrypting messages and sending them back and forth.

In the terminal of the client, just as you are prompted, you can enter a message you want to send to the server. Type it in and press ENTER. The terminal will now display the encrypted message in binary and then send the message to the server.

In the terminal of the server, you will now see the encrypted incoming message as well as the decrypted message. You now have the option to also send a message back and have it encrypted. Type it in and press ENTER. The terminal will now display the encrypted message in binary and then send the message to the client.

This back-and-forth communication can continue forever, allowing encrypted communication between the client user and server user.

### How The Code Works

The server.py file and client.py files both make calls to the imported DES class in des.py. Before sending the messages across the TCP connection, the following steps are taken to encrypt the message:

1. The message (ASCII) is converted into binary
2. The binary is converted into 8 bit blocks
3. Each 8-bit chunk is encrypted using the DES class
4. Each encrypted 8-bit chunk is then concatenated into one long message

This message is now sent to the other user. To decrypt the message, the following steps are taken:

1. The message (binary) is converted into 8 bit chunks
2. Each chunk is decrypted using the DES class
3. Each decrypted 8-bit chunk is then concatenated into one long message
4. This long message (still binary) is now converted to ASCII

### How The Toy DES Encryption Works

The algorithm uses a 2-round Feistel cipher. Each round uses 2 S-boxes which are given a 4-bit input and will yield an output of  2 bits. A 10-bit master key is provided which yields an 8-bit key in each of its 2 rounds.

The decryption is the same exact algorithmic implementation as the encryption and simply swaps the order of the keys to decrypt the message.

### References

1. https://shakeelosmani.wordpress.com/2015/04/13/python-3-socket-programming-example/ 
2. https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa



# ToyDES
