from distutils.core import setup

setup(name='web_pet_project',
      version='1.0',
      description='PET project for automation practice',
      author='Greg Ward',
      author_email='gward@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['pytest'],
      install_requires=['pytest',
                        'selenium',
                        ]
     )
