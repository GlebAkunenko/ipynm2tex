import base64

def save_image_from_string(data: str, file_name: str):
	with open(file_name, "wb") as fh:
		fh.write(base64.decodebytes(bytes(data, 'utf-8')))


_pattert = r"""
\begin{figure}[h!]
  \centering
  \includegraphics[width=0.9\textwidth]{img/[INDEX].png}
  \caption{[CAPT]}
  \label{fig:[INDEX]}
\end{figure}
"""

def get_image_code(picture_index: int | str, caption = "") -> str:
	picture_index = str(picture_index)
	return _pattert.replace("[INDEX]", picture_index).replace("[CAPT]", caption)