input_text = """
Companions of the Stone
Alignment: Western esotericism, Hermeticism, Rosicrucianism, Freemasonry, ceremonial magic, Kabbalah, alchemy
Goal: spiritual enlightenment, self-realization, attainment of divine wisdom, unity with the divine, personal transformation
Purpose: study and practice of occult sciences, preservation of esoteric knowledge, initiation into mysteries, development of magical abilities
Tradition: ancient mystery schools, Neoplatonism, Renaissance magic, Rosicrucian manifestos, Freemasonry, 1800s occult revival
Practices: ritual magic, invocation, evocation, divination, astrology, tarot, geomancy, skrying, pathworking, grade initiations, lodge work
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
