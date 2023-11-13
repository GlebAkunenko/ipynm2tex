def _convert_sections(line: str) -> str:
	if not line.startswith('#'):
		return line
	count = 0
	for i in range(len(line)):
		if line[i] != "#":
			count = i
			break
	if count == 1:
		return r"\section{" + line[count:] + "}\n"
	if count > 1:
		return r"\subsection{" + line[count:] + "}\n"
	return line

def edit_string(string: str) -> str:
	string = string.\
		replace(r' \"', " ``").\
		replace(r'\" ', "'' ").\
		replace(r'" ', "'' ").\
		replace(r' "', " ``").\
		replace('**', "").\
		replace('`', '').\
		replace("__", '').\
		replace("_", "\\_")
	lines = string.split("\n")
	lines = [_convert_sections(line) for line in lines]
	return "\n".join(lines)