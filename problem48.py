x=0
for i in range (1,1001):
	po=pow(i,i)
	x=po+x
l=str(x)
print(x)
print('Total de dígitos','-'*6,'>',len(l))
print(l[-10:])




