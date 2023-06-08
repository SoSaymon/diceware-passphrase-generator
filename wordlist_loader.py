def load_wordlist(file: str) -> list[str]:
    try:
        with open(file, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"File not found {file} {FileNotFoundError}")
    except IOError:
        print(f"IOError {IOError}")
    except Exception as e:
        print(f"{e}")
    finally:
        f.close()


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
    tmp = load_wordlist(filename)
    return make_wordlist(tmp)
