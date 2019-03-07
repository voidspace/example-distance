import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="distance",
    version="0.1.0",
    author="Michael Foord",
    author_email="michael@python.org",
    description="A simple example web app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/voidspace/example-distance",
    packages=['distance'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0 or later (GPL-3.0-or-later)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "django",
        'location',
    ],
    # Will eventually be deprecated and we should be able to use this URL directly in install_requires
    dependency_links=[
        'git+ssh://git@github.com/voidspace/location@master#egg=location-0.1.0'
    ]
)