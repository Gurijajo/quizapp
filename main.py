questions = ("When did they open the London underground?: ",
             "When was Netflix founded?: ",
             "Which football team is known as ‘The Red Devils’?: ",
             "How many keys does a classic piano have?: ",
             "When was the first issue of Vogue published?: ")

options = (("A. 1863 ", "B. 1858 ", "C. 1864 ", "D. 1898 "),
           ("A. 2001 ", "B. 1997 ", "C. 2009 ", "D. 2015 "),
           ("A. Manchester City ", "B. Real Madrid ", "C. Ajax", "D. Manchester United "),
           ("A. 78 ", "B. 85 ", "C. 88 ", "D. 92 "),
           ("A. 1892 ", "B. 1960 ", "C. 2000 ", "D. 2004 "))

answers = ("A", "B", "D", "C", "A")
guesses = []
score = 0

for question_num, question in enumerate(questions):
    print("Quiz App\n______________")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is: {answers[question_num]}")

print("______________\nResults\n______________")
print("Answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score_percentage = (score / len(questions)) * 100
print(f"\nYour score is: {score_percentage}%")
