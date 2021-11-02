import sagemath
import math

#Berk Kalelioglu - 17050433 - assignment 1
def cos_calculation(x):
    sum = 0
    for k in range(100):
        sum = sum + (((-1)**k * (x)**(2*k))) / (math.factorial(2*k))
    print("cos({}): {}".format(x, sum))
cos_calculation(2)


#Berk Kalelioglu - 17050433 - assignment 2.1
def arctan(x):
    sum = 0
    for k in range(5000):
        a = (-1)**k
        b = x**((2*k)+1)
        c = (2*k)+1
        sum = sum + a*b/c
    print("arctan({}): {}".format(x, sum))
arctan(1)

#Berk Kalelioglu - 17050433 - assignment 2.2
def alternating_harmonic_series():
    sum = 0
    for k in range(1,2000):
        sum = sum + (-1)**(k+1) / k
    print("The alternating harmonic series is: ", sum)
alternating_harmonic_series()

def list_compehension():
    my_list_without_squares = [x for x in range(8)]
    my_list_squares = [x**2 for x in range(8)]
    my_list = [[my_list_without_squares[i], my_list_squares[i]] for i in range(len(my_list_squares))]
    print("the list of lists: ", my_list)
list_compehension()

# #Berk Kalelioğlu - 17050433 - assignment 3.1
def my_sequence():
    my_list = []
    my_list.append(x_0)
    my_list.append(x_1)


    for i in range(2,n+1):
        my_list.append((1/my_list[i-1] + 1/my_list[i-2]))
    return my_list

print("-----assignment 3.1------")
x_0 = int(input('enter your first x: '))
x_1 = int(input('enter your second x: '))
n = int(input('enter your range: '))
print(my_sequence())
print("-----------------------------------------------")

#Berk Kalelioğlu - 17050433 - assignment 3.2
def fib_less_than():
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print("-----assignment 3.2------")
n = int(input('enter your fib range: '))
print(fib_less_than())
print("-----------------------------------------------")

#Berk Kalelioğlu - 17050433 - assignment 3.3
def fib_less_than_prime(n):
    fib_prime = [0,1]
    pop_list = []
    prime_check = 0
    for i in range(2, n):
        fib_prime.append(fib_prime[i-1]+fib_prime[i-2])

    if fib_prime[i] > 2:
        for i in range(2,n):
            if fib_prime[i] > 2:
                for n in range(2, int(fib_prime[i] ** 1 / 2)):
                    if fib_prime[i] % n == 0:
                        pop_list.append(i)
                        break

        pop_list = sorted(pop_list, reverse= True)
        for i in range(len(pop_list)):
            temp = pop_list[i]
            fib_prime.pop(temp)

    return fib_prime

print("-----assignment 3.3------")
n = int(input('enter your prime fib range: '))
print(fib_less_than_prime(n))
print("-----------------------------------------------")

#Berk Kalelioğlu - 17050433 - assignment 3.4
def py_triples():
    c, m = 0, 2

    while c < n:
        for i in range(1,m):
            a = m*m - i*i
            b = 2*m*i
            c = m*m + i*i

            if c > n:
                break
            if a < b:
                print(a, b, c)
            else:
                print(b, a, c)
        m = m + 1


print("-----assignment 3.4------")
n = int(input("write your Pythagorean triple limit: "))
py_triples()
print("-----------------------------------------------")