import modules.logger as logger
import io

class JavascriptCompiler():

    def __init__(self):
        self.variables = {}
        self.toggle_contant_evaluation = False
        self.log = logger.Logger()
        self.consts = {
            "lang": "\"js\""
        }

    def process_entry(self, byte_array):
        loc1 = byte_array
        loc2 = ""
        arg_num = 0
        parsed_command = {}
        opcode_buffer = ""
        parsed = False
        while True:
            cursor = loc1.read(1).decode()
            if (cursor != " " and cursor != ";"):
                opcode_buffer += cursor
            else:
                if (cursor == ";"):
                    loc1 = io.BytesIO(b";"+loc1.read())
                break;
        parsed_command["op"] = opcode_buffer
        cursor = loc1.read(1)
        reading_symmetrical = False
        toggle_contant_evaluation = False
        while parsed == False:
            if (cursor == b"\""):
                reading_symmetrical = not reading_symmetrical
            if (cursor == b";" and not reading_symmetrical):
                break
            if (cursor == b" " and not reading_symmetrical):
                arg_num += 1
                cursor = loc1.read(1)
                continue
            if not parsed_command.get(f"arg_{arg_num}"):
                parsed_command[f"arg_{arg_num}"] = ""
            parsed_command[f"arg_{arg_num}"] += cursor.decode()
            cursor = loc1.read(1)
        opcode = parsed_command["op"]
        if opcode == "wrt":
            loc2 += "console.log("
            current_arg = 0
            current_arg_check = parsed_command.get(f"arg_{current_arg}")
            args = []
            while current_arg_check:
                args.append(current_arg_check)
                current_arg += 1
                current_arg_check = parsed_command.get(f"arg_{current_arg}")

            for arg in args:
                if (self.variables.get(arg) and self.toggle_contant_evaluation):
                    arg = self.variables.get(arg)
                loc2 += str(arg)
                loc2 += ","
            loc2 = loc2[:-1]
            loc2 += ");"
        elif opcode == "var":
            name_ = parsed_command["arg_0"]
            val_ = parsed_command["arg_1"]
            loc2 += f"var {name_} = {val_};"
            self.variables[name_] = val_
        elif opcode == "gc":
            const_name = parsed_command["arg_0"]
            target_var = parsed_command["arg_1"]
            const_name = self.consts[const_name]
            loc2 += f"{target_var} = {const_name}"
            self.variables[target_var] = const_name
        elif opcode == "mlt":
            first_val = parsed_command["arg_0"]
            second_val = parsed_command["arg_1"]
            var_name = parsed_command["arg_2"]
            loc2 += var_name
            loc2 += " = "
            if (self.toggle_contant_evaluation and str(first_val).isdigit() and str(second_val).isdigit()):
                loc2 += str(int(first_val)*int(second_val))
            else:
                if (self.variables.get(first_val) and self.toggle_contant_evaluation):
                    first_val = self.variables.get(first_val)
                if (self.variables.get(second_val) and self.toggle_contant_evaluation):
                    second_val = self.variables.get(second_val)
                if (self.toggle_contant_evaluation and str(first_val).isdigit() and str(second_val).isdigit()):
                    loc2 += str(int(first_val)*int(second_val))+";"
                    self.variables[var_name] = int(first_val)*int(second_val)
                else:
                    loc2 += str(first_val)+" * "+str(second_val)+";"
        elif opcode == "div":
            first_val = parsed_command["arg_0"]
            second_val = parsed_command["arg_1"]
            var_name = parsed_command["arg_2"]
            loc2 += var_name
            loc2 += " = "
            if (self.toggle_contant_evaluation and str(first_val).isdigit() and str(second_val).isdigit()):
                loc2 += str(int(first_val)/int(second_val))
            else:
                if (self.variables.get(first_val) and self.toggle_contant_evaluation):
                    first_val = self.variables.get(first_val)
                if (self.variables.get(second_val) and self.toggle_contant_evaluation):
                    second_val = self.variables.get(second_val)
                if (self.toggle_contant_evaluation and str(first_val).isdigit() and str(second_val).isdigit()):
                    loc2 += str(int(first_val)/int(second_val))+";"
                    self.variables[var_name] = int(first_val)/int(second_val)
                else:
                    loc2 += str(first_val)+" / "+str(second_val)+";"
        elif opcode == "sub":
            first_val = parsed_command["arg_0"]
            second_val = parsed_command["arg_1"]
            var_name = parsed_command["arg_2"]
            loc2 += var_name
            loc2 += " = "
            if (self.toggle_contant_evaluation and str(first_val).isdigit() and str(second_val).isdigit()):
                loc2 += str(int(first_val)-int(second_val))
            else:
                if (self.variables.get(first_val) and self.toggle_contant_evaluation):
                    first_val = self.variables.get(first_val)
                if (self.variables.get(second_val) and self.toggle_contant_evaluation):
                    second_val = self.variables.get(second_val)
                if (self.toggle_contant_evaluation and str(first_val).isdigit() and str(second_val).isdigit()):
                    loc2 += str(int(first_val)-int(second_val))+";"
                    self.variables[var_name] = int(first_val)-int(second_val)
                else:
                    loc2 += str(first_val)+" - "+str(second_val)+";"
        elif opcode == "add":
            first_val = parsed_command["arg_0"]
            second_val = parsed_command["arg_1"]
            var_name = parsed_command["arg_2"]
            loc2 += var_name
            loc2 += " = "
            if (self.toggle_contant_evaluation and str(first_val).isdigit() and str(second_val).isdigit()):
                loc2 += str(int(first_val)+int(second_val))
            else:
                if (self.variables.get(first_val) and self.toggle_contant_evaluation):
                    first_val = self.variables.get(first_val)
                if (self.variables.get(second_val) and self.toggle_contant_evaluation):
                    second_val = self.variables.get(second_val)
                if (self.toggle_contant_evaluation and str(first_val).isdigit() and str(second_val).isdigit()):
                    loc2 += str(int(first_val)+int(second_val))+";"
                    self.variables[var_name] = int(first_val)+int(second_val)
                else:
                    loc2 += str(first_val)+" + "+str(second_val)+";"
        elif opcode == "tce":
            self.toggle_contant_evaluation = not self.toggle_contant_evaluation
        elif opcode == "nwl":
            loc2 += "\n"
        elif opcode == "arr":
            arr_name = parsed_command["arg_0"]
            arr_len = parsed_command["arg_1"]
            loc2 += f"var {arr_name} = ["
            cnt = 0
            while cnt < int(arr_len):
                loc2 += "null,"
                cnt += 1
            if loc2 != f"var {arr_name} = [":
                loc2 = loc2[:-1]
            loc2 += "];"
        elif opcode == "sav":
            arr_name = parsed_command["arg_0"]
            arr_index = parsed_command["arg_1"]
            arr_val = parsed_command["arg_2"]
            loc2 += f"{arr_name}[{arr_index}] = {arr_val};"
        elif opcode == "sfun":
            function_name = parsed_command["arg_0"]
            loc2 += f"function {function_name}("
            current_arg = 1
            current_arg_check = parsed_command.get(f"arg_{current_arg}")
            args = []
            while current_arg_check:
                args.append(current_arg_check)
                current_arg += 1
                current_arg_check = parsed_command.get(f"arg_{current_arg}")

            for arg in args:
                if (self.variables.get(arg) and self.toggle_contant_evaluation):
                    arg = self.variables.get(arg)
                loc2 += str(arg)
                loc2 += ","
            if (len(args) > 0):
                loc2 = loc2[:-1]
            loc2 += "){"
            
        elif opcode == "efun":
            loc2 += "}"
        elif opcode == "gfun":
            function_name = parsed_command["arg_0"]
            return_var = parsed_command["arg_1"]
            loc2 += f"{return_var} = {function_name}("
            current_arg = 2
            current_arg_check = parsed_command.get(f"arg_{current_arg}")
            args = []
            while current_arg_check:
                args.append(current_arg_check)
                current_arg += 1
                current_arg_check = parsed_command.get(f"arg_{current_arg}")

            for arg in args:
                if (self.variables.get(arg) and self.toggle_contant_evaluation):
                    arg = self.variables.get(arg)
                loc2 += str(arg)
                loc2 += ","
            if len(args) > 0:
                loc2 = loc2[:-1]
            loc2 += ");"
        elif opcode == "cfun":
            function_name = parsed_command["arg_0"]
            loc2 += f"{function_name}("
            current_arg = 1
            current_arg_check = parsed_command.get(f"arg_{current_arg}")
            args = []
            while current_arg_check:
                args.append(current_arg_check)
                current_arg += 1
                current_arg_check = parsed_command.get(f"arg_{current_arg}")

            for arg in args:
                if (self.variables.get(arg) and self.toggle_contant_evaluation):
                    arg = self.variables.get(arg)
                loc2 += str(arg)
                loc2 += ","
            if len(args) > 0:
                loc2 = loc2[:-1]
            loc2 += ");"
        elif opcode == "ret":
            loc2 += "return "
            current_arg = 0
            current_arg_check = parsed_command.get(f"arg_{current_arg}")
            args = []
            while current_arg_check:
                args.append(current_arg_check)
                current_arg += 1
                current_arg_check = parsed_command.get(f"arg_{current_arg}")

            for arg in args:
                if (self.variables.get(arg) and self.toggle_contant_evaluation):
                    arg = self.variables.get(arg)
                loc2 += str(arg)
                loc2 += ","
            if len(args) > 0:
                loc2 = loc2[:-1]
            loc2 += ";"
        elif opcode == "idn":
            amount = int(parsed_command["arg_0"])
            loc2 += "    "*amount
        elif opcode == "fiv":
            var_name = parsed_command["arg_0"]
            callback = parsed_command["arg_1"]
            loc2 += f"{var_name}.forEach({callback});"
        elif opcode == "whl":
            rule = parsed_command["arg_0"]
            rule = rule[:-1]
            rule = rule[1:]
            loc2 += f"while({rule}){{"
        elif opcode == "imp":
            package_name = parsed_command["arg_0"]
            loc2 += f"import {package_name}"
        elif opcode == "ima":
            package_name = parsed_command["arg_0"]
            as_name = parsed_command["arg_1"]
            loc2 += f"import {package_name} as {as_name}"
        elif opcode == "imf":
            package_name = parsed_command["arg_0"]
            current_arg = 1
            current_arg_check = parsed_command.get(f"arg_{current_arg}")
            args = []
            while current_arg_check:
                args.append(current_arg_check)
                current_arg += 1
                current_arg_check = parsed_command.get(f"arg_{current_arg}")

            loc2 += "import "
            for arg in args:
                loc2 += arg+", "
            loc2 = loc2[:-2]
            loc2 += f" from {package_name}"
        elif opcode == "raw":
            raw_code = parsed_command["arg_0"]
            raw_code = raw_code[1:]
            raw_code = raw_code[:-1]
            loc2 += raw_code
        elif opcode == "###":
            comment = parsed_command["arg_0"]
            comment = comment[1:]
            comment = comment[:-1]
            loc2 += f"// {comment}"
        elif opcode == "if":
            condition = parsed_command["arg_0"]
            condition = condition[1:]
            condition = condition[:-1]
            loc2 += f"if ({condition}){{"
        elif opcode == "eif":
            condition = parsed_command["arg_0"]
            condition = condition[1:]
            condition = condition[:-1]
            loc2 += f"}} else if ({condition}){{"
        elif opcode == "els":
            loc2 += f"}} else {{"
        if (opcode != "END"):
            loc2 += self.process_entry(loc1)
            
        return loc2
