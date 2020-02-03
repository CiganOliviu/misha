import click
import sys

from setup import environment_variables

sys.path.insert(0, 'dependencies/')

from dependencies.compilers import compilers, exe_compilers, run_check_sys

class misha_compilers_system():

    def __init__(self):
        super(misha_compilers_system, self).__init__()

    @click.command()
    @click.option('--compiler', help='The compiler you want to use')
    @click.option('--file_name', help='The file that you want to compile')
    def manage_compiler(compiler, path, file_name):

        compiler_refference = compilers()
        verification = run_check_sys()

        if verification.check_name(compiler, 'gcc'):
            compiler_refference.gcc_compiler(environment_variables.workflow_space_path, file_name)

        if verification.check_name(compiler, 'java'):
            compiler_refference.jit_compiler(environment_variables.workflow_space_path, file_name)

        if verification.check_name(compiler, 'python2'):
            compiler_refference.python2_run(environment_variables.workflow_space_path, file_name)

        if verification.check_name(compiler, 'python3'):
            compiler_refference.python3_run(environment_variables.workflow_space_path, file_name)

        if verification.check_name(compiler, 'go-run'):
            compiler_refference.go_run(environment_variables.workflow_space_path, file_name)

        if verification.check_name(compiler, 'go-build'):
            compiler_refference.go_build(environment_variables.workflow_space_path, file_name)

    @click.command()
    @click.option('--file_program', help="The exe file you want to run")
    def run_compilers_management(file_program):
        exe_compiler_refference = exe_compilers()
        verification = run_check_sys()

        if verification.check_name(file_program, 'python2'):
            exe_compiler_refference.python2_exe()

        if verification.check_name(file_program, 'python3'):
            exe_compiler_refference.python3_exe()
