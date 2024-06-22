input_text = """
Taoism
alignment: spiritual, philosophical, naturalistic, holistic, harmonious
goal: align with the Tao (the Way), attain serenity and inner peace, achieve harmony and balance, cultivate virtues, realize true self
purpose: live in accord with nature's rhythms, embrace simplicity and spontaneity, transform consciousness, nourish life essence, provide guidance for good living
tradition: ancient Chinese origins, influenced by Lao Tzu and Zhuangzi, religious and philosophical branches, syncretism with Buddhism and Confucianism
practices: meditation, qigong, tai chi, feng shui, ritual, divination, alchemy, self-cultivation, living in harmony with seasons and natural cycles
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
