#!/usr/bin/env python
# coding: utf-8

# # Introduction

# ## Say "Hello, World!" With Python

# In[ ]:


if __name__ == '__main__':
    print("Hello, World!")


# ## Python If-Else

# In[ ]:


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n  % 2 != 0:
        print("Weird")
    elif  n >= 2 and n <= 5 and n  % 2 == 0 :
        print("Not Weird")
    
    elif  n >= 6 and n <= 20 and  (n  % 2) == 0 :
        print("Weird")
    
    elif n > 20:
        print("Not Weird")
    
    


# ## Arithmetic Operators

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# ## Python: Division

# In[ ]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


# ## Loops

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)


# ## Write a function

# In[ ]:


def is_leap(year):
    
    if year % 4 == 0 :
        if year % 100 == 0:
            if year % 400== 0 :
                return True 
            else:
                return False
        return True
    else:
        return False
            
year = int(input())


# ## Print Function

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")


# # Basic Data Types

# ## Find the Runner-Up Score!

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    score=list(arr)
    score.sort()
    score.reverse()
    
    for i in range(0,len(score)-1):
        if score[i] != score[i+1]:
            print(score[i+1])
            break


# ## Nested Lists

# In[ ]:


if __name__ == '__main__':
    lista=[]
    lista_numeri=[]
    for _ in range(int(input())):
        listino=[]
        name = input()
        score = float(input())
        
    
        listino.append(name)
        listino.append(score)
        lista.append(listino)
        lista_numeri.append(score)
        
    lista_numeri.sort()

    elemento=lista_numeri[0]
    second_lower=None
    for i in range(0,len(lista_numeri)-1):
        if lista_numeri[i] != lista_numeri[i+1]:
            second_lower=lista_numeri[i+1]
            break
        
        
    ordine=[]
    for i in range(0,len(lista)):
        if second_lower in lista[i]:
            ordine.append(lista[i][0])
    ordine.sort()
    
    for i in range(0,len(ordine)):
        print(ordine[i])


# ## Finding the percentage

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    voti=student_marks[query_name]
    somma=0
    for i in range(0,len(voti)):
        somma += voti[i]
    n=len(voti)
    media=somma/n
    media=round(media,2)
  
    print("%.2f" % media)


# ## Lists

# In[ ]:


if __name__ == '__main__':
    import re
    N = int(input())
    
    lista=[]
    for i in range(0,N):
        
        a=str(input())
        #Estrazione comando
        pattern=re.compile(r"[\w]{1,}")
        comando=pattern.search(a)[0].strip().lower()
       
        #Estrazione numeri
        numeri=re.findall(r"[\d]+",a)
 
        if comando =="insert" :
            lista.insert(int(numeri[0]),int(numeri[1]))
        
        elif comando=="remove":
            lista.remove(int(numeri[0]))

        elif comando=="append":
            lista.append(int(numeri[0]))
        elif comando=="sort":
            lista.sort()
        elif comando=="pop":
            lista.pop()
        elif comando=="reverse":
            lista.reverse()
            
        elif comando =="print":
            print(lista)


# ## Tuples

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tupla=tuple(list(integer_list))
    print(hash(tupla))


# ## List Comprehensions

# In[ ]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    lista=[[xx,yy,zz] for xx in range(0,x+1) for yy in range(0,y+1) for zz in range(0,z+1) if xx+yy+zz != n]
    lista.sort()
    print(lista)


# # Strings

# ## sWAP cASE

# In[ ]:


def swap_case(s):
    a=s.swapcase()
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# ## String Split and Join

# In[ ]:


def split_and_join(line):
    lista=line.split(" ")
    stringa="-".join(lista)
    
    
    # write your code here
    return stringa


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# ## What's Your Name?

# In[ ]:


def print_full_name(first, last):
    print("Hello "+str(first)+" "+str(last)+"! You just delved into python.")
    # Write your code here


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# ## Mutations

# In[ ]:


def mutate_string(string, position, character):
    stringa=""
    for i in range(0,len(string)):
        if i == position:
            stringa=stringa + character
        else:
            stringa=stringa + string[i]
    
    return stringa



if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# ## Find a string

# In[ ]:


import re
def count_substring(string, sub_string):
    l=len(sub_string)
    contatore=0
    for i in range(0,len(string)):
        if string[i:(l+i)] == sub_string:
            contatore += 1
        
    
    return contatore

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# ## String Validators

# In[ ]:


if __name__ == '__main__':
    s = input()
    
    uno=False
    due=False
    tre=False
    quattro=False
    cinque=False
    for i in range(0,len(s)):
        if s[i].isalnum()==True:
            uno = True
        if s[i].isalpha()==True:
            due=True
        if s[i].isdigit()==True:
            tre=True
        if s[i].islower()==True:
            quattro=True
        if s[i].isupper()==True:
            cinque=True
    print(uno)
    print(due)
    print(tre)
    print(quattro)
    print(cinque)


