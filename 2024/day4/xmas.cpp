#include <bits/stdc++.h>
using namespace std;

// Algorithm: when the letter X is found, look left, right, up,
// and down to find the remaining characters

// r, c are the zero-indexed row and column respectively 
// where the letter x was found, return 1
// if found and 0 otherwise 
int checkLeft(vector<string>& lines, int r, int c) {
	// Out of bounds check
	if (c >= 3) {
		if (lines[r][c-1] == 'M' && lines[r][c-2] == 'A' 
					&& lines[r][c-3] == 'S') {
			return 1;
		}
	}	
	return 0;
}

int checkRight(vector<string>& lines, int r, int c) {
	string currLine = lines[r];
	// Out of bounds check
	if (c <= currLine.size() - 4) {
		if (lines[r][c+1] == 'M' && lines[r][c+2] == 'A' 
					&& lines[r][c+3] == 'S') {
			return 1;
		}
	}	
	return 0;
}

int checkDown(vector<string>& lines, int r, int c) {
	// Out of bounds check
	if (r <= lines.size() - 4) {
		if (lines[r+1][c] == 'M' && lines[r+2][c] == 'A' 
					&& lines[r+3][c] == 'S') {
			return 1;
		}
	}	
	return 0;
}

int checkUp(vector<string>& lines, int r, int c) {
	// Out of bounds check
	if (r >= 3) {
		if (lines[r-1][c] == 'M' && lines[r-2][c] == 'A' 
					&& lines[r-3][c] == 'S') {
			return 1;
		}
	}	
	return 0;
}

vector<int> prefixCounts(string& line, char c) {
	vector<int> counts = vector<int>(line.size());
	int idx = 0;
	for (char currChar : line) {
		if (currChar == c) {
			for (int id2 = idx; id2 < line.size(); id2++) {
				counts[id2] += 1;
			}
		}
		idx += 1;
	}
	return counts;
}

int main() {
	vector<string> lines;
	string currLine;
	while (getline(cin, currLine)) {
		lines.push_back(currLine);
	}
	int numXmas = 0;
	for (int r = 0; r < lines.size(); r++) {
		cout << lines[r] << endl;
		for (int c = 0; c < lines[r].size(); c++) {
			if (lines[r][c] == 'X') {
				numXmas += checkLeft(lines, r, c);			
				numXmas += checkRight(lines, r, c);			
				numXmas += checkUp(lines, r, c);			
				numXmas += checkDown(lines, r, c);			
			}
		}
	}
	cout << numXmas << endl;
}
