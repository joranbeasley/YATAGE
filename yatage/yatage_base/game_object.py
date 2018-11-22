import collections


class GameObject(object):
    fields = ['name']
    def defaults(self,field_name=None):
        default_value = getattr(self,"__default__",None)
        defaults = getattr(self,"__defaults__",dict.fromkeys(self.fields,default_value))
        if isinstance(defaults,collections.Iterable) and not isinstance(defaults,dict):
            defaults = dict(zip(self.fields,[d() if callable(d) else d for d in defaults]))
        for key in self.fields:
            if key not in defaults:
                defaults[key] = default_value
        return defaults
    def __str__(self):
        return self.name

    def __init__(self,*args,**kwargs):
        pending_values = []
        defaults = self.defaults()
        for slot in self.fields:
            pending_values.append(slot)
            setattr(self, slot, defaults.get(slot,None))
        for key in kwargs.keys():
            if key in self.fields:
                kwargs.pop(key)
                setattr(self, key, kwargs[key])

        for slot,arg in zip(self.fields,args):
            if slot in kwargs:
                raise ValueError("'{slot}' was declared twice".format(slot=slot))
            setattr(self,slot,arg)
        self.PostInit(kwargs)
    def PostInit(self,leftover_kwargs):
        pass
class GameItem(GameObject):
    """
    >>> str(GameItem("Sword of Damacles!",damage=[20,30],max_stack=1))  # doctest:+ELLIPSIS
    'Sword of Damacles!'

    """
    fields = GameObject.fields + ['count','damage','effects','max_stack','movable']
    __defaults__ = {'item_type':'junk','count':1,'max_stack':20,'movable':1}


class Location(GameObject):
    """
    >>> Location("The Fields",{"north":"The Town","south":"The Woods"},{})
    """
    fields = GameObject.fields + ['exits','items','ai']
    __defaults__ = {'exits':lambda:{}, 'items':lambda: [], 'ai':lambda: []}

class Mob(GameObject):
    """
    >>> Mob("Goblin",[GameItem("GOLD",22),],hp=22)

    """
    fields = GameObject.fields + ['inventory','max_inventory','stats','equipment']
    __defaults__ = {'inventory':lambda:[],'max_inventory':20,'stats':lambda:{'hp':100,'aggressive':False}}
    def PostInit(self,leftover_kwargs):
        print(leftover_kwargs)

class GameWorld(object):
    @staticmethod
    def from_json(json_file):
        pass
    def __init__(self,player,current_room):
        self.current_room = current_room
        self.player = player