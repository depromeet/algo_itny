import sys
N = int(sys.stdin.readline())
words = list(sys.stdin.readline().rstrip())
ans = float('-inf')


def dfs(i, value):
    global ans
    if N == i:
        ans = max(ans, int(value))
        return
    # 괄호 사용 o
    if i+4 <= N:
        dfs(i+4, str(eval(''.join([value, words[i]] + [str(eval(''.join(words[i+1:i+4])))]))))
    # 괄호 사용 x
    if i+2 <= N:
        dfs(i+2, str(eval(''.join([value] + words[i:i+2]))))
dfs(1, words[0])
print(ans)
