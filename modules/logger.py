class Logger():

    #Brainrot code XD
    def __init__(self):
        self.compsyntax = "TML_COMPILER"
        self.debug_mode = False

    def enable_debug(self):
        self.debug_mode = True
        
    def info(self, msg):
        print(f"[{self.compsyntax}] [INFO] - {msg}")

    def debug(self, msg):
        if (self.debug_mode):
            print(f"[{self.compsyntax}] [DEBUG] - {msg}")

    def error(self, msg):
        print(f"[{self.compsyntax}] [ERROR] - {msg}")

    def warn(self, msg):
        print(f"[{self.compsyntax}] [WARN] - {msg}")
