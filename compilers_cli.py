import click
import sys

sys.path.insert(0, 'dependencies/')

from dependencies.compilers import compilers, run_check_sys

class misha_compilers_system():

    def __init__(self):
        super(misha_compilers_system, self).__init__()

    @click.command()
    @click.option('--compiler', help='The compiler you want to use')
    @click.option('--path', help="The path to the file")
    @click.option('--file_name', help='The file that you want to compile')
    def manage_compiler(compiler, path, file_name):

        compiler_refference = compilers()
        verification = run_check_sys()

        if verification.check_name(compiler, 'gcc'):
            compiler_refference.gcc_compiler(path, file_name)

        if verification.check_name(compiler, 'java'):
            compiler_refference.jit_compiler(path, file_name)

        if verification.check_name(compiler, 'python2'):
            compiler_refference.python2_run(path, file_name)

        if verification.check_name(compiler, 'python3'):
            compiler_refference.python3_run(path, file_name)

        if verification.check_name(compiler, 'go-run'):
            compiler_refference.go_run(path, file_name)

        if verification.check_name(compiler, 'go-build'):
            compiler_refference.go_build(path, file_name)

        if verification.check_name(compiler, 'swift-compiler'):
            compiler_refference.swift_compiler(path, file_name)
