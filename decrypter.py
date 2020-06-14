#decrypting
import os
check = False
g = open("pass.txt", "r")
code1 = g.readline()
code2 = g.readline()
if(g.readline()=='0'):
	check = True




slope = (int(code2)-int(code1))
print(f'The slope of it is: {str(slope)}')
orignal = int(code1)-(int(slope))

if(check):
	orignal = '0' + str(orignal)
else:
	orignal = str(orignal)

print(f'The converted orignal text was {orignal}')
#print(len(str(pass1)))

va = ''
for i in range(len(orignal)):
	if(i%3==0):
		start = i
		end = i + 3
		va = str(va) + str(chr(int(orignal[start:end])))

print('The orignal text was "' + va +'"')

with open('main_data.txt', 'w') as f:
	f.write(va)
f.close()


os.remove('pass.txt')