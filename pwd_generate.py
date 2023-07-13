import random
import os

def pwd_16bit_generate():
	pwd_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
				'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
				'u', 'v', 'w', 'x', 'y', 'z',
				 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
				 'U', 'V', 'W', 'X', 'Y', 'Z',
				  '!', '@', '#', '$', '%', '^', '&', '*']
	x = ''
	for i in range(1,20):
		x += str(random.choice(pwd_list))
	return x

if __name__ == '__main__':
	pwd_16bit_generate()
	print(pwd_16bit_generate())