from setup import environment_variables

if (environment_variables.misha_datasets_system):
    from datasets_cli import misha_datasets_system

if __name__ == "__main__":
    misha_datasets_system.datasets()
