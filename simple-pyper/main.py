import cmd
import os
import ast
import importlib.util
import inspector
class MyShell(cmd.Cmd):
    intro = '========================\n Welcome! Simple-pyper can be your personal toolbox to run any pipeline! input help to get start.\n'
    prompt = '(myshell) '

    def do_run(self, arg):
        'Run a Python file with arguments:  RUN [filename] [arg1] [arg2] ...'
        args = arg.split()
        if not args:
            print("Please provide a filename.")
        elif not os.path.isfile(args[0]):
            print(f"{args[0]} does not exist.")
        else:
            with open(args[0]) as file:
                tree = ast.parse(file.read())
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == 'main':
                    required_args = [arg.arg for arg in node.args.args]
                    if len(args[1:]) != len(required_args):
                        print(f"Invalid number of arguments. Expected: {required_args}")
                        return
            spec = importlib.util.spec_from_file_location("module.name", args[0])
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module.main(*args[1:])
        
    def do_continue(self, arg):
        'Run the last inspected Python file with arguments:  RUN'
        if not self.last_inspected_file:
            print("Please inspect a file first.")
        else:
            spec = importlib.util.spec_from_file_location("module.name", self.last_inspected_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            with open(self.last_inspected_file) as file:
                inspector.import_and_inspect(self.last_inspected_file)
                tree = ast.parse(file.read())
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == 'main':
                    required_args = [arg.arg for arg in node.args.args]
                    arg_dict = {}
                    for arg in required_args:
                        user_input = input(f"Please input {arg}: ")
                        arg_dict[arg] = user_input
            
            module.main(*[arg_dict[arg] for arg in required_args])

    def help_run(self):
        print("\n".join([
            "run [filename] [arg1] [arg2] ...",
            "Run a Python file with arguments.",
            ""
        ]))

    def do_inspect(self, arg):
        'Inspect a Python directory:  INSPECT [directory]'
        args = arg.split()
        if not args:
            print("Please provide a directory.")
        elif not os.path.isdir(args[0]):
            print(f"{args[0]} does not exist.")
        else:
            files = [f for f in os.listdir(args[0]) if f.endswith('.py')]
            if not files:
                print("No Python files found in the directory.")
            else:
                print("Python files in the directory:")
                for i, file in enumerate(files, start=1):
                    print(f"{i}. {file}")
                file_num = input("Enter the number of the file you want to inspect: ")
                if not file_num.isdigit() or int(file_num) < 1 or int(file_num) > len(files):
                    print("Invalid file number.")
                else:
                    file_to_inspect = files[int(file_num) - 1]
                    self.last_inspected_file = os.path.join(args[0], file_to_inspect)  # 更新属性
                    inspector.import_and_inspect(self.last_inspected_file)

    def do_exit(self, arg):
        'Exit the shell:  EXIT'
        print("Goodbye!")
        return True

    def help_exit(self):
        print("\n".join([
            "exit",
            "Exit the shell.",
            ""
        ]))

if __name__ == '__main__':
    MyShell().cmdloop()