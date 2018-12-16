#include<iostream>
using namespace std;


const int neighbor[4][2][2] = { 
    { { -1, 1 },{ 0, 1 } },
    { { 0, 1 },{ 1, 0 } },
    { { 1, 0 },{ 1, 1 } },
    { { 0, 1 },{ 1, 1 } } 
};


int countCases(int w, int h, bool game_board[][20]) {
    // Check all blocks are black.
    int x, y;
    bool flag = false;
    for (y = 0; y < h; y++) {
        for (x = 0; x < w; x++) {
            if (game_board[x][y]) {
                flag = true;
                break;
            }
        }
        if (flag) {
            break;
        }
    }

    // If yes, return 1.
    if (!flag) {
        return 1;
    }

    // Else, cover white blocks..
    else {
        int x1, y1, x2, y2;
        int result = 0;
        for (int k = 0; k < 4; k++) {
            x1 = x + neighbor[k][0][0];
            y1 = y + neighbor[k][0][1];
            x2 = x + neighbor[k][1][0];
            y2 = y + neighbor[k][1][1];
            if (x1 >= 0 && x1 < w && y1 >= 0 && y1 < h
                && x2 >= 0 && x2 < w && y2 >= 0 && y2 < h
                && game_board[x1][y1] && game_board[x2][y2]) {
                game_board[x][y] = game_board[x1][y1] = game_board[x2][y2] = false;
                result += countCases(w, h, game_board);
                game_board[x][y] = game_board[x1][y1] = game_board[x2][y2] = true;
            }
        }
        return result;
    }
}


int main() {
    int c, h, w;
    bool game_board[20][20];

    cin >> c;
    cin >> h >> w;

    for (int i = 0; i < c; i++) {
        memset(game_board, false, sizeof(game_board));
        for (int j = 0; j < h; j++) {
            for (int k = 0; k < w; k++) {
                char block;
                cin >> block;
                if (block == '.')
                    game_board[k][j] = true; 
            }
        }
        cout << countCases(w, h, game_board);
    }
    return 0;
}

