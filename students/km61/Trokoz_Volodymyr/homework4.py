#task1------------------------------------------------
"""
���� ��� ����� ����� A � B (��� ���� A ? B). 
�������� ��� ����� �� A �� B ������������.
"""
#�������� ��� ��������� ������ �������� �����, ������ �� ������
#number, ���:int. ������ ������������ ����� 
#i, ���:int. ��������� ��������� ��������
#���� �������� ����������
number = int(input('������ ���� �����'))

#����������
i=1

while (i**2)<=N:

    print(i**2)

    i+=1
#-----------------------------------------------------


#task2------------------------------------------------
"""
���� ����� �����, �� ������� 2. 
�������� ��� ���������� ����������� ��������, �������� �� 1.
"""
#�������� ��� ����������� ���������� ������������ �������
#number, ���:int. ������ ������������ ����� 
#i, ���:int. ��������� ��������� ��������
#���� �������� ����������
number = int(input('������ ���� �����, �� ����� 2'))

#����������
i=2

if n%2==0:

    print('��������� ����������� ������: ', i)

else:

    while n%i!=0:

        i+=1
    
print('��������� ����������� ������: ', i)
#-----------------------------------------------------


#task3------------------------------------------------
"""
�� ������� ������������ ����� N ������� ���������� ����� ������� ������, �� ������������� N. 
�������� ���������� ������� � ���� �������.
��������� ���������� � ������� ������������ ������!
"""
#�������� ��� ����������� ���������� ������� ����� 2
#number, ���:int. ������ ������������ ����� 
#two_in_power, ���:int. ��������� ��������� ��������
#power, ���:int. ��������� ��������� ��������
#���� �������� ����������
number = int(input('������ ���� �����, �� ����� 2'))

#����������
two_in_power = 2

power = 1

while two_in_power <= n:

    two_in_power *= 2

    power += 1

