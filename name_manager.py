import os

class Name:
    def __init__(self, path: str, real_path:str="") -> None :
        self.real_path = real_path
        self.path = path
        self.original_name:str = os.path.basename(path)
        self.no_space:str = self.original_name.replace(" ", "").lower()
        print(f"{self.original_name} \n[SERIES]: {self.get_path()}\n\n")

    def is_series(self) -> bool:
        # print(f'{self.get_s_number_index(self.no_space)}>0 or {self.get_s_number_index(self.no_space, "season")}>0) and ({self.get_s_number_index(self.no_space, "e")}>0 or {self.get_s_number_index(self.no_space, "episode")}>0)')
        return ((self.get_s_number_index(self.no_space)>0 or self.get_s_number_index(self.no_space, "season")>0) and 
                (self.get_s_number_index(self.no_space, "e")>0 or self.get_s_number_index(self.no_space, "episode")>0))
    
    def get_addition_zero(self, num:int) -> str:
        return str(num) if num > 9 else f"0{num}"
    
    def get_path(self) -> str:
        path:str = os.path.dirname(self.path)
        if self.is_series():
            number = self.get_number()
            number = number if number != -1 else self.get_number("s")
            path += f"\\Series\\{self.get_series_name()}\\Season {self.get_addition_zero(number)}"
        elif self.is_movie():
            pass
        return path
    
    def get_filename(self):
        return self.original_name

    def get_series_name(self) -> str:
        index = self.get_s_number_index(self.original_name, "season")
        index = self.get_s_number_index(self.original_name) if index==-1 else index
        return self.original_name[:index-1].title().strip()
    
    def get_s_number_index(self, text:str, searched:str = "s") -> int:
        i = 0
        matched:bool = False
        text = text.lower()
        searched = searched.lower().strip()
        while i < len(text):
            if(not matched and text[i:i+len(searched)]==searched):
                matched = True
            elif(matched and text[i+len(searched)-1].isdigit()):
                return i-1
            elif(matched and text[i+len(searched)-1] != " "):
                matched = False
            i += 1
        return -1
    
    def get_number(self, after:str = "season") -> int:
        number:str = ""
        i = 0
        matched:bool = False
        text = self.no_space.lower()
        searched = after.lower().strip()
        while i < len(text):
            if(not matched and text[i:i+len(searched)]==searched):
                matched = True
                number = ""
            elif(matched and text[i+len(searched)-1].isdigit()):
                number += text[i+len(searched)-1]
            elif(matched and text[i+len(searched)-1] != " "):
                matched = False
            i += 1
        return int(number) if number != "" else -1

    def is_number(self, text:str, index:int) -> bool:
        text[index].isdigit()

    def is_movie(self) -> bool:
        file_size_mb = os.path.getsize(self.real_path) / (1024 * 1024)
        return not self.is_series() and file_size_mb > 350
    