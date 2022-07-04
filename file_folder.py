import glob
import os 

class ListAllFileFolder: 
    """List all file/folder is you can search for a file/folder"""
    def all_file_folder(self, reading_disc: str) -> list[list[str]]:
        """Return the file and folder.
        List all the files folder of your windows."""
        folder = []
        file = []
        for all_file_directory in glob.glob(reading_disc+"**", recursive=True): 
            if os.path.isfile(all_file_directory): 
                file.append(str(all_file_directory))

            elif os.path.isdir(all_file_directory):
                folder.append(str(all_file_directory))

        return [file, folder]

    
    @classmethod
    def get_file(cls) -> list[str]: 
        if os.name == "nt": 
            return ListAllFileFolder().all_file_folder("C://")[0]
        
        else: 
            return ListAllFileFolder().all_file_folder("/")[0]
        

    @classmethod
    def get_folder(cls)-> list[str]: 
        if os.name == "nt":         
            return ListAllFileFolder().all_file_folder("C://")[1]

        else: 
            return ListAllFileFolder().all_file_folder("/")[1]


if __name__ == "__main__": 
    test = ListAllFileFolder()
    test.all_file_folder("C://")