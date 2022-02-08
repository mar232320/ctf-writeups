I was given the <a href="2022/ret2">binary</a> and the <a href="2022/ret2.c">source code</a>

My goal was to execute the print_flag() function.

Address of this function was 0x00000000004011f7

The buffer of char input is 16 and char takes 8 bytes itself so the overflow value must be 24. My payload was a*24 + \xf7\x11@\x00\x00\x00\x00\x00
