import requests
import json
import html
import random
import pprint
sep = '---------------------------------------'
url = 'https://opentdb.com/api.php?amount=1&category=27&difficulty=easy&type=multiple'
print(sep)
#pprint.pprint(question)
''' pip install html
for solve html error text '''


''' Take note
3. Edit answer = correct answer = +1 score
'''
score = 0
inc_score = 0
while True:
    r = requests.get(url)
    #print(r.status_code)
    question = json.loads(r.text)
    question1 = question['results'][0]['question']
    # Question Title
    print(html.unescape(question1) + "\n")
    print('Choose the number of answer choices')

    #Choice part
    choice_lib = []
    choice_lib.append(question['results'][0]['correct_answer'])
    choice_lib.append(question['results'][0]['incorrect_answers'][0])
    choice_lib.append(question['results'][0]['incorrect_answers'][1])
    choice_lib.append(question['results'][0]['incorrect_answers'][2])
    random.shuffle(choice_lib)
    #print(choice_lib)
    correct_answer = question['results'][0]['correct_answer'] #naming
    #print(correct_answer)

    #Show choice
    num_c = 1
    for x in choice_lib:
        print(str(num_c) + '. ' + x )
        num_c += 1



    while True:
        answer = input('Choose the number >> ')
        try:
            answer = int(answer)
            if answer <= 0 or answer > 4:
                continue
            else:
                break
        except:
            print('Undefined answer. Try again!')
            continue

    if answer == 1:
        answer = [choice_lib[0]]
    elif answer == 2:
        answer = [choice_lib[1]]
    elif answer == 3:
        answer = [choice_lib[2]]
    elif answer == 4:
        answer = [choice_lib[3]]


    if answer[0] == correct_answer:
        print('Correct!')
        score = score + 1
        print('Your score =', score)
        print(" ")
    else:
        print(answer[0], 'is incorrect answer. The correct answer is :',correct_answer)
        print(' ')
        inc_score = inc_score +1

    print('Do you want to play more?')
    try_more = input("Type 'No' if you want to quit >> ").lower()
    print(" ")
    if try_more == 'no':
        break

print('##############################')
print('Thank for playing')
print('Your score =', score)
print('Incorrect score =', inc_score)
print('##############################')


'''debug
print(answer)
print(type(answer))
print(type(correct_answer))
'''