file = open('testfile.txt')
count = 0

for line in file:
    count += 1
    if line.startswith('hello'):
        continue
    print(str(count) + " " + line)
    print('***')