import string

sentence = input("Input: ")
inputString = sentence.lower()+'#'

alphabetList = list(string.ascii_lowercase)
stateList = ['q0', 'q1', 'q2',  'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17',
             'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35',
             'q36', 'q37', 'q38', 'q39', ]

transitionTable = {}

for state in stateList:
    for alphabet in alphabetList:
        transitionTable[(state, alphabet)] = 'error'
    transitionTable[(state, '#')] = 'error'
    transitionTable[(state, ' ')] = 'error'

# initial state
transitionTable['q0', ' '] = 'q0'

# reads
transitionTable[('q0', 'r')] = 'q1'
transitionTable[('q1', 'e')] = 'q2'
transitionTable[('q2', 'a')] = 'q3'
transitionTable[('q3', 'd')] = 'q4'
transitionTable[('q4', 's')] = 'q5'
transitionTable[('q5', ' ')] = 'q28'
transitionTable[('q5', '#')] = 'accept'
transitionTable[('q28', ' ')] = 'q28'
transitionTable[('q28', '#')] = 'accept'

# cake
transitionTable['q0', 'c'] = 'q6'
transitionTable['q6', 'a'] = 'q7'
transitionTable['q7', 'k'] = 'q8'
transitionTable['q8', 'e'] = 'q9'
transitionTable['q9', ' '] = 'q28'
transitionTable['q9', '#'] = 'accept'

# cookies
transitionTable['q6', 'o'] = 'q10'
transitionTable['q10', 'o'] = 'q11'
transitionTable['q11', 'k'] = 'q12'
transitionTable['q12', 'i'] = 'q13'
transitionTable['q13', 'e'] = 'q14'
transitionTable['q14', 's'] = 'q5'

# cola
transitionTable['q10', 'l'] = 'q34'
transitionTable['q34', 'a'] = 'q35'
transitionTable['q35', 's'] = 'q5'

# mom
transitionTable['q0', 'm'] = 'q15'
transitionTable['q15', 'o'] = 'q16'
transitionTable['q16', 'm'] = 'q17'
transitionTable['q17', ' '] = 'q28'
transitionTable['q17', '#'] = 'accept'

# dad
transitionTable['q0', 'd'] = 'q18'
transitionTable['q18', 'a'] = 'q19'
transitionTable['q19', 'd'] = 'q20'
transitionTable['q20', ' '] = 'q28'
transitionTable['q20', '#'] = 'accept'

# eats
transitionTable['qo', 'e'] = 'q21'
transitionTable['q21', 'a'] = 'q22'
transitionTable['q22', 't'] = 'q23'
transitionTable['q23', 's'] = 'q5'

# books
transitionTable['q0', 'b'] = 'q24'
transitionTable['q24', 'o'] = 'q25'
transitionTable['q25', 'o'] = 'q26'
transitionTable['q26', 'k'] = 'q27'
transitionTable['q27', 's'] = 'q5'

# drinks
transitionTable['q18', 'r'] = 'q29'
transitionTable['q29', 'i'] = 'q30'
transitionTable['q30', 'n'] = 'q31'
transitionTable['q31', 'k'] = 'q32'
transitionTable['q32', 's'] = 'q5'

# jenny
transitionTable['q0', 'j'] = 'q36'
transitionTable['q36', 'e'] = 'q37'
transitionTable['q37', 'n'] = 'q38'
transitionTable['q38', 'n'] = 'q39'
transitionTable['q39', 'y'] = 'q40'
transitionTable['q40', ' '] = 'q28'
transitionTable['q40', '#'] = 'accept'

# finalstate back to
transitionTable['q28', 'r'] = 'q1'
transitionTable['q28', 'c'] = 'q6'
transitionTable['q28', 'm'] = 'q15'
transitionTable['q28', 'd'] = 'q18'
transitionTable['q28', 'j'] = 'q36'
transitionTable['q28', 'b'] = 'q24'
transitionTable['q28', 'e'] = 'q21'

idxChar = 0
state = 'q0'
currenToken = ''
while state != 'accept':
    currenChar = inputString[idxChar]
    currenToken += currenChar
    state = transitionTable[(state, currenChar)]
    if state == 'q28':
        print('Current token:', currenToken, ', valid')
        currenToken = ' '
    if state == 'error':
        print('error')
        break
    idxChar += 1

if state == 'accept':
    print('Semua token di input: ', sentence, ', valid')
