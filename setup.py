import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slobs-websocket",
    version="0.0.1",
    author="Mario Steele",
    author_email="mario@ruby-im.net",
    description="A StreamlabsOBS Websocket Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eumario/slobs_websocket",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)