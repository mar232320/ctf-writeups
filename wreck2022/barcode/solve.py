import PIL.Image

img = PIL.Image.open("output.png")

s, w = img.size

aaa = []

for i in range(1, s):
    p = img.getpixel((i - 1, 0))
    c = img.getpixel((i, 0))
    if p != c:
        aaa.append(i)
             
pos = []

for i in aaa:
    o = i / 16
    pos.append(o)
    
b = ""

n = s / 16

white = True

for i in range(n):
    if i in pos:
        white = not white
    if white:
        b += "0"
    else:
        b += "1"

flag = hex(int(b, 2))[2:-1].decode("hex")

print flag