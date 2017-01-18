def minion_game(S):
    n = len(S)
    # consonants
    stuart = 0
    # vowels
    kevin = 0

    for i in range(n):
        if S[i] in ('A', 'E', 'I', 'O', 'U'):
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print('Kevin', kevin)
    elif stuart > kevin:
        print('Stuart', stuart)
    else:
        print('Draw')

if __name__ == '__main__':
    #Test Input = BANANA
    #Test Output = Stuart 12
    s = input()
    minion_game(s)
