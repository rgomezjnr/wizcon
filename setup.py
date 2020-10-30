import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wizcon",
    version="0.1.0",
    author="Robert Gomez, Jr.",
    author_email="rgomezjnr@gmail.com",
    description="Control Philips WiZ Connected smart light bulbs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rgomezjnr/wizcon",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=["pywizlight"],
    license="MIT",
    entry_points ={'console_scripts':['wizcon=wizcon.wizcon:main_async']},
    keywords="philips wiz wifi wireless home automation cli tool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Home Automation",
        "Topic :: Utilities",
    ],
)