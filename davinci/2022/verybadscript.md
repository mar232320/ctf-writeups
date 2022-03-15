When I downloaded the <a href="../../../../raw/main/davinci/2022/verybadscript.doc">doc file</a>
I opened it in libre office without executing the macro. I copied the macro code and started to reverse-engineer it
The <a href="../../../../raw/main/davinci/2022/macro.vba">macro</a> was obfuscated. I renamed the random function names and got the partly <a href="../../../../raw/main/davinci/2022/makro.vba">deobfuscated macro</a> with xor decrypting function. I modified the macro to display the xor password
which turned out to be
`Qx7BM0v9GDD2YYgfAxtWm2CShiUx2ikHTazpgtf90bEGuUwk46nFlDwmJFfGuLcFxp30f7iQpYIogbVhjqV9Us03sJNQqFTrViarTSJzNBnXY5rFYy6QVxwqfqQrAKUHa3PBu81C4zT4YRE3jX8lFiNQ7JHQBVuXAEQXIajamj1EDqa9n34eHZ7y0XbfuxPt7pMjWo7Jm0btMvzatyCPbZjczioyr3RbIbZDklpZDvbZdKnjKZroMg6EzZA1y2`

I made a <a href="../../../../raw/main/davinci/2022/vbsolver.py">python script</a> to decrypt all the xor strings in the macro and there I found that the macro doesn't do anything malicious but sends a message with the flag via post request to `http://dvc.tf:9001`

<a href="../../../../raw/main/davinci/2022/final.vba">final.vba</a>

# dvCTF{vb4_0bfu5c4710n_5h3n4n164n5}
