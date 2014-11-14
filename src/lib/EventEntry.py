import json

class EventEntry(object):
    def __init__ (self, jsonString):
        entry = json.loads(jsonString)
        self.header = entry['header']
        self.body = entry['body']

    def get_header(self):
        return self.header
    
    def get_body(self):
        return self.body
    
    def to_json(self):
        entry = {}
        entry['header'] = self.header
        entry['body'] = self.body
        return json.dumps(entry)