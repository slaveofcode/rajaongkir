from setuptools import setup
setup(
  name='rajaongkir',
  packages=['rajaongkir'],  # must be filled with your python directories
  version='1.1.2',
  description='Simple Python module to grab api data from rajaongkir.com',
  author='Aditya Kresna Permana',
  author_email='zeandcode@gmail.com',
  url='https://github.com/slaveofcode/rajaongkir',  # use the URL to the github repo
  download_url='https://github.com/slaveofcode/rajaongkir/archive/v1.1.2.zip',
  install_requires=[
    'requests'
  ],
  keywords=['ongkir', 'rajaongkir', 'JNE', 'TIKI', 'Pos'],  # arbitrary keywords
  classifiers=[],
)