def remove_nth_occurrence(word_list, word_to_remove, n):
    """
    Remove the nth occurrence of a word from a given list.

    Parameters:
    - word_list (list): The list of words.
    - word_to_remove (str): The word to be removed.
    - n (int): The occurrence number to be removed.

    Returns:
    - list: The updated list after removing the nth occurrence of the word.
    """

    # Initialize a count to keep track of occurrences
    count = 0

    # Iterate over the list and remove the nth occurrence of the word
    for i in range(len(word_list)):
        if word_list[i] == word_to_remove:
            count += 1
            if count == n:
                del word_list[i]
                break

    return word_list


# Example usage:
word_list = ['apple', 'banana', 'apple', 'orange', 'apple', 'kiwi']
word_to_remove = 'apple'
n = 2

updated_list = remove_nth_occurrence(word_list, word_to_remove, n)
print("Updated list:", updated_list)
