#! /usr/local/bin/python3.10
from pathlib import Path 
import projet_fini.AB_recupio.arguments as arguments

def computer_list(): 
    """Liste tout les fichier est dossier a partir de la racine

    Yields:
        Path: fichier ou dossier 
    """
    
    for element in Path('/').rglob("**"): 
        yield element
        

args = arguments.args()

for element in computer_list(): 
    if Path(element).is_file() and args.: 
        pass 
    elif Path(element).is_dir(): 
        pass 