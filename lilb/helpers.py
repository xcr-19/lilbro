import os
import json

class Helpers():

    @staticmethod
    def get_env(key):
        return os.getenv(key)
    
    @staticmethod
    def read_json_file(key):
        with open(key) as f:
            data = json.load(f)
        return data
    
    @staticmethod
    def read_multi_line_file(key):
        with open(key) as f:
            data = [line.strip() for line in f]
            return data