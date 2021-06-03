sentence = 'adik membaca buku'
tokens = sentence.lower().split()
tokens.append('EOS')

nonTerminals = ['S', 'NN', 'VB']
terminals = ['adik', 'kakak', 'bakso', 'tahu', 'buku',
             'sepatu', 'topi', 'membaca', 'makan', 'memakai']

parseTable = {}

parseTable[('S', 'kakak')] = ['NN', 'VB', 'NN']
parseTable[('S', 'adik')] = ['NN', 'VB', 'NN']
parseTable[('S', 'bakso')] = ['NN', 'VB', 'NN']
parseTable[('S', 'tahu')] = ['NN', 'VB', 'NN']
parseTable[('S', 'buku')] = ['NN', 'VB', 'NN']
parseTable[('S', 'sepatu')] = ['NN', 'VB', 'NN']
parseTable[('S', 'topi')] = ['NN', 'VB', 'NN']
parseTable[('S', 'membaca')] = ['error']
parseTable[('S', 'makan')] = ['error']
parseTable[('S', 'memakai')] = ['error']
parseTable[('S', 'EOS')] = ['error']

parseTable[('NN', 'kakak')] = ['kakak']
parseTable[('NN', 'adik')] = ['adik']
parseTable[('NN', 'bakso')] = ['bakso']
parseTable[('NN', 'tahu')] = ['tahu']
parseTable[('NN', 'buku')] = ['buku']
parseTable[('NN', 'sepatu')] = ['sepatu']
parseTable[('NN', 'topi')] = ['topi']
parseTable[('NN', 'membaca')] = ['error']
parseTable[('NN', 'makan')] = ['error']
parseTable[('NN', 'memakai')] = ['error']
parseTable[('NN', 'EOS')] = ['error']

parseTable[('VB', 'kakak')] = ['error']
parseTable[('VB', 'adik')] = ['error']
parseTable[('VB', 'bakso')] = ['error']
parseTable[('VB', 'tahu')] = ['error']
parseTable[('VB', 'buku')] = ['error']
parseTable[('VB', 'sepatu')] = ['error']
parseTable[('VB', 'topi')] = ['error']
parseTable[('VB', 'membaca')] = ['membaca']
parseTable[('VB', 'makan')] = ['makan']
parseTable[('VB', 'memakai')] = ['memakai']
parseTable[('VB', 'EOS')] = ['error']

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
