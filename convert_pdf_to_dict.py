from pdfminer.high_level import extract_text

# мне вот этот больше нравится. Достаточно быстрый, элегантный, понятный.
def convert_pdf_in_dict_1_1(file):
    text_from_pdf = extract_text(file)

    key_value_list = [i.split(":") for i in text_from_pdf.split("\n") if len(i.split(":")) == 2]
    keys = [i[0] for i in key_value_list]
    values = [i[1] for i in key_value_list]

    return {key.strip(): value.strip() for (key, value) in zip(keys, values)}

def convert_pdf_in_dict_1_0(file):

    key_value_list = [i.split(":") for i in extract_text(file).split("\n") if len(i.split(":")) == 2]
    keys = [i[0] for i in key_value_list]
    values = [i[1] for i in key_value_list]

    return {key.strip(): value.strip() for (key, value) in zip(keys, values)}


def convert_pdf_in_dict_2(file):
    key_value_list = []

    text_from_pdf = extract_text(file)

    split_text_from_pdf = text_from_pdf.split("\n")
    for i in split_text_from_pdf:
        i = i.split(":")
        if len(i) == 2:
            key_value_list.append(i)
    keys = [i[0] for i in key_value_list]
    values = [i[1] for i in key_value_list]

    return {key.strip(): value.strip() for (key, value) in zip(keys, values)}