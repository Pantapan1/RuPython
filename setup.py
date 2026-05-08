from setuptools import setup

setup(
    name='rpython-lang',
    version='0.4.1',
    description='Русский Python — пиши код на русском языке',
    py_modules=['transpiler'],
    entry_points={
        'console_scripts': [
            'ruspy=transpiler:main',
        ],
    },
    python_requires='>=3.6',
)
