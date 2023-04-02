class MyList(list):
    def append(self, val):
        if isinstance(val, int):
            super().append(val)
        else:
            print("Error: Only integers can be added to the list.")
