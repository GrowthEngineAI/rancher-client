import sys
from setuptools import setup

if sys.version_info.major != 3:
    raise RuntimeError("This package requires Python 3+")

with open('./requirements.txt') as r:
    # strip fixed version info from requirements file
    requirements = [line.split('=', 1)[0] for line in r]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='rancher-client',
    version='0.0.1',
    py_modules=['rancher'],
    url='https://github.com/growthengineai/rancher-client',
    license='MIT Style',
    description='Python client for the Rancher API with Async Support',
    author='Tri Songz',
    author_email='ts@growthengineai.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
    ]
)