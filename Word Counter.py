def main():
    """Main entry point of the app"""

    def print_words(filename):
        words = word_counter(filename)
        print("All of the words in the text and how many times they each appear: ")
        for word in sorted(words, key=words.get, reverse=True):
            print(word, words[word])

    def print_top(filename):
        words = word_counter(filename)
        print("The twenty most common words in the text are: ")
        words = sorted(words, key=words.get, reverse=True)
        for word in range(20):
            print(words[word])

    def word_counter(filename):
        # Utility function to create dict for use in other functions
        word_count = {}
        with open(filename, 'r') as file:
            text = file.read()
            # Cleaning text of punctuation while maintaining word structure
            for char in '".!?-`()[]_:;*':
                text = text.replace(char, ' ')
            for char in "',":
                text = text.replace(char, '')
            text = text.lower()
            text = text.split()
            # Takes each word and creates dict
            for word in text:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
            return word_count

    user_file = input("What is the name of your file? ")

    print_words(user_file)
    print('\n')
    print_top(user_file)

if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()
