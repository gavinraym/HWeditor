'''
css-comment
css-number
css-property
css-pseudoclass (e.g. :hover)
css-string 
'''
from pygments.lexers.css import CssLexer as lexer
styleDict = {
    'class="c"':'class="css-comment"', # Comment
    'class="c1"':'class="css-comment"', # Comment.Single
    'class="ch"':'class="css-comment"', # Comment.Hashbang
    'class="cm"':'class="css-comment"', # Comment.Multiline
    'class="cp"':'class="css-comment"', # Comment.Preproc
    'class="cpf"':'class="css-comment"', # Comment.PreprocFile
    'class="c1"':'class="css-comment"', # Comment.Single
    'class="cs"':'class="css-comment"', # Comment.Special
    'class="kc"':'class="css-property"', # Keyword.Constant
    'class="kd"':'class="css-property"', # Keyword.Declaration
    'class="kn"':'class="css-property"', # Keyword.Namespace
    'class="kp"':'class="css-property"', # Keyword.Pseudo
    'class="kr"':'class="css-property"', # Keyword.Reserved
    'class="kt"':'class="css-property"', # Keyword.Type
    'class="s"':'class="css-string"', # Literal.String
    'class="na"':'class="css-property"', # Name.Attribute
    'class="nb"':'class="css-builtin"', # Name.Builtin
    'class="nc"':'class="css-class"', # Name.Class
    'class="no"':'class="css-property"', # Name.Constant
    'class="nd"':'class="css-pseudoclass"', # Name.Decorator
    'class="ni"':'class="css-property"', # Name.Entity
    'class="ne"':'class="css-property"', # Name.Exception
    'class="nf"':'class="css-property"', # Name.Function
    'class="nl"':'class="css-property"', # Name.Label
    'class="nn"':'class="css-id"', # Name.Namespace
    'class="nt"':'class="css-property"', # Name.Tag
    'class="nv"':'class="css-property"', # Name.Variable
    'class="n"':'class="css-property"', # Name.Variable
    'class="ow"':'class="css-operator"', # Operator.Word
    'class="mb"':'class="css-number"', # Literal.Number.Bin
    'class="mf"':'class="css-number"', # Literal.Number.Float
    'class="mh"':'class="css-number"', # Literal.Number.Hex
    'class="mi"':'class="css-number"', # Literal.Number.Integer
    'class="mo"':'class="css-number"', # Literal.Number.Oct
    'class="sa"':'class="css-string"', # Literal.String.Affix
    'class="sb"':'class="css-string"', # Literal.String.Backtick
    'class="sc"':'class="css-string"', # Literal.String.Char
    'class="dl"':'class="css-string"', # Literal.String.Delimiter
    'class="sd"':'class="css-string"', # Literal.String.Doc
    'class="s2"':'class="css-string"', # Literal.String.Double
    'class="se"':'class="css-string"', # Literal.String.Escape
    'class="sh"':'class="css-string"', # Literal.String.Heredoc
    'class="si"':'class="css-string"', # Literal.String.Interpol
    'class="sx"':'class="css-string"', # Literal.String.Other
    'class="sr"':'class="css-string"', # Literal.String.Regex
    'class="s1"':'class="css-string"', # Literal.String.Single
    'class="ss"':'class="css-string"', # Literal.String.Symbol
    'class="bp"':'class="css-builtin"', # Name.Builtin.Pseudo
    'class="fm"':'class="css-property"', # Name.Function.Magic
    'class="vc"':'class="css-property"', # Name.Variable.Class
    'class="vg"':'class="css-property"', # Name.Variable.Global
    'class="vi"':'class="css-property"', # Name.Variable.Instance
    'class="vm"':'class="css-property"', # Name.Variable.Magic
    'class="il"':'class="css-number"', # Literal.Number.Integer.Long
}