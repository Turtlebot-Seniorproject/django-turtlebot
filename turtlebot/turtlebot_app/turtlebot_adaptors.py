import socket


def establish_connection_and_send_destination(location_id=None):
    s = socket.socket()
    host = "192.168.1.6"
    port = 10888
    s.connect((host, port))
    if s.recv(1024) == "Connection established":
        if location_id:
            s.send(location_id)
        else:
            s.send("ERROR: No Room Name")
        print "message sent"
