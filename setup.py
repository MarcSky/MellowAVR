import os
from distutils.core import setup
from setuptools import setup
import src

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "MellowAVR",
    version = "0.0.1",
    author = "Levan Gogohia",
    author_email = "levangogohia@yandex.ru",
    description = ("IDE for microcontroller AVR"),
    license = "GNU GPL v2",
    keywords = "IDE AVR",
    long_description=read('README.txt'),
    install_requires=[
        'avr-gcc > 3.5',
	'pyqt >= 4'
    ]
)

