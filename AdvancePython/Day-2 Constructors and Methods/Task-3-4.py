# Task 3:
# 4. Accessors:
class AcsCar:
    def __init__(self, brand):
        self._brand = brand

    @property
    def brand_name(self):
        return self._brand.upper()
    
car3 = AcsCar("BMW")
print(car3.brand_name)