sam = "Pro-Tek Consulting is in San Jose City. Which is in Santa Clara County."
dc = {}
a = sam.split(" ")

for i in range(0,len(a)):
    if dc.get(a[i]):
        dc[a[i]]+=1
    else:
        dc[a[i]] = 1
