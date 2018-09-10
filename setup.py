import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Github-API-Example',
    version='0.1',
    author='Kyle Mann',
    author_email='KyleThMann@gmail.com',
    description = 'a coding challenge api wrapping Github',
    long_description= long_description,
    long_description_content_type = "text/markdown",
    packages=['Tests', 'src',],
    url='https://github.com/KyMann/Github-API',
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 ],

)