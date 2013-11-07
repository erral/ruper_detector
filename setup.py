from setuptools import setup, find_packages

version = '1.0'

setup(name='ruper_detector',
      version=version,
      description="EITB Irratian Ruper Ordorikaren kantuen detektorea",
      long_description=open("README.rst").read() + "\n" +
                       open("HISTORY.txt").read(),

      classifiers=[],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'beautifulsoup4'
      ],
      entry_points={
        'console_scripts': [
              'ruper_detector = ruper.main:main',
        ]
      },
      )
