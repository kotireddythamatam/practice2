input = ("a1,a2","a3,a4","a2,a1","a5,a3")
lis = []
output = set()
for i in input:
	if ','.join(sorted(i.split(","))) not in output:
		lis.append(i)
		output.add(i)
print(lis)



# 

# b = i.split(',')
# 	c = b[::-1]
# 	d = ','.join(c)
# 	if i or d not in lis: