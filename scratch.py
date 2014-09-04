a = raw_input("Enter text: ")
words = a.split(" ")

new = []
vowels = ['a', 'e', 'i', 'o', 'u']
for w in words:
	if w[0] in vowels:
		s = w + "way"
	else:
		init = w[0]
		s = w[1:] + init + "ay"
	new.append(s)

for n in new:
	print n, 
	