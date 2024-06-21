input_text = """
grimoires
alignment: textbook of magic, belief in magical powers imbued in the books themselves, mixture of healing recipes and demon invocation
goal: provide instructions for creating magical objects, casting spells, performing divination, and summoning supernatural entities
purpose: preserve and transmit occult knowledge, enable magic practitioners to access powers and entities, achieve specific magical effects
tradition: ancient roots in Europe and Near East, medieval and Renaissance ceremonial magic, influenced modern occult revival and fantasy fiction
practices: creation of talismans and amulets, spells and charms, rituals for summoning angels, demons, spirits, preparation of magical tools, lists of ingredients and correspondences
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
