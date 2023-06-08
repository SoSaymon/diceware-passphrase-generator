import dice
import wordlist_loader


def find_index(wordlist, number):
    for index, element in enumerate(wordlist):
        if isinstance(element, dict) and element.get("number") == number:
            return index

    return -1


def get_word(wordlist, index):
    tmp = wordlist[index]
    return tmp.get("word")


def main(number_of_words, wordlist_name):
    wordlist = wordlist_loader.main(wordlist_name)
    passphrase = ""

    for i in range(number_of_words):
        number = dice.main()
        index = find_index(wordlist, number)
        word = get_word(wordlist, index).capitalize()
        passphrase += word

    print(passphrase)


if __name__ == '__main__':
    main(5, "wordlist.txt")
