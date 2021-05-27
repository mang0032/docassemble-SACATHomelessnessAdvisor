import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.SACATHomelessnessAdvisor',
      version='1.0',
      description=(''),
      long_description='# SACAT Homelessness Advisory App\r\n\r\nThe SACAT Homelessness Advisory App was created by Thomas Press, Julianne Keefe\r\nand Nicholas Siemelink for use by SACAT.\r\n\r\nIt provides assistance for people who have received vacant possession orders\r\nfrom SACAT and are facing homelessness.\r\n',
      long_description_content_type='text/markdown',
      author='Julianne Keefe, Thomas Press, Nicholas Siemelink',
      author_email='llaw3301@achelp.net',
      license='(c) 2019 Flinders University.  All rights reserved',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/SACATHomelessnessAdvisor/', package='docassemble.SACATHomelessnessAdvisor'),
     )

