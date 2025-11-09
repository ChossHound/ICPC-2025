#include <iostream>
#include <string>
using namespace std;

int cardinalToDeg(const string& c) {
    if (c == "N") return 0;
    if (c == "NE") return 45;
    if (c == "E") return 90;
    if (c == "SE") return 135;
    if (c == "S") return 180;
    if (c == "SW") return 225;
    if (c == "W") return 270;
    if (c == "NW") return 315;
    return -1;
}

string degToDirection(int deg) {
    if (deg == 0) return "Keep going straight";
    if (abs(deg) == 180) return "U-turn";
    if (deg > 180)
        return "Turn " + to_string(360 - deg) + " degrees port";
    return "Turn " + to_string(deg) + " degrees starboard";
}

int main() {
    string heading;
    string desired;

    cin >> heading >> desired;

    int going = cardinalToDeg(heading);
    int fin = (cardinalToDeg(desired) - going) % 360;

    if (fin < 0) fin += 360;

    cout << degToDirection(fin);
    return 0;
}