print('������: ', power - 1, '�������� ����� � �������:', 'two_in_power // 2)
#-----------------------------------------------------


#task4------------------------------------------------
"""
� ������ ���� ��������� �������� x ����������, � ����� �� ������ ���� ���������� ������ �� 10% �� ����������� ��������. 
�� ������� ����� y ���������� ����� ���, �� ������� ������ ���������� �������� �� ����� y ����������.

��������� �������� �� ���� �������������� ����� x � y � ������ ������� ���� ����������� �����.
"""
#�������� ��� ���������� ����� �������
#x, ���:float. ������ ������������ ����� 
#y, ���:float. ������ ������������ ����� 
#days, ���:int. ��������� ��������� ��������
#���� �������� ����������
x = float(input('������ ��������� ������� ��������'))

y = float(input('������ ������ ������� ��������'))

#����������
days = 1

while (x < y):

    x *= 1.1

    days += 1

print('ʳ������ ����:', days)
#-----------------------------------------------------


#task5------------------------------------------------
"""
����� � ����� ���������� x ������. �������� �� ������������� �� p ���������, ����� ���� ������� ����� ������ �������������.
����������, ����� ������� ��� ����� �������� �� ����� y ������.
��������� �������� �� ���� ��� ����������� �����: x, p, y � ������ ������� ���� ����� �����.
"""
#�������� ��� ���������� �������� �����������
#x, ���:int. ������ ������������ �����
#p, ���:int. ������ ������������ ����� 
#y, ���:int. ������ ������������ ����� 
#years, ���:int. ��������� ��������� ��������
#���� �������� ����������
x = int(input('������ ����� ����������� ������'))

p = int(input('������ ��������� ������'))

y = int(input('������ ����� �������� ������'))

#����������
years = 1

while (x < y):

    x *= 1 + p / 100

    x = int(100 * x) / 100

    years += 1

print('ʳ������ ����: ', years)
#-----------------------------------------------------


#task6------------------------------------------------
"""
��������� �������� �� ���� ������������������ ����� ��������������� �����, ������ ����� �������� � ��������� ������.
������������������ ����������� ������ 0, ��� ���������� �������� ��������� ������ ��������� ���� ������ � ������� ���������� ������ ������������������ (�� ������ ������������ ����� 0).
�����, ��������� �� ������ 0, ��������� �� �����.
"""
#�������� ��� ���������� ������� �����������
#length, ���:int. ��������� ��������� �������� 
#��������� 
length = 0
#����������
while int(input("������ ���� ����'���� �����")) != 0:

    len += 1

print('������� �����������: ', len)
#-----------------------------------------------------


#task7------------------------------------------------
"""
���������� ����� ���� ��������� ������������������, ������������� ������ 0. 
� ���� � �� ���� ��������� ������� �����, ��������� �� ������ �����, ��������� �� �����.
"""
#�������� ��� ���������� ���� �����������
#sum, ���:int. ��������� ��������� �������� 
#element, ���:int. ������ ������������ �����
#��������� 
sum = 0
#����������
element = int(input("������ ���� �����"))

while element != 0:

    sum += element

    element = int(input("������ ���� �����"))

print('���������: ', sum)
#-----------------------------------------------------


#task8------------------------------------------------
"""
���������� ������� �������� ���� ��������� ������������������, ������������� ������ 0.
"""
#�������� ��� ���������� ���������� ���� �����������
#sum, ���:int. ��������� ��������� �������� 
#len, ���:int. ��������� ��������� �������� 
#element, ���:int. ������ ������������ �����
#����������
sum = 0
len = 0

element = int(input('������ ���� �����'))

while element != 0:

    sum += element

    len += 1

    element = int(input('������ ���� �����'))

print('���������: ', sum / len)
#-----------------------------------------------------


#task9------------------------------------------------
"""
������������������ ������� �� ����������� ����� � ����������� ������ 0. 
���������� �������� ����������� �������� ������������������.
"""
#�������� ��� ���������� ���������� ��������
#max, ���:int. ��������� ��������� �������� 
#element, ���:int. ������ ������������ �����
#����������
max = 0

element = -1

while element != 0:

    element = int(input('������ ���� �����'))

    if element > max:

        max = element

print('���������: ', max)
#-----------------------------------------------------


#task10-----------------------------------------------
"""
������������������ ������� �� ����������� ����� � ����������� ������ 0. ���������� ������ ����������� �������� ������������������. 
���� ���������� ��������� ���������, �������� ������ ������� �� ���. ��������� ��������� ���������� � ����.
"""
#�������� ��� ���������� ������� ���������� ��������
#max, ���:int. ��������� ��������� �������� 
#len, ���:int. ��������� ��������� �������� 
#index_of_max, ���:int. ��������� ��������� �������� 
#element, ���:int. ������ ������������ �����
#����������
max = 0

index_of_max = -1

element = -1

len = 0

while element != 0:

    element = int(input('������ ���� �����'))

    if element > max:

        max = element

        index_of_max = len

    len += 1

print('���������: ', index_of_max)

#-----------------------------------------------------


#task11-----------------------------------------------
"""
���������� ���������� ������ ��������� � ������������������, ������������� ������ 0.
"""
#num_even, ���:int. ��������� ��������� �������� 
#element, ���:int. ������ ������������ �����
#����������
num_even = -1

element = -1

while element != 0:

    element = int(input('������ ���� �����'))

    if element % 2 == 0:

        num_even += 1

print('���������: ', num_even)
#-----------------------------------------------------


#task12-----------------------------------------------
"""
������������������ ������� �� ����������� ����� � ����������� ������ 0. 
����������, ������� ��������� ���� ������������������ ������ ����������� ��������.
"""
#answer, ���:int. ��������� ��������� �������� 
#prev, ���:int. ������ ������������ �����
#next, ���:int. ������ ������������ �����
#����������
prev = int(input('������ ���� �����'))

answer = 0

while prev != 0:

    next = int(input('������ ���� �����'))

    if next != 0 and prev < next:

        answer += 1

    prev = next

print('���������: ', answer)
#-----------------------------------------------------


#task13-----------------------------------------------
"""
������������������ ������� �� ��������� ����������� ����� � ����������� ������ 0. ���������� �������� ������� �� �������� �������� � ���� ������������������.
�������������, ��� � ������������������ ���� ���� �� ��� ��������.
"""
#first_max, ���:int. ��������� ��������� �������� 
#second_max, ���:int. ��������� ��������� �������� 
#element, ���:int. ������ ������������ �����
#����������
first_max=0

while 1==1:

    element=int(input('������ ���� �����'))

    if x > first_max:

        second_max = first_max

        first_max = element

    elif element > second_max:

        second_max = element
    if element == 0:

        print('���������: ', second_max)

        break
#-----------------------------------------------------


#task14-----------------------------------------------
"""
������������������ ������� �� ����������� ����� � ����������� ������ 0. 
����������, ������� ��������� ���� ������������������ ����� �� ����������� ��������.
"""
#max, ���:int. ��������� ��������� �������� 
#i, ���:int. ��������� ��������� �������� 
#element, ���:int. ������ ������������ �����
#����������
max=0

i=1

while 1==1:

    element=int(input('������ ���� �����'))

    if element>max:

        max=element

        i=1

    elif element==max:

        i+=1

    if element==0:

        print(i)

        break
#-----------------------------------------------------


#task15-----------------------------------------------
"""
�� ������� ����� n ���������� n-� ����� ��������� ?n.

��� ������ ����� ������ � ������ for.
"""
#n, ���:int. ������ ������������ ����� 
#a,b,c,i, ���:int. ��������� ��������� ��������
#����������
n=int(input())

a=1

b=1

c=1

i=2

if n==0:
    print("0")

else:

    while i<n:

        c=a+b

        a=b

        b=c

        i+=1

    print(c)
#-----------------------------------------------------


#task16-----------------------------------------------
"""
���� ����������� ����� A. 
����������, ����� �� ����� ������ ��������� ��� ��������, �� ���� �������� ����� ����� n, ��� ?n = A. 
���� � �� �������� ������ ���������, �������� ����� -1.
"""
#a,b,c,i, ���:int. ��������� ��������� �������� 
#X, ���:int. ������ ������������ �����
#����������
X=int(input())

a=1

b=1

c=0

i=2

while c<X:
    c=a+b

    a=b

    b=c

    i+=1

if c==X:

    print(i)

else:

    print("-1")
#-----------------------------------------------------


#task17-----------------------------------------------
"""
���� ������������������ ����������� �����, ������������� ������ 0. 
����������, ����� ���������� ����� ������ ������ ��������� ���� ������������������ ����� ���� �����.
"""
#y,i,j ���:int. ��������� ��������� �������� 
#x, ���:int. ������ ������������ �����
#����������
y=0

i=1

j=1

while 1==1:

    x=int(input())

    if x==y:

        i+=1

    else:

        if j<i:

            j=i

        i=1

    y=x

    if x==0:

        print(j)

        break
#-----------------------------------------------------