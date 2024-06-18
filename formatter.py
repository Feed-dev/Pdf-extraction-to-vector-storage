input_text = """
Alchemy
Alignment: ancient philosophy, natural science, spiritual practice, esoteric tradition
Goal: transmutation of metals, immortality elixir, universal panacea, perfection of matter and spirit
Purpose: uncover secrets of nature, achieve spiritual enlightenment, acquire divine knowledge
Tradition: Greco-Roman Egypt, Islamic world, medieval Europe, ancient China, India
Practices: laboratory techniques, symbolic language, ciphers, allegorical illustrations, chemical experiments, spiritual rituals
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
