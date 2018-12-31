""" setup script for shifter.py """
import cx_Freeze

executables = [cx_Freeze.Executable("shifter.py", base = "Win32GUI")]

cx_Freeze.setup(
    name = "SHIFTER",
    options = {"build_exe":{"packages":["pygame"],
                            "include_files":["library.py",
                            "game_functions.py", "levels"]}},
    executables = executables
    )
