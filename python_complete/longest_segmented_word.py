f = open("D:\my_files\Coding\python_codes\words.txt", 'r')
# unallowed_letters = "gkmqvwxz" with potential "io"
allowed_words = []

def search_allowed(file):
    '''
    Search for all words allowed.
    Add them to allowed_words without escape characters.
    '''
    for line in file:
        if re.search("[gkmqvwxz]",line):
            pass
        else:
            allowed_words.append(line[0:len(line)-1])


if __name__ == "__main__":
    import re

    search_allowed(f)

    print(len(allowed_words))
    print(max(allowed_words, key=len))
