'''print("Hello world")
print("Hello, how are you?")
name="fareed"
print("Hell0 " +name)
print(4+9)
print(9/4)
print(3**10)



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)'''



'''num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")'''

'''principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
interest = (principal * rate * time) / 100
print("Simple Interest:", interest)


n = int(input("Enter a positive integer: "))
total_sum = 0
for i in range(1, n+1):
    total_sum += i
print("Sum of first", n, "natural numbers is:", total_sum)



num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is: {factorial}")


num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
    
    
numbers = [10, 25, 17, 9, 30, 12]
largest = max(numbers)
print("The largest number is:", largest)


fruits = ['apple', 'banana', 'cherry', 'apple', 'cherry', 'banana', 'apple']
count_apple = fruits.count('apple')

print("Number of apples:", count_apple)
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)  
print("List after removing 3:", my_list)


del my_list[1]  
print("List after removing element at index 1:", my_list)



my_list = [1, 2, 4, 5]
my_list.insert(2, 3)

print("Updated list:", my_list)



def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"Factorial of {num} is:", factorial(num))



def is_palindrome(s):
    return s == s[::-1]

word = "radar"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")'''
    
    
    
import re

def rearrange_name(name):

    result = re.search(r"^([\w .]*), ([\w .]*)$", name)

    if result == None:

        return name

    return "{} {}".format(result[2], result[1])