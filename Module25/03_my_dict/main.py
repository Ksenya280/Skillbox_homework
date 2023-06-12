class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


my_dict = MyDict({'a': 1, 'b': 2})
print(my_dict.get('c'))
