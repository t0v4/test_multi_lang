import modules.logger as logger

class CompilerExceptions():

    def __init__(self):
        self.ERROR_CONSTS = {
            "nfe": "Provided file does not exist!",
            "lns": "Requested language output is not supported yet!"
        }
        self.log = logger.Logger()
        
    def throw(self, exception_code):
        error_string = ""
        if exception_code in self.ERROR_CONSTS:
            self.log.error(f"Compiler error: {self.ERROR_CONSTS[exception_code]}")
            self.log.error(f"Compiler error code: {exception_code}")
        else:
            self.log.error(f"Compiler error code: {exception_code}")
