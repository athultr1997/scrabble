import sys
import re

letter_values = {
	"e":1,"a":1,"i":1,"o":1,"n":1,"r":1,"t":1,"l":1,"s":1,"u":1,
	"d":2,"g":2,
	"b":3,"c":3,"m":3,"p":3,
	"f":4,"h":4,"v":4,"w":4,"y":4,
	"k":5,
	"j":8,"x":8,
	"q":10,"z":10,
}


def find_scrabble_value(word):
	global letter_values
	scrabble_value = 0
	for w in word:
		scrabble_value += letter_values[w]

	return scrabble_value


def scrabble_sort(words):
	n = len(words)
	for i in range(n):
		for j in range(0, n-i-1):
			if find_scrabble_value(words[j])<find_scrabble_value(words[j+1]):
				a = words[j]
				words[j] = words[j+1]
				words[j+1] = a

	return words


def create_reg_exp_object(pattern):
	reg_exp = ""
	for s in pattern:
		if s=="_":
			reg_exp += "\D"
		else:
			reg_exp += s

	return re.compile(reg_exp)


def check_validity(required_letters,word):
	for w in word:
		if w not in required_letters:
			if "*" in required_letters:
				required_letters = required_letters.replace("*","",1)
			else:
				return False
		else:
			required_letters = required_letters.replace(w,"",1)

	return True


if __name__ == '__main__':
	pattern = None
	required_letters = None

	if len(sys.argv)<=1:
		print("Please enter the pattern to search")
		print("Usage: python3 srabble_helper.py <pattern> <letters required>")
		sys.exit()
	else:
		pattern = sys.argv[1]
		required_letters = sys.argv[2]

		for p in pattern:
			if p!="_":
				required_letters += p

	pattern_reg_object = create_reg_exp_object(pattern)

	word_list = open("word_list.txt","r")
	possible_words = list()

	for word in word_list:
		word = word.rstrip()

		if check_validity(required_letters,word)==True:
			if pattern_reg_object.search(word) != None:
				possible_words.append(word)

	possible_words = scrabble_sort(possible_words)

	for w in possible_words:
		print(w,find_scrabble_value(w))