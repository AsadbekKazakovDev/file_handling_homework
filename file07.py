def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    result  = 0
    #rows = data.split("\n")
    for row in range(len(data)):
        if data[row].isdigit():
            result+=int(data[row])
    return result
f = open("data/data07.txt","r")
data  = f.read()
f.close

print(main(data))
    
# Read data from file