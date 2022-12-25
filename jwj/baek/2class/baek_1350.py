import math

N = int(input())
files = list(map(int, input().split()))
cluster = int(input())

disk = 0
for file in files:
    disk += math.ceil(file / cluster) * cluster

print(disk)

