from socket import *
import ssl

context = ssl.create_default_context()

msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = "smtp.gmail.com"
# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start

clientSocket = socket(AF_INET, SOCK_STREAM) #creating the socket
clientSocket = ssl.wrap_socket(clientSocket) #using SSL to wrap the socket
clientSocket.connect((mailserver,465)) #Connecting to the gmail servers


#Fill in end

recv = clientSocket.recv(1024).decode() 
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response.
heloCommand = 'HELO GMAIL\r\n' 
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

clientSocket.send(('AUTH LOGIN\r\n').encode())
recv2 = clientSocket.recv(1024).decode() 
print(recv2)

#Need gmail account and password, also need to go to security and allow external softwares to access account
#Program will now work without this part done correctly
clientSocket.send(('gmail username encoded in base 64\r\n').encode())
print(clientSocket.recv(1024).decode())
clientSocket.send(('gmail password encoded in base 64\r\n').encode())
print(clientSocket.recv(1024).decode() )


# Send MAIL FROM command and print server response.
 
# Fill in start

mail = 'MAIL from: <EMAIL YOU AUTHED WITH>\r\n'  #leave this, does not need to change
clientSocket.send(mail.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.

# Fill in start
rcpt = 'RCPT TO: <andrewschaus3@gmail.com>\r\n'  #this is my gmail
clientSocket.send(rcpt.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end




# Send DATA command and print server response.

# Fill in start
data = 'Data\r\n'
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end


# Send message data.

# Fill in start
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.

# Fill in start
clientSocket.send(endmsg.encode())
# Fill in end

# Send QUIT command and get server response.

# Fill in start
x = 'QUIT\r\n'
clientSocket.send(x.encode())
clientSocket.close()
# Fill in end
