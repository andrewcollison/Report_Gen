# '''
# Python Report Generator
# Author: Andrew Collison
# Date Started: 11-Nov-18
# '''

import pandas as pd 
import os
from string import Template
from subprocess import call, check_call





f = open('template.tex',encoding="latin-1")
tex_template = f.read()
# print(tex_template)

s = Template(tex_template)
output = s.substitute({'title':'Python and LaTeX: Dream Team', 'BH':'Welcome', 'name': 'Mr Andrew Collison'})

print(output)
output_file = open('output.tex', 'w')
output_file.write(output)
output_file.close()

print('BUILDING LATEX FILE')
# os.system('pdflatex -silent output.tex')
call("pdflatex -silent output.tex")


# call(['pdflatex', '-help'])
print('DONE')







