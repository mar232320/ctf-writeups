org = open("orginal.pyc").read()
mod = open("modified.pyc").read()

dif = ""

for i in range(1605):
    if org[i] != mod[i]:
        dif += mod[i]
        
print dif
