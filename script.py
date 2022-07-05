#! /usr/local/bin/python3.10
from pathlib import Path
import arguments as arguments


def computer_list(file: bool = False, folder: bool = False):
    """Liste tout les fichier est dossier a partir de la racine

    Yields:
        Path: fichier ou dossier 
    """

    for element in Path('/').rglob("**"):
        if file and element.is_file():
            yield element

        elif folder and element.is_dir():
            yield element

        elif not folder and not file:
            yield element


def search(file: str | Path, research: str) -> bool:
    if isinstance(file, Path):
        file = str(file)

    return (file.startswith(research) or file.endswith(research)) or (file == research or file in research)


if __name__ == '__main__':
    args = arguments.args()

    if args.folder:
        for folder in computer_list(folder=True):
            if search(folder, args.folder):
                print(folder)

    elif args.file:
        for file in computer_list(file=True):
            if search(file, args.file):
                print(file)
