from . import python, html, css, js, java

refs = {
    'python': (python.styleDict, python.lexer),
    'html': (html.styleDict, html.lexer),
    'CSS': (css.styleDict, css.lexer),
    'js': (js.styleDict, js.lexer),
    'java': (java.styleDict, java.lexer),
}

def get_language(language):
    # Get the language module
    return refs[language]