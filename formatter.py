input_text = """
kabbalah
Alignment: occultism, ceremonial magic, Kabbalah, Tarot, Hermeticism, Catholicism
Goal: reconcile magic and religion, attain spiritual enlightenment, master occult forces
Purpose: revive Western magical tradition, influence esoteric thought, inspire secret societies
Tradition: French occultism, Rosicrucian and Masonic influences, Christian Kabbalah, Goetia
Practices: ritual magic, astral projection, magnetism, divination, magical evocation, esoteric writing
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
