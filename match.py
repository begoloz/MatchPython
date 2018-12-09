def physical_characteristics() :
    questions = ("What is your gender?",
                 "What is your sexual preference?",
                 "What is your height?",
                 "What height do you prefer your partner to be?")
    posible_answers = ("\n1) Male \n2) Female \n3) Other \nPlease enter your answer: ",
                       "\n1) Tall \n2) Medium \n3) Short")
    answer_question_relation=(0,0,1,1)
    physical = ask_question(questions,posible_answers,answer_question_relation)
    print(ask_question(questions,posible_answers,answer_question_relation))
    return physical

def personality_questions():
    questions= ("Do you find it easy to introduce yourself to other people?",
                "Do you usually initiate conversations?",
                "Do you often do something out of sheer curiosity?",
                "Do you prefer being out with a large group of friends rather than spending time on your own?")
    posible_answers = ("\n 1) Yes \n 2) Most of time \n 3) Neutral \n 4) Some times \n 5) No \nPlease enter your answer: ",)
    answer_question_relation=(0,0,0,0)
    personality = ask_question(questions,posible_answers, answer_question_relation)
    print(ask_question(questions,posible_answers,answer_question_relation))
    return personality

        
def ask_question(questions,posible_answers,answer_question_relation):
    answers = ()
    for i in range(0,len(questions)):
        x=answer_question_relation[i]
        print(questions[i],posible_answers[x])
        answer = int(input())
        answers = answers + (answer,)
    return answers

physical_characteristics()
personality_questions()

