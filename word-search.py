import os


def get_word_frequency_list(word, extension, directory):
    if not directory:
        directory = os.getcwd()
    for f in find_files(word, extension, directory):
        print(f)  # we could use numpy or pandas to output it to a csv
                  # or export as json object and send to an api
                  # or make a direct db request insert into table etc etc


def find_files(word, extension, directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                path = os.path.abspath(os.path.join(root, file))
                count = word_frequency_count(word, path)
                if count and (count > 0):
                    yield [file, count, path]
                else:
                    continue


def word_frequency_count(word, file):
    """ This solution works on small files as we discussed at the kb size
        if the files go into the gigs or higher, it would be safer to use a
        generator"""
    try:
        with open(file) as file_object:  # 'with' automatically closes file
            contents = file_object.read()
    except FileNotFoundError:
        pass
        # print("file not found")
    except UnicodeDecodeError:
        pass
        # print("unicode error")
    else:
        return contents.lower().count(word.lower())


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='Get the frequency of a '
                                                 'word in all files')

    parser.add_argument("--word", "-w", dest="word", type=str, required=True,
                        help='The string to search for')
    parser.add_argument("--file-extension", "-f", dest="extension", type=str,
                        required=True,
                        help='The file type to search in')
    parser.add_argument("--dir", "-d", dest="directory", type=str,
                        default=None,
                        help='Directory to search in')

    args = parser.parse_args()
    get_word_frequency_list(args.word, args.extension, args.directory)


