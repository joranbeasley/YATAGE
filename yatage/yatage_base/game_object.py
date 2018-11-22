import collections


class GameObject(object):
    fields = ['name']
    def defaults(self,field_name=None):
        default_value = getattr(self,"__default__",None)
        defaults = getattr(self,"__defaults__",dict.fromkeys(self.__slots__,default_value))
        if isinstance(defaults,collections.Iterable) and not isinstance(defaults,dict):
            defaults = dict(zip(self.__slots__,[d() if callable(d) else d for d in defaults]))
        for key in self.__slots__:
            if key not in defaults:
                defaults[key] = default_value
        return defaults
    def __init__(self,*args,**kwargs):
        pending_values = []
        defaults = self.defaults()
        for slot in self.fields:
            pending_values.append(slot)
            setattr(self, slot, defaults.get(slot,None))
        for key in kwargs:
            if key in self.fields:
                setattr(self, key, kwargs[key])
        for slot,arg in zip(self.fields,args):
            if slot in kwargs:
                raise ValueError("'{slot}' was declared twice".format(slot=slot))
            setattr(self,slot,arg)
class GameItem(GameObject):
    """
    >>> GameItem("Sword of Damacles!")
    """
    fields = GameObject.fields + ['count','damage','effects','max_stack']
    __defaults__ = {'item_type':'junk'}
    def __init__(self,*args,**kwargs):
        super(GameItem,self).__init__(self)