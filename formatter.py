input_text = """
Astrology
Alignment: cosmos, celestial bodies, zodiac, constellations, ecliptic, seasons
Goal: self-understanding, personality insights, life guidance, decision-making, timing
Purpose: meaning, patterns, cycles, archetypes, mythology, symbolism, synchronicity
Tradition: ancient, Babylonian, Hellenistic, Vedic, Western, Chinese, Mesoamerican
Practices: horoscope, natal chart, zodiac signs, planetary movements, astrological readings
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
