#! /usr/local/bin/python3.10
from colorama import Fore, Back
from pathlib import Path

import arguments as arguments



def computer_list(file: bool = False, folder: bool = False):
    """Liste tout les fichier est dossier a partir de la racine

    Yields:
        Path: fichier ou dossier 
    """
    for element in Path(Path.cwd().root).rglob("*"):

        try:
            if file and element.is_file():
                yield element

            elif folder and element.is_dir():
                yield element

            elif not folder and not file:
                yield element

        except PermissionError:
            pass


def search(file: str | Path, research: str) -> bool:
    if isinstance(file, Path):
        file = str(file)

    return (file.startswith(research) or file.endswith(research)) or (file == research or file in research)


if __name__ == '__main__':
    print(Fore.RED, """
          
        
         $$$$$$\  $$$$$$$\                                                            $$\           
        $$  __$$\ $$  __$$\                                                           \__|          
        $$ /  $$ |$$ |  $$ |         $$$$$$\   $$$$$$\   $$$$$$$\ $$\   $$\  $$$$$$\  $$\  $$$$$$\  
        $$$$$$$$ |$$$$$$$\ |        $$  __$$\ $$  __$$\ $$  _____|$$ |  $$ |$$  __$$\ $$ |$$  __$$\ 
        $$  __$$ |$$  __$$\         $$ |  \__|$$$$$$$$ |$$ /      $$ |  $$ |$$ /  $$ |$$ |$$ /  $$ |
        $$ |  $$ |$$ |  $$ |        $$ |      $$   ____|$$ |      $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |
        $$ |  $$ |$$$$$$$  |        $$ |      \$$$$$$$\ \$$$$$$$\ \$$$$$$  |$$$$$$$  |$$ |\$$$$$$  |
        \__|  \__|\_______/ $$$$$$\ \__|       \_______| \_______| \______/ $$  ____/ \__| \______/ 
                            \______|                                        $$ |                    
                                                                            $$ |                    
                                                                            \__|                    
          """, Fore.RESET)
    args = arguments.args()
    cmpt = {'file': 0, 'folder': 0} 

    try: 
        
        if args.folder:
            for folder in computer_list(folder=True):
                if search(folder, args.folder):
                    cmpt['folder'] += 1 
                    print(Fore.YELLOW, folder, Fore.RESET)

        if args.file:
            for file in computer_list(file=True):
                if search(file, args.file):
                    cmpt['file'] += 1 
                    print(Fore.CYAN, file, Fore.RESET)
    
    except FileNotFoundError: 
        pass 
                
    print(Back.GREEN, Fore.MAGENTA,f"file: {cmpt['file']} folder: {cmpt['folder']}", Fore.RESET, Back.RESET)
