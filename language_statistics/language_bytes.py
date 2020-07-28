import os
import logging
import yaml
import random
import pkgutil


def form_language_dictionary() -> dict:
    # define languages and their associated extensions
    languages = pkgutil.get_data(__name__, "data/languages.yml")

    parsed_languages = yaml.load(languages, Loader=yaml.FullLoader)

    extensions_languages = {}
    filename_languages = {}
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

        try:
            for name in parsed_languages[element]["filenames"]:
                filename_languages[name] = [element, parsed_languages[element]["type"]]

                if "color" in parsed_languages[element]:
                    filename_languages[name].append(
                        parsed_languages[element]["color"]
                    )
                else:
                    # create random hex color if not present
                    filename_languages[name].append(
                        "#{:06x}".format(random.randint(0, 0xFFFFFF))
                    )

        except KeyError:
            pass

    return extensions_languages, filename_languages


# reproduced from Jean-François Fabre on Stack Overflow
# under creative commons license: https://stackoverflow.com/a/42720847/12876940
def scanrec(root, maximum_depth):
    rval = []

    depth = 0

    def do_scan(start_dir, output, d):
        for f in os.listdir(start_dir):
            ff = os.path.join(start_dir, f)
            if os.path.isdir(ff):
                if d < maximum_depth:
                    do_scan(ff, output, d + 1)

            else:
                output.append(ff[len(os.getcwd()) + 1 :])

    do_scan(root, rval, depth)
    return rval


def get_files(depth) -> list:
    # all files in the root directory and lower

    onlyfiles = scanrec(os.getcwd(), depth)

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

# match the correct filename to its language
def match_filename(filename: str):
    if (
        filenames_languages[filename][1] == "programming"
        or filenames_languages[filename][1] == "markup"
    ):
        language = filenames_languages[filename][0]
        files_bytes[language] = [0, filenames_languages[filename][2]]

        if "language" in files_bytes:  # either create key or add to key
                files_bytes[language][0] += os.stat(
                    filename
                ).st_size  # add bytes size of language to dictionary
        else:
            # check if it is not an empty file
            if os.stat(filename).st_size != 0:
                files_bytes[language][0] = os.stat(filename).st_size
            else:
                pass

    return files_bytes

def read_file_data(depth, excludes, exclude_name) -> dict:
    onlyfiles = get_files(depth)
    files_bytes = {}
    for i in range(len(onlyfiles)):
        filename, file_extension = os.path.splitext(onlyfiles[i])
        if file_extension not in excludes:
            files_bytes = match_language(filename, file_extension)

        elif file_extension == '':
            # support for excluding named files
            if filename not in exclude_name:
                files_bytes = match_filename(filename)

    data = {k: v for k, v in reversed(sorted(files_bytes.items(), key=lambda x: x[1]))}

    return data


extensions_languages, filenames_languages = form_language_dictionary()
files_bytes = {}  # holds languages and bytes
