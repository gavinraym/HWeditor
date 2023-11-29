styleDict = {
    'class="c"':'class="python-comment"', # Comment
    'class="c1"':'class="python-comment"', # Comment.Single
    'class="ch"':'class="python-comment"', # Comment.Hashbang
    'class="cm"':'class="python-comment"', # Comment.Multiline
    'class="cp"':'class="python-comment"', # Comment.Preproc
    'class="cpf"':'class="python-comment"', # Comment.PreprocFile
    'class="c1"':'class="python-comment"', # Comment.Single
    'class="cs"':'class="python-comment"', # Comment.Special
    'class="kc"':'class="python-variable"', # Keyword.Constant
    'class="kd"':'class="python-variable"', # Keyword.Declaration
    'class="kn"':'class="python-variable"', # Keyword.Namespace
    'class="kp"':'class="python-variable"', # Keyword.Pseudo
    'class="kr"':'class="python-variable"', # Keyword.Reserved
    'class="kt"':'class="python-variable"', # Keyword.Type
    'class="s"':'class="python-string"', # Literal.String
    'class="na"':'class="python-variable"', # Name.Attribute
    'class="nb"':'class="python-builtin"', # Name.Builtin
    'class="nc"':'class="python-variable"', # Name.Class
    'class="no"':'class="python-variable"', # Name.Constant
    'class="nd"':'class="python-variable"', # Name.Decorator
    'class="ni"':'class="python-variable"', # Name.Entity
    'class="ne"':'class="python-variable"', # Name.Exception
    'class="nf"':'class="python-variable"', # Name.Function
    'class="nl"':'class="python-variable"', # Name.Label
    'class="nn"':'class="python-variable"', # Name.Namespace
    'class="nt"':'class="python-variable"', # Name.Tag
    'class="nv"':'class="python-variable"', # Name.Variable
    'class="n"':'class="python-variable"', # Name.Variable
    'class="ow"':'class="python-operator"', # Operator.Word
    'class="mb"':'class="python-number"', # Literal.Number.Bin
    'class="mf"':'class="python-number"', # Literal.Number.Float
    'class="mh"':'class="python-number"', # Literal.Number.Hex
    'class="mi"':'class="python-number"', # Literal.Number.Integer
    'class="mo"':'class="python-number"', # Literal.Number.Oct
    'class="sa"':'class="python-string"', # Literal.String.Affix
    'class="sb"':'class="python-string"', # Literal.String.Backtick
    'class="sc"':'class="python-string"', # Literal.String.Char
    'class="dl"':'class="python-string"', # Literal.String.Delimiter
    'class="sd"':'class="python-string"', # Literal.String.Doc
    'class="s2"':'class="python-string"', # Literal.String.Double
    'class="se"':'class="python-string"', # Literal.String.Escape
    'class="sh"':'class="python-string"', # Literal.String.Heredoc
    'class="si"':'class="python-string"', # Literal.String.Interpol
    'class="sx"':'class="python-string"', # Literal.String.Other
    'class="sr"':'class="python-string"', # Literal.String.Regex
    'class="s1"':'class="python-string"', # Literal.String.Single
    'class="ss"':'class="python-string"', # Literal.String.Symbol
    'class="bp"':'class="python-builtin"', # Name.Builtin.Pseudo
    'class="fm"':'class="python-variable"', # Name.Function.Magic
    'class="vc"':'class="python-variable"', # Name.Variable.Class
    'class="vg"':'class="python-variable"', # Name.Variable.Global
    'class="vi"':'class="python-variable"', # Name.Variable.Instance
    'class="vm"':'class="python-variable"', # Name.Variable.Magic
    'class="il"':'class="python-number"', # Literal.Number.Integer.Long
}

#  .o { color: #666666 } /* Operator */
# .ch { color: #3D7B7B; font-style: italic } /* Comment.Hashbang */
# .cm { color: #3D7B7B; font-style: italic } /* Comment.Multiline */
# .cp { color: #9C6500 } /* Comment.Preproc */
# .cpf { color: #3D7B7B; font-style: italic } /* Comment.PreprocFile */
# .c1 { color: #3D7B7B; font-style: italic } /* Comment.Single */
# .cs { color: #3D7B7B; font-style: italic } /* Comment.Special */
# .gd { color: #A00000 } /* Generic.Deleted */
# .ge { font-style: italic } /* Generic.Emph */
# .ges { font-weight: bold; font-style: italic } /* Generic.EmphStrong */
# .gr { color: #E40000 } /* Generic.Error */
# .gh { color: #000080; font-weight: bold } /* Generic.Heading */
# .gi { color: #008400 } /* Generic.Inserted */
# .go { color: #717171 } /* Generic.Output */
# .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
# .gs { font-weight: bold } /* Generic.Strong */
# .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
# .gt { color: #0044DD } /* Generic.Traceback */
# .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
# .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
# .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
# .kp { color: #008000 } /* Keyword.Pseudo */
# .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
# .kt { color: #B00040 } /* Keyword.Type */
# .m { color: #666666 } /* Literal.Number */
# .s { color: #BA2121 } /* Literal.String */
# .na { color: #687822 } /* Name.Attribute */
# .nb { color: #008000 } /* Name.Builtin */
# .nc { color: #0000FF; font-weight: bold } /* Name.Class */
# .no { color: #880000 } /* Name.Constant */
# .nd { color: #AA22FF } /* Name.Decorator */
# .ni { color: #717171; font-weight: bold } /* Name.Entity */
# .ne { color: #CB3F38; font-weight: bold } /* Name.Exception */
# .nf { color: #0000FF } /* Name.Function */
# .nl { color: #767600 } /* Name.Label */
# .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
# .nt { color: #008000; font-weight: bold } /* Name.Tag */
# .nv { color: #19177C } /* Name.Variable */
# .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
# .w { color: #bbbbbb } /* Text.Whitespace */
# .mb { color: #666666 } /* Literal.Number.Bin */
# .mf { color: #666666 } /* Literal.Number.Float */
# .mh { color: #666666 } /* Literal.Number.Hex */
# .mi { color: #666666 } /* Literal.Number.Integer */
# .mo { color: #666666 } /* Literal.Number.Oct */
# .sa { color: #BA2121 } /* Literal.String.Affix */
# .sb { color: #BA2121 } /* Literal.String.Backtick */
# .sc { color: #BA2121 } /* Literal.String.Char */
# .dl { color: #BA2121 } /* Literal.String.Delimiter */
# .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
# .s2 { color: #BA2121 } /* Literal.String.Double */
# .se { color: #AA5D1F; font-weight: bold } /* Literal.String.Escape */
# .sh { color: #BA2121 } /* Literal.String.Heredoc */
# .si { color: #A45A77; font-weight: bold } /* Literal.String.Interpol */
# .sx { color: #008000 } /* Literal.String.Other */
# .sr { color: #A45A77 } /* Literal.String.Regex */
# .s1 { color: #BA2121 } /* Literal.String.Single */
# .ss { color: #19177C } /* Literal.String.Symbol */
# .bp { color: #008000 } /* Name.Builtin.Pseudo */
# .fm { color: #0000FF } /* Name.Function.Magic */
# .vc { color: #19177C } /* Name.Variable.Class */
# .vg { color: #19177C } /* Name.Variable.Global */
# .vi { color: #19177C } /* Name.Variable.Instance */
# .vm { color: #19177C } /* Name.Variable.Magic */
# .il { color: #666666 } /* Literal.Number.Integer.Long */