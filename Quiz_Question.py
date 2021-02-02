import json
import time

TOPICS_LIST = ['science', 'history', 'commerce', 'technology', 'worldgk']

def load_question(filename):
    question =None
    with open(filename,"r") as read_file:
        question = json.load(read_file)

    return question

def score_one_question(key,meta):
    actual = meta["answer"]

    if actual.lower() == meta["user_response"].lower():
        print(key, "Absolutely Correct")
    else:
        print(key , "Is Incorrect!")
        print(actual , "Is correct!")
        print("Learn more :",meta["more_info"])
        return -1

def ask_one_question(question):
    print("The Question :",question)
    chooce=input(['a','b','c','d'])
    while True:
        if chooce.lower() in ['a','b','c','d']:
            return chooce
        else:
            print("Invalid Input")
            chooce = input(['a', 'b', 'c', 'd'])

def test(questions):
    score = 0
    print(
        "General Instructions:\n1. Please enter only the choice letter corresponding to the correct answer.\n2. Each question carries 2 points\n3. Wrong answer leads to -1 marks per question\nQuiz will start momentarily. Good Luck!\n")
    time.sleep(10)
    for key,meta in questions.items():
        questions[key]["user_response"] = ask_one_question(meta["question"])

    print("\n***************** RESULT ********************\n")

    for key, meta in questions.items():
        score += score_one_question(key,meta)

    print("Total Score = ",score)

def play_quiz():
    flag=False
    try:
        choice = int(input("Welcome to Today's Quiz!\nChoose your domain of interest:\n(1). Science\n(2). History of India\n(3). Commerce\n(4). Technology\n(5). World Gk\nEnter Your Choice [1/2/3/4/5]: "))
        if choice>len(TOPICS_LIST) or choice <1:
            print("Invalid Input")
            flag=True
    except ValueError as a:
        print("Invalid Input")
        flag = True

    if not flag:
        questions = load_question('topics/' + TOPICS_LIST[choice - 1] + '.json')
        test(questions)
    else:
        play_quiz()

def user_begin():
    print("Do you want to test your GK?\n a)yes \n b)no ")
    choice=input()
    if choice.lower()=='a' or choice.lower() == 'y':
        play_quiz()
    elif choice.lower()=='b' or choice.lower()=='n':
        print("Thank You")
    else:
        print("Invalid Input")
        user_begin()

def excute():
    user_begin()

if __name__ == "__main__":
    print("\t\t Welcome in Quiz Game \t\t")
    name = input("Enter Your Name ")
    print("Welcome "+name)
    excute()