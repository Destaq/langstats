from language_statistics import language_bytes
import cairo
import math
from PIL import Image
import os


def hex_to_rgb(code):
    hexf = code.lstrip("#")
    hlen = len(hexf)
    return tuple(int(hexf[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


def draw_statistics(extension: str, other: int, maximum: int, depth: int, exclude: list):
    data = language_bytes.read_file_data(depth, exclude)

    bytesum = 0
    for ele in data:
        bytesum += data[ele][0]

    language_percentages = {}
    current_total_percentage = 0
    count = 0
    removed_dictionary = data.copy()
    for language in data:
        if current_total_percentage > 100 - other or count >= maximum:
            if 'Other' in language_percentages:
                language_percentages['Other'] += round(data[language][0] / bytesum, 4) * 100
                removed_dictionary['Other'][0] += removed_dictionary.pop(language)[0]
            else:
                language_percentages['Other'] = round(data[language][0] / bytesum, 4) * 100
                removed_dictionary['Other'] = removed_dictionary.pop(language)
                removed_dictionary['Other'][1] = '#aaaaaa'
        else:
            try:
                language_percentages[language] = round(data[language][0] / bytesum, 4) * 100
            except ZeroDivisionError:
                language_percentages[language] = 0

        try:
            current_total_percentage += round(data[language][0] / bytesum, 4) * 100
        except ZeroDivisionError:
            pass

        count += 1

    data = removed_dictionary
    WIDTH, HEIGHT = 410, 400


    y_len = 60
    x_len = 25
    surf_sample = cairo.SVGSurface("output.svg", WIDTH, HEIGHT)
    ctx_sample = cairo.Context(surf_sample)

    if extension.lower() == 'svg':
        for language in language_percentages:
            if (
            x_len
            + ctx_sample.text_extents(language + ' ')[2]
            + 40
            + ctx_sample.text_extents(str(round(language_percentages[language], 2)))[2]
            >= WIDTH):
                x_len = 25
                y_len += 30

            x_len += ctx_sample.text_extents(language + " ")[2] + 10
            output_2f = "%.2f" % round(language_percentages[language], 2)
            x_len += ctx_sample.text_extents(output_2f + "%")[2] + 30

        surface = cairo.SVGSurface("output.svg", WIDTH, y_len + 30) # create some bottom space
        is_png = False

    else:
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
        is_png = True

    ctx = cairo.Context(surface)

    x, text_x, text_y, text_height = 3, 25, 60, 0
    for language in language_percentages:

        if (
            text_x
            + ctx.text_extents(language + ' ')[2]
            + 40
            + ctx.text_extents(str(round(language_percentages[language], 2)))[2]
            >= WIDTH
        ):
            text_x = 25
            text_y += 20

        ctx.rectangle(
            x, 20, round(language_percentages[language] * 4), 10
        )  # modify the third (width)

        x += round(language_percentages[language] * 4)

        code = data[language][1][1:]
        output = hex_to_rgb(code)

        ctx.set_source_rgb(output[0] / 255, output[1] / 255, output[2] / 255)

        ctx.fill()

        # draw box for the legend
        # ctx.rectangle(text_x - 20, text_y - 15, 15, 15)
        ctx.arc(text_x - 8, text_y - 5, 4, 0, 2 * math.pi)
        ctx.fill()

        # draw the text for that language
        ctx.set_source_rgb(0, 0, 0)

        ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(14)

        ctx.move_to(text_x, text_y)
        ctx.show_text(language + " ")

        text_x += ctx.text_extents(language + " ")[2] + 10

        ctx.select_font_face("Arial", cairo.FONT_SLANT_ITALIC, cairo.FONT_WEIGHT_NORMAL)
        ctx.set_font_size(14)
        output_2f = "%.2f" % round(language_percentages[language], 2)
        ctx.show_text(output_2f + "%")

        text_x += (
            ctx.text_extents(output_2f + "%")[2] + 30
        )

    if is_png == True:
        # crop image

        surface.write_to_png("output.png")

        im = Image.open("output.png") 

        im.crop((0, 0, WIDTH, text_y + 30)).save("output.png") # in case last is not other


    else:
        pass