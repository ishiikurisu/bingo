default: main

main:
	python main.py

sketch:
	pdflatex sketch.tex

clean:
	rm filled*
