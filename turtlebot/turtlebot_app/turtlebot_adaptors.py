import socket


def establish_connection_and_send_destination(location_id=None, ip=None):
    s = socket.socket()
    if ip:
        host = ip
    else:
        host = "127.0.0.1"
    print host
    port = 10888
    s.connect((host, port))
    if s.recv(1024) == "Connection established":
        if location_id:
            s.send(location_id)
        else:
            s.send("ERROR")
