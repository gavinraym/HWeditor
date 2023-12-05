'''
html-attribute
html-comment
html-tag
html-value
'''
from pygments.lexers.html import HtmlLexer as lexer
styleDict = {
    'class="c"':'class="html-comment"', # Comment
    'class="c1"':'class="html-comment"', # Comment.Single
    'class="ch"':'class="html-comment"', # Comment.Hashbang
    'class="cm"':'class="html-comment"', # Comment.Multiline
    'class="cp"':'class="html-comment"', # Comment.Preproc
    'class="cpf"':'class="html-comment"', # Comment.PreprocFile
    'class="c1"':'class="html-comment"', # Comment.Single
    'class="cs"':'class="html-comment"', # Comment.Special
    'class="kc"':'class="html-attribute"', # Keyword.Constant
    'class="kd"':'class="html-attribute"', # Keyword.Declaration
    'class="kn"':'class="html-attribute"', # Keyword.Namespace
    'class="kp"':'class="html-attribute"', # Keyword.Pseudo
    'class="kr"':'class="html-attribute"', # Keyword.Reserved
    'class="kt"':'class="html-attribute"', # Keyword.Type
    'class="s"':'class="html-value"', # Literal.String
    'class="na"':'class="html-attribute"', # Name.Attribute
    'class="nb"':'class="html-builtin"', # Name.Builtin
    'class="nc"':'class="html-attribute"', # Name.Class
    'class="no"':'class="html-attribute"', # Name.Constant
    'class="nd"':'class="html-attribute"', # Name.Decorator
    'class="ni"':'class="html-attribute"', # Name.Entity
    'class="ne"':'class="html-attribute"', # Name.Exception
    'class="nf"':'class="html-attribute"', # Name.Function
    'class="nl"':'class="html-attribute"', # Name.Label
    'class="nn"':'class="html-attribute"', # Name.Namespace
    'class="nt"':'class="html-tag"', # Name.Tag
    'class="nv"':'class="html-attribute"', # Name.attribute
    'class="n"':'class="html-attribute"', # Name.attribute
    'class="ow"':'class="html-operator"', # Operator.Word
    'class="mb"':'class="html-value"', # Literal.Number.Bin
    'class="mf"':'class="html-value"', # Literal.Number.Float
    'class="mh"':'class="html-value"', # Literal.Number.Hex
    'class="mi"':'class="html-value"', # Literal.Number.Integer
    'class="mo"':'class="html-value"', # Literal.Number.Oct
    'class="sa"':'class="html-value"', # Literal.String.Affix
    'class="sb"':'class="html-value"', # Literal.String.Backtick
    'class="sc"':'class="html-value"', # Literal.String.Char
    'class="dl"':'class="html-value"', # Literal.String.Delimiter
    'class="sd"':'class="html-value"', # Literal.String.Doc
    'class="s2"':'class="html-value"', # Literal.String.Double
    'class="se"':'class="html-value"', # Literal.String.Escape
    'class="sh"':'class="html-value"', # Literal.String.Heredoc
    'class="si"':'class="html-value"', # Literal.String.Interpol
    'class="sx"':'class="html-value"', # Literal.String.Other
    'class="sr"':'class="html-value"', # Literal.String.Regex
    'class="s1"':'class="html-value"', # Literal.String.Single
    'class="ss"':'class="html-value"', # Literal.String.Symbol
    'class="bp"':'class="html-builtin"', # Name.Builtin.Pseudo
    'class="fm"':'class="html-attribute"', # Name.Function.Magic
    'class="vc"':'class="html-attribute"', # Name.attribute.Class 
    'class="vg"':'class="html-attribute"', # Name.attribute.Global
    'class="vi"':'class="html-attribute"', # Name.attribute.Instance
    'class="vm"':'class="html-attribute"', # Name.attribute.Magic
    'class="il"':'class="html-value"', # Literal.Number.Integer.Long
}