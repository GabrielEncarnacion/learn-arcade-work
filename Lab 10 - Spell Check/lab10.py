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
    for line in chapter:
        current_position += 1
        word_list = split_line()
        for word in word_list:
            i = 0
            while i < len(dictionary_possibilities) and dictionary_possibilities[i] != word.upper():
                i += 1
            if i == len(dictionary_possibilities):
                print("the_line", str(current_position), "The_Word", word)
    chapter.close()

    # Binary Search
    print("---Binary Search---")
    chapter = open("AliceInWonderLand200.txt")

    current_position = 0
    for line in chapter:
        current_position += 1
        word_list = split_line()
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_possibilities) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_line = (lower_bound + upper_bound) // 2
                if dictionary_possibilities[middle_line] < word.upper():
                    lower_bound = middle_line + 1
                elif dictionary_possibilities[middle_line] > word.upper():
                    upper_bound = middle_line - 1
                else:
                    found = True
            if not found:
                print("the_line", str(current_position), "The_Word:", word)
    chapter.close()


main()
