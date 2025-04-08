from setuptools import setup, find_packages

setup(
    name="vyxm",
    version="0.0.1",
    description="A modular AI framework with agent protocols, memory, cv and llm based machine learning algorithims.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Vyomie",
    author_email="me@vyxm.in",
    url="https://github.com/vyomie/vyxm",
    packages=find_packages(exclude=["tests*", "examples*"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "requests",
        "torch>=2.0.0",
        "transformers>=4.36.0",
        "diffusers",
        "pydantic>=2",
        "numpy",
        "typing-extensions",
        "uuid"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="vyxm agents ai protocol transformers multi-agent ml learning memory computer-vision llm neural networks",
    project_urls={
        "Source": "https://github.com/vyomie/vyxm",
        "Tracker": "https://github.com/vyomie/vyxm/issues",
    },
)
