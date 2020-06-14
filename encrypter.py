#encrypting
from random import randint
import os

zero = False
try:
	g = open("main_data.txt", "r")
	text = g.read()
	g.close()
except IOError:
	print("File does not exist, make main_data.txt file first or input text below.\n")
	text = input('Enter the text you want to convert:\n \n')
crypt = ''


def random_n(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start, range_end)

def converter(text):
	global crypt
	for value in text:
		if ord(value)<100:
			crypt = crypt + '0' + str(ord(value))
		else:
			crypt = crypt + str(ord(value))
	return crypt


crypt = converter(text)
print(f'This is the converted form {crypt} and it has a length of {len(crypt)}')

num = random_n(len(crypt))
pass1 = num*1 + int(crypt)
pass2 = num*2 + int(crypt)
print(f'The random seed was: {num}')
if crypt[0]=='0':
	zero = True
	print('\nIt has a 0 at the start\n')
print(f'The two new keys are, \nPass1: {pass1} \nPass2: {pass2}')


with open('pass.txt', 'w') as f:
	f.write(str(pass1))
	f.write('\n')
	f.write(str(pass2))
	if(zero):
		f.write('\n')
		f.write('0')
f.close()
try:
	os.remove('main_data.txt')
except IOError:
	pass
