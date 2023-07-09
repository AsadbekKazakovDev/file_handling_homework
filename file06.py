def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    result  = []
    rows = data.split("\n")
    for row in rows:
        result.append(len(row))
    return result
f = open("data/data06.txt","r")
data  = f.read()
f.close

print(main(data))
# Read data from file
# Read data from file