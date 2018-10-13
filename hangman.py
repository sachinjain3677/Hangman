import random

words = open("/usr/share/dict/words").read().splitlines()

print ("Welcome to my first python mini-project, Hangman!!")

name = input("What is your name: ")

blank = input("Hello "+name+". Press Enter to continue")

word=random.choice([a for a in words if a.isalpha()])

print("Word guessed.")

w_len = len(word)

visible = [0 for i in range(w_len)]

for i in range(w_len):
	print("_",end="")

print()

turns=10
failed=0
len_matched=0;
print("Turns remaining: "+str(turns))

match=False;

letters_guessed = []

while failed<turns:
	print("Letters already guessed: ",end="")
	for c in letters_guessed:
		print(c+", ",end="")
	print()
	if(len_matched==w_len):
		break;
	match=False;
	guess=input("Guess letter: ")
	print()

	if(guess in letters_guessed):
		print("Letter already guessed. Make another guess")
		match=True

	if not guess.isalpha():
		print("Invalid. Make another guess")
		match=True
	else:	
		for i in range(w_len):
			if word[i].lower()==guess and visible[i]==0:
				match=True;
				visible[i]=1;
				len_matched+=1;
				if(guess not in letters_guessed):
					letters_guessed.append(guess)


	for i in range(w_len):
		if visible[i]==1:
			print(word[i],end="")
		else:
			print("_",end="")

	print()
	
	if match==False:
		failed+=1;
		if(guess not in letters_guessed):
			letters_guessed.append(guess)
	print("Turns remaining: "+ str(turns-failed));

if len_matched<w_len:
	print("Failed to guess. word was: "+word)
else:
	print("Successfully guessed :)")