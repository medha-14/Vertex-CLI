from setuptools import setup, find_packages

setup(
    name="Vertex-CLI",  # Package name
    version="0.1.0",  # Initial version
    packages=find_packages(),  # Auto-detect packages
    install_requires=[
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "tex=cli.prompt:main",  # tex --setup / tex "How are you?" / tex --config <model_name> <api_key>
        ],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
