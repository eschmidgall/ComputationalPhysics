#include <iostream>
#include <stdlib.h>
#include <math.h>
using namespace std;

double function(double pos){
	double funcVal;
	funcVal = pow(pos,2.0)-5.0;
	return funcVal;
}

double derivative(double pos){
	double derVal; 
	derVal = 2.0*pos; 
	return derVal; 
}

double nextStep(double oldPos){
	double newPos; 
	double funcVal; 
	double derVal; 
	funcVal = function(oldPos);
	derVal = derivative(oldPos);
	newPos = oldPos-funcVal/derVal; 
	return newPos; 
}

int main(){
	double val; 
	double thresh;
	bool done; 
	double testVal; 
	int counter; 
	cout<<"Newton's method for x^2-5. Enter a starting value. "<<endl;
	cin>>val; 
	cout<<"Enter a threshold value for accuracy. "<<endl; 
	cin>>thresh; 
	done = false;
	counter = 0; 
	while(! done){
		val = nextStep(val); 
		cout<<"x = "<<val<<endl; 
		testVal = fabs(val-sqrt(5.0)); 
		if(testVal<thresh){
			done = true; 
			cout<<"Final value for x = "<<val<<endl; 
			system("pause"); 
			return 0; 
		}
		if(counter>10000){
			done = true; 
			cout <<"Over 10000 steps. Not reaching accuracy for threshold "<<thresh<<endl; 
			system("pause"); 
			return 0; 
		}
		counter++; 
	}
	return 0; 
}


		
