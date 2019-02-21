from setuptools import setup

def readme():
    with open('README.md') as file:
        return file.read()

setup(name='tiobeindexpy',
      version='1.0.0',
      description='A Python package for getting TIOBE Index',
      long_description=readme(),
      url='https://github.com/amrrs/tiobeindexpy',
      keywords=['tiobe', 'programming language ranking', 'index', 'programming language'],
      author='AbdulMajedRaja RS',
      author_email='amrrs.data@gmail.com',
      license='MIT',
      packages=['tiobeindexpy'],
      install_requires=[
          'requests',
          'beautifulsoup4',
          'pandas'
      ],
      zip_safe=False)
