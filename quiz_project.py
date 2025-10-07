# a dictionary that stores questions and answers 
# have  a variable that tracks the score of the player 
# loop through the dictionary using the key values pairs 
# display each questions to the user and allow them to answer 
# tell them if they are right or wrong 
# show the final result when quiz is completed 

quiz = {
    'question1':{ 
        'question': 'what is the capital of france?',
        'answer': 'paris'
    },'question2':{ 
        'question': 'what is the capital of India?',
        'answer': 'Delhi'
    },'question3':{ 
        'question': 'what is the capital of United Kingdom?',
        'answer': 'London'
    },'question4':{ 
        'question': 'what is the capital of America?',
        'answer': 'California'
    },'question5':{ 
        'question': 'what is the capital of Andhra Pradesh?',
        'answer': 'Vizag'
    },'question6':{ 
        'question': 'what is the capital of Tamilnadu?',
        'answer': 'Chennai'
    },'question7':{ 
        'question': 'what is the capital of Karnataka?',
        'answer': 'Banglore'
    },
}

score = 0 

for key,value in quiz.items():
    print(value['question'])
    answer = input('Answer? ')
    
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1 
        print('Your score is: '+str(score))
    else:
        print('Wrong!')
        print('The answer is :' + value['answer'])
        print('Your score is: ' + str(score))
        print('')
        print('')
        
print('you got' + str(score) + 'out of 7 questions correctly')
print('your percentage is' + str(int(score/7 * 100))+'%')
        
        
        
