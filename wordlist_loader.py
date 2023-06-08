def load_wordlist(file: str) -> list[str]:
    try:
        with open(file, 'r') as f:
            return f.readlines()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file}") from e
    except IOError as e:
        raise IOError(f"IOError occurred {e}") from e
    except Exception as e:
        raise Exception(f"An error occurred: {e}") from e
    finally:
        return []


def make_dict(line: str) -> dict[str, str]:
    t = line.split()
    word_dict = {
        "number": t[0],
        "word": t[1]
    }
    return word_dict


def make_wordlist(wordlist: list[str]) -> list[dict[str, str]]:
    dict_list = []
    for i in range(len(wordlist)):
        dict_list.append(make_dict(wordlist[i]))
    return dict_list


def wordlist_maker(filename: str) -> list[dict[str, str]]:
    try:
        wordlist = load_wordlist(filename)
    except FileNotFoundError as e:
        print(f"File not found: {filename}")
        print("Using default wordlist")
        wordlist = load_wordlist("wordlist.txt")
    except IOError as e:
        print(f"IOError occurred {e}")
        print("Using default wordlist")
        wordlist = load_wordlist("wordlist.txt")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Restart the program")
        exit(1)
    return make_wordlist(wordlist)
