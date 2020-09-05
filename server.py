#server.py
import socket
def server_program():
        # get the hostname
        host = socket.gethostname()
        port = 8090  # initiate port no above 1024
        
        server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together
        
        # configure how many client the server can listen simultaneously
        server_socket.listen(2)
        ip = socket.gethostbyname(socket.gethostname())
        print ("[*] Starting listening on ",ip,": ",port)
        client, address = server_socket.accept()  # accept new connection
        print("[*] Got a connection from " + str(address))
        while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
                data = client.recv(1024).decode()
                print ("[*] Received '",data,"' from the client (Admin)")
                print ("   Processing data")
                if(str(data) == "turn right"):
                        client.send("Okay Admin\nTurning Right".encode())
                        print ("    Processing done.\n[*] Reply sent")
                elif(str(data) == "turn left"):
                        client.send("Okay Admin\nTurning Left".encode())
                        print ("    Processing done.\n[*] Reply sent")
                elif(str(data) == "scan"):
                        client.send("Okay Admin\nScanning Surrounding".encode())
                        print ("    Processing done.\n[*] Reply sent")
                elif(str(data) == "disconnect"):
                        client.send("Goodbye".encode())
                        client.close()
                        print("Shuting Down Server")
                        break
                else:
                        client.send("Invalid Command".encode())
                        print ("    Processing done. Invalid Data \n[*] Reply sent")

        client.close()  # close the connection


if __name__ == '__main__':
        server_program()
