from setuptools import setup

setup(name='lash',
      version='0.1',
      description='A tool to calculate approximate distance for long genome sequence',
      url='https://github.com/pinkmonz/lash',
      author='Ziyn Wang',
      author_email='zywong159@gmail.com',
      license='MIT',
      packages=['lash'],
      install_requires=[
          'numpy',
          'mmh3',
      ],
      zip_safe=False)