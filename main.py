import os
import jinja2 as jinja
import numpy.random

def build(names):
    outlet = []
    i = 0
    line = ''

    for name in names:
        i += 1
        if i % 5 == 0:
            line += '{} \\\\ \\hline\n'.format(name)
        elif i % 5 == 1:
            outlet.append(line)
            line = '{} & '.format(name)
        else:
            line += '{} & '.format(name)

    outlet.append(line)
    return outlet

def draw_table(tex, names, output):
    template = jinja.Template(tex)
    outlet = template.render(lines=build(names))
    with open(output, 'w') as fp:
        fp.write(outlet)
    os.system('pdflatex {}'.format(output))

if __name__ == '__main__':
    tex = ''
    with open('empty.tex', 'r') as fp:
        tex = fp.read()

    all_names = []
    with open('nomes.txt', 'r') as fp:
        for line in fp:
            all_names.append(line.strip())

    names = all_names
    for i in range(5):
        names = numpy.random.permutation(names)
        output = 'filled{0}.tex'.format(i+1)
        draw_table(tex, names[0:20], output)
