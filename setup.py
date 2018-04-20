from setuptools import setup
setup(name='deadwind',
      version='0.2',
      description='Converts Medvinds xsls (MS excell) shedule data to csv data suitable for export to google calendar',
      url='https://github.com/johanoeh/deadwind.git',
      author='Johan Oh',
      author_email='johan.oh1980@gmail.com',
      license='MIT',
      packages=['deadwind'],
      install_requires=['openpyxl'],
      zip_safe=False)
