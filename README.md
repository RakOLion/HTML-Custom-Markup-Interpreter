# HTML-Custom-Markup-Interpreter

Simple interpreter to translate a custom markup script into HTML code for a blog post

## Installation
1. Download the files for the project.
2. Install required dependencies (ideally within a virtual environment - [Tutorial](https://docs.python.org/3/tutorial/venv.html)).
3. Create a stylesheet for your end-page and install prism.js (for code blocks). Place these within your project directory and (if necessary) modify the prefix string to reference the correct file path. 
4. (Optional) Install Notepad++ and import the [.udl file](blog-markdown-formatting.udl) file for custom syntax highlighting.

## Usage
Import the [.udl file](blog-markdown-formatting.udl) as a custom language in Notepad++ (Language > User Defined Language > Define your language > Import). 

Try opening the [sample template](sample-template.txt) included within the project files. Your window should look something like this (you might have to change your Notepad theme to Monokai with Settings > Style Configurator).

<img width="633" alt="udl_screenshot" src="https://user-images.githubusercontent.com/42822671/151635252-19f0fc38-659d-4037-ad37-2569e5d3a837.png">

You can run the interpreter with the following command in your project directory.

```python interpreter.py [infile.txt] [outfile.html]```

The css file I created, when paired with the output HTML file from the interpreter, produces an ouput which looks something like this. Customize your own page how you see fit.

<img width="633" alt="post_screenshot" src="https://user-images.githubusercontent.com/42822671/151635817-e391134a-049d-4ecf-80b9-0e6e2e3178fa.png">
