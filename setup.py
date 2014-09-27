from setuptools import setup, find_packages


setup(
    name='pelicanium',
    version=0.1,
    url='https://github.com/dimazest/pelicanium',
    author="Dmitrijs Milajevs",
    author_email="dimazest@gmail.com",
    description='A port of the Ghostium theme to Pelican.',
    long_description=open("README.rst").read(),
    license='MIT',
    packages=find_packages(),
    package_data={'': [
        'LICENSE',
        'README.rst',
        'static/*',
        'templates/*',
    ]
    },
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
    install_requires=[
        'pelican',
        'pelican-edit-url',
        'pelican_extended_authors',
    ],
)
