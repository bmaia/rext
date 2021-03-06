#This file is part of REXT
#core.Harvester.py - super class for harvester scripts
#Author: Ján Trenčanský
#License: GNU GPL v3

import cmd

import core.globals
import interface.utils
from interface.messages import print_error, print_help


class RextHarvester(cmd.Cmd):
    host = ""
    port = "80"

    def __init__(self):
        cmd.Cmd.__init__(self)
        interface.utils.change_prompt(self, core.globals.active_module_path + core.globals.active_script)
        self.cmdloop()

    def do_exit(self, e):
        return True

    def do_run(self, e):
        pass

    def do_set(self, e):
        args = e.split(' ')
        try:
            if args[0] == "host":
                if interface.utils.validate_ipv4(args[1]):
                    self.host = args[1]
                else:
                    print_error("please provide valid IPv4 address")
            elif args[0] == "port":
                if isinstance(args[1], int):
                    self.port = args[1]
                else:
                    print_error("port value must be integer")
        except IndexError:
            print_error("please specify value for variable")

    def help_exit(self):
        print_help("Exit script")

    def help_run(self, e):
        print_help("Run script")