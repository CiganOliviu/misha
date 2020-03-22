from setup import environment_variables
from misha_command_line_interface import misha_command_line_interface_system

misha_cli = misha_command_line_interface_system()

if environment_variables.misha_datasets_system:
    from datasets_cli import misha_datasets_system
    misha_cli.set_datasets_cli()

if environment_variables.misha_templates_system:
    from templates_cli import misha_templates_system
    misha_cli.set_templates_cli()

if environment_variables.misha_backup_system:
    from backup_system_cli import misha_backup_system
    misha_cli.set_backup_cli()

if __name__ == "__main__":
    misha_command_line_interface_system.misha_command_line_interface()
