dic = {}
MAXIM = 0
WORD = ''
file = open('sherlock.txt', 'r')
split_sherlock = []
for line in file:
    stripping = line.strip()
    splitting = stripping.split()
    split_sherlock.append(splitting)
add = sum(split_sherlock, [])
for i in add:
    dic[i]=0
for i in add:
    dic[i]+=1
    if dic[i]>MAXIM:
        MAXIM = dic[i]
        WORD = i
file.close()
print(f'\n"{WORD}" occured {MAXIM} times. Hence "{WORD}" is the most used word in Sherlock')