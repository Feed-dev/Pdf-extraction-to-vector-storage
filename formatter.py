input_text = """
Goetia
Alignment: demonology, sorcery, occultism, ceremonial magic, Western esotericism, evocation
Goal: summon and control demons, acquire knowledge and power, fulfill desires, spiritual exploration
Purpose: engage with spiritual entities, explore the psyche, personal transformation, self-empowerment
Tradition: ancient Greco-Roman magic, medieval grimoires, The Lesser Key of Solomon, occult revival
Practices: invocation rituals, magic circles, protective evocation, use of seals and sigils, negotiation with spirits
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
