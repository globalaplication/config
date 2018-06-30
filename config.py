# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
class load(object):
    def __init__(self, file):
        self.file = file
        self.keys = []
        if os.path.exists(file) is False:
            with open(file ,"w") as version:
                version.write("version:0.1\n")
        for test in open(file):
            self.keys.append(test.strip("\n").split(":")[0])
    def get(self, key):
        if key not in self.keys:
            return "None"
        for test in open(self.file):
            if test.split(":")[0] == key:
                value = test.split(":")[1].strip("\n")
        return value
    def set(self, key, value): #merhaba
        key, value = str(key), str(value)
        string = ""
        if key not in self.keys:
            with open(self.file, "a") as add:
                add.write("{}:{}\n".format(key, value))
        else:
            for test in self.keys:
                if test == key:
                    string = string + "{}:{}\n".format(test, value)
                else:
                    string = string + "{}:{}\n".format(test, self.get(test))
            with open(self.file, "w") as save:
                save.write(string)
         


