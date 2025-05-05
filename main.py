# import statement
from collections import Counter

# An empty list
word_list = []

# TODO create a function 
def analizer(file_path):
    """
    open the text file message loop through it count:
    number of word = int
    number of lines = int
    number of charaters = int
    create a variable for each and print the result at the end of the function.

    """
    # TODO create a variable for each section
    num_word = 0
    num_line = 0
    num_char = 0 

# TODO open the file and start analizing

    with open(file_path, 'r') as file:
        
        for message in file: # for line the line name is handling all on the job

            # coun the num of lines
            num_line += 1
    

            # count the num of words
            num_word += len(message.split())

            # count the num of charaters
            num_char += len(message)

        print(f'The number of words is: {num_word}')
        print(f'The number of lines is: {num_line}')
        print(f"The number of charaters is: {num_char}")


def most_repeated_word(file_path):
    """
    open the file count the most repeated word in the file:
    print the common word with number of times it repeated.
    """

    # open the text file by passing the file path
    with open(file_path) as text_file:
        # loop through the file and extend each word to a new list
        for word in text_file:
            word_list.extend(word.split())
            
        # count the word in a list
        common_word = Counter(word_list)

        # show the most common word repeat in the list
        most_cmn_wrd = common_word.most_common(1)
        # word name
        frequent = most_cmn_wrd[0][0]
        # number of times it repeated in the file
        word_repeat = most_cmn_wrd[0][1]
        # combine the result for easy to read
        result = f"The Most Common Word is: '{frequent.title()}' it repeated [{word_repeat}] times."

        return result
       

# TODO show the result
file_name = f'file.txt' # your file path

# analizer function is call here
analizer(file_name)

# most repeated word function
repeated = most_repeated_word(file_name)
print(repeated)