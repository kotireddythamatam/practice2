import re
regex = re.compile(r"^(4|5|6)\d{3}-\d{4}-\d{4}-\d{4}")
while True:
	card_number = input('enter your card number:')
	if len(card_number) == 19:
		print(len(card_number))
		a = regex.search(card_number)
		if a:
			print('matched')
			break
		else:
			print('not matched')
	else:
		print('plese provide 14 digits')