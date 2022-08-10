# 요세푸스
N, K = map(int, input().split())
lst = list(range(1,N+1))

# class Queue:
#     def __init__(self):
#         self.items=[]
#         self.front_index = 0
#     def enqueue(self, val):
#         self.items.append(val)
#     def dequeue(self):
#         if self.front_index == len(self.items):
#             print('Q is empty')
#         else :
#             x = self.items[self.front_index]
#             self.front_index += 1
#             return x
result = []
while lst :
    for _ in range(K-1):
        a = lst.pop(0)
        lst.append(a)
    b = lst.pop(0)
    result.append(b)

print('<'+ ', '.join(map(str, result))+'>')