# ## Text Wrap

# In[ ]:


import textwrap

def wrap(string, max_width):
    stringa=""
    for i in range(0,len(string)):
        stringa= stringa + string[i]
        if (i +1 ) % max_width == 0:
            stringa=stringa +"\n"

    return stringa



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# ## String Formatting

# In[316]:


def print_formatted(number):
    esa=hex(number)[2:]
    if esa.isalpha()==True:
        esa=esa.upper()
    #Lunghezze massime :
    prima=len(str(number))
    seconda=len(str(oct(number)[2:]))
    terza=len(str(esa))
    quattro=len(str(bin(number)[2:]))
    
   
    for i in range(1,(number+1)):
        esa=hex(i)[2:]
        if esa.isalpha()==True:
            esa=esa.upper()
        
        #Assegnare a variabile i valori convertiti
        a=str(i)
        b=oct(i)[2:]
        c=esa
        d=bin(i)[2:]

        print(a.rjust(quattro),b.rjust(quattro),c.rjust(quattro),d.rjust(quattro))

        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# ## Designer Door Mat

# In[ ]:


mn=list(map(int,input().split()))
N=mn[0]
M=mn[1]




for i in range(1,N,2):
    a=".|."
    tratti=M-len(a*i)
    tratto=int(round(tratti/2,0))
    print(tratto*"-"+a*i+tratto*"-")

tratti=M-len("WELCOME")
tratto=int(round(tratti/2,0)) 
print(tratto*"-"+"WELCOME"+tratto*"-")    

    
for i in range(N-2,0,-2):
    a=".|."
    tratti=M-len(a*i)
    tratto=int(round(tratti/2,0))
    print(tratto*"-"+a*i+tratto*"-")


# ## Alphabet Rangoli

# In[ ]:


def print_rangoli(size):
    alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"
    ,"q","r","s","t","u","v","w","x","y","z"]
    lettere=alfabeto[0:size]
    lettere.reverse()
    

    t=(size-1)*2
    l=(size*2)-1
    
    dim=t+l
    
    
    listino=[]
    m=[]
    bb=[]
    for i in range(0,size):
        a=[]
        listino.append(lettere[i])
        a.extend(listino)
        m.extend(listino)
        m.reverse()
        
        a.extend(m[1:])
        
        stringa="-".join(a)
        lunghezza_stringa=len(stringa)
        ltratti=int(round((dim-len(stringa))/2))
        
        bb.append(ltratti*"-"+stringa+ltratti*"-")
        m=[]
        

    cc=bb[:len(bb)-1]
    cc.reverse()
    bb.extend(cc)
    print("\n".join(bb))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# ## Capitalize

# In[ ]:


import math
import os
import random
import re
import sys

import re
def solve(s):
    
    lista=re.split(r'(\s+)', s)
    stringa=""
    for i in range(0,len(lista)):
        lista[i] = lista[i].capitalize()
    stringa="".join(lista)
        
    
    return stringa.strip()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# ## The Minion Game
# Funziona ma viene bloccato per timeout

# In[ ]:


import re
def minion_game(string):
    
    #Stuart
    #Iniziale
    if string[0] not in ["A","E","I","O","U"]:
        punteggioS=1
        punteggioK=0
    else:
        punteggioS=0
        punteggioK=1
       
        
    #Trovare possibili parole
    consonanti=[]
    vocali=[]
    for i in range(1,len(string)):
        for j in range(0,len(string)):
            sub=string[j:i+j]
            if sub[0] not in ["A","E","I","O","U"] and len(sub)==i and sub not in consonanti:
                consonanti.append(sub)
                p=re.findall(r"(?=("+sub+"))",string)
                punteggioS += len(p)
            elif  sub[0]  in ["A","E","I","O","U"] and len(sub)==i and sub not in vocali:
                vocali.append(sub)
                p=re.findall(r"(?=("+sub+"))",string)
                punteggioK += len(p)
            
    
    if punteggioK > punteggioS:
        print("Kevin",punteggioK)
    elif punteggioK < punteggioS :
        print("Stuart",punteggioS)
    else:
        print("Draw")
    
    


# ## Merge the Tools!

# In[ ]:


def merge_the_tools(string, k):
    k=int(k)

    for i in range(0,len(string),k):
        sottostringa=string[i:k+i]
        a=""
        for j in range(0,len(sottostringa)):
            if sottostringa[j] not in a:
                a += sottostringa[j]
        print(a)
                
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# ## Text Alignment

# In[279]:


thickness =int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).center(thickness*10))


# # Sets

# ## Introduction to Sets

# In[ ]:


def average(array):

    no_duplicati=list(dict.fromkeys(array))
    somma=sum(no_duplicati)

    media=somma/len(no_duplicati)
    media="%.3f" % media
    
    return media
  
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# ## Symmetric Difference

