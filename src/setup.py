import sys
from cx_Freeze import setup, Executable


# python setup.py build --target-name=moonprot
if __name__ == "__main__":
    # Dependencies are automatically detected, but it might need fine tuning.
    build_exe_options = {"packages": ["os", "pygame", "math"],
            "excludes": ["tkinter"]}

    # GUI applications require a different base on Windows (the default is for a
    # console application).
    base = None
    if sys.platform == "win32":
        base = "Win32GUI"

    setup(name="moonprotection", version="1.0", description="Moon Protection",
            options={"build_exe": build_exe_options},
            executables=[Executable("main.py", base=base)])
