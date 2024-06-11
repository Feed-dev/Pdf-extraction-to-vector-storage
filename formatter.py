input_text = """
Edgar Cayce
Alignment: spirituality, holistic health, psychic abilities, reincarnation, Atlantis, Christianity
Goal: help others, access higher wisdom, promote spiritual growth, heal mind-body-spirit
Purpose: give psychic readings, offer spiritual guidance, advance soul development, serve humanity
Tradition: Christian mysticism, Theosophy, New Thought, Akashic records, dream interpretation
Practices: trance readings, meditation, prayer, dream analysis, holistic remedies, past life readings
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
