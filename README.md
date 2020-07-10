# language-statistics
With `language-statistics`, you can create a high-quality image (both as an SVG or PNG) of the programming languages and their percentages used in your directory. It is **runnable anywhere** and is **highly customizable**, an improved clone of the `linguist` package that comes with GitHub itself. And best of all, it takes just two clicks to install and one line to run!

<p align="center">
  <img src="screenshots/output.svg" alt = "Output image">
</p>

## Features
### Available Globally
This is an executable Python script that can be run from any folder or location on your device. This means that you can easily view the language distribution for folders that don't have the python script in their directories. By implementing this, a *major advantage* is introduced over `linguist`, which can only be used for visualizations for GitHub repositories, often takes hours to refresh, and has very weak text-only command-line functionality.

### Tweakable
It's very easy to change the look of your outputted image. You can easily specify at what percentage programming languages will merge into the 'Other' category, as well as how many unique languages to display at once. Likewise, you can limit the depth that the program searches for files based on distance from the root directory. You can even choose which file extensions to ignore!

## Usage
### Installation
This program is bundled as a *Python package*. This makes it very easy to install, cross-platform, and available globally. All you need to do is run the command `statistics` from *anywhere* in order to get your outputted image. These are the steps you need to take to install the Python package locally on your device (PyPI package coming soon).
1. **Clone** or **download** this repository by going to the top right, clicking `Code`, and clicking `Download zip` or clone with HTTPS/GitHub Desktop.
2. If you downloaded the zip, make sure to unzip it in a location that you will remember (such as `Desktop`, `Downloads`, `Documents`, etc.)
3. Navigate to the root folder of the program in your terminal. For example, if you had it unzipped in your Desktop as `language-statistics`, you'd type: `cd Desktop/language-statistics`.
4. **UBUNTU ONLY**: Ubuntu and `pycairo` don't like each other. You have to manually install `pycairo`'s dependencies first by running the following commands below.
These will clone pycairo, install its dependencies, and then add it as a Python package locally. Make sure to change the `cd /home/username/` etc. to wherever you want to clone it.
```
>>> cd /home/username/Programming/Repositories/
>>> sudo git clone git://git.cairographics.org/git/pycairo
>>> sudo apt-get install libcairo2-dev libjpeg-dev  libgif-dev
>>> cd pycairo
>>> sudo python3 setup.py install
```
5. Type: `python3 -m pip install -e .`. Don't forget the `.` at the end! This will install the package and make it executable using the information in `setup.py`.

*Note: uninstalling is easy too! You can type `python3 -m pip uninstall language-statistics` or you can simply edit/update your clone of the repo! Because this is a local package, it will stay completely synced with the folder it was made in.*

### Running the program
You should know be able to run the command `statistics` from anywhere in your terminal and get the `.svg` file. If not, it may be because you are using `zsh` or a non-bash shell, in which case you can follow the instructions [here](####zsh-instructions).

If it works, great! By running `statistics`, the program will search through all files in the root directory and lower, and then create a file named `output.svg` in the root directory! You can view this by right-clicking and then selecting: *View in: \<Your browser here>*. You can also explore the various ways to generate it with argparse.

Likewise, you can also choose to **output the image as a png**, or specify other flags, below.

The following flags are available, and they are all optional (if you ignore them, nothing will happen):
- **-d or --depth:** how many directories 'deep' the program should search for files in, default 3. A depth of one means reading files only in the root directory, a depth of 2 means files only in root directory + subdirectories, etc. *Example: `statistics -d 5` will search to a 'depth' of 5 from the root directory.*<br>I highly recommend **trying this command out on your Desktop** with a depth of 5 or 6, the results are incredible!
- **-t or --type:** the type of file outputted - svg or png. Defaults to svg as that is much higher quality. Specify 'png' to choose png. *Example: `statistics -t png`*
- **-l or --limit:** how small a language as a percentage of the whole must be to be excluded. Default is 1. *Example: `statistics -l 5` (if it takes up less than 5 percent, it will be grouped with other)*
- **-m or --maximum:** the maximum number of unique languages to show (excluding 'Other'). Default is 8. *Example: `statistics -m 3` will show at most 3 other languages in addition to 'Other'*
- **-e or --exclude:** which file extensions to exclude when searching for files and creating the image. These files will be ignored and will not affect the total percentage or show up. You can specify multiple. *Example: `statistics -e .ipynb .css .html`*

The above flags can be used in any order, combined, and are completely optional (`statistics --type png -l 5 -m 3 --depth 4 -e .ipynb`). If you are ever in doubt you can run `statistics -h` to get a help output on console reminding you of the flags.

#### Zsh Instructions
Some shells (such as the one for MacOS Catalina) do not use bash. In that case, you need to quickly configure Python commands to be runnable from terminal. There's a quick, temporary option 1 or a long-term, more complicated option 2.

##### Option 1 - Quick but Temporary
In your terminal, type: `bash -login`. You will now be in the bash shell. You can use it like a normal shell and you will be able to run the `statistics` command there.

##### Option 2 - Longer but Permanent
1. Type: `open ~/.bash_profile` and `open ~/.zshrc`. You will have two files open, one with the profile for bash and one with the profile for zsh.
2. You should see a PATH for your Python installation in the `bash_profile` file.
    ```
    # Setting PATH for Python 3.8
    # The original version is saved in .bash_profile.pysave
    PATH="/Library/Frameworks/Python.framework/Versions/3.8/bin:${PATH}"
    export PATH
    ```
    This may be slightly different for you if you have a different Python version. Copy this and paste it at the top of your `.zshrc` file.

3. Write the following command into your `.zshrc` file as well to support packages: `export PATH=$PATH:~/.local/bin` on a new line. <br> Once you are done, save the `.zshrc` file and close both.

4. Go back to your terminal, and type: `source ~/.zshrc` to refresh the profile.

5. All done! Just restart your terminal and you will be able to run the `statistics` command and *any* other Python command-line commands from `zsh` as well.

## Requirements
All you need to do is make sure that you are running this on **Python 3** and have **pip installed** (`sudo easy_install pip`).

There is no need to individually install any packages because when you create the local package, it will automatically install those for you as it is being created. As long as you correctly type in `python3 -m pip install -e .` in the root directory of the project, you're good to go!

### Credits
I based this idea off of [linguist](https://github.com/github/linguist), which is the default GitHub program used to generate the color bar used in every repository. I also used their `languages.yml` file to recognize languages (with permission due to the MIT License).
