#TASK 1
# Check if a number is even or odd
num = int(input("Enter the number to check,is it even or odd?: "))
if num%2==0:
    print(f"{num} is an Even Number.")
else:
    print(f"{num} is an Odd Number.")




#TASK 2
# Sum of integers from 1 to 50
sum = 0
for num in range(1,51):
    sum =sum+num
print(f"The sum of numbers from 1 to 50 is: {sum}")