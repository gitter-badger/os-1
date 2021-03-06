OpenStereo
==========

[![Build status](https://ci.appveyor.com/api/projects/status/hur1k36y06c3x7nr?svg=true)](https://ci.appveyor.com/project/endarthur/os)
[![Documentation Status](https://readthedocs.org/projects/openstereo/badge/?version=latest)](https://openstereo.readthedocs.io/en/latest/?badge=latest)

------------------------------------------------------------------------

OpenStereo is an open source, cross-platform software for structural geology analysis.

The software is written in Python, a high-level, cross-platform programming language and the GUI is designed with Qt5, which provide a native look on all OS. Numeric operations (like matrix and linear algebra) are performed with the Numpy module and all graphic capabilities are provided by the Matplolib library, including on-screen plotting and graphic exporting to common desktop formats (emf, eps, ps, pdf, png, svg).

OpenStereo is released under the GNU General Public License v.3.

## Windows Installation

Download the installer .exe from the latest release:

https://github.com/endarthur/os/releases/latest

## Installation from Source

You can install this version of openstereo using:

```bash
$ pip install git+https://github.com/endarthur/os#egg=openstereo
```

Additionally, install PyQt5 from PyPI (for python 2.7, use package python-qt5 instead).

Then run with

```bash
$ openstereo
```

or

```bash
$ python -m openstereo
```

## Known Issues

1. Python 2.7 only works with excel spreadsheet files (.xls|.xlsx) for now, thanks to unicode literals headaches. Should sort this soon, if possible.
