sentence = input("Input:")
tokens = sentence.lower().split()
tokens.append('EOS')

nonTerminals = ['S', 'NN', 'VB']
terminals = ['mom', 'dad', 'jenny', 'books', 'cake',
             'cola', 'cookies', 'drinks', 'eats', 'reads']

parseTable = {}

parseTable[('S', 'mom')] = ['NN', 'VB', 'NN']
parseTable[('S', 'dad')] = ['NN', 'VB', 'NN']
parseTable[('S', 'jenny')] = ['NN', 'VB', 'NN']
parseTable[('S', 'books')] = ['error']
parseTable[('S', 'cake')] = ['error']
parseTable[('S', 'cola')] = ['error']
parseTable[('S', 'cookies')] = ['NN', 'VB', 'NN']
parseTable[('S', 'drinks')] = ['NN', 'VB', 'NN']
parseTable[('S', 'eats')] = ['NN', 'VB', 'NN']
parseTable[('S', 'reads')] = ['NN', 'VB', 'NN']
parseTable[('S', 'EOS')] = ['error']

parseTable[('VB', 'mom')] = ['error']
parseTable[('VB', 'dad')] = ['error']
parseTable[('VB', 'jenny')] = ['error']
parseTable[('VB', 'books')] = ['error']
parseTable[('VB', 'cake')] = ['error']
parseTable[('VB', 'cola')] = ['error']
parseTable[('VB', 'cookies')] = ['error']
parseTable[('VB', 'drinks')] = ['drinks']
parseTable[('VB', 'eats')] = ['eats']
parseTable[('VB', 'reads')] = ['reads']
parseTable[('VB', 'EOS')] = ['error']

parseTable[('NN', 'mom')] = ['mom']
parseTable[('NN', 'dad')] = ['dad']
parseTable[('NN', 'jenny')] = ['jenny']
parseTable[('NN', 'books')] = ['books']
parseTable[('NN', 'cake')] = ['cake']
parseTable[('NN', 'cola')] = ['cola']
parseTable[('NN', 'cookies')] = ['cookies']
parseTable[('NN', 'drinks')] = ['error']
parseTable[('NN', 'eats')] = ['error']
parseTable[('NN', 'reads')] = ['error']
parseTable[('NN', 'EOS')] = ['error']

stack = []
stack.append('#')
stack.append('S')

idxToken = 0
symbol = tokens[idxToken]

while (len(stack) > 0):
    top = stack[len(stack)-1]
    print('top = ', top)
    print('symbol = ', symbol)
    if top in terminals:
        print('top adalah simbol terminal')
        if top == symbol:
            stack.pop()
            idxToken += 1
            symbol = tokens[idxToken]
            if symbol == 'EOS':
                print('isi stack: ', stack)
                stack.pop()
        else:
            print('error')
            break
    elif top in nonTerminals:
        print('top adalah simbol non-terminal')
        if parseTable[(top, symbol)][0] != 'error':
            stack.pop()
            symboltobePushed = parseTable[(top, symbol)]
            for i in range(len(symboltobePushed)-1, -1, -1):
                stack.append(symboltobePushed[i])
        else:
            print('error')
            break
    else:
        print('error')
        break
    print('isi stack: ', stack)
    print()

print()
if symbol == 'EOS' and len(stack) == 0:
    print('Input string ', sentence, ' diterima, sesuai grammar')
else:
    print('Error, Input string: ', sentence, ' diterima, tidak sesuai grammar')
