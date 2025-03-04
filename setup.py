from setuptools import setup, find_packages


setup(
    name="Vertex-CLI",
    version="0.1.22",
    packages=find_packages(),
    description="A CLI tool for debugging and generating AI outputs based on prompts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email="prathamhole@gmail.com",
    include_package_data=True,
    install_requires=[
        "rich",
    ],
    extras_require={
        "dev": ["twine"],
    },
    entry_points={
        "console_scripts": [
            "tex=cli.prompt:main",  # tex --setup / tex "How are you?" / tex --config <model_name> <api_key>
            "tex-init=cli.utils:install_requirements",
        ],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
