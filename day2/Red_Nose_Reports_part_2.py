from pathlib import Path
from typing import List

def ispositive(a: int) -> bool:
    """Check if a given integer is positive"""
    return a > 0

def isnegative(a: int) -> bool:
    """Check if a given integer is negative"""
    return a < 0

def check_for_equalality(a: int, b: int) -> bool:
    """Check whether given two integers are of same sign"""
    return (ispositive(a) and ispositive(b)) or (isnegative(a) and isnegative(b))

def parse_input_file(filename: Path) -> List:
    """Parse input file and return list of sequences"""
    parsed_data = []
    with open(filename) as f:
        file_data = f.readlines()
    for i in file_data:
        parsed_data.append(i.replace("\n", "").split())
    return parsed_data

def is_sequence_safe(sequence: List[str]) -> bool:
    """Check if a sequence is safe according to the rules"""
    if len(sequence) < 2:
        return True
        
    symbol = None
    for i in range(len(sequence) - 1):
        current = int(sequence[i])
        next_val = int(sequence[i + 1])
        res = current - next_val
        
        if res == 0 or abs(res) > 3:
            return False
            
        if symbol is None:
            symbol = res
        elif not check_for_equalality(res, symbol):
            return False
            
    return True

def red_nosed_reports_with_dampener(array: List) -> int:
    """Count safe reports with Problem Dampener functionality"""
    safe_count = 0
    
    for sequence in array:
        if is_sequence_safe(sequence):
            safe_count += 1
            continue
            
        for i in range(len(sequence)):
            modified_sequence = sequence[:i] + sequence[i+1:]
            if is_sequence_safe(modified_sequence):
                safe_count += 1
                break
                
    return safe_count

result = red_nosed_reports_with_dampener(parse_input_file("input2.txt"))
print(f"Number of safe reports with Problem Dampener: {result}")