# -*- coding: utf-8 -*-
"""setup -- setuptools setup file for kytten.
GUI Framework for Pyglet
"""

from setuptools import setup, find_packages

setup(name="felyne",
      version="7.0.1",
      author="Conrad 'Lynx' Wong (originator), Raymond Chandler III (fork), DeflatedPickle (fork)",
      description="A Python 3 fork of Kytten, a widget toolkit for Pyglet.",
      url="https://github.com/DeflatedPickle/felyne",
      license="BSD",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: MacOS X",
          "Environment :: Win32 (MS Windows)",
          "Environment :: X11 Applications",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Natural Language :: English",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python",
          ("Topic :: Software Development :: Libraries :: Python Modules"),
          ("Topic :: Games/Entertainment"),
      ],
      packages=["kytten"],
      install_requires=['pyglet>=1.1.4'],
      zip_safe=False)
