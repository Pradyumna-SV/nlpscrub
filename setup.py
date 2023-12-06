from setuptools import setup, find_packages

setup(
    name='nlpscrub',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'emoji',
        'nltk'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description='NLP text preprocessing library',
    license='MIT',
    include_package_data=True,
)
