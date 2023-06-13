import argparse

parser = argparse.ArgumentParser(description='CLI program to capitalize text content of a file.')
parser.add_argument('--input_file', help='path to the input file')
parser.add_argument('--output_file', help='path to the output file')
parser.add_argument('--reverse', action='store_true', help='reverse the capitalized content')

args = parser.parse_args()
input_file = args.input_file
output_file = args.output_file
reverse = args.reverse

def capitalize_file(input_file, output_file, reverse):
    with open(input_file, 'r') as file:
        content = file.read()

    capitalized_content = content.upper()

    if reverse:
        capitalized_content = capitalized_content[::-1]

    with open(output_file, 'w') as file:
        file.write(capitalized_content)


capitalize_file(input_file, output_file, reverse)