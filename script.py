#! /usr/local/bin/python3.10
from pathlib import Path
import arguments as arguments


def computer_list(file: bool=False, folder: bool=False):
    """Liste tout les fichier est dossier a partir de la racine

    Yields:
        Path: fichier ou dossier 
    """

    for element in Path('/').rglob("**"):
        if file and element.is_file(): 
            yield element
        
        elif folder and element.is_dir(): 
            yield element
            
        else: 
            yield element
            

def search(file: str, research: str) -> bool: 
    if isinstance(file, Path): 
        file = str(file)
    
    return file.startswith(research) or file.endswith(research) or file == research or file in research



args = arguments.args()

for element in computer_list():
    if not args.folder and not args.file:
        pass
    elif Path(element).is_file() and args.file:
        pass
    elif Path(element).is_dir() and args.folder:
        pass
