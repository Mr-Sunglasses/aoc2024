from pathlib import Path
from typing import List

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

def parse_input_file(filename: Path) -> List:
    parsed_data = []
    with open(filename) as f:
        file_data = f.readlines()

    for i in file_data:
        parsed_data.append(i.replace("\n", "").split())

    return parsed_data


def red_nosed_reports(array: List) -> int:
    safe = 0
    for x in array:
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
    return safe

print(red_nosed_reports(parse_input_file("input.txt")))