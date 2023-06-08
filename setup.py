import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="portfolio",
    version="1.0.0",
    author="Vaibhav Kumar",
    author_email="vaibhav.kr.779@email.com",
    description="A flask framework webpage to define my resume on hosted site",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vaibhavkumar779/portfolio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        "flask",
        "psutil",
        # Add any other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "run_command=portfolio.app:main",
        ],
    },
    license="MIT",
)
