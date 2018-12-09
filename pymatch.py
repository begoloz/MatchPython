import partners

QUESTIONS = (("\
     \nWhat is your gender?",
    "What is your sexual preference?",
    "What is your height?",
    "What height do you prefer your partner to be?"),\
    ("\nWe will now ask you some questions to try to determine your personality type.\
     \nDo you find it easy to introduce yourself to other people?",
    "Do you usually initiate conversations?",
    "Do you often do something out of sheer curiosity?",
    "Do you prefer being out with a large group of friends rather than spending time on your own?"))

CHOICES = (("\
    \n1) Male \n2) Female \n3) Other \nPlease enter your answer: ",
    "\n1) Tall \n2) Medium \n3) Short \nPlease enter your answer: "),\
    ("\n 1) Yes \n 2) Most of time \n 3) Neutral \n 4) Some times \n 5) No \nPlease enter your answer: ",))

CHOICES_QUESTIONS_RELATION = ((0,0,1,1),(0,0,0,0))
        
def ask_questions(questions,choices,choices_questions_relation):
    """Asks a question, displays the multiple choice answers, and saves the user's response.

    Parameters:
        questions (tuple): Two groups of strings for questions (physical characteristics and personality questions).
        choices (tuple): Two groups of strings for multiple choice answers.
        choices_questions_relation (tuple): two groups of integers that represent the correspondence betwen each one
            of the questions and its designated multiple choice answer.

    Return:
        tuple: All the responses given to the questions asked.
    
    """
    name = input("Welcome to PyMatch\n\nPlease enter your name: ")
    print ("\nHello ",name)
    user_answers = (name,)
    personality_answers=0
    # iterates through the physical characteristics questions first, and then through the personality questions.
    # if the answer is valid it saves it in the user_answers variable
    for j in range(0,len(questions)):
        for i in range(0,len(questions[j])):
            x = choices_questions_relation[j][i]
            print(questions[j][i],choices[j][x])
            answer = int(input())
            if j==0:
                # checks that the input for the response is valid for the first group of questions (1,2, or 3).
                if answer<=3 and answer>=1:
                    user_answers= user_answers + (answer,)
                else:
                    print("invalid answer")
                    exit()
            #calculates the score for the second group of questions and saves the result in personality_answers.
            else:
                # checks that the input for the response is valid for the second group of questions (1,2,3,4 or 5).
                if answer<=5 and answer>=1:
                    personality_answers=personality_answers+answer
                else:
                    print("invalid answer")
                    exit()
    user_answers= user_answers + (personality_answers*2,)
    #user_answers = (name(str), gender(int), prefered gender(int), height(int), prefered height(int), personality score(int))
    return user_answers

def characteristic_to_number(characteristic):
    """Transforms a string answer to its equivalent integer representation.

    Parameters:
        characteristic (str): The answer to be convrted in to a numeric choice.

    Return:
        int: The number of answer choice.
    """
    if characteristic == 'male' or characteristic == 'tall':
        number=1
    elif characteristic == 'female' or characteristic == 'medium':
        number=2
    else:
        number=3
    return number

def get_partners():
    """
    Gets the database of all potential partners.

    Return:
        tuple: Group of tuples for the partnes and all the information for each one of them.

    Precondition:
        import partners

    """
    potential_partners = partners.Partners()
    all_partners =()
    while potential_partners.available() :
        #potential_partner_answers = (name(str), sex preference(int), gender(int), prefered height(int), height(int),personality score(int)).
        potential_partner_answers = (potential_partners.get_name(),\
                                     (characteristic_to_number(potential_partners.get_sexual_pref())),\
                                     (characteristic_to_number(potential_partners.get_gender())),\
                                     (characteristic_to_number(potential_partners.get_height_pref())),\
                                     (characteristic_to_number(potential_partners.get_height())),\
                                     (potential_partners.get_personality_score()) )
        all_partners = all_partners + ((potential_partner_answers),)
    return all_partners 

def match(user_answers,all_partners):
    """
    Finds the best match for the user.

    Iterates through the potential partners database contained, to find the closest match to the user's answers.

    Parameters:
        user_answers (tuple): all the answers given by the user for all of the questions.
        all_partners (tuple): gropup of all the potential partners, with all of the answers given by each one of them, for all of the questions given.

    Return:
        str: name of the closest match for the user.
        None: When there is no possible match for the user.
    """
    #initiates "last_score" with the biggest possible score difference plus 1 (41).
    last_score=10*(len(user_answers)-2)+1
    match=None
    for i in range (0, len(all_partners)):
        #checks for gender preference match
        if (user_answers[1]==all_partners[i][1] and user_answers[2]==all_partners[i][2]):
            score_difference = abs(user_answers[5]-all_partners[i][5])   
            if last_score > score_difference:
               last_score = score_difference
               partner = i                               
            elif last_score == score_difference:
                #checks for height preference match
                if user_answers[4]==all_partners[i][4]:
                    if user_answers[4]!=all_partners[partner][4]:
                       partner = i                    
                elif user_answers[3]==all_partners[i][3]:
                    if user_answers[3]!=all_partners[partner][3]:
                        partner = i
            match = all_partners[partner][0]
    return match

print(match(ask_questions(QUESTIONS,CHOICES,CHOICES_QUESTIONS_RELATION),get_partners()))
