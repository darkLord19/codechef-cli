from setuptools import setup

setup(
    name='chef',
    version='0.9',
    py_modules=['chef'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        chef=chef:cli
    ''',
)