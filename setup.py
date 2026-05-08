from setuptools import setup, find_packages

setup(
    name='rpython-lang',
    version='0.4.0',
    description='Русский Python — пиши код на русском языке',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rpython=rpython.transpiler:main',
        ],
    },
    python_requires='>=3.6',
)