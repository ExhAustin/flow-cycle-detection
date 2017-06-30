#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class TransData{
	int count;
	vector<int> timestamp;

	TransData(){count = 0;};
};

class AdjacencyMatrix{
private:
	vector<string> labels;
	vector<vector<TransData>> graph;

public:
	AdjacencyMatrix();
	void addEdge(string S1, string S2);

};
