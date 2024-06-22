input_text = """
esoteric psychology
alignment: spiritual, philosophical, esoteric, non-dogmatic, universal
goal: spiritual enlightenment, self-realization, understanding the mysteries of life, harmonizing science/philosophy/religion, promoting brotherhood
purpose: help humanity find wisdom and meaning, nurture spiritual growth, provide a rational basis for religious ideas, further the search for truth
tradition: ancient wisdom, perennial philosophy, influenced by Eastern and Western mysticism, esotericism, modernist re-evaluation of religious traditions
practices: study, meditation, self-transformation, living one's beliefs, open-minded inquiry, altruistic service, comparative study of religions and philosophies
"""


# Function to format the input text and convert to lowercase
def format_text(input_text):
    lines = input_text.strip().split('\n')
    namespace = lines[0].lower()
    formatted_output = f'namespace = "{namespace}"\n'

    for line in lines[1:]:
        key, value = line.split(': ')
        key = key.strip().lower()
        value = ' '.join(value.lower().split(', ')).strip()
        formatted_output += f'{key} = "{value}"\n'

    return formatted_output


# Get the formatted text
formatted_text = format_text(input_text)
print(formatted_text)
