import os
class load(object):
    def __init__(self, config):
        self.config = config
        with open(config) as r:
            r = r.read()
        self.source = r
    def get(self, options):
        c = open(self.config)
        for test in c:
            if test.strip("\n").startswith(options) is True:
                get = test.split(",")[1].strip("\n")
        return get
    def set(self, key, value, string=""):
        if os.path.exists(self.config) is True:
            if self.source.find(key) is -1:
                with open(self.config, "a") as a:
                    a.write(string + key + "," + str(value) + "\n")
            w = open(self.config)
            for test in w:
                test = test.strip("\n")
                if test.strip("\n").startswith(key) is True:
                    string = string + key + "," + str(value) + "\n"
                    continue
                string = string + test + "\n"
            with open(self.config, "w") as w:
                w.write(string)
        else:
            os.system("touch "+self.config)
        return "Yeni ayar kaydedildi."
