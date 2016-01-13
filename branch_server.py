from optparse import OptionParser
import socket
from threading import Thread
import time

# Funcs #

def recv (bytes, con, cons):
    while True:
        data = con.recv (bytes)
        for i in cons:
            i.send (data)
            print data + ' sent'
# ----- #

op = OptionParser ('--ip <ip> --port <port>')
op.add_option('--ip', dest='ip', type='string')
op.add_option('--port', dest='port', type='int')
(op, args) = op.parse_args ()

connections = []
addresses = []

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

s.bind ((op.ip, op.port))
s.listen(128)
connection, address = s.accept ()

connections.append(connection)
addresses.append(address)

Thread (target=recv, args=(10500, connection, connections,)).start ()