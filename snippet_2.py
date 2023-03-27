def is_valid_parenthesis(s):
    # should be in one line for readability
    # dc should be changed to parenthesises
    parenthesises = {'(': ')',"{": "}",'[': ']'}
    stack = []
    # i should be char 
    for char in s:
        # two lines are good for readablity instead
        if char in parenthesises.keys():
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            
            # op should be changed to parentheses to make it descriptive
            parentesis = stack.pop()
            if parenthesises[parentesis] != char:
                return False
    # unneccessary return statements should removed for readabilty
    return len(stack)==0
