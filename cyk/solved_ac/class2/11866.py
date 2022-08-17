# 요세푸스
N, K = map(int, input().split())    # N = 7, k = 3
lst = list(range(1,N+1))            # [1, 2, 3, 4, 5, 6, 7]
result = []

while lst:                          # lst에 요소가 없다면 while 끝
    for _ in range(K-1):            # k번째의 요소를 없애햐 하기 때문에 k-1번 반복하여 앞의 요소들을 뒤로 보냄
        a = lst.pop(0)
        lst.append(a)
    b = lst.pop(0)                  # k번째 요소를 제거하여 b에 할당
    result.append(b)                # 제거된 요소들의 집합

print('<'+ ', '.join(map(str, result))+'>')     # 제거된 순서대로 출력 <3, 6, 2, 7, 5, 1, 4>











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