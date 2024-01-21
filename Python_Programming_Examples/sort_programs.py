# Sort the values using bubble sort
x = [1, 3, 6, 4, 10, 43, 23, -1]
for i in range(len(x)-1):
    for j in range(len(x)-1):
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]
print(x)

# Sort the key and values

d = {"name": "model", "python": "course"}
c = {}
for k, v in d.items():
    c[v] = k
print(c)
