import socket
from optparse import OptionParser

op = OptionParser ('--ip <ip> --port <port> --nick <nick-name>')
op.add_option('--ip', dest='ip', type='string')
op.add_option('--port', dest='port', type='int')
op.add_option ('--nick', dest='nick', type='string')
(op, args) = op.parse_args ()

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect((op.ip, op.port))

while True:
    d = raw_input('Message: ')
    s.send ('[' + op.nick + '] ' + d)
    data = s.recv (1024)
    print data