try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Test project for performing various analyses on downloaded articles.',
        'author': 'Zach',
        'url': 'zach-woodward.com',
        'download_url': 'zach-woodward.com/does_not_exist/',
        'author_email': 'zachw38@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['articleanalysis'],
        'scripts': [],
        'name': 'ArticleAnalysis'
}

setup(**config)
