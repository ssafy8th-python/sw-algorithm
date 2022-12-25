N, M = map(int, input().split())
box = list(map(int, input().split()))
books = list(map(int, input().split()))

print(sum(box) - sum(books))