# In[ ]:


if __name__=="__main__":
    M=int(input())
    M_i=set(input().split())
    
    N=int(input())
    N_i=set(input().split())
    
    m=M_i.difference(N_i)
    n=N_i.difference(M_i)
   
    
    
    tot=n.union(m)
    tot=list(map(int,tot))
    tot.sort()
    for i in range(0,len(tot)):
        print(tot[i])


# ## Set .add()

# In[ ]:


if __name__=='__main__':
    N=int(input())
    
    a=set()
    for i in range(0,N):
        n=str(input())
        a.add(n)
    print(len(a))


# ## Set .discard(), .remove() & .pop()

# In[ ]:


import re
n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(0,N):
    stringa=str(input())
    
    pattern=re.compile(r"[a-zA-Z]+")
    
    comando=pattern.search(stringa)
    comando=comando[0].strip()
    
    numero=re.findall(r"[\d]+",stringa)
    numero=list(map(int,numero))
    
    #print(comando[0],numero)
    if comando=="pop":
        #print(s)
        s.pop()

    elif comando=="remove" and numero[0] in s:
        s.remove(numero[0])
   
    elif comando=="discard":
        s.discard(numero[0])
       
print(sum(s))


# ## Set .union() Operation

# In[ ]:


n=int(input())
a=set(map(int,input().split()))

nn=int(input())
b=set(map(int,input().split()))

print(len(a.union(b)))


# Set .intersection() Operation

# In[ ]:


n=int(input())
a=set(map(int,input().split()))

nn=int(input())
b=set(map(int,input().split()))

print(len(a.intersection(b)))


# ## Set .difference() Operation

# In[ ]:


n=int(input())
a=set(map(int,input().split()))

nn=int(input())
b=set(map(int,input().split()))

print(len(a.difference(b)))


# ## Set .symmetric_difference() Operation

# In[ ]:


n=int(input())
a=set(map(int,input().split()))

nn=int(input())
b=set(map(int,input().split()))

print(len(a.symmetric_difference(b)))


# ## Set Mutations

# In[ ]:


n=int(input())
A=set(map(int,input().split()))

N=int(input())
for i in range(0,N):
 
    comandi=input().split()

    comando=comandi[0]
    
    B=set(map(int,input().split()))
    
    if comando=="update":
        A.update(B)
    elif comando=="intersection_update":
        A.intersection_update(B)
    elif comando=="symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif comando=="difference_update":
        A.difference_update(B)
print(sum(A))


# ## Check Subset

# In[ ]:


test=int(input())
for i in range(0,test):
    n=int(input())
    A=set(map(int,input().split()))

    n=int(input())
    B=set(map(int,input().split()))

    intersezione=A.intersection(B)
    if A==intersezione:
        print(True)
    else:
        print(False)


# ## Check Strict Superset

# In[ ]:


A=set(map(int,input().split()))
n=int(input())

condizione=True
for i in range(0,n):
    B=set(map(int,input().split()))

    if B==A.intersection(B) and len(B) < len(A):
        continue
        
    condizione=False 
    
print(condizione)


# ## No Idea!

# In[ ]:


o=list(map(int,input().split()))

array=list(map(int,input().split()))

A=set(map(int,input().split()))
B=set(map(int,input().split()))



happy=0
for i in range(0,len(array)):
    if array[i] in A:
        happy += 1
    elif array[i] in B:
        happy += -1
print(happy)


# ## The Captain's Room

# In[ ]:


from collections import Counter

n=int(input())
gruppi=input().split()


C=Counter()
for i in range(0,len(gruppi)):
    C[gruppi[i]]+=1


for i in C.keys():
    if C[i] != n :
        print(i)


# # Collection

# ## collections.Counter()

# In[ ]:


X=int(input()) 
scarpe=list(map(int,input().split()))
C=int(input()) 

guadagno=0
for i in range(0,C):
    richiesta=list(map(int,input().split()))
    
    taglia=richiesta[0]
    prezzo=richiesta[1]
    if taglia in scarpe:
        guadagno += prezzo
        scarpe.remove(taglia)
    
print(guadagno)


# ## Collections.namedtuple()

# In[ ]:


from collections import namedtuple 
N=int(input())
columns_name=input().split()
info=namedtuple("info",columns_name)

contatore =0 
for i in range(0,N):
    riga=input().split()

    riga=info._make(riga)
    contatore += int(riga.MARKS)
print("%.2f"% (contatore/N))


# ## Collections.OrderedDict()

# In[ ]:


from collections import OrderedDict
import re 
N=int(input())
diz=OrderedDict()
for i in range(0,N):
    o=input()
    nome=re.findall(r"[a-zA-Z \s]+",o)
    nome=nome[0].strip()
    prezzo=re.findall(r"[\d]+",o)
    prezzo=int(prezzo[0].strip())
    if nome not in diz:
        diz[nome]=prezzo
    else:
        valore=diz[nome]
        diz[nome]= valore + prezzo
