class JsonParser:
    def __init__(self, connector=".") -> None:
        self.connector = connector
    
    def parse_json(self, inp_json):
        
