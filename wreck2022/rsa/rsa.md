rsa was a crypto challenge in WRECK CTF 2022. The goal was to break 2048 bit RSA signature and get a sign for a specific message.

[rsa.py](rsa.py)

I found a non-intended easy solution to this challenge. I simply added a null byte in front of the message that I needed to get a signature of. The message was converted to a number with bytes_to_long() function and the null byte was converted to 0s which were stripped. The author of the challenge did not predict someone using two different messages that give exact bytes_to_long() result ;)

[solve script](solve.py)

> flag{dan_likes_moes}
