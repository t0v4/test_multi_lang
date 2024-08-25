import os
import io
import modules.exceptions as exceptions
import modules.logger as logger
import sys
from collections import deque

import language_compilers.python as python_c
import language_compilers.javascript as javascript_c

class Compiler():


    def __init__(self):
        self.error = exceptions.CompilerExceptions()
        self.ver = "0.0.1"
        self.toggle_contant_evaluation = False
        self.variables = {}
        self.langs = {
            "py": python_c.PythonCompiler(),
            "js": javascript_c.JavascriptCompiler()
        }
        self.log = logger.Logger()
        self.log.info(f"Using TestMultiLang Compiler v.{self.ver}")

    def compile(self, input_name, output_name):
        loc1 = b"" #Bytes of the opened file
        loc2 = os.path.exists(input_name) #Check if the input file exists
        TARGET_LANG = output_name.split(".")[-1]
        if not loc2:
            return self.error.throw("nfe")
        with open(input_name, "r+") as loc3:
            loc1 = loc3.read()
        ops = loc1.splitlines()
        loc1 = b""
        for op in ops:
            loc1 += op.strip().encode()
        loc1 = io.BytesIO(loc1)
        self.log.info(f"Started compilation for {input_name}; Target language: ({TARGET_LANG})")
        if not self.langs.get(TARGET_LANG):
            return self.error.throw("lns")
        loc4 = self.langs[TARGET_LANG].process_entry(loc1)
        with open(output_name, "w+") as loc5:
            loc5.write(loc4)
        self.log.info(f"Compiled {input_name} as {output_name}!")
        return loc4
        
compile_options = sys.argv
comp = Compiler()
output_array = compile_options[2].split("/")
if len(output_array) > 1:
    for output_fl in output_array:
        comp.compile(compile_options[1],output_fl)
else:
    comp.compile(compile_options[1],output_array[0])
