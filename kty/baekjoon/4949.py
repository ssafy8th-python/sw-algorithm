def pack(sentence):
    for i in sentence:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == ')' and stack[-1] == '[':
                return 'no'
            elif i == ']' and stack[-1] == '(':
                return 'no'
            elif not stack:
                return 'no'
    if stack:
        return 'no'
    else:
        return 'yes'
stack = []

while True:
    sentence = input()
        break
    print(pack(sentence))