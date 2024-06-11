input_text = """
Meditation
Alignment: mindfulness, self-awareness, inner peace, spiritual growth, mental well-being
Goal: calm the mind, reduce stress, gain insight, cultivate compassion, attain enlightenment
Purpose: develop concentration, increase self-understanding, promote relaxation, enhance overall well-being
Tradition: ancient practice, Eastern religions (Buddhism, Hinduism), yoga, adapted in Western contexts
Practices: breath awareness, mantra repetition, visualization, loving-kindness, body scan, walking meditation
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
