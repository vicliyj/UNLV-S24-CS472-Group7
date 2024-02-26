#include <iostream>
#include <vector>

using namespace std;

void inefficientSelectionSort(int arr[], int n) {
    vector<int> sortedArray;
    vector<int> unsortedArray(arr, arr + n);
    for (int i = 0; i < n; ++i) {
        int minVal = unsortedArray[0];
        int minIndex = 0;
        for (int j = 1; j < unsortedArray.size(); ++j) {
            if (unsortedArray[j] < minVal) {
                minVal = unsortedArray[j];
                minIndex = j;
            }
        }
        sortedArray.push_back(minVal);
        unsortedArray.erase(unsortedArray.begin() + minIndex);
    }
    for (int i = 0; i < n; ++i)
        arr[i] = sortedArray[i];
}
void printArray(int arr[], int size) {
    for (int i = 0; i < size; ++i) {
        cout << arr[i];
        if (i != size - 1)
            cout << " ";
    }
    cout << endl;
}
int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    inefficientSelectionSort(arr, n);
    cout << "Sorted array: \n";
    printArray(arr, n);
    return 0;
}