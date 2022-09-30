# 트리 순회
# 이진트리를 입력받아 전위순회, 중위순회, 후위순회한 결과를 출력하는 프로그램을 작성
def preorder(T):
    print(T, end='')
    if dct.get(T)[0] != '.':
        preorder(dct.get(T)[0])
    if dct.get(T)[1] != '.':
        preorder(dct.get(T)[1])

def inorder(T):
    if dct.get(T)[0] != '.':
        inorder(dct.get(T)[0])
    print(T, end='')
    if dct.get(T)[1] != '.':
        inorder(dct.get(T)[1])


def postorder(T):
    if dct.get(T)[0] != '.':
        postorder(dct.get(T)[0])
    if dct.get(T)[1] != '.':
        postorder(dct.get(T)[1])
    print(T, end='')

N = int(input())
dct = dict()
for i in range(1, N+1):
    p, left, right = input().split()
    dct[p] = [left, right]
# {'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'], 'E': ['.', '.'], 'F': ['.', 'G'], 'D': ['.', '.'], 'G': ['.', '.']}
preorder('A')
print()
inorder('A')
print()
postorder('A')