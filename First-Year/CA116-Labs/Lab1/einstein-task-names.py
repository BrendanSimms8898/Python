 #!/usr/bin/env python

s = raw_input()

while s != "end":
    i = 0
    count = 0
    while i < len(s) and count < 4:
        if s[i] == "/":
            count += 1
        i = i + 1
    i += 1
    j = i
    while j < len(s) and s[j:j + 3] != ".py":
        j += 1
    if j < len(s):
        print s[i:j + 3]
    s = raw_input()
