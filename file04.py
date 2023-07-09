import re
def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    result = []
    non_digit_characters = re.findall(r'\D', data)

        # Add each non-digit character to the result list
    for character in non_digit_characters:
        result.append(character)

    return result
f = open("data/data04.txt","r")
data  = f.read()
f.close

print(main(data))
    
# Read data from file