#include <iostream>
#include <cmath>
#include <fstream>

using namespace std; 

int enumerateRandWalk(int x, int N){
	if((N==1)&&(x==0)){
		return 0; 
	}
	else if((N==1)&&(abs(x)==1)){
		return 1; 
	}
	else if(abs(x)>N){
		return 0; 
	}
	else{
		return enumerateRandWalk(x-1,N-1)+enumerateRandWalk(x+1,N-1); 
	}
}

int main(){
	int N; 
	int x;
	int numWalks; 
	ofstream f; 
	f.open("randomWalks.txt"); 
	f<<"n,x,numWalks\n"; 
	cout<<"Please input the maximum value for N ="<<endl;
	cin>>N;
	for(int n=1; n<N+1;n++){
		cout<<"n="<<n<<endl;
		for(int x=-1*n; x<n+1; x++){
			numWalks = enumerateRandWalk(x,n); 
			f<<n<<","<<x<<","<<numWalks<<endl;
		}
	}
	f.close(); 
	cout<<"Results for walks up to N="<<N<<" steps written to file randomWalks.txt."<<endl; 
	system("pause"); 
	return 0; 
}
