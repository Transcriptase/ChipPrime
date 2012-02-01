try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'Automate the design of primers for ChIP-PCR',
    'author': 'Russell Williams',
    'url':'https://github.com/Transcriptase/chipprime',
    'download': 'https://github.com/Transcriptase/chipprime',
    'author_email': 'russell.d.williams@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name': 'chipprime'
}

setup(**config)