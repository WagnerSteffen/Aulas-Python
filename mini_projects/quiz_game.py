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
        answer_bool = False
        question = qst.keys()
        print(list(question)[0])
        answer = str(input("Type your answer: ")).lower()
        if answer == "exit":
            break
        # print(list(qst.values())[0])
        for i in list(qst.values())[0]:
            if answer == i:
                answer_bool = True
                score.append(True)
            # print(i)
        if answer_bool:
            print("Correct! \n")
        else:
            score.append(False)
            print("Wrong! \n")
    return score


if __name__ == "__main__":
    main()
