
def checkEvenOrOdd(value:int):
	if value % 2 == 0:
		return "Even"
	else:
		return "Odd"

num = input("Enter the number to be checked: ")

print(checkEvenOrOdd(int(num)))
