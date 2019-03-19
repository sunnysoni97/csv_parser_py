def check_validity(data):
	cols = len(data[0])
	rows = len(data)
	flag = True
	for i in range(rows):
		colt = len(data[i])
		if(colt!=cols):
			flag = False
			break
	return flag

filename = str(input("Enter the name of the csv file to parse (including file extension): "))

try:
	file = open(filename,"r+")
	temp = ""
	data = []
	row = []
	while(True):
		ch = file.read(1)
		if(len(ch) < 1):
			break
		else:
			if(ch==','):
				row.append(temp)
				temp=""

			elif(ch=='\n'):
				data.append(row)
				row=[]
				temp=""
			elif(ch=='"'):
				temp = ""
				while(True):
					ch = file.read(1)
					if((len(ch)<1) or ch=='"'):
						break
					else:
						temp+=ch
			else:
				temp+=ch
	if(check_validity(data)):
		print ("Data present in the file : ")
		cols = len(data[0])
		for i in range(cols):
			print(data[0][i], end="| ")
		print('')
		for i in range(1,len(data)):
			for j in range(cols):
				print(data[i][j], end="| ")
			print('')
	else:
		print ("Invalid CSV File")
except IOError:
	print("File couldnt be found or operations failed!")

finally:
	file.close()
