class Entity:

    def __init__(self,size,x,y):
        self.x,self.y = x,y
        self.size = size

    def __call__(self, x, y):

        self.x, self.y = x,y

pos = Entity(2,1,1)
pos.__call__(10,10)
print pos.x,pos.y