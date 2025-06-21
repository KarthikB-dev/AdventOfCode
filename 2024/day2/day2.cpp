#include <bits/stdc++.h>

int main() {
	std::string curr_line = "";
	long long num_safe=0;
	bool incr=false;
	bool decr=false;
	int prev;
	int curr;
	long long iters=0;
	int margin = 0;
	while (std::getline(std::cin, curr_line)) {
		incr=true;
		decr=true;
		iters=0;
		std::stringstream ss(curr_line);
		while ((ss >> curr) && (incr || decr)) {
			if (iters != 0) {
				if (curr > prev) {
					decr = false;
				}
				if (curr < prev) {
					incr = false;
				}
				margin = std::abs(curr - prev);
				std::cout << margin << " ";
				if ((margin > 3) || (margin < 1)) {
					decr = false;
					incr = false;
				}
			}
			iters += 1;
			prev = curr;
		}
        num_safe += (incr || decr) ? 1 : 0;	
		std::cout << std::endl;
	}
	std::cout << num_safe << std::endl;
}
