# def foo(codeList, shoppingCart):
#     # Write your code here
#     code_pointer , shopping_pointer = 0,0
#     while shopping_pointer < len(shoppingCart):
#         item = shoppingCart[shopping_pointer]
#         if item == codeList[code_pointer][0] or codeList[code_pointer][0] == "anything":
#             codes = codeList[code_pointer]
#             code_ptr = 0
#             shop_ptr = shopping_pointer
#             flag = 0
#             while code_ptr < len(codes) and shop_ptr < len(shoppingCart) and flag == 0:
#                 if codes[code_ptr] == shoppingCart[shop_ptr] or codes[code_ptr]=="anything":
#                     code_ptr+=1
#                     shop_ptr+=1
#                 else:
#                     flag +=1
#             if code_ptr >= len(codes) and flag == 0:
#                 code_pointer +=1
#                 shopping_pointer+= len(codes)
#     if code_pointer >= len(codeList):
#         return 1
#     return 0

# a = [['orange'],['apple','apple'],['banana','orange','apple'],['banana']]
# b = ['orange','apple','apple','banana','orange','apple','banana']
# print(foo(a, b))
a = []
a.append(1)
a.append(2)
a.append(3)
a.append(4)
print(a)
a.pop()
print(a)
a.pop()
print(a)