for i in diz.keys():
    print(i,diz[i])


# ## Word Order

# In[ ]:


from collections import OrderedDict
n=int(input())
diz=OrderedDict()
for i in range(0,n):
    stringa=input().strip()
    if stringa not in diz:
        diz[stringa]=1
    else:
        valore=diz[stringa]
        diz[stringa]=valore +1 
print(len(diz))

for i in diz.keys():
    print(diz[i],end=" ")


# ## Collections.deque()

# In[ ]:


from collections import deque
n=int(input())
d=deque()
for i in range(0,n):
    comandi=input().split()
    comando=comandi[0].strip()
    
    if comando=="append":
        d.append(int(comandi[1]))
    elif comando=="appendleft":
        d.appendleft(int(comandi[1]))
    elif comando=="pop":
        d.pop()
    elif comando=="popleft":
        d.popleft()
    elif comando=="remove":
        d.remove(int(comandi[1]))
    elif comando=="reverse":
        d.reverse()
    elif comando=="rotate":
        d.rotate(int(comandi[1]))
    elif comando=="extend":
        d.extend(int(comandi[1]))
for i in d:
    print(i,end=" ")


# ## Company Logo

# In[ ]:


import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    cont=Counter()
    s = input()
    s=list(s)
    s.sort()
    s="".join(s)
    
    #print(s)
    for i in range(0,len(s)):
        cont[s[i]] +=1 
    elementi=cont.most_common(3)
    #elementi=list(map(str,elementi))
    
    for i in range(len(elementi)):
        print(elementi[i][0],elementi[i][1])        


# ## DefaultDict Tutorial

# In[ ]:


from collections import defaultdict,Counter
inn=list(map(int,input().split()))
n=inn[0]
m=inn[1]

A=defaultdict(list)


for i in range(0,n):
    word=input()
    A[word].append(str(i+1))

for b in range(0,m):
    parola=input()
    if parola  in A:
        print(" ".join(A[parola]))
    else:
        print("-1") 


# ## Piling Up!

# In[ ]:


from collections import deque 

T=int(input())
for i in range(0,T):
    nblock=int(input())
    blocco=list(map(int,input().split()))
    
    d=deque()
    d.extend(blocco)
    ordine=[]
    for i in range(0,len(d)):
        if d[0]>=d[-1]:
            ordine.append(d[0])
            d.popleft()
        elif d[-1]> d[0]:
            ordine.append(d[-1])
            d.pop()

    blocco.sort(reverse=True)

    if blocco==ordine:
        print("Yes")
    else:
        print("No") 


# # Date and Time

# ## Calendar Module

# In[ ]:


from datetime import datetime
data=input().split()
data="/".join(data)
a=datetime.strptime(data, '%m/%d/%Y')

print(a.strftime("%A").upper())


# ## Time Delta

# In[34]:


