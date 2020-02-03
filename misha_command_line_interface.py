import click

from datasets_cli import misha_datasets_system
from servers_workflow_cli import misha_servers_system
from compilers_cli import misha_compilers_system

class misha_command_line_interface_system():

    def __init__(self):
        super(misha_command_line_interface_system, self).__init__()

    @click.group()
    def misha_command_line_interface():
        pass

    def set_datasets_cli(self):
        datasets_commands = misha_datasets_system()
        self.misha_command_line_interface.add_command(datasets_commands.auto_create_float_list_dataset)
        self.misha_command_line_interface.add_command(datasets_commands.auto_create_integer_list_dataset)
        self.misha_command_line_interface.add_command(datasets_commands.auto_create_float_matrix_dataset)
        self.misha_command_line_interface.add_command(datasets_commands.auto_create_integer_matrix_dataset)
        self.misha_command_line_interface.add_command(datasets_commands.auto_create_string_dataset)
        self.misha_command_line_interface.add_command(datasets_commands.create_linear_dataset)
        self.misha_command_line_interface.add_command(datasets_commands.create_matrix_dataset)

    def set_servers_cli(self):
        servers_commands = misha_servers_system()
        self.misha_command_line_interface.add_command(servers_commands.manage_server)

    def set_compilers_cli(self):
        compilers_commands = misha_compilers_system()
        self.misha_command_line_interface.add_command(compilers_commands.manage_compiler)
        self.misha_command_line_interface.add_command(compilers_commands.run_compilers_management)
