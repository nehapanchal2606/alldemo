# def fun(sentence):
#     a = sentence.split()
#     b = a[::-1]
#     return b
#
# print(fun("dog bites man"))
# def odd_values(str):
#     result = ""
#     for i in range(len(str)):
#         if i % 2 == 0:
#             result = result + str[i]
#             return result
# print(odd_values("Welcome"))

# z = "welcome"
# k=""
# for val in range(len(z)):
#     if val%2 == 0:
#         print(val[k])
#     else:
#         print(val)


# num = 1
# for i in range(1,4):
#     for j in range(0,i):
#         print(num, end=" ")
#         num += 1
#     print(num)

str = input("enter string")
result= ''
for i in range(len(str)):
    if i % 2 == 0:
        result = result + str[i]
print(result)

