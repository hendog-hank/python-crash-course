glossary = {
    "variable": "A name that stores a value in memory.",
    "data type": "The kind of value a variable holds (e.g., int, float, str, list, bool).",
    "function": "A reusable block of code that performs a specific task.",
    "list": "An ordered, changeable collection of items.",
    "dictionary": "A collection of key-value pairs.",
    "loop": "A construct used to repeat code multiple times (for or while).",
    "conditional": "Code that runs only if a specific condition is true.",
    "module": "A separate Python file that contains functions, classes, or variables you can reuse.",
    "class": "A blueprint for creating objects that bundle data and behavior.",
    "exception": "An error that occurs during program execution; can be handled with try/except.",
}

for k, v in glossary.items():
    print(f"{k.title()}: {v.lower()}")

