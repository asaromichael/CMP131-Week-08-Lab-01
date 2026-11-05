print("Pattern 1:\n")
pattern1 = ""
pattern2 = ""

for i in range(0, 10):
    pattern1 = pattern1 + "+"
    print(pattern1)
print("\n")

print("Pattern 2:\n")
for i in range(10, 0, -1):
    pattern2 = ""
    for j in range(i):
        pattern2 = pattern2 + "+"
    print(pattern2)


