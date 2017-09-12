from __future__ import print_function
import time
import math
import os
import sys
filename = 'test'

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

msg = '{' + raw_input("Message: ") + '}'
print ('Transfer...')
msg_bit = (tobits(msg))
print (''.join(str(x) for x in msg_bit))
for i in msg_bit:
	if(i):
		os.chmod(filename, 0o777)
	else:
		os.chmod(filename, 0o444) # for example
	time.sleep(0.1)
	sys.stdout.flush()
	print(i, end = '')
print ('')




