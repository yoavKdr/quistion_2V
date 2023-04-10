import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        # receive the mass
        if client_socket == None:
            print('Connection from {}:{} been close'.format(*client_address))
            return

        mass = client_socket.recv(1024).decode()

        # check if the client has disconnected
        if not mass:
            break

        # solve
        result = physics_calculator(float(mass))

        # send back the result to the client
        client_socket.send(str(result).encode())

    # close the connection
    print('Connection from {}:{} been close'.format(*client_address))
    client_socket.close()

def start_server():
    # create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to a specific address and port
    server_address = ('localhost', 5555)
    server_socket.bind(server_address)

    # listen for incoming connections
    server_socket.listen(5)
    print('Server is listening on {}:{}'.format(*server_address))

    # handle each incoming connection in a separate thread
    while True:
        client_socket, client_address = server_socket.accept()
        print('Received connection from {}:{}'.format(*client_address))
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address,))
        client_thread.start()

def physics_calculator(mass):
    # נתונים סטטיים
    team_mass = 35000 # המסע של המטוס עם חברי היחידה וצוות
    f = 100000 # כוח המנועים
    v = 140 # מהירות המרא

    fly_time = v * (team_mass + mass) / f # t = v/a

    max_m = (300000 / 7) - team_mass; # t = v/a => 60 = v/a => 60 = 140m/100000 המסה הגדולה ביותר
    mass_to_destroy = 0
    if mass > max_m:
        mass_to_destroy = mass - max_m
    
    fly_d = v * fly_time + 0.5 * f / (team_mass + mass) * fly_time * fly_time  # x = x0 + vt + 0.5a(t^2)

    return "the fly destence is: " + str(fly_d) + "\nthe fly time is: " + str(fly_time) + "\nif you want to fly in less then 60 sec you need to remove: " + str(mass_to_destroy) + " mass\n"

if __name__ == '__main__':
    start_server()
