import sublime, sublime_plugin
import os, string
import re
import subprocess

MDE_SEARCH_COMMAND = '/usr/local/bin/rg'

class ExternalSearch:
    """
    Static class to group all external search related functions.
    """
    # EXTERNALIZE = '.search_results.zkr'   # '' to skip

    def __init__(self, search_cmd):
        self.search_cmd=search_cmd


    @staticmethod
    def rg_search_in(self, folder, regexp):
        """
        Perform an external search for regexp in folder.
        """
        print("in rg_search_in")
        args = [self.search_cmd]
        args.extend(['-l', regexp, folder])
        print('args={}'.format(args))
        return self.run(args, folder)


    @staticmethod
    def rg_search_for_file(self, folder, glob):
        """   
        Perform an external search for files matching glob in folder.
        """
        print("in rg_search_for_file")
        args = [self.search_cmd]
        args.extend(['-g', glob, '--files', folder])
        print('args={}'.format(args))
        return self.run(args, folder)


    @staticmethod
    def run(self, args, folder):
        """
        Execute SEARCH_COMMAND to run a search, handle errors & timeouts.
        Return output of stdout as string.
        """
        output = b''
        verbose = True
        if verbose or True:
            print('cmd:', ' '.join(args))
        try:
            output = subprocess.check_output(args, shell=False, timeout=10000)
        except subprocess.CalledProcessError as e:
            print('sublime_zk: search unsuccessful:')
            print(e.returncode)
            print(e.cmd)
            for line in e.output.decode('utf-8', errors='ignore').split('\n'):
                print('    ', line)
        except subprocess.TimeoutExpired:
            print('sublime_zk: search timed out:', ' '.join(args))
        if verbose:
            print(output.decode('utf-8', errors='ignore'))
        return output.decode('utf-8', errors='ignore').replace('\r', '')