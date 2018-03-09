import os
class load(object):
    def __init__(self, file):
        self.file = file
        self.dict = {}
        self.options = []
        if os.path.exists(self.file) is False:
            os.system("touch "+self.file)
        re = open(self.file)
        for test in re:
            self.options.append(test.strip("\n").split(",")[0])
    def get(self, key):
        for options in open(self.file):
            key = options.strip("\n").split(",")[0]
            value = options.strip("\n").split(",")[1]
            self.dict.update({key:value})
        return self.dict[key]
    def set(self, key, value):
        key = str(key)
        value = str(value)
        if os.path.exists(self.file) is False:
            os.system("touch "+self.file)
        if key not in self.options:
            with open(self.file, "a") as a:
                a.write(key+","+value+"\n")
        return 
