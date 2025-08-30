
num = input("Enter the number to find the factorial: ")

fact = 1

for iter in range(1, int(num)+1):
	fact *= iter

print("The factorial of the number is", fact)
