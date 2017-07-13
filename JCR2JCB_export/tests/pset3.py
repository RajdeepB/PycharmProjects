




def find_longest(s):
    substr=''
    for i in range (len(s)):
        if i<9:
            if s[i+1]>s[i]:
                substr+=s[i:i+2]
                print(substr)

    print(substr)

def find_longest2(s):
    s += '!'
    winner = ''
    temp = s[0]
    for i in range(len(s)-1):
        if s[i] <= s[i+1]:
            temp += s[i+1]
        else:
            if len(temp) > len(winner):
                winner = temp
            temp = s[i+1]

    print('Longest substring in alphabetical order is:', winner)

find_longest2('asdjhfklas')


