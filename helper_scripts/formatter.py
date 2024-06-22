input_text = """
kabbalah
alignment: Jewish mysticism, esoteric, theosophical, meditative, practical/magical
goal: unite with divine, understand creation, transform consciousness, manifest desires, align lower and higher realities
purpose: give meaning to religious practice, redeem spiritual realms through human conduct, achieve spiritual enlightenment, cultivate virtues and life purpose
tradition: medieval Zoharic Kabbalah, Lurianic Kabbalah, Ecstatic/Prophetic Kabbalah of Abulafia, Practical/Magical Kabbalah, Hermetic Qabalah
practices: Torah study (PaRDeS), meditation, prayer, white magic, talismans, letter/number mysticism, Tree of Life, Sefirot contemplation
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
