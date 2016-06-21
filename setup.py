try:
  from distutils.core import setup
except ImportError:
  from setuptools import setup

import sys

req_file = open('requirements.txt','r')
req_list = [l.strip() for l in req_file]

extra = {}
if sys.version_info >= (3,):
  extra['use_2to3'] = True

setup(
  name = 'codeforces-dl',

  packages = ['codeforcesDl'],

  version = '1.0.0.1',

  description = 'Downloads any problem/problem set '\
  'from any contest hosted in codeforces.com',

  author = 'Shravan Murali',

  author_email = 'shravanmurali@gmail.com',

  install_requires= req_list,

  entry_points= {
      'console_scripts':['codeforcesdl = codeforcesDl:'\
      'main']
  } ,

  url = 'https://github.com/shravan97/codeforces-dl',

  keywords = ['downloader', 'download as pdf',
  'codeforces','competitive programming'],

  classifiers = ['Operating System :: POSIX :: Linux',
                 'License :: OSI Approved :: GNU General '\
                 'Public License v3 (GPLv3)',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Education'],

  license='GNU General Public License v3 (GPLv3)'
)