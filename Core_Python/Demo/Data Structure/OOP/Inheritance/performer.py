from singer import Singer
from dancer import Dancer



class Performer(Dancer, Singer):
    def __init__(self, song_type, dance_type, exp):
        
        Singer.__init__(self, song_type)
        
        Dancer.__init__(self, dance_type)
        
        self.exp = exp
        
        
    def show(self):
        print('Show method of Performer')
        
        
    
p1 = Performer('Classical', 'Katthak', 5)

p1.display()