import math
import os
import random
import re
import sys
from datetime import datetime
def time_delta(t1, t2):

    t1=datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2=datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    delta=t1-t2
    diff=delta.total_seconds()
    diff=abs(round(int(diff),0))
    return str(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# # Errors and Exceptions

# ## Exceptions

# In[ ]:


T=int(input())
for i in range(0,T):
    try:
        numeri=list(map(int,input().split()))
    except ValueError as e:
        print("Error Code:",e)  
        continue
    
        

    try:    
        divisione=numeri[0]//numeri[1]
        print(divisione)
    except ZeroDivisionError as e:
        print("Error Code:",e)  


# # Built-ins

# ## zipped

# In[43]:


NX=list(map(int,input().split()))
N=NX[0] #numero studenti
X=NX[1] #numero materie

tutti=[]
for i in range(0,X):
    a=list(map(float,input().split()))
    tutti.append(a)

voti=list(zip(*tutti))
for i in range(0,len(voti)):
    media=sum(voti[i])/X
    print(round(media,1))


# ## Athlete Sort

# In[ ]:


import math
import os
import random
import re
import sys
from collections import defaultdict
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    
    k = int(input())
    diz=defaultdict(list)
    for i in range(0,len(arr)):
        chiave=str(arr[i][k])
        diz[chiave].append(arr[i])
            
    chiavi=list(map(int,list(diz.keys())))
    chiavi.sort()
    #print(diz)
    #print(chiavi)
    for i in range(0,len(chiavi)):
        elemento=diz[str(chiavi[i])]
        #print(elemento,len(elemento))
        if len(elemento) >1 :
            for j in range(0,len(elemento)):
                elementoj=list(map(str,elemento[j]))
                print(" ".join(elementoj))
        else :    
           elementoj=list(map(str,elemento[0]))
           #print(elementoj)
           print(" ".join(elementoj))


# ## ginortS

# In[ ]:


s=input()

lower=[]
upper=[]
pari=[]
dispari=[]
for i in range(0,len(s)):
    if s[i].islower()==True:
        lower.append(s[i])
    elif s[i].isupper()==True:
        upper.append(s[i])
    else:
        numero=int(s[i])
        if numero % 2 == 0:
            pari.append(str(numero))
        else:
            dispari.append(str(numero))

lower.sort()
upper.sort()
pari.sort()
dispari.sort()
lower.extend(upper)
lower.extend(dispari)
lower.extend(pari)

a="".join(lower)
print(a)


# # Python Functionals

# ## Map and Lambda Function

# In[ ]:


cube = lambda x: x**3

def fibonacci(n):
 
    c=[]
    for i in range(0,n):
        if i==0:
            c.append(i)
        elif i==1:
            c.append(i)
        else:
            c.append(c[i-2]+c[i-1])
    return c

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# # Regex and Parsing

# ## Detect Floating Point Number

# In[ ]:


import re
from collections import Counter
T=int(input())
for i in range(0,T):
    s=input()
    l=len(s)
    o=re.findall(r"[+-\.]?[\d]*\.[\d]+",s)
    if o!=[] and l==len(o[0]) :
        punti=re.findall(r"\.",o[0])
        if len(punti) > 1 or len(o[0])==1:
            print(False)
        else:
            print(True)
    else:
        print(False)


# ## Re.split()

# In[ ]:


regex_pattern = r"[,\.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


# ## Group(), Groups() & Groupdict()

# In[ ]:


import re
stringa=input()
def luca_nervi(s):
    p=re.findall(r"[a-zA-Z0-9]*",s)
    s="".join(p)
    for i in range(0,len(s)-1):
        if s[i] ==s[i+1]:
            return (s[i])
    return "-1"

print(luca_nervi(stringa))


# ## Re.findall() & Re.finditer()

# In[ ]:


import re

s=input()

gruppi_vocali=re.finditer(r"(?=([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]))",s)
notoverlap = [(i.group(1)) for i in gruppi_vocali]

vocali="".join(notoverlap)
vocali=re.findall(r"[AEIOUaeiou]{2,}",vocali)
if vocali==[]:
    print("-1")

else:
    print("\n".join(vocali)) 


# ## Re.start() & Re.end()

# In[ ]:


import re
S=input()
k=input()

def d(S,k): 
    width=len(k)
    out=[]
    for i in range(0,len(S)):
        #print(i,width+i)
        #print(S[i:width+i])
        a=re.search(r""+k+"",S[i:width+i])
        if bool(a)==True:
            t=tuple((i,width+i-1))
            out.append(t)
    if len(out) <1 :
        return [(-1,-1)]
    return out
o=d(S,k)
for i in range(0,len(o)):
    print(o[i])


# ## Regex Substitution

# In[ ]:


import re 
N=int(input())
for i in range(N):
    linea=input()
 
    sostituzioni=re.findall(r"(?= [\&]{2} )",linea)
    for j in range(0,len(sostituzioni)):
        linea=re.sub(r" \&\& "," and ",linea)
        
    sostituzioni=re.findall(r"(?= [\|]{2} )",linea)
    for j in range(0,len(sostituzioni)):
        linea=re.sub(r" \|\| "," or ",linea)
    
    print(linea)


# ## Validating phone numbers

# In[ ]:


import re
N=int(input())
for i in range(N):
    stringa=input()
    b=re.match(r"[789]{1}[\d]{9}",stringa)
    if bool(b)==True and len(stringa)==10:
        print("YES")
    else:
        print("NO")


# ## Validating and Parsing Email Addresses

# In[ ]:


import re
n=int(input())
for i in range(n):
    stringa=input().split()

    nome=stringa[0]
    email=stringa[1]

    bb=re.match(r"<[a-zA-Z]{1}[a-zA-Z0-9-._]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>",email)
 
    if bool(bb)==True:
        print(nome,email)


# ## Hex Color Code

# In[ ]:


import re
N=int(input())

gate=False
for i in range(N):
    stringa=input()
    
    openn=re.match(r".*[{].*",stringa)
    #print(openn)
    if bool(openn)==True:
        gate=True
        continue
        
        
    closed=re.match(r".*[}].*",stringa)
    if bool(closed)==True:
        gate=False
        continue
    
    if gate==True:
        colori=re.findall(r"#[0-9A-Fa-f]{3,6}",stringa)
        if len(colori) >= 1:
            print("\n".join(colori))                     


# ## Validating UID

# In[ ]:


import re 
def UID(uid):
    
    boool=re.match(r"[a-zA-Z0-9]{10}",uid)
    if len(uid.strip())==10 and bool(boool)==True:
        uppercase=re.findall(r"[A-Z]",uid)
        if  len(uppercase) >= 2:
            numeri=re.findall(r"[0-9]",uid)
            if len(numeri) >= 3:
                lista=[]
                for i in range(0,len(uid)):
                    if uid[i]  not in lista:
                        lista.append(uid[i])
                    else:
                        return "Invalid"        
                return "Valid" 
            else:
                return "Invalid"              
        else:
            return "Invalid"
    else:
        return "Invalid"
        
T=int(input())
for i in range(0,T):
    uid=input()
    print(UID(uid))      


# ## Validating Credit Card Numbers

# In[ ]:


import re
def valida(card):
    # It must start with a 4, 5 or 6.
    test1=re.match("[456]",card)
    if bool(test1)==False:
        return "Invalid"
        
    #It must NOT use any other separator like ' ' , '_', etc.
    #It must only consist of digits (0-9).
    controllo_caratteri=re.search(r"[^0-9-]",card)
    if bool(controllo_caratteri)==True:
        return "Invalid"
        
    #It must contain exactly 16 digits.
    digits=re.findall(r"[0-9]",card)
    if len(digits) != 16:
        return "Invalid"
    

    #Style: 5122-2368-7954-3214
    gruppi=re.search(r"([0-9]{4})-([0-9]{4})-([0-9]{4})-([0-9]{4})",card)
    if bool(gruppi)==True:
        carta=re.sub(r"-","",gruppi[0])
        c=0
        for i in range(0,len(carta)-1):
           
            if carta[i] == carta[i+1]:
                c += 1 
                if c > 2:
                    return "Invalid"
            
            else:
                c=0
            
        return "Valid"
        
      
    gruppi=re.search(r"([0-9]{4})([0-9]{4})([0-9]{4})([0-9]{4})",card)
    if bool(gruppi)==True:
        c=0
        for i in range(0,len(gruppi[0])-1):
            if gruppi[0][i] ==gruppi[0][i+1]:
                c += 1 
                if c > 2:
                    return "Invalid"
            
            else:
                c=0
        return "Valid"
    return "Invalid"
    
N=int(input())
for i in range(0,N):
    print(valida(input()))


# ## Validating Roman Numerals

# In[ ]:


import re
import sys

numero=input()
a=re.match(r"(M{,3})?(CD|CM|C{1,3}|D[C]{,3})?(XL|XC|X{1,3}|L[X]{,3})?(IV|IX|I{1,3}|V[I]{,3})?",numero)
if len(numero)== len(a[0]) and bool(a)==True:
    print(True)
else:
    print(False)

 
sys.exit(0)#I using "sys.exit(0)" from sys in order to ignore mandatory lines of code by Hackerrank and so, writing my very own program.
#With "sys.exit(0)" i  will ignored those lines of code made mandatory by Hackerrank
print(str(bool(re.match(regex_pattern, input())))) #will be ignored.


# ## Validating Postal Codes

# In[ ]:


import re
regex_integer_in_range = r"^[0-9]{6}$"
regex_alternating_repetitive_digit_pair = r"([0-9])(?=[0-9]\1)"

P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# ## HTML Parser - Part 1

# In[ ]:


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    #def handle_comment(self, data):
     #   print("Comment  :", data)
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            a=list(map(str,attr))
            print("->",a[0],">",a[1])
            
            
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            a=list(map(str,attr))
            print("->",a[0],">",a[1])
N=int(input())
parser = MyHTMLParser()

for i in range(N):
    S=input()
    parser.feed(S)


# ## HTML Parser - Part 2

# In[ ]:


from html.parser import HTMLParser
import re
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if bool(re.search(r"\n",data))==True:
            print(">>> Multi-line Comment")
            print(data)
        else:
           print(">>> Single-line Comment")
           print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)
