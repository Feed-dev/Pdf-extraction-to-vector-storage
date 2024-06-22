input_text = """
tarot
alignment: spiritual, intuitive, introspective, holistic, self-reflective
goal: gain insight and wisdom, align with purpose, set and achieve goals, make decisions, personal growth and transformation
purpose: access inner wisdom, create the future, manifest desires, promote self-awareness, provide guidance and clarity
tradition: ancient divination, playing cards, esoteric associations, fortune-telling, modern psychological and spiritual tool
practices: card reading, intuitive interpretation, spreads, meditation, journaling, visualization, integration into goal-setting and planning
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
