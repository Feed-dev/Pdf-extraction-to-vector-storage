input_text = """
Dion Fortune
Alignment: Western esotericism, occultism, ceremonial magic, Hermeticism, Kabbalah, Jungian psychology
Goal: spiritual development, self-realization, psychic self-defense, esoteric wisdom, service to humanity
Purpose: teach esoteric principles, empower individuals, heal psychological wounds, unite occult traditions
Tradition: Hermetic Order of the Golden Dawn, Theosophy, Christian mysticism, Glastonbury, Arthurian legends
Practices: meditation, visualization, ritual magic, path working, dream analysis, writing, training others
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
