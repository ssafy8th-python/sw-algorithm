exp = input()

result = ''

out_rank = {'+': 1, '-': 1,  '*': 2, '/': 2, '(': 3}
in_rank = {'+': 1, '-': 1,  '*': 2, '/': 2, '(': 0}

stack = []

for char in exp:

    if 65 <= ord(char) <= 90:
        result += char
    else:
        if not stack:
            stack.append(char)
        else:
            if char == ')':
                while stack[-1] != '(':
                    result += stack.pop()
                stack.pop()

            elif in_rank.get(stack[-1]) < out_rank.get(char):
                stack.append(char)
            else:
                while stack and in_rank[stack[-1]] >= in_rank[char]:
                    result += stack.pop()
                stack.append(char)
while stack:
    result += stack.pop()

print(result)
