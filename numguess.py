import random

guess = int(input('Guess a number between 1 and 100: '))
num = random.randint(1,100)
tries = 0

while guess != num:
	if guess < num:
		guess = int(input('Higher! Guess again: '))
		tries += 1
	elif guess > num:
		guess = int(input('Lower! Guess again: '))
		tries += 1
		
print('You got it in ',tries,'! the number was ',num)
