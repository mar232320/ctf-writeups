I was given the <a href="2022/gets">binary</a> and it's <a href="2022/gets.c">source code </a>

In there there is the vulnerable gets() function and a variable magic I had to overflow. ascii reprezentation of 42 is * .

The buffer of char input is 16, char takes 8 bytes itself and int 4 bytes so the overflow value must be 28. My payload was a*28 + *
Sending it gave me the flag

# nactf{buff3r_0v3rfl0w_b3g1nn1ngs}
