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
            "vertex-cli=cli.prompt:main",  # vertex-cli --setup
            "tex2=cli.prompt:handle_all_quries",  # Update this with your actual main script
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
