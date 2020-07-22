import setuptools


def readme():
    try:
        with open('README.md') as file:
            return file.read()
    except FileNotFoundError:
        return ''


def requirements():
    try:
        with open('requirements.txt') as file:
            return file.read().split('\n')
    except FileNotFoundError:
        return ''


setuptools.setup(
    name='pugmark',
    version='0.1',
    packages=setuptools.find_packages(),
    description='Easy output of text with markdown',
    long_description=readme(),
    author='Charles D. Holmes',
    author_email='holmes@wustl.edu',
    url='https://github.com/holmescharles/pugmark',
    zip_safe=False,
    install_requires=requirements(),
    )
