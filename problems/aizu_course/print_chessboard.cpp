#include <iostream>
using namespace std;

int main() {
    int h,w;

    while (cin >> h >> w) {
        if (h == 0 && w == 0) {break;}

        for (int i = 1; i <= h ; i++) {
            for ( int j =1 ; j <= w ; j++) {
                // if row = odd numer 
                if ( i%2 == 1 ) {
                    // if column = odd number
                    if ( j%2 == 1 ) {
                        cout << "#";
                    } else {
                        cout << ".";
                    }
                } else {
                    // if column = odd number
                    if ( j%2 == 1 ) {
                        cout << ".";
                    } else {
                        cout << "#";
                    }
                }
            }
            cout << "\n";
        }
        cout << "\n";
    }
}