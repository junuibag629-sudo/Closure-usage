def countdown(n):
        i = n
    def count():
        nonlocal i
        i -= 1
        return i
    return count

n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end= '')