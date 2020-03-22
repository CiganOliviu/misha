from pathlib import Path
from distutils.dir_util import copy_tree
import shutil
import os

class backup_system():

    def __init__(self):
        super(backup_system, self).__init__()

    def backup_data(self, folder, data):

        folder = str(folder)
        data = str(data)

        if Path(data).exists():

            if os.path.isdir(data):

                if Path(folder).exists():

                    copy_tree(data, folder)
                else:
                    print("The folder " + folder + " is no longer in your project arhitecture")

            elif os.path.isfile(data):

                if Path(folder).exists():

                    shutil.copy2(data, folder)

                else:
                    print("The folder " + folder + " is no longer in your project arhitecture")

        else:

            print("Can't backup, " + data + " does not exist")

    def clean_backup(self, folder):

        folder = str(folder)

        if Path(folder).exists():

            for root, dirs, files in os.walk(folder):

                for files_iterator in files:

                    os.unlink(os.path.join(root, files_iterator))

                for dirs_iterator in dirs:
                    shutil.rmtree(os.path.join(root, dirs_iterator))
        else:
            print("The folder " + folder + " is no longer in your project arhitecture")
