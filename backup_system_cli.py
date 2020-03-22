import click
import sys

from setup import environment_variables

sys.path.insert(0, 'dependencies/')

from dependencies.backup_system import backup_system

class misha_backup_system():

    def __init__(self):
        super(misha_backup_system, self).__init__()

    @click.command()
    @click.option('--folder', help='Folder where the backup should be made')
    @click.option('--data', help='Data that should be backup')
    def backup_sys_data(folder, data):
        backup = backup_system()

        backup.backup_data(folder, data)

    @click.command()
    @click.option('--folder', help='Folder backup to clean')
    def clean_sys_backup(folder):
        backup = backup_system()

        backup.clean_backup(folder)
