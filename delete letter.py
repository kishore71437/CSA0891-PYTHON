# Input strings
s = "hello world"
c = "l"
delchar = lambda s, c: ''.join([char for char in s if char != c]) if len(c) == 1 else s
result = delchar(s, c)
print(result)