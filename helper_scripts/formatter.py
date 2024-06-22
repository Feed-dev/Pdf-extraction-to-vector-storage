input_text = """
zos kia sorcery
alignment: individualistic, transgressive, ecstatic, antinomian, subconscious
goal: access Kia (primal self), excreate/manifest desires, transcend duality, attain magical power and wisdom
purpose: liberate from societal/mental limitations, empower true will, evolve consciousness, achieve cosmic self-love
tradition: developed by Austin Osman Spare, influenced by Thelema, witchcraft, tantra, atavistic resurgence
practices: sigil magic, mantras, death posture, sacred alphabet, sexual gnosis, automatic drawing, dream control
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
