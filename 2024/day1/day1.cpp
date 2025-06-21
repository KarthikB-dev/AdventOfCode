#include <iostream>
#include <vector>
#include <algorithm>

int main() {
	std::vector<int> l1;
	std::vector<int> l2;

	int n;
	long long distance = 0;
	bool is_l1 = true;
	while (std::cin >> n) {
		if (is_l1) {
			l1.push_back(n);
		}
		else {
			l2.push_back(n);
		}
		is_l1 = !is_l1;
	}	

	std::sort(l1.begin(), l1.end());
	std::sort(l2.begin(), l2.end());

	for (int i = 0; i < l1.size(); i++) {
		distance += std::abs(l1[i] - l2[i]);
	}	
	
	std::cout << distance << std::endl;
}
