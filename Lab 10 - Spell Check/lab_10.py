import re


def main():
    # This function takes in a line of text and returns
    # a list of words in the line.
    def split_line():
        return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
    the_file = open("dictionary.txt")


    dictionary_possibilities = []
    for line in the_file:
        line = line.strip()
        dictionary_possibilities.append(line)
    the_file.close()


    # Linear Search
    print("---linear Search---")
    chapter = open("AliceInWonderLand200.txt")


    current_position = 0
    for line in story:
        current_position += 1
        word_list = split_line()
        for word in word_list:
            i = 0
            key = word.upper()
            while i < len(the_file) and the_file[i] != key:
            i += 1
            if i == len(the_file):
                print("the_line", str(current_position), "The_Word", word)
    story.close()

    # Binary Search
    print("---Binary Search---")
    story = open("AliceInWonderLand200.txt")


    current_line_position = 0
    for line in story:
        current_line_position += 1
        word_list = split_line()
        for word in word_list:
            lower_bound = 0
            upper_bound = len(spelling_reference_list) - 1
            found = False
            key = word.upper()
            while lower_bound <= upper_bound and not found:
                middle_line = (lower_bound + upper_bound) // 2


            if spelling_reference_list[middle_line] < key:
                lower_bound = middle_line + 1
            elif spelling_reference_list[middle_line] > key:
                upper_bound = middle_line - 1
            else:
                found = True


        if not found:
            print("the_line", str(current_line_position), "The_Word:", word)

     story.close()


main()
