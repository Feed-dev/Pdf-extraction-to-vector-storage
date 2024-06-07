input_text = """
Astrology
alignment: zodiac sign traits, cosmic energies, moral alignment, lawful good, chaotic evil, true nature, purpose
goal: self-understanding, wise decisions, align actions, true purpose, career, relationships, personal growth, realistic goals, zodiac sign strengths, challenges
purpose: life path, celestial bodies at birth, self-discovery, personality insights, potential, life purpose, explain personality types, tendencies, decision-making, fulfilling life, meaningful life, true self
tradition: ancient, extra-scientific knowledge, mythology, cosmic nature of being, Mesopotamia, 19th-17th century BCE, Ancient Greece, Rome, Islamic world, Europe, traditional astrology, prediction, modern astrology, explanation, self-actualization, core principles, 12 zodiac signs, planets, houses
practices: birth chart analysis, horoscope readings, zodiac sign analysis, planetary aspects and transits, house systems
"""


# Function to format the input text
def format_text(input_text):
    lines = input_text.strip().split('\n')
    namespace = lines[0].lower()
    formatted_output = f'namespace = "{namespace}"\n'

    for line in lines[1:]:
        key, value = line.split(': ')
        key = key.strip()
        value = ' '.join(value.split(', ')).strip()
        formatted_output += f'{key} = "{value}"\n'

    return formatted_output


# Get the formatted text
formatted_text = format_text(input_text)
print(formatted_text)
