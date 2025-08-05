class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW= "LOW"

    def __init__(self,code: str, title:str,text: str,importace: str):
        self.code=code
        self.title=title
        self.text=text

class Notebook:
    notes = []
