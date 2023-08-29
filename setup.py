from setuptools import setup

setup(
    name='Weather App',
    version='1.0',
    description='Weather App',
    author='Muhammad Raza',
    author_email="iamraza1998@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    long_description="Weather App",
    packages=["weather_app"],
    include_package_data=True,
    entry_points= {
        "console_scripts": [
            "weather_app = weather_app.main:main",
        ],
    },
    install_requires=[
        'requests',
        'argparse',
        'pytest'
    ],
    python_requires='>=3.6'
)