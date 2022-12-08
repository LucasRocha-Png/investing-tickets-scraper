from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Scraps stocks tickets from "Investing.com" using Selenium'

with open("README.md", "r") as rdm:
    LONG_DESCRIPTION = rdm.read()

# Setting up
setup(
    name="investing-tickets-scrapper",
    version=VERSION,
    author="Lucas Rocha",
    author_email="lucasrocha.png@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas>=1.3.3', 'selenium>=4.1.3', 'beautifulsoup4>=4.4.1'],
    keywords=['python', 'tickers', 'index', 'stocks', 'exchange', 'investing'],
    classifiers=[
        "Development Status :: 2 - In Work",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)