def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    result = []
    elements = data.split(",")
    for element in elements:
        result.append(int(element))
    return result
f = open("data/data01.txt","r")
data  = f.read()
f.close
k  = main(data)
print(k)   
# Read data from file