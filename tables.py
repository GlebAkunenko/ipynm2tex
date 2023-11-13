import pandas


def _parse_body(table: str) -> str:
	data = pandas.read_html(table)[0]
	head = data.keys().tolist()
	if isinstance(head[0], tuple):
		head = list(map(lambda x: " ".join(x), head))
	result = " & ".join(head[1:]) + r" \\ \hline" + "\n"
	for v in data.values:
		row = list(map(str, v.tolist()))
		result += " & ".join(row[1:]) + r" \\" + "\n"
	return result


def _get_column_count(table: str) -> int:
	data = pandas.read_html(table)[0]
	return data.keys().size


_pattern_resized = r"""
\begin{table}[h!]
    \centering
    \caption{}
    \resizebox{\textwidth}{!}{
    \begin{tabular}{[C]}
    \hline
[BODY]
	\hline
    \end{tabular}}
    \label{tab:my_label}
\end{table}
"""

_pattern = r"""
\begin{table}[h!]
    \centering
    \caption{}
    \begin{tabular}{[C]}
    \hline
[BODY]
	\hline
    \end{tabular}
    \label{tab:label}
\end{table}
"""


def parse_html_table(table: str) -> str:
	n =  _get_column_count(table)
	c = "c".join(["|"] * n)
	pattern = _pattern_resized if n > 5 else _pattern
	return pattern.\
		replace("[C]", c).\
		replace("[BODY]", _parse_body(table))


