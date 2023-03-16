enc = "oujp{xkurpjcxah_ljnbja_lryqna}"

flag = ""

for i in enc:
    flag += chr((ord(i) - ord("a") + 43) % 26 + ord("a"))
    
print flag