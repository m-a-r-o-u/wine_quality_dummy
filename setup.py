# setup.py

from setuptools import setup, find_packages

setup(
    name="wine_quality",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        'pyYAML',
    ],
    entry_points={
        "console_scripts": [
            "wine_quality_predictor = wine_quality.main:main",
        ],
    },
)

