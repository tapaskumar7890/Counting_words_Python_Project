def word_count(text):
    """
    Function to count the number of words in a given text.
    
    Parameters:
    - text (str): Input text in which words need to be counted.
    
    Returns:
    - int: Number of words in the input text.
    """
    if not text.strip():  # Check if the input text is empty or just whitespace
        return 0
    
    words = text.split()  # Split the text by whitespace to get a list of words
    return len(words)  # Return the number of words in the list


def main():
    """
    Main function to run the Word Counter program.
    """
    print("Welcome to Word Counter!")
    print("Please enter a sentence or paragraph:")
    
    user_input = input()  # Prompt user for input
    
    # Calculate word count
    count = word_count(user_input)
    
    # Print the result
    print(f"Word count: {count}")


# Entry point of the program
if __name__ == "__main__":
    main()