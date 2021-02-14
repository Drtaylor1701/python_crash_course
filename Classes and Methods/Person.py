class Person:
    def __init__(self, name):
        self.name = name
    """Outputs a message with the name of the person"""
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(name = self.name)
