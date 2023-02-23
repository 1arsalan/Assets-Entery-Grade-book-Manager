class Asset:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.assets = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def add_asset(self, asset):
        self.assets.append(asset)

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_total_assets(self):
        return sum(asset.value for asset in self.assets)
