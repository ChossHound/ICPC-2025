#include <algorithm>
#include <iostream>
#include <vector>

bool comp(const int& a, const int& b) {
    std::cout << "? " << a << " " << b << std::endl;
    std::cout.flush();
    int result;
    std::cin >> result;
    return result == a;
}

int main() {
    int numApplicants, numToAdvance;
    std::cin >> numApplicants >> numToAdvance;
    std::vector<int> poets;
    for (int i = 1; i <= numApplicants; i++) poets.push_back(i);

    std::nth_element(poets.begin(), poets.begin() + numToAdvance, poets.end(), comp);

    std::cout << "! ";
    for (int i = 0; i < numToAdvance; i++) std::cout << " " << poets[i];
}
