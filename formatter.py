input_text = """
aleister crowley
alignment: occultist, religious skeptic, decadent lifestyle, rejected Christianity, individualistic
goal: cause change in conformity with Will, provoke change aligned with True Will, become one's true self beyond ego and expectations
purpose: bring oriental wisdom to Europe, restore purer form of paganism, merge with higher power, align individuals with their True Will in new Aeon of Horus
tradition: Hermetic Order of the Golden Dawn, Ordo Templi Orientis, founded own order A∴A∴ and religion of Thelema, influenced by ceremonial magic, Rosicrucianism, Kabbalah, yoga, Buddhism
practices: ritual magic, sex magic, drug use, mountaineering, poetry, art, channeled writing of The Book of the Law, defined "Magick" as science and art of causing change in conformity with Will
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
