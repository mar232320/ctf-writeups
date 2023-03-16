The challenge gives 2 files - [image](output.png) and a [script](encode.py) used to create it

Every black stripe in the image is of the same height but different width
The width is always multiple of 16
I found the positions where black changes into white - the starting and ending points of stripes
Every white is a 0 bit and black is 1

I made a [script](solve.py) to get the flag

> flag{not_really_a_barcode_i_guess}
