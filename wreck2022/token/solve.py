import socket

def send(conn, data):
    conn.send(data + "\n")
    
def recv(conn, amount = 1024):
    res = conn.recv(amount)
    return res
    
s = socket.socket()

s.connect(("challs.wreckctf.com", 31522))

print recv(s)

send(s, "2")

print recv(s)

payload = "gary" + chr(12) * 12

send(s, payload)

x = recv(s)

token = x.split()[3]

mod = token[:32]

send(s, "1")

print recv(s)

send(s, mod)

print recv(s)

s.close()