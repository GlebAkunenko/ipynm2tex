def is_table_even(table: str | list[str]) -> bool:
	if isinstance(table, str):
		table = table.split('\n')
	lengths = list(map(len, table))
	return max(lengths) - min(lengths) < 2