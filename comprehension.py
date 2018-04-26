letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = [str(x) for x in range(0,10)]
non_alphanumeric = '.?!&#,;:-_*'

def password(p):
    if len([x for x in p if x in numbers]) == 0:
        print "Needs a number"
    if len([x for x in p if x in letters]) == 0:
        print "Needs a lowercase letter"
    if len([x for x in p if x in letters.upper()]) == 0:
        print "Needs an uppercase letter"
    else:
        print "Congratulations! You've met the minimum threshold."

password("Hi123")

def passwordStrength(p):
    score = 1 #min score
    num = [x for x in p if x in numbers]
    lowerLet = [x for x in p if x in letters]
    upperLet = [x for x in p if x in letters.upper()]
    nonAlpha = [x for x in p if x in non_alphanumeric]
    #0-5 points for mix of upper to lowercase letters
    if len(upperLet) > len(lowerLet):
        score += 10 * len(lowerLet)/(len(lowerLet) + len(upperLet))
    else:
        score += 10 * len(upperLet)/(len(lowerLet) + len(upperLet))
    #2 points for including a number
    if len(num) >= 1:
        score += 2
    #2 points for including a non-alphanumeric char
    if len(nonAlpha) >= 1:
        score += 2
    return score


print passwordStrength("AbCDEfghiJkLmnoop123.")
