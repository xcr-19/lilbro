import os
import json
import random
import lilb.constants as constants

class Helpers():

    @staticmethod
    def get_env(key):
        return os.getenv(key)
    
    def read_json_file(self,key):
        with open(key) as f:
            data = json.load(f)
        return data
    
    def read_multi_line_file(self,key):
        with open(key) as f:
            data = [line.strip() for line in f]
            return data
    
    '''
    Returns a random valorant map
    '''
    @staticmethod
    def get_random_map():
        chosen_map = random.choice(constants.VALO_MAPS)
        map_name = chosen_map["name"]
        image_path = chosen_map["image_path"]
        return map_name,image_path