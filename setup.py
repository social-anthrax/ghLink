from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name='ghlink',
    version='0.0.1',
    author='Artemis Livingstone',
    author_email='ar.d.livingstone@gmail.com',
    license='MIT',
    description='A tool to get line permalink',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='www.github.com/social_anthrax/ghlink',
    py_modules=['ghlink', 'app'],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        ghlink=ghLink:cli
    '''
)
