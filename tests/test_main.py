import test_wordlist_loader
import test_dice
import test_passgen


def test_main():
    test_wordlist_loader.test_wordlist_loader()
    test_dice.test_dice()
    test_passgen.test_passgen()


if __name__ == "__main__":
    test_main()
