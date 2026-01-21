# Task 2:
class DemoClass:
    def instance_method(self):
        return "Instance method called"

    @classmethod
    def class_method(cls):
        return "Class method called"

    @staticmethod
    def static_method():
        return "Static method called"
    
method = DemoClass()
print(method.instance_method())
print(DemoClass.class_method())
print(DemoClass.static_method())