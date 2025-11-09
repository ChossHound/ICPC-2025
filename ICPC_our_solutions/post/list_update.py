import time

a = []

start = time.time()
for i in range(300000):
    a.append(i)

mid = time.time()

for i in range(300000):
    del a[0]

end = time.time()

creation = mid - start
deletion = end - mid

print(f"CREATE: {creation}s\nDELETE: {deletion}s")