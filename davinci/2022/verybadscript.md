When I downloaded the doc file I opened it in libre office without executing the macro. I copied the macro code and started to reverse-engineer it
The macro was obfuscated. I renamed the random function names and got the partly deobfuscated macro with xor decrypting function. I modified the macro to display the xor password
which turned out to be
`Qx7BM0v9GDD2YYgfAxtWm2CShiUx2ikHTazpgtf90bEGuUwk46nFlDwmJFfGuLcFxp30f7iQpYIogbVhjqV9Us03sJNQqFTrViarTSJzNBnXY5rFYy6QVxwqfqQrAKUHa3PBu81C4zT4YRE3jX8lFiNQ7JHQBVuXAEQXIajamj1EDqa9n34eHZ7y0XbfuxPt7pMjWo7Jm0btMvzatyCPbZjczioyr3RbIbZDklpZDvbZdKnjKZroMg6EzZA1y2`

I made a python script to decrypt all the xor strings in the macro and there I found that the macro doesn't do anything malicious but sends a message with the flag via post request to `http://dvc.tf:9001`

final.vba

# dvCTF{vb4_0bfu5c4710n_5h3n4n164n5}
