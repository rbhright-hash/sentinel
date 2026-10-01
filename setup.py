from setuptools import setup

setup(
    name="sentinel",
    version="1.0.0",
    packages=["src"],
    python_requires=">=3.9",
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "sentinel=src.cli:main",
        ],
    },
)
