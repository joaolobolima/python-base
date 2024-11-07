#!/usr/bin/env python3
"""This text is used as a documentation for the code for what this do.

Hello World Multi Language.

Usage:

Have the variable LANG configured:

    export LANG=pt_BR

    Execution:

    python3 hello.py
    or
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "João Lobo"
__licence__ = "Unlicense"
#import the library for the code to communicate with the OS
import os

current_language = os.getenv("LANG", "pt_BR").split(".")[0]

#LANG[:5] will show only the first 5 characters
#LANG.split(".") will split the text where it finds "."
#LANG.split(".")[0] pega somente o que está antes do ponto


msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_MX":
    msg = "Hola, Mundo!"


print(msg)
