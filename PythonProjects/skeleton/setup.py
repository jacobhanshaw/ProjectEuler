try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jacob Hanshaw',
    'url': 'jacobhanshaw.com',
    'download_url': 'github.com/jacobhanshaw',
    'author_email': 'jacobhanshaw0@gmail.com',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
