input_text = """
esoteric psychology
alignment: spiritual, soul-centered, inner-focused, philosophical, integrative
goal: understand soul and personality, express soul purpose, attain spiritual wisdom and enlightenment, transform consciousness
purpose: bridge personality and soul, promote soul evolution and incarnation, apply ancient wisdom teachings to psychology, expand beyond mainstream psychology
tradition: Ancient Wisdom, Theosophy, Alice Bailey teachings, Seven Rays, Hermeticism, Western Esotericism
practices: meditation, study of soul and personality types, ray analysis, building antahkarana (bridge to higher self), alignment and balancing of subtle bodies, self-reflection and introspection
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
