import time
import os
filename = 'test'

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

print ('Receiving...')
bin_char = ''
for i in range(1000):
	info = os.stat(filename)
	if (info.st_mode == 33279):
		bin_char = str(bin_char) + str(1)
	elif (info.st_mode == 33060):
		bin_char = str(bin_char) + str(0)		
	if (bin_char.rfind('01111101') != -1):
		break
	time.sleep(0.1)

start = bin_char.find('01111011')
end = bin_char.rfind('01111101')
bin_char = bin_char[start:end + 8]
message  = (frombits(bin_char))
print message
