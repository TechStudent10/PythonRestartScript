import random

numbers = []
for i in range(1, 100):
	numbers.append(i)

def checkAnswer(answer):
	global RANDOM_NUMBER
	if answer != RANDOM_NUMBER:
		if answer > RANDOM_NUMBER:
			return "The number is smaller"
		elif answer < RANDOM_NUMBER:
			return "The number is bigger"
	else:
		return "The answer is correct"

def Game(maxGuesses=5, guess=""):
	guesses = 0

	RANDOM_NUMBER = random.choice(numbers)
	print(RANDOM_NUMBER)

	print("I am thinking of a number between 1 and 100. What number is it?")

	while guess != RANDOM_NUMBER:
		if guesses >= maxGuesses:
			print("You are out of guesses.")
			break

		guess = input("Guess> ")
		guesses += 1
		isAnswerCorrect = checkAnswer(int(guess))
		print(isAnswerCorrect)
		
		if isAnswerCorrect == "The answer is correct":
			print('You have won!')
			break

def main():
	while 1:
		game = Game()
		playAgain = input("Do you want to play again (Y/N)? ")
		if playAgain.lower() == "y":
			continue
		else:
			break

if __name__ == '__main__':
	main()