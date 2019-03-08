def comp(a,b,c):
	if a>b and a>c:
		big = a
		print(big,"is the largest of all")
	elif b>a and b>c:
		big = b
		print(big,"is the largest of all")
	else:
		print(c,"is largest")

x = int(input())
y = int(input())
z = int(input())
comp(x,y,z)