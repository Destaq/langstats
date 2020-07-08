import os
import logging
import yaml
import random


def form_language_dictionary() -> dict:
    # define languages and their associated extensions
    languages = open("languages.yml")
    parsed_languages = yaml.load(languages, Loader=yaml.FullLoader)

    extensions_languages = {}
    for element in parsed_languages:
        try:
            for extension in parsed_languages[element]["extensions"]:
                extensions_languages[extension] = [
                    element,
                    parsed_languages[element]["type"],
                ]
                if "color" in parsed_languages[element]:
                    extensions_languages[extension].append(
                        parsed_languages[element]["color"]
                    )
                else:
                    # create random hex color if not present
                    extensions_languages[extension].append(
                        "#{:06x}".format(random.randint(0, 0xFFFFFF))
                    )

        except KeyError:  # no extensions provided only filename (will be in later update)
            pass

    print("YAML has been parsed.")
    return extensions_languages


def get_files() -> list:
    # all files in the root directory and lower
    onlyfiles = []
    for path, subdirs, files in os.walk(
        os.getcwd()
    ):  # change for command line to any directory
        for name in files:
            filename = os.path.join(path, name)
            filename = filename[len(os.getcwd()) + 1 :]
            onlyfiles.append(filename)
    return onlyfiles


# match the correct extension to its language
def match_language(filename: str, extension: str) -> dict:
    try:
        language = extensions_languages[extension][0]
        if (
            extensions_languages[extension][1] == "programming"
            or extensions_languages[extension][1] == "markup"
        ):
            files_bytes[language] = [0, extensions_languages[extension][2]]
            if "language" in files_bytes:  # either create key or add to key
                files_bytes[language][0] += os.stat(
                    filename + extension
                ).st_size  # add bytes size of language to dictionary
            else:
                # check if it is not an empty file
                if os.stat(filename + extension).st_size != 0:
                    files_bytes[language][0] = os.stat(filename + extension).st_size
                else:
                    pass
        else:
            logging.info(
                f"{filename + extension} has been excluded as it is not a programming or markup language file."
            )
    except:
        logging.info(f"The extension {extension} could not be found.")

    return files_bytes


def read_file_data() -> dict:
    onlyfiles = get_files()
    for i in range(len(onlyfiles)):
        filename, file_extension = os.path.splitext(onlyfiles[i])
        files_bytes = match_language(filename, file_extension)

    data = {k: v for k, v in reversed(sorted(files_bytes.items(), key=lambda x: x[1]))}

    return data


extensions_languages = form_language_dictionary()
files_bytes = {}  # holds languages and bytes
