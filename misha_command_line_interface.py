import click

from datasets_cli import misha_datasets_system
from templates_cli import misha_templates_system

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

    def set_templates_cli(self):
        templates_commands = misha_templates_system()
        self.misha_command_line_interface.add_command(templates_commands.standard_cpp_algo_data_structures_implementation)
        self.misha_command_line_interface.add_command(templates_commands.standard_c_algo_data_structures_implementation)
        self.misha_command_line_interface.add_command(templates_commands.standard_easyPass_implementation)
        self.misha_command_line_interface.add_command(templates_commands.standard_esential_implementation)
        self.misha_command_line_interface.add_command(templates_commands.standard_misha_implementation)
