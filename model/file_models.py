# GRID MODEL
class Grid():
    def __init__(self, w: int, h: int) -> None:
        self.w = w
        self.h = h
        
    def __str__(self) -> str:
        return f"{self.w}, {self.h}"
   
# GOLDEN POINT MODEL
class GoldenPoint():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return f"{self.x}, {self.y}"
   
# SILVER POINT MODEL 
class SilverPoint():
    def __init__(self, x: int, y: int, score: int) -> None:
        self.x = x
        self.y = y
        self.score = score
        
    def __str__(self) -> str:
        return f"{self.x}, {self.y}, {self.score}"
    
    
# TILE MODEL
class Tile():
    def __init__(self, id: str, cost: int, num: int) -> None:
        self.id = id
        self.cost = cost
        self.num = num
        
    def __str__(self) -> str:
        return f"{self.id}, {self.cost}, {self.num}"