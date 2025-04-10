first_name = "Kannappan"
last_name = 'Ram'
print(first_name)
print('Employee Name : ',first_name,last_name) #
print(type(first_name)) #

x = int(3.1)
print(x)


#num=float("hello")
#print(type(num))

#print(num)

vdata="hello world"
print(vdata[0])
for ne in vdata:
    print(ne)

for vr in vdata:
    print(vr)
    if vr == 'r':
        break;


for t in range(0,30,3):
    print(t)

data=[1,4,6,7,8,12,45,67]
i=1
while i<=5:
    print(data[i])
    i+=1
else:
    print("iteration complete",i)