def edit_string(string: str) -> str:
	string = string.\
		replace(r' \"', " ``").\
		replace(r'\" ', "'' ").\
		replace(r'" ', "'' ").\
		replace(r' "', " ``").\
		replace('**', "").\
		replace('`', '').\
		replace("__", '').\
		replace("_", "\\_").\
		replace("#", "")
	return string