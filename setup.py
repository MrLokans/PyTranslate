__author__ = 'anders-lokans'

from distutils.core import setup
setup(name='yatranslate',
      version='0.4a',
      description='Yandex Translate Module',
      author='MrLokans',
      author_email='trikster1911@gmail.com',
      install_requires=['requests>=2.4.3'],
      scripts = ['bin/yatranslate']
      )