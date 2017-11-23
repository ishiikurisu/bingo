import os
import jinja2 as jinja

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

def draw_table(tex, names):
    template = jinja.Template(tex)
    outlet = template.render(lines=build(names))
    with open('filled.tex', 'w') as fp:
        fp.write(outlet)
    os.system('pdflatex filled.tex')

if __name__ == '__main__':
    tex = ''
    with open('empty.tex', 'r') as fp:
        tex = fp.read()

    all_names = []
    with open('nomes.txt', 'r') as fp:
        for line in fp:
            all_names.append(line.strip())

    draw_table(tex, all_names[:20])
