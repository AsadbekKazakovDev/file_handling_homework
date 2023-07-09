import re
def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a  = "0123456789"
    result = []
    numbers = re.findall(r'\d', data)
        
        # Convert each number to a string and store them in a list
    for number in numbers:
        result.append(number)
    
    return result  
f = open("data/data03.txt","r")
data  = f.read()
f.close

print(main(data))

# Read data from file
