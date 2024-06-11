input_text = """
Solomon
Alignment: ceremonial magic, demonology, Solomonic magic, Judeo-Christian, Western esotericism
Goal: invoke and control spirits, acquire knowledge and power, fulfill desires, spiritual attainment
Purpose: provide detailed instructions for magical operations, act as a comprehensive guide to ceremonial magic
Tradition: attributed to King Solomon, influenced by Jewish mysticism, Hermeticism, medieval grimoires
Practices: complex rituals, consecration of magical tools, drawing of magical circles, sigils, and pentacles, prayers and invocations, spirit evocation
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
