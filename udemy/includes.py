def includes(collection, val, index=0):
    """
    Checks if a given value is present in a collection starting from a specified index.

    Args:
    - collection (str, list, dict): The collection to search for the value.
    - val: The value to search for in the collection.
    - index (int, optional): The index from which to start the search. Defaults to 0.

    Returns:
    - bool: True if the value is found in the collection starting from the specified index, False otherwise.
    """

    # Check if the collection is a string or a list
    if type(collection) in [str, list]:
        # If it's a string or a list, check if the value is present starting from the specified index
        if val in collection[index:]:
            return True
    # Check if the collection is a dictionary
    elif type(collection) == dict:
        # If it's a dictionary, check if the value is present in the dictionary values
        if val in collection.values():
            return True
    # Return False if the value is not found in the collection
    return False


# Define a sample collection, value, and starting index for testing
sample_collection = [1, 2, 3, 4, 5]
sample_value = 3
start_index = 1

# Call the includes function to check if the value is present in the collection starting from the specified index
print(includes(sample_collection, sample_value, start_index))
