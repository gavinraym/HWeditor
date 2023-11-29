
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from modules.snippets import languages
import re


def get_styles(language):
    # Get a list of available styles for the lexer
    return HtmlFormatter().get_style_defs('.highlight')


def highlight_code(code, language):
    # Prep incoming code
    code = code.replace('\r\n', '\n')
    code = code.replace('\r', '\n')
    code = code.split('\n')
    # Initialize list for storing output
    styled_lines = []
    # Initialize the lexer and formatter
    lexer = get_lexer_by_name(language, stripall=True)
    formatter = HtmlFormatter()
    # To use regex to remove the extra junk and split on mark and del
    junk_pattern = r'<div class="highlight"><pre><span></span>|\n</pre></div>\n'
    mark_del_strings = ['`<mark>`', '`</mark>`', '`<del>`', '`</del>`']
    mark_del_pattern = '|'.join(map(re.escape, mark_del_strings))
    # Get HW language map
    language_map = languages.get_language(language)
    print(type(language_map))
    # Add line numbers
    line_number = 0
    # Highlight each line of code
    for line in code:
        line_number += 1

        # find any breaks in the line
        new_line = ""
        # Split the line on the substrings
        split_line = re.split(f'({mark_del_pattern})', line)
        print(split_line)
        for split in split_line:
            print("old line =", repr(new_line)  )
            if split == '':
                continue
            elif split in mark_del_strings:
                new_line += split[1:-1]
            else:
                # Count blank spaces at beginning and end
                starting_spaces = 0
                while len(split) >0 and split[0] == ' ':
                    starting_spaces += 1
                    split = split[1:]
                ending_spaces = 0
                while len(split)>0 and split[-1] == ' ':
                    ending_spaces += 1
                    split = split[:-1]

                highlighted_code = ''
                if len(split) >0:
                    highlighted_code = highlight(split, lexer, formatter)
                    print("highlighted code =")
                    print(repr(highlighted_code))
                    # Use re.sub() to remove the extra junk
                    highlighted_code = re.sub(junk_pattern, '', highlighted_code)
                    print(repr(highlighted_code))
                    # Format for HW site
                    for tag in language_map:
                        highlighted_code = highlighted_code.replace(tag, language_map[tag])
                    # add non breaking spaces
                
                new_line += '&nbsp'*starting_spaces + highlighted_code + '&nbsp'*ending_spaces
            print("new line =", repr(new_line))

        new_line = f"<div class='snippet-row'><div class='line-number'>{line_number}</div><div class='code'>{new_line}</div></div>"
        styled_lines.append(new_line)

    # Return the highlighted code
    return ''.join(styled_lines)



'''def highlight_code(code, language, markStarts, markEnds, delStarts, delEnds):
    # Prep incoming code
    code = code.replace('\r\n', '\n')
    code = code.replace('\r', '\n')
    
    # Consolidate all mark and del breaks
    breaks = markStarts + markEnds + delStarts + delEnds
    # Sort the breaks
    breaks.sort()


    code = code.split('\n')
    styled_lines = []
    # Initialize the lexer and formatter
    lexer = get_lexer_by_name(language, stripall=True)
    language_pack = languages.get_language(language)
    formatter = HtmlFormatter()
    # Pygment adds this extra junk to the beginning and end of the code
    pattern = r'<div class="highlight"><pre><span></span>|</pre></div>'
    # Add line numbers
    line_number = 0
    len_of_lines = 1
    # Highlight each line of code
    for line in code:
        line_number += 1
        len_of_lines += len(line)-1

        # find any breaks in the line
        new_line = ""
        for break_point in [_ for _ in breaks if _ < len_of_lines]:
            breaks.remove(break_point)
            new_line += highlight(line[:break_point], lexer, formatter)
            if break_point in markStarts:
                new_line += "<mark>"
            elif break_point in markEnds:
                new_line += "</mark>"
            elif break_point in delStarts:
                new_line += "<del>"
            elif break_point in delEnds:
                new_line += "</del>"
            line = line[break_point:]
        new_line +=  highlight(line, lexer, formatter)

        # Use re.sub() to remove the extra junk
        new_line = re.sub(pattern, '', new_line)
        for tag in languages.get_language(language):
            new_line = new_line.replace(tag, languages.get_language(language)[tag])
        new_line = f"<div class='snippet-row'><div class='line-number'>{line_number}</div><div class='code'>{new_line}</div></div>"
        new_line = new_line.replace("\n", "")
        styled_lines.append(new_line)

    # Return the highlighted code
    return ''.join(styled_lines)'''