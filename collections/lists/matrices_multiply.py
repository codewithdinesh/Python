m1 = [[3, 5], [6, 8]]
m2 = [[2, 5], [2, 7]]
m3 = [[0, 0], [0, 0]]

for i in range(0, len(m1)):
    for j in range(0, len(m1)):
        m3[i][j] = m1[i][j]*m2[i][j]
print(m3)
