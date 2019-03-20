import os
from time import sleep

def print_data():
	print("\r",end='')
	sz = os.get_terminal_size()[0]
	for i in range(sz):
		print("-", end='')


for i in range(10):
	sleep(1)
	print_data()

print('')

