# rows = 3
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print(" ")
#
# for i in range(rows + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print()

rows = 5
rows = int(rows)
for i in range(0, rows):
    for j in range(0 * 2, i + 1):
        print("* ", end='')
    print("\r")
for i in range(rows, 0, -1):
    for j in range(0, i -1):
        print("* ", end='')
    print("\r")



