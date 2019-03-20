import os

def print_line():
	sz = os.get_terminal_size()[0]
	for i in range(sz):
		print('-',end='')
	print('')

def ret_metrics(data, attr):
	cols = len(attr)
	rows = len(data)
	return (cols,rows)

def check_validity(data,cols,rows):
	flag = True
	for i in range(rows):
		colt = len(data[i])
		if(colt!=cols):
			flag = False
			break
	return flag

def sort_func(data, attr):
	flag = str(input("Do you want to sort the data?(Y/N) : ")).upper()
	if(flag=="N"):
		return
	try: 
		print_line()
		print ("List of columns : ")
		print_line()
		for col in attr:
			print(col)
		print_line()
		col_name = str(input("Enter the column according to which the data will be sorted : "))
		col_index = attr.index(col_name)
		data.sort(key=lambda col: col[col_index])
	except ValueError:
		print("Column Name not found!")

def disp_data(data,attr,cols):
	print_line()
	print ("Data : ")
	print_line()
	for i in range(cols):
		print(attr[i], end=" | ")
	print('')
	for i in range(len(data)):
		for j in range(cols):
			print(data[i][j], end=" | ")
		print('')
	print_line()

def add_data(data, attr, cols, rows):
	flag = str(input("Do you want to add new entry ? (Y/N) : ")).upper()
	if(flag=="N"):
		return rows
	try:
		print_line()
		print("Enter data for the new entry : ")
		print_line()
		new_row=[]
		for col in attr:
			temp = str(input(str(col)+" : "))
			new_row.append(temp)
		print_line()
		data.append(new_row)
		rows+=1
		sort_func(data,attr)
		disp_data(data,attr,cols)
		return rows
	except Exception:
		print("Couldnt add new entry!")

def write_sort_data(file, data, attr, cols, rows):
	flag = str(input("Do you want to write the changes to csv file ? (Y/N) : ")).upper()
	if(flag=="N"):
		return
	try:
		file.seek(0,0)
		for temp in attr:
			if(temp.find(',')!=(-1)):
				temp = str('\"'+temp+'\"')
			file.write(temp+",")
		file.seek(file.tell()-1,0)
		file.write('\n')
		for i in range(rows):
			for j in range(cols):
				if(data[i][j].find(',')!=(-1)):
					data[i][j] = str('\"'+data[i][j]+'\"')
				file.write(data[i][j]+",")
			file.seek(file.tell()-1,0)
			file.write('\n')

	except Exception:
		print("Couldnt write data onto the file!")


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
				row.append(temp)
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
	(cols, rows) = ret_metrics(data,attr)
	if(check_validity(data, cols, rows)):
		sort_func(data, attr)
		disp_data(data, attr, cols)
		rows = add_data(data,attr,cols,rows)
		write_sort_data(file,data,attr,cols,rows)
	else:
		print ("Invalid CSV File!")
	file.close()

except FileNotFoundError:
	print("File couldnt be found!")
