n = int(input())
arr = [0 for _ in range(10001)]

for _ in range(n):
    arr[int(input())] += 1
  
for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)