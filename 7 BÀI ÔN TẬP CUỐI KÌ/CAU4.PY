t = [73,74,75,71,69,72,76,73]

ans = [0]*len(t)
stack = []

for i in range(len(t)):
    while stack and t[i] > t[stack[-1]]:
        j = stack.pop()
        ans[j] = i - j
    stack.append(i)

print(ans)