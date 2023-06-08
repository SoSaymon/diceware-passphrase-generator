def load_wordlist(file):
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


def make_dict(line):
    t = line.split()
    word_dict = {
        "number": t[0],
        "word": t[1]
    }
    return word_dict


if __name__ == "__main__":
    wordlist = load_wordlist('wordlist.txt')

    dict_list = []
    for i in range(len(wordlist)):
        dict_list.append(make_dict(wordlist[i]))
    print(dict_list)
