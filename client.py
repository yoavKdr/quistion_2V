import socket

def start_client():
    # create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the server's address and port
    server_address = ('localhost', 5555)
    client_socket.connect(server_address)

    while True:
        # get the mass from the user
        mass = input('Enter a mass (or "quit" to exit): ')

        # check if the user wants to quit
        if mass == 'quit':
            break

        # send the mass to the server
        client_socket.send(mass.encode())

        # receive the result from the server
        result = client_socket.recv(1024).decode()

        # print the result
        print('Result: {}'.format(result))

    # close the connection
    client_socket.close()

if __name__ == '__main__':
    start_client()
