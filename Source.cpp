#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
int main()
{
	cout << "hello";
	ifstream fin;
	fin.open("Matrix-Transpose_InputForSubmission_1.txt");
	int a[500][500];
		//vectors of vectors;
	
	bool bo = true, go = true;
	string input;
	int num;
	int counterNum = 0, counterLine = 0, numPerLine = 0;
	while (!fin.eof())
	{
		getline(fin, input);
		counterLine++;
	}
	fin.close();
	fin.open("Matrix-Transpose_InputForSubmission_1.txt");
	while (!fin.eof())
	{
		fin >> num;
		counterNum++;
	}
	fin.close();
	//cout << counterLine << endl << counterNum;
	numPerLine = counterNum / counterLine;
	fin.open("Matrix-Transpose_InputForSubmission_1.txt");

	for (int i = 0; i < counterLine; i++)
	{
		for (int j = 0; j < numPerLine; j++)
		{
			fin >> a[i][j];
		}
	}
	fin.close();
	ofstream fout;
	fout.open("outputfile.txt");
	for (int j = 0; j < numPerLine; j++)
	{
		for (int i = 0; i < counterLine; i++)
		{
			fout << a[i][j] << " ";
		}
		fout << endl;
	}
	fout.close();


	return 0;
}