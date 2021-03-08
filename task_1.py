def dfs(v, matrix, component):
    used[v] = True
    component.add(v)
    [dfs(next_v, matrix, component) for next_v in range(len(matrix)) if matrix[v][next_v] and not used[next_v]]
    return component


with open("in.txt") as file:
    n = int(file.readline())
    matrix, used = [[int(v) for v in file.readline().split()] for line in range(n)], [False for v in range(n)]
components = [dfs(v, matrix, set()) for v in range(n) if not used[v]]
print()
with open("out.txt","w") as file:
    file.write(str(len(components)) + "\n" + "\n".join([" ".join([str(v + 1) for v in line]) + " 0" for line in components]))

# вариант 2
"""
def dfs(v, matrix, component):
    used[v] = True
    component.add(v)
    for next_v in range(len(matrix)):
        if matrix[v][next_v] and not used[next_v]:
            dfs(next_v, matrix, component)
    return component

with open("in.txt") as file:
    n = int(file.readline())
    matrix, used = [[int(v) for v in file.readline().split()] for line in range(n)], [False for v in range(n)]

count = 0
components = []
for v in range(n):
    if not used[v]:
        component = set()
        count += 1
        dfs(v, matrix, component)
        components.append(component)

with open("out.txt", "w") as file:
    file.write(str(count) + "\n")
    file.write("\n".join([" ".join([str(v + 1) for v in line]) + " 0" for line in components]))
"""
