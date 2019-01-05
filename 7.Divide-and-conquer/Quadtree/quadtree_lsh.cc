#include<iostream>
#include<string>
#include<algorithm>
using namespace std;


string turnOver(string tree, int* index) {
    char node = tree.at(*index);
    if (node == 'w' || node == 'b') {
        *index += 1;
        return string(1, node);
    }
    else {
        *index += 1;
        string a[4];
        for (int i = 0; i < 4; i++) {
            a[i] = turnOver(tree, index);
        }
        return "x" + a[2] + a[3] + a[0] + a[1];
    }
}


int main() {
    int c;
    cin >> c;

    for (int i = 0; i < c; i++) {
        string tree;
        cin >> tree;

        int index = 0;
        int* index_addr = &index;
        cout << turnOver(tree, index_addr) << endl;
    }

    /*
    int index = 0;
    int* index_addr = &index;
    cout << turnOver("w", index_addr) << endl;
    index = 0;
    cout << turnOver("xbwwb", index_addr) << endl;
    index = 0;
    cout << turnOver("xbwxwbbwb", index_addr) << endl;
    index = 0;
    cout << turnOver("xxwwwbxwxwbbbwwxxxwwbbbwwwwbb", index_addr)<<endl;
    */
    return 0;
}
