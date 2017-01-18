def CheckValue(target,guess):
    return(guess==target)

def compareValue(target,guess):
    new_Target = []
    new_Guess = []
    compResult = []
    for each in str(target):
        new_Target.append(each)
    for each in str(guess):
        new_Guess.append(each)

    #print([x for x in new_Guess if x in new_Target])

    for x in range(0,len(new_Target)):
        if new_Guess[x]==new_Target[x]:
            compResult.append('0')
        elif new_Guess[x] in new_Target:
            compResult.append('?')
        else:
            compResult.append('X')

    print(compResult, '\n')
