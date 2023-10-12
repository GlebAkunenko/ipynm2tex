# ipynm2tex

This is a small ugly script that can convert your **Jupyter Notebook file to a LaTeX report**.
It supports converting tables and listings but markdown is pretty broken, I am sorry.

<img width="960" alt="img1" src="https://github.com/GlebAkunenko/ipynm2tex/assets/47637357/da61ff9c-3bab-41cb-b877-3a68c9bf23b7">


## Installation

For using this one you just need the Python and this repository,
that can be cloned by
```
git clone https://github.com/GlebAkunenko/ipynm2tex.git
```
The execution file is `ipynm2tex.py`.
For getting short manual write `python ipynm2tex.py -h`

## Requirements

The project require some libraries. So you have to use
a virtual environment inside this one (I've loaded it to the
repo, but I don't know is it a good idea).

Or if you use Windows you can just load all requirements
from `requirements.txt` by entering command below.
```
pip install -r requirements.txt
```
In this case you can delete the 160 Mb venv folder!

## Features and problems
It can and cannot convert these parts of notebook.
- [x] table;
- [x] code to listing;
- [x] code result to listing;
- [ ] markdown (I am lazy);
- [ ] images (may be later);
- [ ] graphics (may be later);

## Shortcut

If you are the Windows user you may create
a cmd shortcut for move convenient usage.
```
@echo off
<python in venv / python> <path to project>\ipynm2tex.py %cd% %1 %2 %3
```

If you want upgrade this project you can contact with me by tg: @Gleb1000
