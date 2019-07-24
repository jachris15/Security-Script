import ipaddress 

ip_list = open("sorted.txt", "r").read()
ip = ip_list.split()

#ip = ipaddress.ip_address(ip)

#print(ip)

total = 1
x = 0

for x in range(1, len(ip)):
	current_ip = ipaddress.ip_address(ip[x])
	previous_ip = ipaddress.ip_address(ip[x-1])
	
	if current_ip == previous_ip:
		total = total + 1
	else:
		print('Total number ',total, 'IP Address ', previous_ip)
		total = 1
print("Total number ",total,'IP Address ', current_ip)
