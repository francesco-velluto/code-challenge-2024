from ply.yacc import yacc
from model.file_models import GoldenPoint, SilverPoint, Tile, Grid

import json

WIDTH = 0
HEIGHT = 0
GP = 0 # Number of GOLDEN POINTS
SP = 0 # Number of SILVER POINTS
NT = 0 # Number of TAILS

class Parser():
    @staticmethod
    def parse_file(file_path):
        with open(file_path, 'r') as file:
            data = file.readline()
            
            WIDTH = int(data.split()[0])
            HEIGHT = int(data.split()[1])
                        
            GP = int(data.split()[2])
            SP = int(data.split()[3])
            NT = int(data.split()[4])
            
            gp_list = []
            sp_list = []
            t_list = []
            
            for i in range(GP):
                data = file.readline()
                gp_list.append(GoldenPoint(int(data.split()[0]), int(data.split()[1])))
                
            for i in range(SP):
                data = file.readline()
                sp_list.append(SilverPoint(int(data.split()[0]), int(data.split()[1]), int(data.split()[2])))
                
            for i in range(NT):
                data = file.readline()
                t_list.append(Tile(str(data.split()[0]), int(data.split()[1]), int(data.split()[2])))
                
                
            json_obj = {
                "grid": str(Grid(WIDTH, HEIGHT)),
                "golden_points": [str(gp) for gp in gp_list],
                "silver_points": [str(sp) for sp in sp_list],
                "tiles": [str(t) for t in t_list]
            }
            
            with open("input_file_parsed.json", 'w') as file:
                file.write(json.dumps(json_obj, indent=4))
            
            return json_obj
                
            
                
            
            
            
            
                