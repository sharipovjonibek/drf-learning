from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

code = 'print("Hello, World!")'

lexer = PythonLexer()

formatter = HtmlFormatter(full=True,style="colorful")

highlighed_code = highlight(code,lexer,formatter)

with open("highlighted_code.html","w") as f:
    f.write(highlighed_code)
    

