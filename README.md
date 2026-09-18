 # ProjectForge 📦

> **⚠️ Version 1 — Early Project**
>
> ProjectForge is currently a **V1 project**, so don't expect advanced or complex features yet. The current goal is to provide a simple, useful boilerplate generator. More features may be added in future versions.

ProjectForge is a Python package that quickly creates a clean, ready-to-use project structure for web projects.

Instead of manually creating folders and files every time, ProjectForge generates the basic structure with a single function.

## 🚀 Installation

Install ProjectForge using pip:

```bash
pip install projectforge
```

## 🛠️ Usage

Import the `project_structure` function and provide the name of your project:

```python
from projectforge import project_structure

project_structure("MyProject")
```

This will create:

```text
MyProject/
├── template/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── assets/
│   ├── fonts/
│   ├── icons/
│   └── images/
│
├── README.md
├── .gitignore

## 📁 Project Structure

### `template/`

Contains HTML templates for the project.

### `static/`

Contains static files such as:

* CSS
* JavaScript

### `assets/`

Contains additional project resources:

* Fonts
* Icons
* Images

### `README.md`

Documentation for the generated project.

### `.gitignore`

Used to specify files and folders that Git should ignore.


## 🎯 Purpose

ProjectForge was created to make starting new web projects faster and more organized.

The goal is to provide a basic boilerplate structure without having to manually create the basic folders and files.

It is designed for:

* **Beginners** who aren't sure how to structure a project.
* **Developers** working on larger projects who don't want to manually create basic, repetitive files and folders.
* **Anyone** who wants to quickly get a basic project structure ready for development.

## 🧪 Example

```python
from projectforge import project_structure

project_structure("Portfolio")
```

Output:

```text
🎉🎉 Portfolio created successfully! 🎉🎉
```

## 👤 Author

**HisHighnessTroy**

    
    """
