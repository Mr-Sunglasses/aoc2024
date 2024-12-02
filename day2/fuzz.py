def ispositive(a: int) -> bool:
    """
    Check for a given integer is positive
    """
    if a > 0:
        return True
    else:
        return False

def isnegative(a: int) -> bool:
    """
    Check for a given integer is negative
    """
    if a < 0:
        return True
    else:
        return False 


def check_for_equalality(a: int, b: int) -> bool:
    """
    check weather given two integer is of same sign
    """
    return (ispositive(a) and ispositive(b)) or (isnegative(a) and isnegative(b))

l = [['7','6','4','2','1'], ['1', '2', '7', '8', '9'], ['9', '7', '6', '2', '1'], ['1', '3', '2', '4', '5'], [8, 6, 4, 4, 1], [1 ,3 ,6 ,7 ,9]]

safe = 0

for x in l:
    symbol = int()

    for node in range(len(x)):
    
        if node == 0:
            res = int(x[node]) - int(x[node+1])
            if res==0 or abs(res) > 3:
                # print("breaking")
                break
            else:
                symbol = res
        if node!=len(x)-1:
            res = int(x[node]) - int(x[node+1])
            if check_for_equalality(res, symbol):
                if res==0 or abs(res) > 3:
                    # print("breaking")
                    break
                else:
                    symbol = res
            else:
                # print("breaking")
                break
        else:
            safe+=1

print(safe)

# x = ['1', '2', '7', '8', '9']
# x = ['9', '7', '6', '2', '1']
# x = ['1', '3', '2', '4', '5']
# x = [8, 6, 4, 4, 1]
# x = [1 ,3 ,6 ,7 ,9]

# symbol = int()

# for node in range(len(x)):
    
#     if node == 0:
#         res = int(x[node]) - int(x[node+1])
#         if res==0 or abs(res) > 3:
#             print("breaking")
#             break
#         else:
#             symbol = res
#     if node!=len(x)-1:
#         res = int(x[node]) - int(x[node+1])
#         if check_for_equalality(res, symbol):
#             if res==0 or abs(res) > 3:
#                 print("breaking")
#                 break
#             else:
#                 symbol = res
#         else:
#             print("breaking")
#             break
#     else:
#         print("passed")
# # print(symbol)