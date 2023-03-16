import socket

def send(conn, data):
    conn.send(data + "\n")
    
def recv(conn, amount = 1024):
    res = conn.recv(amount)
    return res
    
s = socket.socket()

s.connect(("challs.wreckctf.com", 31745))

m = "PANDAMAN! I LOVE PANDAMAN! PANDAMAN MY BELOVED! PANDAMAN IS MY FAVORITE PERSON IN THE WHOLE WORLD! PANDAMAN!!!!"
p = "\x00" + m

send(s, "1")

recv(s)

send(s, p)

x = recv(s).split()[0]

send(s, "2")

recv(s)

send(s, x)

print recv(s)

s.close()