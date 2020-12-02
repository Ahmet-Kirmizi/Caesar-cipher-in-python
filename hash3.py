import string
import collections 


def hashFunc(string_to_translate, shift_num):
	lower = collections.deque(string.ascii_lowercase)
	upper = collections.deque(string.ascii_uppercase)

	upper.rotate(shift_num)
	lower.rotate(shift_num)

	upper = ''.join(list(upper))
	lower = ''.join(list(lower))

	return string_to_translate.translate(str.maketrans(string.ascii_lowercase, lower)).translate(str.maketrans(string.ascii_uppercase, upper))

	

print(hashFunc('Wassup',3))