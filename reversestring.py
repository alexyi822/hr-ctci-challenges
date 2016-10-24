# TWO SOLUTIONS
import sys

def reverse(str):
	return str[::-1]

def reverse2(str):
	chars = []
	chars.extend(str)
	size = len(chars)

	for i in range(0,size/2):
		temp = chars[i]
		chars[i] = chars[size-1-i]

		# can also do
		# chars[i], chars[size-1-i] = chars[size-1-i], chars[i]
		chars[size-1-i] = temp

	return ''.join(chars)

def main():
	str = sys.argv[1]

	print(reverse(str))
	print(reverse2(str))

if __name__ == "__main__":
	main()