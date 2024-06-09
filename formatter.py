input_text = """
parapsychology
Alignment: parapsychology, psychical research, anomalous experiences, altered states of consciousness, spiritualism
Goal: investigate paranormal phenomena, explore the nature of consciousness, expand scientific understanding, challenge materialist paradigms
Purpose: document evidence of psi, develop theories and models, refine methodologies, educate the public, advance the field
Tradition: 19th century origins, Society for Psychical Research, J.B. Rhine and experimental parapsychology, survival research, skeptic/proponent dialogue
Practices: case studies, field investigations, experimental testing, statistical analysis, qualitative approaches, theoretical discourse, peer-reviewed journals
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
