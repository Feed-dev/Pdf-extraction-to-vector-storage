input_text = """
setian
alignment: individualistic, self-deifying, left-hand path, psyche-centric, isolate existence
goal: attain immortality of consciousness, preserve and strengthen individual essence, become one's own god, achieve Xeper (self-transformation/evolution)
purpose: reject surrender to external deities, uphold individual agency and power, reach personal apotheosis, magically influence subjective universe
tradition: Temple of Set (founded 1975), influenced by Church of Satan hierarchy, Egyptian god Set as archetype of isolate self-consciousness
practices: initiatory degrees, application and evaluation for membership, individual ritual magic, birthday celebrations, pursuit of self-development
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
