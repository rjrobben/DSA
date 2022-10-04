
/*
ID: rjrobbe1
TASK: ride
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int compute(string str){
	int sum =1;
	for(char& c : str){
		int tmp = int(c) - 64;
		sum*=tmp;
	}
	return sum%47;
}

int main(){
	ofstream fout ("ride.out");
	ifstream fin ("ride.in");

	string a,b;
	fin >> a >> b;
	cout <<a << " " << b << "\n" ;
	if (compute(a) == compute(b)){
		fout << "GO" << endl;
	}else{
		fout << "STAY" << endl;
	}
	return 0;
}




