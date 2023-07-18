n = int(input())

parr = []
marr = []
result = 0
for i in range(n):
    a= int(input())
    if a == 1:
        result += 1
    elif a > 0:
        parr.append(a)
    else:
        marr.append(a)
    
parr.sort()
marr.sort(reverse=True)

while len(parr) != 0:
    if len(parr) == 1:
        result += parr.pop()
    else:
        result += parr.pop() * parr.pop()
while len(marr) != 0:
    if len(marr) == 1:
        result += marr.pop()
    else:
        result += marr.pop() * marr.pop()
print(result)