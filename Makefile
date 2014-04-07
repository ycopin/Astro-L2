# Time-stamp: <2014-04-07 10:43:29 ycopin>

all: etudiant enseignant

etudiant: TD_astro_L2.tex
	pdflatex "\def\sanscorrige{}\input{TD_astro_L2}"
	pdflatex "\def\sanscorrige{}\input{TD_astro_L2}"
	mv TD_astro_L2.pdf TD_astro_L2_fascicule.pdf

enseignant: TD_astro_L2.tex
	pdflatex TD_astro_L2.tex
	pdflatex TD_astro_L2.tex
	mv TD_astro_L2.pdf TD_astro_L2_corrige.pdf
