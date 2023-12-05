
from pygments import highlight
from pygments.formatters import HtmlFormatter
from modules.snippets import languages
import re


def get_styles(language):
    # Get a list of available styles for the lexer
    return HtmlFormatter().get_style_defs('.highlight')

def highlight_code(code, language):
    # Retrieve language map and lexer
    language_map, lexer = languages.get_language(language)
    # Initialize the formatter for HTML output
    formatter = HtmlFormatter(nowrap=True)
    # Highlight code
    highlighted_code = highlight(code, lexer(), formatter)
    # Add line numbers
    line_number = 0
    lines = []
    # Iterate lines and add HW specific formatting
    for line in highlighted_code.split('\n'):
        # Ensuring spaces are not lost
        line = re.sub(r'^(\s+)', lambda match: '\u00A0' * len(match.group(1)), line)
        line = re.sub(r'^(<span class="w">(\s+)</span>)+', lambda match: '\u00A0' * len(match.group(2)), line)
        # Add line number
        line_number += 1
        line = f"<div class='snippet-row'><div class='line-number'>{line_number}</div><div class='code'>{line}</div></div>"
        # Add line to list
        lines.append(line)
    result = ''.join(lines)
    # Change language tags to HW specific tags
    for tag in language_map:
        result = result.replace(tag, language_map[tag])
    return result
    
