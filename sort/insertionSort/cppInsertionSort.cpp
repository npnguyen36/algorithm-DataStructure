#include <stdio.h>
#include <iostream>

using namespace std;

//Declare the prototypes
void PrintArray(int arr[], int length);
void InsertionSort(int arr[], int length);

//Driver method

int main(int argc, char * argv[])
{
	int arr[6] = {5, 4, 12, 81, 7, 6};
	InsertionSort(arr, 6);
	PrintArray(arr, 6);
	return 0;
}

//Insertion Sort function
void InsertionSort(int arr[], int length){
	int i, j, key;
	for (i = 1; i < length; i++) {
		key = arr[i];
		j = i-1;
		while(j >= 0 && arr[j]>key){
			arr[j+1] = arr[j];
			j--;
		}
		arr[j+1] = key;	
	}
}

//Print Array function

void PrintArray(int arr[], int length){
	int j;
	for(j = 0; j < length; j++){
		cout << arr[j] << " ";
	}
	cout << endl;
}