N=int(input())
parser = MyHTMLParser()

com=False
for i in range(N):
    S=input().strip()

    if bool(re.search(r"<\!--",S))==True or com==True:
        com=True
 
        if bool(re.search(r"-->",S))==True:
            com=False
        elif bool(re.search(r"<\!--[.]*-->",S))==False:
            S += "\n"
             
    parser.feed(S)


# ## Detect HTML Tags, Attributes and Attribute Values

# In[ ]:


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            a=list(map(str,attr))
            print("->",a[0],">",a[1])
            
            
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            a=list(map(str,attr))
            print("->",a[0],">",a[1])
N=int(input())
parser = MyHTMLParser()

for i in range(N):
    S=input()
    parser.feed(S)


# ## Matrix Script

# In[ ]:


import re

inn=list(map(int,input().split()))
righe=inn[0]
colonne=inn[1]

matrice=[]
for i in range(0,righe):
    riga=[]
    contenuto=str(input())

    for j in range(0,colonne):
        riga.append(contenuto[j])
    matrice.append(riga)

    
testo=""
for j in range(colonne):
    for i in range(righe):
        testo += str(matrice[i][j])

gruppi=re.finditer(r"([a-zA-Z0-9])([^a-zA-Z0-9]+)([a-zA-Z0-9])",testo)
for i in gruppi:
   # print(i.group(2))
    testo=testo.replace(i.group(2)," ",1)
