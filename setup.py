from distutils.core import setup

setup(name='web_pet_project',
      version='1.0',
      description='PET project for automation practice',
      author='Ivan Demianchuk',
      url='http://the-internet.herokuapp.com/',
      packages=['pytest'],
      install_requires=['allure-pytest',
                        'pytest',
                        'selenium',
                        ])
