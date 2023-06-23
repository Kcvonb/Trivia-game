print("Welcome to Python Trivia!")
print("\n")

def welcome():
    name = input("What is your name Player > ")
    print("\n")
    print(f"Wecome {name}! Let's get started!") 

welcome()

def trivia_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("")
        print(key)
        for i in answers[question_num - 1]:
            print(i)
        print("\n")
        guess = input("Enter a, b, c, or d > ")

        guess = guesses
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),(guess))
        question_num += 1 

    show_score(correct_guesses, guesses)
    
def check_answer(answer, guess):
    if [answer] == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

def show_score(correct_guesses, guesses):
    print("")
    print("Results")
    print("")
    print("answers:", end="")
    for i in questions: 
        print(questions.get(i), end="")
    print()

    print("guesses: ", end="")
    for i in guesses: 
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

questions = {
    'Question 1: What are some basic data types?': "a", 
    'Question 2: When would we use a disctionary?': "b", 
    'Question 3: What is Global Scope?' : "d", 
    'Question 4: What are common Python errors?': "a"
}

answers = [["A. String, Integer, Float, Boolean, None.", "B. String, Number, Float, Boolean, Some.", "C. Sum, Subtraction, Modulus, Multiplication, Division.", "D. List, Tuples, Dictionaries, String, Float."],
           ["A. When the data is changing over time AND homogenous.", "B. When you need to associate two or more pieces of data.", "C. When you are keeping track of one thing." ,"D. When the data is heterogeneous."],
           ["A. A variable.", "B. Any variable inside the function body is in the local scope, including the function’s parameters", "C. A telescope", "D. Any variable defined outside of functions are globally available"],
           ["A. SyntaxError, IdentificationError, TypeError, NameError, IndexError", "B. SyntaxError, VariableError, FloatError, ErrorError, NameError", "C. TypeError, IdentificationError, BugError, RobotError, ComputerError", "D. SyntaxError, CodeError, TaxcodeError, PythonError, SnekError"]]

trivia_game()
