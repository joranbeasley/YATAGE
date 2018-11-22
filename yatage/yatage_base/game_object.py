class GameObject(object):
    fields = ['name']
    def __init__(self,name):
        self.name = name

class GameItem(GameObject):
    fields = GameObject.fields + ['count','damage']