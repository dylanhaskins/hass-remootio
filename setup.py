from setuptools import setup, find_packages

setup(
    name='remootio',
    version='2.2',
    author='TritonNet',
    author_email='info@kushan.me',
    description='Asynchronous Python client for interfacing with Remootio devices.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TritonNet/hass-remootio',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
