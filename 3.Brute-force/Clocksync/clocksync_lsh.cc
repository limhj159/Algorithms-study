#include<iostream>
#include<algorithm>
using namespace std;

const int INF = 987654321;

const bool is_connected[10][16] = {
    { 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
    { 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0 },
    { 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1 },
    { 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 },
    { 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0 },
    { 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 },
    { 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 },
    { 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1 },
    { 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
    { 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0 }
};


void pressSwitch(int switch_idx, int press_num, int* clocks) {
    for (int i = 0; i < 16; i++) {
        if (is_connected[switch_idx][i])
            clocks[i] += 3 * press_num;
    }
}


int findOpt(int clocks[16], int switch_idx) {
    if (switch_idx == 10) {
        for (int i = 0; i < 16; i++) {
            if (clocks[i] % 12 != 0)
                return INF;
        }
        return 0;
    }
    else {
        int opt = INF;
        for (int i = 0; i < 4; i++) {
            pressSwitch(switch_idx, i, clocks);
            opt = min(opt, i + findOpt(clocks, switch_idx + 1));
            pressSwitch(switch_idx, -i, clocks);
        }

        if (switch_idx == 0 && opt == INF)
            return -1;
        else
            return opt;
    }    
}


int main() {
    int c;
    cin >> c;

    for (int i = 0; i < c; i++) {
        int clocks[16];
        for (int j = 0; j < 16; j++) {
            cin >> clocks[j];
        }
        cout << findOpt(clocks, 0) << endl;
    }
    return 0;
}

