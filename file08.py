import re
def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    digits = [int(digit) for digit in data if digit.isdigit()]
    if digits:
        return max(digits)
f = open("data/data08.txt","r")
data  = f.read()
f.close

print(main(data))
    

# Read data from file