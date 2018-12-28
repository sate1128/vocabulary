import random
vocabularies = []
with open('vocabulary.txt','r') as inputfile:
    for line in inputfile:
        word, meaning = line.split('/')
        vocabularies.append([word,meaning])
try:
    while True:
        question = vocabularies[random.randint(0,len(vocabularies))-1]
        head = question[0][0]
        answer = input('Q:'+question[1]+'\n'+head)
        if head+answer == question[0]:
            print('Correct!')
        else:
            print('Wrong! Answer is:',question[0])
except KeyboardInterrupt:
    pass