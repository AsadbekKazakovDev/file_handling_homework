import re
def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    digits = re.findall(r'\d', data)
    digit_count = len(digits)

        # Count the number of non-digit characters
    non_digits = re.findall(r'\D', data)
    non_digit_count = len(non_digits)

    return [digit_count, non_digit_count]
f = open("data/data05.txt","r")
data  = f.read()
f.close

print(main(data))
# Read data from file