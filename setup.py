import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = "0.0.0"
REPO_NAME = "Text-Summarize"
AUTHOR_USER = "saurabh-121"
SRC_REPO = "Text-Summarize"
AUTHOR_EMAIL = "saurabh@example.com"

setuptools.setup(
    name=SRC_REPO,
    version=version,
    author=AUTHOR_USER,
    author_email=AUTHOR_EMAIL,
    description="A small python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER}/{SRC_REPO}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "nltk",
        "spacy",
        "gensim",
        "transformers",
        "torch",
        "tensorflow",
        "flask",
        "fastapi",
        "uvicorn",
        "gunicorn",
        "pytest",
        "black",
        "isort",
        "mypy",
    ],
)