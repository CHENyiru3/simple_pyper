import inspect
import os
import importlib.util

def import_and_inspect(filename):
    spec = importlib.util.spec_from_file_location("module.name", filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    print(f"Inspecting {filename}:")

    functions = inspect.getmembers(module, inspect.isfunction)
    if functions:
        print("Functions:")
        for name, func in functions:
            if name == 'main':
                print(f"- {name}")
                argspec = inspect.getfullargspec(func)
                for arg, annotation in zip(argspec.args, argspec.annotations.values()):
                    print(f"  - Parameter: {arg}, Type: {annotation}")

