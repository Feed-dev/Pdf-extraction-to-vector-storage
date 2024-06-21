input_text = """
evocation
alignment: ceremonial magic, Hermetic, Neoplatonic, medieval grimoires, spirit summoning
goal: call forth spirits, demons, deities, or supernatural agents to appear externally, command and direct them to perform tasks or impart knowledge
purpose: gain power and knowledge from spirits, bind spirits to the magician's will, access supernatural abilities, divine information
tradition: ancient Neoplatonic theurgy, medieval and Renaissance ritual magic texts like the Keys of Solomon, Lemegeton, Abramelin, 19th-20th century occult revival
practices: ritual circle casting, directing spirits into triangle of manifestation, use of wands, sigils and divine names, incantations and conjurations, offerings or pacts with spirits
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
