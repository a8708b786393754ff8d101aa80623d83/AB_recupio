import argparse

from file_folder import ListAllFileFolder
from search_file_folder import SearchFileFolder


print("""                                                                                                          
   ,---,            ,---,.                                                                             ,---,     
  '  .' \         ,'  .'  \                                                                          ,--.' |     
 /  ;    '.     ,---.' .' |                                                       __  ,-.            |  |  :     
:  :       \    |   |  |: |                 .--.--.                             ,' ,'/ /|            :  :  :     
:  |   /\   \   :   :  :  /                /  /    '      ,---.      ,--.--.    '  | |' |    ,---.   :  |  |,--. 
|  :  ' ;.   :  :   |    ;                |  :  /`./     /     \    /       \   |  |   ,'   /     \  |  :  '   | 
|  |  ;/  \   \ |   :     \               |  :  ;_      /    /  |  .--.  .-. |  '  :  /    /    / '  |  |   /' : 
'  :  | \  \ ,' |   |   . |                \  \    `.  .    ' / |   \__\/: . .  |  | '    .    ' /   '  :  | | | 
|  |  '  '--'   '   :  '; |          ___    `----.   \ '   ;   /|   ," .--.; |  ;  : |    '   ; :__  |  |  ' | : 
|  :  :         |   |  | ;        .'  .`|  /  /`--'  / '   |  / |  /  /  ,.  |  |  , ;    '   | '.'| |  :  :_:,' 
|  | ,'         |   :   /      .'  .'   : '--'.     /  |   :    | ;  :   .'   \  ---'     |   :    : |  | ,'     
`--''           |   | ,'    ,---, '   .'    `--'---'    \   \  /  |  ,     .-./            \   \  /  `--''       
                `----'      ;   |  .'                    `----'    `--`---'                 `----'               
                            `---'                                                                               
""")



def parser_argument(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", help="Enter the file name to search", type=str)
    parser.add_argument("-d","--folder", help="Enter the folder name to search",  type=str)
    return  parser.parse_args()


if __name__ == "__main__":
    args = parser_argument()    
    search = SearchFileFolder()

    result = False 
    
    if args.file:
        print("Searching file: "+args.file)
        research = ListAllFileFolder().get_file()
        result = search.search(args.file,research)
    
    elif args.folder: 
        print("Searching folder: "+args.folder)
        research = ListAllFileFolder.get_folder()
        result = search.search(args.folder,research)

    try: 
        if result: 
            print("Found:", result)

        else: 
            print()
            print("not found")
    except NameError: 
        print("Enter a argument")