print(testo)


# # Numpy

# ## Arrays

# In[ ]:


import numpy
def arrays(arr):
    arr=numpy.array(arr,dtype="f")
    arr=numpy.flip(arr,0)
    
    
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# ## Shape and Reshape

# In[ ]:


import numpy as np

array=np.array(list(map(int,input().split())))
array.shape = (3, 3)
print(array)


# ## Concatenate

# In[ ]:


import numpy as np

inn=list(map(int,input().split()))
N=inn[0]
M=inn[1]
P=inn[2]

n=[]
for i in range(0,N):
   riga=list(map(int,input().split()))
   n.append(riga)
m=[]
for i in range(0,M):
    riga=list(map(int,input().split()))
    m.append(riga)

n=np.array(n)
m=np.array(m)

tot=np.concatenate((n,m),axis=0)
print(tot)


# ## Zeros and Ones

# In[ ]:


import numpy as np

inn=tuple(map(int,input().split()))

print(np.zeros(inn, dtype = "i"))
print(np.ones(inn, dtype = "i"))


# ## Transpose and Flatten

# In[ ]:


import numpy as np

inn=list(map(int,input().split()))
righe=inn[0]

matrice=[]
for i in range(0,righe):
    riga=list(map(int,input().split()))
    matrice.append(riga)

matrice=np.array(matrice)
trasposta=np.transpose(matrice)
print(trasposta)
print(matrice.flatten())


# ## Eye and Identity

# In[ ]:


import numpy
numpy.set_printoptions(legacy="1.13")


inn=list(map(int,input().split()))
righe=inn[0]
colonne=inn[1]
print(numpy.eye(righe,colonne))


# ## Array Mathematics

# In[ ]:


import numpy as  np

NM=list(map(int,input().split()))
N=NM[0]
M=NM[1]

A=[]
for i in range(0,N):
    riga=list(map(int,input().split()))
    A.append(riga)

A=np.array(A)
    
B=[]
for i in range(0,N):
    riga=list(map(int,input().split()))
    B.append(riga)
B=np.array(B)

#ADD
print(np.add(A,B))

#Subtract
print(np.subtract(A,B))

#Multiply
print(np.multiply(A,B))

#Integer division
print(np.floor_divide(A,B))

#MOD
print(np.mod(A,B))

#Power
print(np.power(A,B))


# ## Floor, Ceil and Rint 

# In[ ]:


import numpy as np
np.set_printoptions(legacy="1.13")

arr=np.array(list(map(float,input().split())))
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))


# ## Sum and Prod

# In[ ]:


import numpy as np

NM=list(map(int,input().split()))
N=NM[0]
M=NM[1]

A=[]
for i in range(0,N):
    riga=list(map(int,input().split()))
    A.append(riga)

A=np.array(A)

somma=np.sum(A,axis=0)
prodotto=np.prod(somma)
print(prodotto)


# ## Min and Max

# In[ ]:


import numpy as np


NM=list(map(int,input().split()))
N=NM[0]
M=NM[1]

A=[]
for i in range(0,N):
    riga=list(map(int,input().split()))
    A.append(riga)

A=np.array(A)

minimi=np.min(A,axis=1)
print(np.max(minimi))


# ## Mean, Var, and Std

# In[ ]:


import numpy as np
#np.set_printoptions(legacy="1.13")


NM=list(map(int,input().split()))
N=NM[0]
M=NM[1]

A=[]
for i in range(0,N):
    riga=list(map(int,input().split()))
    A.append(riga)

array=np.array(A)
print(np.mean(array,axis=1))
print(np.var(array,axis=0))
print(round(np.std(array,axis=None),11))


# ## Dot and Cross

# In[ ]:


import numpy as np
#np.set_printoptions(legacy="1.13")

N=int(input())

A=[]
for i in range(0,N):
    riga=list(map(int,input().split()))
    A.append(riga)

A=np.array(A)

B=[]
for i in range(0,N):
    riga=list(map(int,input().split()))
    B.append(riga)
B=np.array(B)


print(np.matmul(A,B))


# ## Inner and Outer

# In[ ]:


import numpy as np

A=np.array(list(map(int,input().split())))
B=np.array(list(map(int,input().split())))

print(np.inner(A,B))
print(np.outer(A,B))


# ## Polynomials

# In[ ]:


import numpy as np


pol=np.array(list(map(float,input().split())))


x=int(input())

print(np.polyval(pol, x))


# ## Linear Algebra

# In[ ]:


import numpy as np
N=int(input())

A=[]
for i in range(0,N):
    riga=list(map(float,input().split()))
    A.append(riga)

