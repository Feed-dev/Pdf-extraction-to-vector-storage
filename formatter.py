input_text = """
Mantak Chia
Alignment: Taoism, inner alchemy, microcosmic orbit, energy cultivation, three treasures, five elements
Goal: self-healing, vitality, longevity, spiritual development, enlightenment, immortality, cosmic unity
Purpose: harmonize body-mind-spirit, transform negative emotions, open energy channels, develop soul and spirit bodies
Tradition: Taoist yoga, qigong, tai chi, iron shirt, healing love, fusion, kan and li, ancient Chinese practices
Practices: inner smile, six healing sounds, microcosmic orbit, iron shirt qigong, healing love, fusion meditations, kan and li, tai chi, chi nei tsang, cosmic healing
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
