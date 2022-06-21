# when to use class and when to use static method
class Item:
    @staticmethod
    def my_static_method(): #no mandatory param needed
        '''
        This should do something that has a relationship 
        with the class but not unique to each instance.
        '''
        pass

    @classmethod
    def my_class_method(cls): #mandatory class param needed, just like self
        '''
        This should also do something that has a relationship
        with the class, but to do something beyond the scope
        of a single object. For example - instantiate multiple
        objects from a single source (csv, json etc)
        '''
        pass