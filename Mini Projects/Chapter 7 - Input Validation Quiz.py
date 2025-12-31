import random

active = True
# q?[0] is the question, q?[1] is the answer
q1 = ("What does the input() function always return?\nA. An integer\nB. A float\nC. A string\nD. The data type of the user’s input", "C")
q2 = ("What do you get if the user inputs 5 into this code? print(type(input('Enter your Age: ')))\nA. <class 'int'>\nB. <class 'float'>\nC. <class 'str'>\nD. It causes an error", "C")
q3 = ("Which loop is best when you don’t know in advance how many times the loop should run?\nA. for loop\nB. while loop\nC. if statement\nD. range loop", "B")
q4 = ("What is the purpose of a sentinel value in a while loop?\nA. To speed up the loop\nB. To count iterations\nC. To signal when the loop should stop\nD. To prevent syntax errors", "C")
q5 = ("What happens if a while loop’s condition never becomes False?\nA. The program skips the loop\nB. The loop runs once\nC. The loop runs forever\nD. Python throws a syntax error", "C")
questions = [q1, q2, q3, q4, q5]
score = 0
tries = 0
while active:
    i = random.randint(0, len(questions) - 1)
    print(questions[i][0])
    user_input = input("Enter your choice: ")
    if user_input == questions[i][1]:
        print("Correct!")
        del questions[i]
        score += 1
        tries += 1
    elif user_input == "A" or user_input == "B" or user_input == "C" or user_input == "D":
        print("Incorrect!")
        tries += 1
    else:
        print("Answer could not be understood!")
    if len(questions) == 0:
        print("Congratulations, you finished the quiz!")
        print(f"Your final score is {score}/{tries}")
        active = False