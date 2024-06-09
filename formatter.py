input_text = """
mystics
Alignment: spirituality, holistic health, mind-body-spirit connection, higher self, soul growth
Goal: self-discovery, self-mastery, spiritual enlightenment, living in alignment with purpose, elevating consciousness
Purpose: provide psychic readings, offer guidance and wisdom, promote spiritual growth, heal mind and body
Tradition: Christian mysticism, Theosophy, New Thought, Akashic records, reincarnation, karma
Practices: meditation, dream interpretation, holistic nutrition, attunement of mind-body-spirit, readings in trance state
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
