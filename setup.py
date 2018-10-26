from setuptools import setup

setup(name='pyhi',
      version='0.1.0',
      packages=['pyhi'],
      entry_points={
          'console_scripts': [
              'pyhi = pyhi.__main__:main'
          ]
      },
      )
