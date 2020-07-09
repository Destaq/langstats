# language-statistics
With `language-statistics`, you can create a high-quality image of the programming languages and their percentages used in your directory. It is **runnable anywhere** and is **highly customizable**, an improved clone of the `linguist` package that comes with GitHub.

## Features
### Available Globally
This is an executable Python script that can be run from any folder or location on your device. This means that you can easily view the language distribution for folders that don't have the python script in their directories. By implementing this, a *major advantage* is introduced over `linguist`, which can only be used for visualizations for GitHub repositories, often takes hours to refresh, and has very weak text-only command-line functionality.

### Tweakable
It's very easy to change the look of your outputted image. You can easily specify at what percentage programming languages will merge into the 'Other' category, as well as how many unique languages to display at once.

## Usage

## Requirements
There's only two requirements, both available on PyPI! You can install them individually or install both at once with `pip3 install -r requirements.txt` in the directory of the program.
- pycairo: `pip3 install pycairo`
- PyYAML: `pip3 install PyYAML`

### Credits
I based this idea off of [linguist](), which is the default GitHub program used to generate the color bar used in every repository. I also used their `languages.yml` file to recognize languages (with permission thanks to the MIT License).