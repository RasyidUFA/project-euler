p = [[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,04,82,47,65],
[19,01,23,75,03,34],
[88,02,77,73,07,63,67],
[99,65,04,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,04,68,89,53,67,30,73,16,69,87,40,31],
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

def createstart(len):
	r = []
	for l in range(1,len+1):
		r.append([0]*l)
	return r

s= createstart(len(p)) 
s[0][0] = p[0][0]
for i in range(1,len(p)):

	for v in range(0,len(p[i])):
		val = p[i][v]
		if v<i:
			local = val + s[i-1][v]
			s[i][v] = max(local,s[i][v])
		if v>=1:
			local = val + s[i-1][v-1]
			s[i][v] = max(local,s[i][v])
print max(s[-1])
		