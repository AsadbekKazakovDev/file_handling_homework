def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    digits = [int(digit) for digit in data if digit.isdigit()]
    if digits:
        return min(digits)
f = open("data/data09.txt","r")
data  = f.read()
f.close

print(main(data))
    

# Read data from file