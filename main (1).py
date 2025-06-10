#list comprension#squares of numbers 
'''l=[i*i for i in range(10)]
#t=tuple(l)
#print(t)
#print(type(t))
print(l)
for i in l:
    print(i,end="")
print(type(l)) '''

'''d={
    "name":"mahesh",
    "roll.no":123,
    "branch":"eee"
}
print(d)
print((type(d)))

d={}
print(d)
print(type(d))'''

'''d={1:100,2:800}
d['a']=500
d[3]=900
d.update({4:1000})
print(d)'''

#d={1:100,2:800,3:400,4:700}
'''print(d.pop(4))
print(d.popitem())
d.pop(1)
d.clear()
print(d)'''

'''print(d.keys())
print(d.values())
print(d.items())'''

'''for i in d.keys():
    print(i,end=" ")
print()    
for i in d.values():
    print(i,end=" ")
print()'''

'''d1=d.copy()
print (d1)'''

'''d={i:i*i for i in range(10)}
print(d)
d={i:i*i for i in range(20) if(i%5==0)}
print(d)'''

n=int(input())
if n==0:
    print(n)
else:
    while n%10==0:
        n=n//10
    print(n)    


