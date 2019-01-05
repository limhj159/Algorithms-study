#include<iostream>
#include<algorithm>
using namespace std;


int cutMax(int *board, int first, int last) {
    if (first == last)
        return board[first];

    int middle = int((last + first) / 2);
    int max_area = max(cutMax(board, first, middle), cutMax(board, middle + 1, last));

    int max_h = min(board[middle], board[middle + 1]);
    for (int h = max_h; h > 0; h--) {
        int w = 2;
        for (int i = 1; middle - i >= first && board[middle - i] >= h; i++)
            w++;
        for (int i = 1; middle + 1 + i <= last && board[middle + 1 + i] >= h; i++)
            w++;

        if (max_area < w * h)
            max_area = w * h;
    }
    return max_area;
}


int main() {
    int n;
    cin >> n;

    int board[20000];

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        for (int j = 0; j < num; j++) {
            cin >> board[j];
        }
        cout << cutMax(board, 0, num - 1) << endl;
    }

    return 0;
}
