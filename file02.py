def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return len(data)
f = open("data/data02.txt","r")
data  = f.read()
f.close

print(main(data))
# Read data from file