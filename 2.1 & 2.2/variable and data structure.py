
name= 'luyun'
print(name)
print('id:',id(name))
print('type:',type(name))
print('value:',name)


year = eval(input('please enter a year:'))

if(year%4==0 and year%100!=0) or year%400==0:
    print('{} is a leap year'.format(year))
else:
    print('{} is a common year'.format(year))

sum=0
a=1
while a<=100:
    if a%2==0:
        sum+=a
    a+=1
print('the sum of integers from 1 to 100:', sum)


def F(n):
    if n == 0:
 return 0

    elif n == 1:
       return 1
    else:
       return F(n - 1) + F(n - 2)

n = 21
list = []
for i in range(0, n):
    Fibonacci = F(i)
 list.append(Fibonacci)
print(list)


empty_dict = {}

grades = {'Hozier':'A', 'Deloria':'A+', 'Betty':'B', 'May':'A'}

print(grades.keys())
print(grades.values())
print(grades.items())

class Employee:

    empCount = 0

    def __init__(self, name, salary):
 self.name = name
 self.salary = salary
 Employee.empCount += 1

 def displayCount(self):
 print('Total Employee %d'% Employee.empCount)

 def displayEmployee(self):
 print('Name:', self.name, ', Salary: ', self.salary)

emp1 = Employee("Selina", 3000)
emp2 = Employee("Adele", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print('Total Employee %d' % Employee.empCount)


def insert_sort(L):

    for x in range(1,len(L)):
        for i in range(x-1,-1,-1):
            if L[i] > L[i+1]:
                temp = L[i+1]
                L[i+1] = L[i]
                L[i] = temp



def select_sort(L):
    for x in range(0,len(L)):
        minimum = L[x]
        for i in range(x+1,len(L)):
            if L[i] < minimum:
                temp = L[i];
                L[i] = minimum;
                minimum = temp

        L[x] = minimum



def bubble_sort(L):
    length = len(L)
    for x in range(1,length):
        for i in range(0,length-x):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp



def insert_shell(L):

    gap = (int)(len(L)/2)

    while (gap >= 1):

        for x in range(gap,len(L)):

            for i in range(x-gap,-1,-gap):

                if L[i] > L[i+gap]:
                   temp = L[i+gap]
                    L[i+gap] = L[i]
                    L[i] =temp

        gap = (int)(gap/2)


def quick_sort(L, start, end):
    if start < end:
        i, j, pivot = start, end, L[start]
        while i < j:
            while (i < j) and (L[j] >= pivot):
                j = j - 1
            if (i < j):
                L[i] = L[j]
                i = i + 1
            while (i < j) and (L[i] < pivot):
                i = i + 1
            if (i < j):
                L[j] = L[i]
                j = j - 1
        L[i] = pivot
        quick_sort(L, start, i - 1)
        quick_sort(L, i + 1, end)



def LEFT(i):
    return 2*i + 1
def RIGHT(i):
    return 2*i + 2
def adjust_max_heap(L,length,i):
    while (1):
        left,right = LEFT(i),RIGHT(i)
        if (left < length) and (L[left] > L[i]):
            largest = left
            print('left node')
        else:
            largest = i
        if (right < length) and (L[right] > L[largest]):
            largest = right
            print('right node')
        if (largest != i):
            temp = L[i]
            L[i] = L[largest]
            L[largest] = temp
            i = largest
            print(largest)
            continue
        else:
            break

def build_max_heap(L):
    length = len(L)
    for x in range((int)((length-1)/2),-1,-1):
        adjust_max_heap(L,length,x)

def heap_sort(L):
    build_max_heap(L)
    i = len(L)
    while (i > 0):
        temp = L[i-1]
        L[i-1] = L[0]
        adjust_max_heap(L,i,0)



def mergearray(L,first,mid,last,temp):
    i,j,k = first,mid+1,0
    while (i <= mid) and (j <= last):
        if L[i] <= L[j]:
            temp[k] = L[i]
            i = i+1
            k = k+1
        else:
            temp[k] = L[j]
            j = j+1
            k = k+1
    while (i <= mid):
        temp[k] = L[i]
        i = i+1
        k = k+1
    while (j <= last):
        temp[k] = L[j]
        j = j+1
        k = k+1
    for x in range(0,k):
        L[first+x] = temp[x]

def merge_sort(L,first,last,temp):
    if first < last:
        mid = (int)((first + last) / 2)
        merge_sort(L,first,mid,temp)
        merge_sort(L,mid+1,last,temp)
        mergearray(L,first,mid,last,temp)

def merge_sort_array(L):
    temp = len(L)*[None]
    merge_sort(L,0,len(L)-1,temp)



def radix_sort_nums(L):
    maxNum = L[0]
    for x in L:
        if maxNum < x:
            maxNum = x
    times = 0
    while (maxNum > 0):
        maxNum = (int)(maxNum/10)
        times = times+1
    return times

def get_num_pos(num,pos):
    return ((int)(num/(10**(pos-1))))%10

def radix_sort(L):
    count = 10*[None]
    bucket = len(L)*[None]
    for pos in range(1,radix_sort_nums(L)+1):
        for x in range(0,10):
           count[x] = 0
        for x in range(0,len(L)):
            j = get_num_pos(int(L[x]),pos)
            count[j] = count[j]+1
        for x in range(1,10):
            count[x] = count[x] + count[x-1]
        for x in range(len(L)-1,-1,-1):
            j = get_num_pos(L[x],pos)
            bucket[count[j]-1] = L[x]
            count[j] = count[j]-1
            L[x] = bucket[x]

def insert_shell(L):
    gap = (int)(len(L)/2)
    while (gap >= 1):
         for x in range(gap,len(L)):
            for i in range(x-gap,-1,-gap):
                if L[i] > L[i+gap]:
                    temp = L[i+gap]
                    L[i+gap] = L[i]
                    L[i] =temp
        gap = (int)(gap/2)






