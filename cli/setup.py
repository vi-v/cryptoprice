from setuptools import setup

setup(
    name='Cryptoprice',
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
        'requests',
        'terminaltables'
    ],
    entry_points='''
        [console_scripts]
        cryptoprice=cryptoprice:cli
    '''
)