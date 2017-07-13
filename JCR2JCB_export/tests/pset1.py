s= 'zyxwvutsrqponmlkjihgfedcba'
s = 'abcdefghijklmnopqrstuvwxyz'

def sol_2(s):
    string_next=s[0]
    string_final=s[0]
    # pointer_lead = 1
    # pointer_lag = 0

    for i in range (len(s)-1):
            if s[i+1]>=s[i]:
                string_next+=s[i]
            else:
                string_next=s[i+1]

            if len(string_next)>len(string_final):
                string_final= string_next

    print("Longest substring in alphabetical order is:"+string_final)


def sol_1(s):
    firstTestChar = 0
    nextTestChar = 1
    testCase = s[0]
    longestString = s[0]

    length = len(s)

    for i in range(length - 1):

        if (s[firstTestChar] <= s[nextTestChar]):
            testCase += s[nextTestChar]
        else:
            testCase = s[nextTestChar]


        if (len(testCase)) > (len(longestString)):
            longestString = testCase

        firstTestChar += 1
        nextTestChar += 1

    print ("Longest substring in alphabetical order is:", longestString)



sol_2(s)
