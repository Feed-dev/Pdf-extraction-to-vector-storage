input_text = """
Grimoires
Alignment: sorcery, witchcraft, low magic, deceptive, fraudulent, heretical, pagan
Goal: instruct in magical practices, summon supernatural entities, attain power and fulfillment
Purpose: transmit magical knowledge, enable casting spells and crafting magical objects, guide divination
Tradition: ancient Mesopotamian and Egyptian origins, influenced by Hellenistic and early Christian magic, attributed to legendary figures like Solomon
Practices: incantations, spells, crafting magical objects, summoning angels/spirits/demons, divination, astrology
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
