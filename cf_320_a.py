n = input()
f = 1
for i in range(0,len(n)):
    if n[i-2] == '1' and n[i-1]=='4' and n[i] == '4':
        i+=3
    elif n[i-1]=='1' and n[i] == '4':
        i+=2
    elif n[i] == '1':
        i+=1
    else:
        f = 0
        break
if f == 1:
    print("YES")
else:
    print("NO")


# li = []
# nl1 = []
# while(n!=0):
#     li.append(n%10)
#     n//=10
# li.reverse()
# f = 0
# # nl1.append(li[0])
# t = li[0]
# if li[0] == 1:
#     for i in range(1,len(li)-1):
#         print(li[i])
#         if li[i]!=t:
#             t = li[i]
#             f = 1
#         elif t==1:
#             continue
#         else:
#             f = 0
#             break
# else:
#     f = 0
#
# if f == 1:
#     print("YES")
# else:
#     print("NO")



# f = 0
# temp = []
# temp.append(n % 10)
# if (n != 1444) and (n != 514) and (n != 414):
#     while n != 0:
#         r = n % 10
#         if (r == 1 or r == 4):
#             if r== 4 and temp[len(temp)-1] ==r:
#                 break
#             f = 1
#         else:
#             f = 0
#             break
#         n = n // 10
#
#     if f == 1:
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")