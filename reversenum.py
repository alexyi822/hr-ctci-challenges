import sys

def reverse(num):
	rev = 0
	if abs(num) < 10:
		return num

	temp = num
	while abs(temp) > 0:
		mod = temp % 10
		rev = (rev * 10) + mod
		temp = temp/10
		

	return rev

def main():
	num = int(sys.argv[1])

	print(reverse(num))

if __name__ == "__main__":
	main()


