# ipynm2tex

This is a small script that can convert your **Jupyter Notebook file to a LaTeX report**.
It supports converting tables and listings whereas markdown is pretty broken, my bad.

<img width="960" alt="img1" src="https://github.com/GlebAkunenko/ipynm2tex/assets/47637357/da61ff9c-3bab-41cb-b877-3a68c9bf23b7">


## Installation

For using this script you need the Python and this repository,
that can be cloned by
```
git clone https://github.com/GlebAkunenko/ipynm2tex.git
```
The execution file is `ipynm2tex.py`.
For getting short manual write `python ipynm2tex.py -h`

## Requirements

The project require some libraries. So you have to use
a virtual environment inside this project (I've loaded it to the
repo, but I don't know whether it is a good idea).

Or if you use Windows you can load all requirements
from `requirements.txt` by entering command given below.
```
pip install -r requirements.txt
```
In this case you may delete the 160 Mb venv folder!

## Features and problems
Script can convert some parts of notebook which are marked with X. 
- [x] table;
- [x] code to listing;
- [x] code result to listing;
- [ ] markdown (I am lazy);
- [ ] images (may be later);
- [ ] graphics (may be later).

## Shortcut

If you are a Windows user you may create
a cmd shortcut for a more convenient usage.
```
@echo off
<python in venv / python> <path to project>\ipynm2tex.py %cd% %1 %2 %3
```

If you want upgrade this project you can contact via tg: @Gleb1000
