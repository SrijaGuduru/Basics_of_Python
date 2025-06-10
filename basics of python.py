#basics of python
#sum of numbers from 1 to n
'''
n = int(input())
sum_n = n * (n + 1) // 2
print(sum_n)
'''
'''lst=list(map(int,input().split()))
count=0
for i in lst:
    if count!=1:
        break
    count+=1
print(count)'''

'''lst=list(map(int,input().split()))
k=int(input())
for i in range(k):
    temp=lst[0]
    for j in range(len(lst)-1):
        lst[j]=lst[j+1]
    lst[-1]=temp    
for i in lst:
    print(i,end=" ")'''
    
    
'''lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
lst=[]
for i in lst1:
    lst.append(i)
for i in lst2:
    lst.append(i)
print(lst)        
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]>=lst[j]):
            lst[i],lst[j]=lst[j],lst[i]
for i in lst:
    print(i,end=" ")'''
    
#1 2 2 3 3 3
#1:1
#2:2
#3:3
'''lst=list(map(int,input().split()))
d={}
for i in lst:
    if(i not in d.keys()):
        count=0
        for j in lst:
            if(i==j):
                count+=1
        d[i]=count
for i,j in d.items():
    print(i,":",j)'''
    
'''n=int(input())
d={}
for i in range(n):
    a,b=input().split()
    d[b]=a
for i,j in d.items():
    print(i,j)'''
    
'''def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))'''

'''def sum_of_n(n):
    if n==0:
        return 0
    else:
        return n+sum_of_n(n-1)
print(sum_of_n(10))'''

'''n=input()
if(n==n[::-1]):
    print("palindrome")
else:
    print("not a palindrome")
print(" ")'''

'''
n=int(input())
temp=n
rev=0
while(temp>0):
    last=temp%10
    rev=(rev*10)+last
    temp//=10
if(rev==n):
    print("palindrome")
else:
    print("not a palindrome")
'''



'''pattern
* * * * * 
* *   * * 
*   *   * 
* *   * * 
* * * * * 
'''
'''
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or i==n or j==1 or j==n or i==j or i+j==n+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''


'''pattern
   *     
  *   *   
*       * 
  *   *   
    *     
'''
'''
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j==4 or i+j==8 or i*j==8):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''



'''pattern
* * * * * 
* * * * 
* * * 
* * 
* 
'''

'''
n=5
for i in range(1,n+1):
    for j in range(n+1-i):
        print("*",end=" ")
        
    print()
'''

'''pattern
* * * * *  
  * * * *  
    * * *  
      * *  
        *  
'''


'''
n=5
for i in range(1,n+1):
    for j in range(n+1):
        if(j>=i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
'''


'''pattern
* * * * * 
*         
* * * * * 
        * 
* * * * * 
'''

'''
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or i==3 or i==5 or i+j==3 or i+j==9):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''




#lists  
'''
l=[12,34,1,3,23,67,12]
print(len(l))#len method is public,hence we can access without object
print(l.index(34))#not public method
print(l.count(12))
print(max(l))
print(min(l))
print(sum(l))
print(sum(l)//len(l))
l.sort()
print(l)
print(sorted(l,reverse=True))
l.append(200)
print(l)
l.insert(-1,500)
print(l)
l2=[30,40,50]
l.extend(l2)
print(l)
l.pop()
print(l)
l.remove(40)
print(l)
l.reverse()
print(l)
print(l[4])
print(l[1:4:1])
print(l[6:1:-1])
'''

'''
#sum of digits
n = input().strip()
sum_of_digits = 0

for digit in n:
    if digit.isdigit():  
        sum_of_digits += int(digit)

print(f"Sum of digits: {sum_of_digits}")
'''

'''
n = int(input())
sum_of_digits = 0
while n > 0:
    sum_of_digits += n % 10  
    n //= 10  
print(f"Sum of digits: {sum_of_digits}")
'''


#list comprension#squares of numbers 
'''
l=[i*i for i in range(10)]
t=tuple(l)
print(t)
print(type(t))
print(l)
for i in l:
    print(i,end="")
print(type(l))
'''

'''
def print_diamond(rows):
  """Prints a diamond pattern of specified rows.

  Args:
    rows: The number of rows in the diamond.
  """

  for i in range(1, rows + 1):
    print(' ' * (rows - i), end='')
    for j in range(1, 2 * i):
      print('*', end='')
    print()
  for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i), end='')
    for j in range(1, 2 * i):
      print('*', end='')
    print()
rows = int(input("Enter the number of rows: "))
print_diamond(rows)
'''

'''
1 1 1 1 1 
1 2 2 2 1 
1 2 3 2 1 
1 2 2 2 1 
1 1 1 1 1 
'''
'''

n=5
for i in range(n):
    for j in range(n):
        if i<=j and i<=n-1-j and i<=n-1-i:
            value=i+1
        if j<=i and j<=n-1-i and j<=n-1-j:
            value=j+1
        if n-1-i<=j and n-1-i<=i and n-1-i<=n-1-j:
            value=n-i
        if n-1-j<=i and n-1-j<=j and n-1-j<=n-1-i:
            value=n-j
        print(value,end=" ")
    print()
'''

#pyramid
'''n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print() ''' 

#diamond    
'''n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()'''
    
#butterfly pattern
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(2*(n-i)):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(2*(n-i)):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''
    
'''n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        if j==1 or i==n or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    
    print()'''
    
'''n=input()
l=[]
count=1
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        count+=1
    else:
        l.append(n[i-1]+str(count))
        count=1
if n:
    l.append(n[-1]+str(count))
print(" ".join(l))'''



#insertatend
'''class Node:
    def _init_(self,data):
        self.data=data
        self.addr=None
class linkedlist:
    def _init_(self):
        self.head=None
    def insertatend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.addr is not None:
                temp=temp.addr
            temp.addr=new_node
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.addr
l=linkedlist()

l.insertatend(10)
l.insertatend(20)
l.insertatend(30)
l.insertatend(40)
l.display()'''

#deletionatend
class Node:
    def _init_(self,data):
        self.data=data
        self.addr=None
class linkedlist:
    def _init_(self):
        self.head=None
    def insertatend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.addr is not None:
                temp=temp.addr
            temp.addr=new_node
    def deletionatend(self):
        if self.head is None:
            print("linkedlist is empty")
        elif self.head.addr is None:
            self.head=None
        else:
            temp=self.head
            while temp.addr.addr is not None:
                temp=temp.addr
            temp.addr=None    
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.addr
l=linkedlist()

l.insertatend(10)
l.insertatend(20)
l.insertatend(30)
l.insertatend(40)
l.deletionatend()
l.display()
