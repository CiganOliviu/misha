import click
import sys

sys.path.insert(0, 'dependencies/')

from dependencies.servers_workflow import servers_workflow, run_check_sys

class misha_servers_system():

    def __init__(self):
        super(misha_servers_system, self).__init__()

    @click.command()
    @click.option('--process', help='The process you want to start')
    def manage_server(process):

        servers = servers_workflow()
        verification = run_check_sys()

        if verification.check_name(process, 'apache'):
            servers.start_apache()

        if verification.check_name(process, 'mysql'):
            servers.start_mysql()

        if verification.check_name(process, 'xampp-start'):
            servers.xampp_start()

        if verification.check_name(process, 'xampp-stop'):
            servers.xampp_stop()

        if verification.check_name(process, 'xampp-shell'):
            servers.xampp_shell()

        if verification.check_name(process, 'xampp-control'):
            servers.xampp_control()

        if verification.check_name(process, 'test-php'):
            servers.test_php()
