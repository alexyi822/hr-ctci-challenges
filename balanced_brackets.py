def is_matched(expression):
    stack = []
    for bracket in expression:
        if bracket == '{' or bracket == '[' or bracket == '(':
            stack.append(bracket)
        if bracket == '}' or bracket == ']' or bracket == ')':
            if len(stack) == 0:
                return False
            if len(stack) > 0 :
                temp = stack.pop()
                if bracket == ']' and temp != '[':
                    return False
                if bracket == ')' and temp != '(':
                    return False
                if bracket == '}' and temp != '{':
                    return False

    if len(stack) == 0:
        return True

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
