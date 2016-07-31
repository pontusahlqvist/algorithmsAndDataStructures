#include <vector>
#include <iostream>

void printArray(const std::vector<int>& a){
  for(int i = 0; i < a.size(); i++){
    std::cout << a[i] << " ";
  }
  std::cout << std::endl;
}

//sorts in place, but here we return the sorted array to keep interface consistency with mergeSort
std::vector<int> insertionSort(std::vector<int>& array){
	std::vector<int> sortedArray(array.begin(), array.end());
	for(int i = 0; i < sortedArray.size(); i++){
		int j = i - 1;
		int key = sortedArray[i];
		while(j >= 0 && sortedArray[j] > key){
			sortedArray[j+1] = sortedArray[j];
			j -= 1;
		}
		sortedArray[j+1] = key;
	}
	return sortedArray;
}

int main(){
	//Create the vector to be sorted
	std::vector<int> a;
	a.push_back(4);
	a.push_back(6);
	a.push_back(2);
	a.push_back(8);
	a.push_back(5);
	a.push_back(6);
	a.push_back(1);

	printArray(a);
	std::vector<int> aSorted = insertionSort(a);
	printArray(aSorted);

	return 0;
}