A=np.array(A)
print(round(np.linalg.det(A),2))


# # Closures and Decorators

# ## Standardize Mobile Number Using Decorators

# In[ ]:


import sys

ordine=[]
lista = [input() for _ in range(int(input()))]

for i in range(0,len(lista)):
    a=lista[i]
    l=len(a)
    numero=int(a[l-10:])
    ordine.append(numero)

ordine.sort()

numeri=[ "+91 "+str(i)[0:5]+" "+str(i)[5:] for i in ordine]
print("\n".join(numeri))

        
sys.exit(0) #I using "sys.exit(0)" from sys in order to ignore mandatory lines of code by Hackerrank and so, writing my very own program.
#With "sys.exit(0)" i  will ignored those lines of code made mandatory by Hackerrank


# ## Decorators 2 - Name Directory

# In[ ]:


import operator
import sys

people = [input().split() for i in range(int(input()))]

lista=[]
for i in range(0,len(people)):
    listino=[]
    #Sesso
    listino.append(int(people[i][2]))
    
    if  people[i][3]=="M":
        nome="Mr. "+people[i][0]+" "+people[i][1]
        listino.append(nome)
      
    else:
        nome="Ms. "+people[i][0]+" "+people[i][1]
        listino.append(nome)
    lista.append(listino)
    #Ordinare   
lista.sort(key=lambda s: s[0])
for i in range(0,len(lista)):
    print(lista[i][1])

sys.exit(0)    #I using "sys.exit(0)" from sys in order to ignore mandatory lines of code by Hackerrank and so, writing my very own program.
@person_lister #With "sys.exit(0)" i  will ignored those lines of code made mandatory by Hackerrank
def name_format(person): #will be ignored
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]#will be ignored

if __name__ == '__main__':#will be ignored
    people = [input().split() for i in range(int(input()))]#will be ignored
    print(*name_format(people), sep='\n')#will be ignored

#!/usr/bin/env python
# coding: utf-8

# # XML

# ## XML 1 - Find the Score

# In[ ]:


import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    att=0

    for i in node.iter(): #prende tutte le tag come se non fossero annidate
           #print(i.attrib)
           att += len(i.attrib)
    return att
    
    
    
    
    
    
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# ## XML2 - Find the Maximum Depth

# In[ ]:


import xml.etree.ElementTree as etree
global levelll
maxdepth = 0
levelll=[]
def depth(elem, level):
    if level==-1:
        level += 1
    global maxdepth 
    levelll.append(level)
    maxdepth=max(levelll)
    for i in elem:
        depth(i,level +1 )
    



    
    
    

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#!/usr/bin/env python
# coding: utf-8

# # Problem 2

# ## Birthday Cake Candles

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    C=Counter()
    for i in candles:
        C[i] += 1
    return C.most_common(1)[0][1]
    
    
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(result)
    fptr.write(str(result) + '\n')

    fptr.close()


# ## kangaroo

# In[ ]:


import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return "NO"
    #calcolo mcm
    elif x1 < x2 and v1==v2:
        return "NO"
    
    t=(x2-x1)/(v1-v2)

    
    if t.is_integer()==False:
        return "NO"
    elif t >= 0:
        return "YES" 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# ## Viral Advertising

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    cumulative=0
    persone=5

    for i in range(0,n):
        like=persone//2
        persone= like * 3
        cumulative += like
    return cumulative
        
        

        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


# ## Recursive Digit Sum

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

def superDigit(n, k):

    if len(n)==1:
        return n
    
    while len(n)!=1:
        conta=0
        for i in range(0,len(n)):
            conta += int(n[i]) 
   
        n = str(conta)
    n=n* k 
    while len(n)!=1:
        conta=0
        for i in range(0,len(n)):
            conta += int(n[i]) 
   
        n = str(conta)
    return conta 
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# ## 

# ## Insertion Sort - Part 1

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys



def insertionSort1(n, arr):
    last=arr[-1]
    a=arr[:-1]
    o=[]
    for i in range(len(arr)-2,-1,-1):
        
        if last < arr[i]:
            o.append(i)
            p=list(map(str,a[:i]))
            k=list(map(str,a[i:]))
            bb=" ".join(p)+" "+str(arr[i])+" "+" ".join(k)
            print(bb.strip())
    
    arr.pop()
    arr.insert(o[-1],last)
    arr=list(map(str,arr))
    arr=" ".join(arr)
    print(arr)   
   # print(o)         
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


# ## Insertion Sort - Part 2

# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys



def insertionSort2(n, arr):
    c=1
    while c < n:

        elemento = arr[c]
        i = c-1
        while elemento < arr[i]  and i >=0  :
                arr[i+1] = arr[i]
                i -= 1

        arr[i+1] = elemento
        stampa=list(map(str,arr))
        print(" ".join(stampa))
        c += 1
            
        
  
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)



