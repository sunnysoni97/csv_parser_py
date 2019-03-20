def check_validity(data, attr):
	cols = len(attr)
	rows = len(data)
	flag = True
	for i in range(rows):
		colt = len(data[i])
		if(colt!=cols):
			flag = False
			break
	return flag

def sort_func(data, attr):
	try: 
		print ("------------------------------")
		print ("List of columns : ")
		for col in attr:
			print(col)
		print ("------------------------------") 
		col_name = str(input("Enter the column according to which the data will be sorted : "))
		col_index = attr.index(col_name)
		data.sort(key=lambda col: col[col_index])
	except ValueError:
		print("Column Name not found!")

def disp_data(data,attr):
	print ("------------------------------")
	print ("Data : ")
	print ("------------------------------")
	cols = len(attr)
	for i in range(cols):
		print(attr[i], end=" | ")
	print('')
	for i in range(len(data)):
		for j in range(cols):
			print(data[i][j], end=" | ")
		print('')
	print ("------------------------------")



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
	attr = data[0]
	del data[0]
	if(check_validity(data, attr)):
		sort_func(data, attr)
		disp_data(data, attr)
	else:
		print ("Invalid CSV File")
	file.close()

except FileNotFoundError:
	print("File couldnt be found!")

