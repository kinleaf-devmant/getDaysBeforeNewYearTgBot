from setuptools import setup, find_packages
setup(
    name="getDaysBeforeNewYearTgBot",
    version="0.1",
    packages=find_packages(),

    install_requires=["requests"],

    # package_data={
    #     # If any package contains *.txt or *.rst files, include them:
    #     '': ['*.txt', '*.rst'],
    #     # And include any *.msg files found in the 'hello' package, too:
    #     'hello': ['*.msg'],
    # },

    # metadata for upload to PyPI
    author="Kinleaf Devmant",
    author_email="kinleaf.devmant@gmail.com",
    description="This is telegram bot that can answer you about how many days left before New Year",
    license="MIT",
    keywords="telegram bot new year",


    # could also include url, long_description, download_url, classifiers, etc.
    # useful setuptools documentation: https://setuptools.readthedocs.io/en/latest/setuptools.html#installing-setuptools
)
