#include <vector>
#include <iostream>

void printArray(const std::vector<int>& a){
  for(int i = 0; i < a.size(); i++){
    std::cout << a[i] << " ";
  }
  std::cout << std::endl;
}

std::vector<int> mergeSort(const std::vector<int>& array){
	int n = array.size();
	if(n == 1){
		return array;
	}
	std::vector<int> arrayLeft  = mergeSort(std::vector<int>(array.begin(), array.begin() + n/2));
	std::vector<int> arrayRight = mergeSort(std::vector<int>(array.begin() + n/2, array.end()));

	int nLeft  = arrayLeft.size();
	int nRight = arrayRight.size();
	std::vector<int> arrayMerged;
	int i = 0;
	int j = 0;
	while(i < nLeft && j < nRight){
		int l = arrayLeft[i];
		int r = arrayRight[j];
		if(l<r){
			arrayMerged.push_back(l);
			i += 1;
		} else{
			arrayMerged.push_back(r);
			j += 1;
		}
	}
	while(i < nLeft){
		arrayMerged.push_back(arrayLeft[i]);
		i += 1;
	}
	while(j < nRight){
		arrayMerged.push_back(arrayRight[j]);
		j += 1;
	}
	return arrayMerged;
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
  std::vector<int> aSorted = mergeSort(a);
	printArray(aSorted);

	return 0;
}
