import json
with open('quiz_questions.json') as file:
    questions = json.load(file)
def main():
    while True:
        print("Hello, do you wanna play a game?")
        answer = str(input("YES or NO: ")).lower()
        if answer.startswith('y'):
            score = play()
            score = score.count(True)
            print(f"You got {score} right! \n")
        else:
            print("Thanks, see you soon")
            break
def play():
    score = []
    for qst in questions.values():
        question = qst.keys()
        print(list(question)[0])
        answer = str(input("Type your answer: ")).lower()
        # print(list(qst.values())[0])
        if answer in list(qst.values())[0]:
            score.append(True)
            print("Correct! \n")
        elif answer == "exit":
            break
        else:
            score.append(False)
            print("Wrong! \n")
    return score
if __name__ == "__main__":
    main()


#Pacific always wrong
#ant work for elephant