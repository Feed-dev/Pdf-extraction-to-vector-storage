input_text = """
Gnostics
Alignment: dualism, anti-materialism, hidden knowledge, divine spark, spiritual awakening
Goal: attain gnosis, reunite divine spark with God, transcend material world, achieve spiritual liberation
Purpose: expose illusory nature of reality, reveal path to enlightenment, free souls from cycle of reincarnation
Tradition: syncretic, Judeo-Christian roots, Platonic and Neoplatonic influences, mystery religions, esoteric wisdom
Practices: ritual, magic, theurgy, liturgy, asceticism, baptism, Eucharist, meditation, mystical union
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
