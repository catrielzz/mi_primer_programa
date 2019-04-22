from time import sleep
import random

WORDS = ['hi', 'bye', 'cya', 'nya']


def write_file_and_screen(filename):
    choice = WORDS[random.randint(0, 3)]
    with open(filename, 'a') as random_word_file:
        random_word_file.write("{}{}".format(choice, "\n"))
        print(choice)


def main():
    while True:
        sleep(3)
        write_file_and_screen("random_word_file.txt")


if __name__ == "__main__":
    main()
