print('Hello world')

s = "this is string example"

print(s)

print(s[0:4][::-1] + " " + s[5:7][::-1] + " " + s[8:14][::-1] + " " + s[16:23][::-1])


ans2 = s.replace(s, s[::-1])

print(ans2)