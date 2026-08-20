def multiply_values(dictionary):
    """
    Multiply all the values in a dictionary.

    Args:
        dictionary (dict): The dictionary containing numerical values.

    Returns:
        int or float: The product of all the values.
    """
    result = 1
    for value in dictionary.values():
        result *= value
    return result


my_dict = {"a": 5, "b": 10, "c": 2}

total_product = multiply_values(my_dict)

print(f"The product of all values in the dictionary is: {total_product}")