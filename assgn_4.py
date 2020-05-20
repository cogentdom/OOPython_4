import os
import sys

class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        while True:
            try:
                with open(self._filename) as fh:
                    for line in fh:
                        line = line.rstrip()
                        key, value = line.split('=', 1)
                        dict.__setitem__(self, key, value)
                    break;
            except IOError:
                sys.stderr.write('Provided path does not exist\n')
                self._filename = input('Please enter a new file or path: ')

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as fh:
            for key, val in self.items():
                fh.write('{0}={1}\n'.format(key, val))

    def __getitem__(self, key):
        if not key in self:
            raise(ConfigKeyError(self, key))
        return dict.__getitem__(self, key)

class ConfigKeyError(Exception):
    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys

    def __str__(self):
        return 'The provided key {0} was not found, Here is a list of availble keys:\n \t[{1}]'.format(self.key, ', '.join(self.keys))


# cd = ConfigDict('config_file.txt')
# print('{0}\n'.format(cd['key']))
# print('{0}\n'.format(cd['not key']))