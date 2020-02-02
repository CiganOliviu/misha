import os

class run_check_sys():

    def __init__(self):
        super(run_check_sys, self).__init__()

    def check_name (self, name_one, name_two) -> bool:
        if (name_one == name_two):
            return True
        return False

class languagesSetup():

    def __init__(self):
        super(languagesSetup, self).__init__()

    GCC = True
    JAVA = True
    PYTHON_TWO = True
    PYTHON_THREE = True
    GO = True
    SWIFT = True

    PYTHON_TWO_PATH = "C:\\Python27amd64 ";
    PYTHON_THREE_PATH = "C:/Users/cigan/AppData/Local/Programs/Python/Python37/python.exe ";
    SWIFT_PATH = "C:\\Swift\\bin"

class compilers(languagesSetup):

    def __init__(self):
        super(compilers, self).__init__()

    def gcc_compiler(self, path, file_name):
        if self.GCC:
            os.chdir(path)
            os.system("g++ -std=c++17 " + str(file_name) + ".cpp -o " + str(file_name))
            os.system(file_name)

    def jit_compiler(self, file_name):
        if self.JAVA:
            os.chdir(path)
            os.system("javac " + file_name + ".java")
            os.system("java " + file_name)

    def python2_run(self, file_name):
        if self.PYTHON_TWO:
            os.chdir(path)
            os.system(self.PYTHON_TWO_PATH + str(file_name) + ".py")

    def python3_run(self, file_name):
        if self.PYTHON_THREE:
            os.chdir(path)
            os.system(self.PYTHON_THREE_PATH + str(file_name) + ".py")

    def go_run(self, file_name):
        if self.GO:
            os.chdir(path)
            os.system("go run " + str(file_name) + ".go")

    def go_build(self, file_name):
        if self.GO:
            os.chdir(path)
            os.system("go build " + (file_name) + ".go")
            self.go_run(file_name)

    def swift_compiler(self):
        if self.SWIFT:
            os.system(SWIFT_PATH + "Swift for Windows")
