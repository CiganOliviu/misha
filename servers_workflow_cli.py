import click
import sys

sys.path.insert(0, 'dependencies/')

from dependencies.servers_workflow import servers_workflow, run_check_sys

class misha_servers_system():

    def __init__(self):
        super(misha_servers_system, self).__init__()

    @click.command()
    @click.option('--server_name', help='The server you want to start')
    def start_server(server_name):

        servers = servers_workflow()
        verification = run_check_sys()

        if verification.check_name(server_name, 'apache'):
            servers.start_apache()

        if verification.check_name(server_name, 'mysql'):
            servers.start_mysql()

        if verification.check_name(server_name, "xampp-start"):
            servers.xampp_start()

        if verification.check_name(server_name, "xampp-stop"):
            servers.xampp_stop()

        if verification.check_name(server_name, "xampp-shell"):
            servers.xampp_shell()

        if verification.check_name(server_name, "xampp-control"):
            servers.xampp_control()
