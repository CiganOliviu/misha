import random

class dataset_type():

    def __init__(self):
        super(dataset_type, self).__init__()

    FILE_NAME = ""
    DATASET_SIZE = 0
    MINIM_LIMIT = 0
    MAXIM_LIMIT = 0

class create_dataset():

    def __init__(self, arg):
        super(create_dataset, self).__init__()

    def create_float_list_dataset(self, dataset_attributes = dataset_type()):

        fileDataStream = open (dataset_attributes.FILE_NAME, "w")

        for values in range(dataset_attributes.DATASET_SIZE):
            fileDataStream.write(
                str(random.uniform(dataset_type.MINIM_LIMIT, dataset_type.MAXIM_LIMIT)) + " ")

        fileDataStream.close()

    def create_integer_list_dataset(self, dataset_attributes=dataset_type()):

        fileDataStream = open(dataset_attributes.FILE_NAME, "w")

        for values in range(dataset_attributes.DATASET_SIZE):
            fileDataStream.write(
                str(random.randint(dataset_type.MINIM_LIMIT, dataset_type.MAXIM_LIMIT)) + " ")

        fileDataStream.close()
