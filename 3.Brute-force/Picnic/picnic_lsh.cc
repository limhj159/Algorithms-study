#include<iostream>
using namespace std;


bool are_friends[10][10];


int countCases(int stu_num, bool has_pair[10]) {
    // Check all students have pair.
    int i;
    for (i = 0; i < stu_num; i++) {
        if (has_pair[i] == false)
            break;
    }

    // If yes, return 1.
    if (i == stu_num)
        return 1;

    // Else, make pair..
    else {
        int result = 0;
        for (int j = 0; j < stu_num; j++) {
            if (are_friends[i][j] == true && has_pair[j] == false) {
                has_pair[i] = has_pair[j] = true;
                result += countCases(stu_num, has_pair);
                has_pair[i] = has_pair[j] = false;
            }
        }
        return result;
    }
}


int main() {
    int ex_num, stu_num, pair_num;
    bool has_pair[10];

    cin >> ex_num;
    for (int i = 0; i < ex_num; i++) {
        cin >> stu_num >> pair_num;

        memset(are_friends, false, sizeof(are_friends));
        for (int j = 0; j < pair_num; j++) {
            int p1, p2;
            cin >> p1 >> p2;
            are_friends[p1][p2] = are_friends[p2][p1] = true;
        }
        memset(has_pair, false, sizeof(has_pair));

        cout << countCases(stu_num, has_pair);
    }
    return 0;
}

