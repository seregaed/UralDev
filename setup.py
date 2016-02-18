from setuptools import setup

setup(
    name='ural',
    description="Maintenance service from Ural",
    version='0.0.1',
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP",
    ],
    url='https://github.com/seregaed/UralDev/',
    packages=['ural'],
    install_requires=[
        'bottle',
    ],
    entry_points={
        'console_scripts': [
            'ural = ural.__main__:main',
        ],
    },
)
