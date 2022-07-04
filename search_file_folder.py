class SearchFileFolder:
    """Class search file or folder in your computer."""
    def search(self, element_for_search: str, list_file_folder: list[str]) -> list[str]:
        element_for_search = element_for_search.strip()
        found_result = []
        for file_or_folder in list_file_folder: 
            if (file_or_folder.startswith(element_for_search) or file_or_folder.endswith(element_for_search) 
                    or file_or_folder == element_for_search 
                    or file_or_folder in element_for_search): 
                found_result.append(file_or_folder)
                
        return found_result
        
