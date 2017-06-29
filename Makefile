make: main.cpp AdjacencyMatrix.h
	g++ main.cpp -o cycledetect -O3

parse: parser.py
	python parser.py

run: cycledetect
	./cycledetect
