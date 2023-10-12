pattern = r"""
\begin{lstlisting}[language={[LANG]},caption={[CAP]}]
[CODE]
\end{lstlisting}
"""


def convert_code(source: str, caption="", lang="Python") -> str:
	return pattern.replace("[CODE]", source).replace("[CAP]", caption).replace("[LANG]", lang)