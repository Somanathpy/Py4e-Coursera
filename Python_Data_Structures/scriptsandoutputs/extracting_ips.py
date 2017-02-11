import re
fname = input("enter a file name:")
path = "C:/Users/SomandLily/Documents/GitHub/Py4e-Coursera/Python_Data_Structures/Data/"
fname = path+fname

try:
	file = open(fname)
except:
	print("file can't open;"+fname)
	exit()

ips_count = {}
ips_list = re.findall(r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})',file.read())
           #re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',str)
for ip in ips_list:
	if ip in ips_count:
		ips_count[ip] += 1
	else:
		ips_count[ip] = 1
for k,v in ips_count.items():
	print(str(k)+"===>"+str(v))
#largest ip
largest = 0
mostip = None


for k,v in ips_count.items():
	if v > largest:
		largest = v
		mostip = k
print("\n")
print("\n")
print("\n")
print("=========Most Frequent IP========")
print(mostip+"*******"+str(largest))

#printin in ascedining order by values

tmp = list()
for (k,v) in ips_count.items():
	tmp.append((v,k))
#print(tmp)
tmp = sorted(tmp,reverse=True)
print("\n")
print("\n")
print("\n")
print("=======list of Ips by its frequency=====")
for i in tmp:
	print(i)