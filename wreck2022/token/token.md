token was a crypto challenge that I got first first blood on. In the [source code](challenge.py) there is aes encryption/authentication oracle. Every time somebody connects to the server a new random 32-byte aes password is generated (in fact it is 32-hex so there is 2^128 possible passwords) The goal is to authenticate as *gary*. There are two functions. First one receives a token, decrypts it, and if the decryption result is 'gary' you are given a flag. The second function encrypt input you give it (with the trick - you cant submit 'gary'), pads it and gives back the output.

aes pads to multiple of 16 bytes. So, when you input 'gary' it encrypts (16 - length(input) mod 16) * char(16 - length(input) mod 16) == 'gary\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c' . I immediately knew that it's a padding attack. I submitted this prepared padded message. However, although the length mod 16 is 0 it pads another 16 bytes with \x10 Since aes is a block cipher, I know what is in the last block and therefore I can throw it out. The server then decrypts the prepared message, unpads it as I wish and authenticates me as gary. Then the only thing I had to do is submitting the flag :)

The solution can be found in [solve.py](solve.py)

> flag{gary_gary_gary_gary_gary_gary}
