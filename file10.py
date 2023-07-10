def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    largest_length = 0
    rows = data.split("\n")
    for row in rows:
        row_length = len(row.strip())
        if row_length > largest_length:
            largest_length = row_length
    
    return largest_length
f = open("data/data10.txt","r")
data  = f.read()
f.close

print(main(data))
# Read data from file