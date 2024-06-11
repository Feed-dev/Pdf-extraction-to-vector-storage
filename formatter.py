input_text = """
tantra
Alignment: Aghora, Ayurveda, Tantra, Jyotish, Western esotericism, spiritual alchemy
Goal: self-realization, spiritual enlightenment, samarasa (equanimity), svatantra (self-functioning), bliss of undifferentiated consciousness
Purpose: disseminate teachings of Aghora and Tantra, bridge Eastern and Western thought, guide spiritual seekers, promote holistic well-being
Tradition: mentored by Aghori Vimalananda, influenced by Indian and Western esoteric traditions, Ayurveda, Yoga, Jyotish
Practices: ritual, mantra, meditation, self-inquiry, extracting rasa (vital essence), navigating personas, intense (ugra) and speedy (shighra) methods
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
