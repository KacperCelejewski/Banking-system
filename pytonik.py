#!/usr/bin/env python
# coding: utf-8

# In[7]:


def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
        
print(list_sum([2, 4, 5, 6, 7]))


# In[8]:


print(list_sum)


# In[3]:


g=[1,2,3,4,5]


# In[32]:


def sum(L):
    if len(g)==1:
        return g[0]
    else:
        return sum(g[0])+sum(g[1:])


# In[ ]:


g=[1,2,3,4,5]
sum(g)


# In[1]:


def conversion(L):
    i=0
    if isinstance(L[i],(int,float))==False:
        str(L[i])
    else:
        return coversion(L[i+1]) 


# In[3]:


g=[1,2,3,4,5]
print(conversion(g))


# In[4]:


listo = [1, 2, [3,4], [5,6]]


# In[13]:


def rec(L):
    L=[]
    if len(L)==1:
        return L[0]
    else:
        return rec(L[0] + L[1:])


# In[14]:


rec(listo)


# In[18]:


def func(NumOfIterates):
    i=1
    for i in range (NumOfIterates-1):
        i=i+1
        if NumOfIterates==1 :
            return 1
        elif i==0:
            print(0)
        else:
            print(i+(i-1))
        
    


# In[7]:


func(1)


# In[19]:


func(10)


# In[4]:


L=[input("Wpisz swój str:")]


# In[5]:


len(L[0])


# In[6]:


for i in range(len(L[0])):
    if i%2==0:
        print(str[::2])


# In[7]:


G=[L[0]]


# In[8]:


str1=str(G[0])


# In[11]:


print(str[::2])


# In[12]:


type(str1)


# In[13]:


# ex 1 from challenges


# In[1]:


num = int(input("Enter a number: "))
L=[]


# In[17]:


def sqFunc (num):
    for i in range(num):
        if pow(i,2)==num:
            print("Koxuwa")
        elif num == 1:
            print("Koxuwa")
            
        


# In[20]:


sqFunc(245)


# In[48]:


def circle_area(radius):
    pi=3.14
    r2=radius**2
    area=(pi*r2)
    print(type(area))
    return area


# In[50]:


circle_area(1.1)


# In[51]:


name=str(input("Wpisz imie: "))


# In[58]:


surname=str(input("Wpisz imie: "))


# In[59]:


reverse = surname+" "+name


# In[60]:


print(reverse)


# In[61]:


lists=[input("Wpisz sekwencje liczb oddzielonych przecinkiem")]


# In[62]:


lists


# In[63]:


get_ipython().run_line_magic('pinfo2', 'split')


# In[66]:


lists[0].split(",")


# In[2]:


tuple=(1,2,3,4)


# In[4]:


type(tuple)


# diff=("a",4.23,1,"vbhjde")

# In[5]:


type(diff)


# In[6]:


diff=("a",4.23,1,"vbhjde")


# In[8]:


type(diff)


# In[31]:


for i in range(len(diff)):
    L={}
    key="val"+str(i)
    val=diff[i]
    L[key]=val
    print(L)


# In[27]:


a = {}
k = 0
while k < 10:
    # dynamically create key
    key = k+1
    # calculate value
    value = k
    a[key] = value 
    k += 1


# In[28]:


a


# In[39]:


b=("ednj",)


# In[40]:


new=diff+b


# In[41]:


new


# In[42]:


str(new)


# In[47]:


new=("s","u","d","o","k","u")


# In[50]:


"".join(new)


# In[51]:


myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)


# In[52]:


myDict


# In[77]:


diff[3:4:2]


# In[54]:


diff


# In[78]:


diff.pop()


# In[ ]:




