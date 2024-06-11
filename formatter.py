input_text = """
golden dawn
Alignment: Western esotericism, Hermeticism, Rosicrucianism, Kabbalah, ceremonial magic, alchemy
Goal: spiritual enlightenment, self-realization, attainment divine wisdom, unity divine
Purpose: study practice occult sciences, preservation esoteric knowledge, initiation mysteries
Tradition: occult revival, Freemasonry, Societas Rosicruciana Anglia, Cipher Manuscripts
Practices: grade initiations, ritual magic, invocation, divination, astrology, tarot, geomancy, Enochian magic
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
