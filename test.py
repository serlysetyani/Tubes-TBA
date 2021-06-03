import string

sentence = 'adik kakak adik'
inputString = sentence.lower()+'#'

alphabetList = list(string.ascii_lowercase)
stateList = ['q0', 'q1', 'q2',  'q3', 'q4', 'q5', 'q6', 'q7', 'q8']

transitionTable = {}

for state in stateList:
    for alphabet in alphabetList:
        transitionTable[(state, alphabet)] = 'error'
    transitionTable[(state, '#')] = 'error'
    transitionTable[(state, ' ')] = 'error'

transitionTable['q0', ' '] = 'q0'

transitionTable[('q0', 'k')] = 'q1'
transitionTable[('q1', 'a')] = 'q2'
transitionTable[('q2', 'k')] = 'q3'
transitionTable[('q3', 'a')] = 'q4'
transitionTable[('q4', 'k')] = 'q7'
transitionTable[('q7', ' ')] = 'q8'
transitionTable[('q7', '#')] = 'accept'
transitionTable[('q8', ' ')] = 'q8'
transitionTable[('q8', '#')] = 'accept'

transitionTable[('q8', 'k')] = 'q1'
transitionTable[('q8', 'a')] = 'q5'

transitionTable[('q0', 'a')] = 'q5'
transitionTable[('q5', 'd')] = 'q6'
transitionTable[('q6', 'i')] = 'q4'
transitionTable[('q4', 'k')] = 'q7'


idxChar = 0
state = 'q0'
currenToken = ''
while state != 'accept':
    currenChar = inputString[idxChar]
    currenToken += currenChar
    state = transitionTable[(state, currenChar)]
    if state == 'q7':
        print('Current token:', currenToken, ', valid')
        currenToken = ' '
    if state == 'error':
        print('error')
        break
    idxChar += 1

if state == 'accept':
    print('Semua token di input: ', sentence, ', valid')
