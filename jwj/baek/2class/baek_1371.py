alphabet = [0] * 26

while True:
    try:
        doc = input()

        for s in doc:
            if s == ' ':
                continue
            alphabet[ord(s) - 97] += 1

    except:
        break

max_a = max(alphabet)
for index in range(26):
    if alphabet[index] == max_a:
        print(chr(index + 97), end="")

