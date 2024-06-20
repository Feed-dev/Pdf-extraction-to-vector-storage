input_text = """
astral workings
alignment: conscious awareness, self-reflective, intentional, eclectic, individualistic
goal: dream control, self-discovery, problem-solving, skill practice, fear confrontation, fulfilling desires
purpose: self-awareness, personal growth, creativity, mental health, spiritual development, entertainment
tradition: ancient, cross-cultural, Hinduism, Buddhism, Tibetan Dream Yoga, Sufism, modern Western interest
practices: reality checks, dream journaling, wake back to bed, mnemonic induction, meditation, supplements, electronic devices
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
