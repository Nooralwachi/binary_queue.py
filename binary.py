from datetime import datetime
def binary(filename):
	binaries=[]
	with open(filename, 'r') as f:
		f.readline()
		for line in f:
			binary,time,date,status = line.strip().split()
			if status not in ['succeeded', 'failed']:
				binaries.append([binary,datetime.strptime(time + ' ' + date, '%H:%M:%S %m/%d/%Y'),status])
			sorted_binaries= sorted(binaries, key=lambda x:(x[2],x[1]))

	# print(binaries)
	print(f'Binary Created_at Status')
	for binary,created_at,status in sorted_binaries:
		print(f'{binary} {datetime.strftime(created_at,"%H:%M:%S %m/%d/%Y")} {status}')





binary('binary_queue.txt')