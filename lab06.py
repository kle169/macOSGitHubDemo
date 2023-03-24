def main():
	#This is branch0
	print('Menu')
	print('-------------')
	print('1. Encode')
	print('2. Decode')
	print('3. Quit')


def encode_password(password):
	encoded_password = ""
	for digit in password:
		# Convert the digit to an integer, shift it up by 3, and wrap around if necessary
		encoded_digit = str((int(digit) + 3) % 10)
		encoded_password += encoded_digit
	return encoded_password


while True:
	option = int(input('Please enter an option: '))
	if option == 1:
		password = input('Please enter your password to encode: ')
		new_password = encode_password(password)
		print(new_password)

	elif option == 2:
		pass
	elif option == 3:
		break


if __name__ == "__main__":
	main()
