import os

class environment_variables():

    def __init__(self):
        super(environment_variables, self).__init__()

    workflow_space_path = os.getcwd()
    misha_datasets_system = True
    misha_templates_system = False
    misha_backup_system = True
