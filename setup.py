from distutils.core import setup
import setuptools

setup(
  name = 'georaptor',
  py_modules = ['georaptor'],
  version = '2.0.2',
  description = 'A Python Geohash Compression Tool',
  long_description = open('README.rst').read(),
  author = 'Ashwin Nair',
  author_email = 'ashwinnair.ua@gmail.com',
  license = "MIT",
  url = 'https://github.com/ashwin711/georaptor',
  download_url = 'https://github.com/ashwin711/georaptor/tarball/2.0.2',
  keywords = ['geohash', 'optimizer', 'compression', 'location'],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
  ],
  install_requires = [
	'clint',
	'argparse'
  ],
  entry_points='''
	[console_scripts]
	georaptor=georaptor:main
  '''
)