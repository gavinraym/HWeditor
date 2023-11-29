from . import python

refs = {
    'python':python.styleDict,
}

def get_language(language):
    # Get the language module
    return refs[language]