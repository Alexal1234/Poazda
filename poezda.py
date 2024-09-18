N = int(input())
M = int(input())
n = 1
m = -1
A = []
B = []
x = 0
y = 0
plus = 0
minus = 0
time = 0
t = 0
tmin = 0
for i in range(N):
    X = int(input())
    A.append(X)
    plus += abs(X)
for i in range(M):
    Y = int(input())
    B.append(Y)
    minus += abs(Y)
time = plus + minus
tmin = time
time = 0
plus = 0


minus = 0
while time <= tmin:
    for i in range(N):
        A[i] += n
        plus += abs(A[i])
    for i in range(M):
        B[i] += m
        minus += abs(B[i])
    time = plus + minus
    if time <= tmin:
        tmin = time
        t += 1
        time = 0
        plus = 0
        minus = 0
    else:
        break
print(t)
