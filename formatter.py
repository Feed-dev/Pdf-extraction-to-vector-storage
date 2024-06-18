input_text = """
astral workings
alignment: spiritual development, self-discovery, personal growth, healing
goal: explore inner self, gain new perspectives, connect with higher consciousness, communicate with spiritual beings
purpose: separate soul/consciousness from physical body, travel to other realms/dimensions beyond physical world
tradition: present in various cultures for centuries, associated with theosophy, mystical Christianity, yoga, Kabbalah, Hindu philosophy
practices: meditation, visualization, lucid dreaming, sensory deprivation, binaural beats, dream journaling, setting intention, Kundalini experiences
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
