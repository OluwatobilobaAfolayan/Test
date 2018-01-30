from pwn import * 
import base64
with open("given.txt", "r") as f:
    for line in f:
  	#with open("output.txt", "a") as out:
	temp = base64.b64decode(line)
        #out.close()
        x = temp[4:8]
	print(x)
