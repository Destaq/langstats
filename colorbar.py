import language_bytes
import cairo
import math


def hex_to_rgb(code):
    hexf = code.lstrip("#")
    hlen = len(hexf)
    return tuple(int(hexf[i : i + hlen // 3], 16) for i in range(0, hlen, hlen // 3))


def draw_statistics(other: int, maximum: int):
    data = language_bytes.read_file_data()

    bytesum = 0
    for ele in data:
        bytesum += data[ele][0]

    language_percentages = {}
    current_total_percentage = 0
    count = 0
    removed_dictionary = data.copy()
    for language in data:
        if current_total_percentage > other or count >= maximum:
            if 'Other' in language_percentages:
                language_percentages['Other'] += round(data[language][0] / bytesum, 4) * 100
                removed_dictionary['Other'][0] += removed_dictionary.pop(language)[0]
            else:
                language_percentages['Other'] = round(data[language][0] / bytesum, 4) * 100
                removed_dictionary['Other'] = removed_dictionary.pop(language)
                removed_dictionary['Other'][1] = '#aaaaaa'
        else:
            language_percentages[language] = round(data[language][0] / bytesum, 4) * 100
            current_total_percentage += round(data[language][0] / bytesum, 4) * 100

        count += 1

    data = removed_dictionary

    WIDTH, HEIGHT = 410, 200

    surface = cairo.SVGSurface("output.svg", WIDTH, HEIGHT)
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
            x, 20, round(language_percentages[language]) * 4, 10
        )  # modify the third (width)

        x += round(language_percentages[language]) * 4

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
        ctx.show_text(str(round(language_percentages[language], 2)) + "%")

        text_x += (
            ctx.text_extents(str(round(language_percentages[language], 2)) + "%")[2] + 30
        )
