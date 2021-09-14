The [modified version](https://github.com/mar232320/ctf-writeups/raw/main/alles2021/manipulated_tictactoe.cpython-36.pyc) of the program was compiled with python 3.6 so I compiled the original [source code](https://github.com/mar232320/ctf-writeups/raw/main/alles2021/tictactoe.py)

I made a [script](http://) to find differences in this two compiled files which had the same length 1605

```python
org = open("orginal.pyc").read()
mod = open("modified.pyc").read()

dif = ""

for i in range(1605):
    if org[i] != mod[i]:
        dif += mod[i]
				
print dif
```
In the output there was the flag

## ALLES!{py7h0n_byt3cod3_s3cr3ts}
