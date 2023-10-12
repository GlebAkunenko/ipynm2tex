import json
from tables import *
import listrings, markdown


def run(input_path: str, output_path: str):

	with open(input_path, 'r', encoding='utf-8') as f:
		data = json.load(f)['cells']

	result = ""

	for block in data:
		match block['cell_type']:
			case "markdown":
				result += markdown.edit_string("".join(block['source']) + "\n")
			case "code":
				code = "".join(block['source'])
				result += listrings.convert_code(code) + "\n"
				if len(block['outputs']) > 0:
					output = block['outputs'][0]
					match output['output_type']:
						case "stream":
							text = "".join(output['text'])
							result += listrings.convert_code(text, "Результат выполнения программы", lang="") + "\n"
						case "execute_result":
							if output['data'].get('text/html'):
								table = "\n".join(output['data']['text/html']).strip()
								result += parse_html_table(table).replace("_", "\\_")
							else:
								text = "".join(output['data']['text/plain'])
								result += listrings.convert_code(text, "Результат выполнения программы", lang="") + "\n"

	with open(output_path, 'w', encoding='utf-8') as f:
		f.write(result)

