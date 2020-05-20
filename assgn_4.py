import os
import sys

class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        # "jgjg"
        return 'The provided key {0} was no{1}'.format(self.key, ', '.join(self.keys))


class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        while True:
            try:
                open(self._filename, 'r').close()
                break;
            except IOError:
                sys.stderr.write('Provided path does not exist\n')
                self._filename = input('Please enter a new file or path: ')
        with open(self._filename) as fh:
            for line in fh:
                line = line.rstrip()
                key, value = line.split('=', 1)
                dict.__setitem__(self, key, value)



    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fh:
            for key, val in self.items():
                fh.write('{0}={1}\n'.format(key, val))

    def __getitem__(self, key):

        try:
            return dict.__getitem__(self, key)
        except KeyError:
            exit('Error the provided key "{0}" is not in the set:\n[ {1} ]'.format(key, ', '.join(self.keys())))

