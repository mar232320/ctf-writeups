I was given a <a href="2022/tracer">binary</a> to reverse-engineer

I disassembled it in gdb at first but it looked like the flag was encrypted
the binary checks the user input with fgets() and strcmp() it with the decrypted flag
I used ltace to trace the library calls. The flag wasn't visible entirely so I changed the string length parameter (-s 128) to see the full flag

# nactf{how_even_do_stream_ciphers_work_i_definitely_did_this_wrong}
