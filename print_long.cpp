#include <iostream>
#include <string>

using namespace std;

int main() {
    string str = "";

    for (int i = 0; i < 500; i++) {
        for (int j = 0; j < 500; j++) {
            str += "0 ";
        }

        str += "\n";
    }

    cout << str;

    return 0;
}