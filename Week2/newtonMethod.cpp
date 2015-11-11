#include <iostream>
#include <stdlib.h>
#include <math.h>
using namespace std;

float roundf(float x)
{
   return x >= 0.0f ? floorf(x + 0.5f) : ceilf(x - 0.5f);
}

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

int getPrecision(double thresh){
	int precision; 
	precision = abs(log10(thresh)) ; 
	return precision; 
}
		

int main(){
	double val; 
	double thresh;
	bool done; 
	double testVal; 
	int counter; 
	int precision; 
	
	cout<<"Newton's method for x^2-5. Enter a starting value. "<<endl;
	cin>>val; 
	cout<<"Enter a threshold value for accuracy. "<<endl; 
	cin>>thresh; 
	precision = getPrecision(thresh); 
	cout<<"Precision is "<<precision<<endl;
	done = false;
	counter = 0; 
	while(! done){
		val = nextStep(val); 
		printf("x= %12.*f \n",precision,val); 
		testVal = fabs(val-sqrt(5.0)); 
		if(testVal<thresh){
			done = true; 
			printf("Final value for x = %12.*f \n",precision, val); 
			printf("For reference, sqrt(5.0) is %12.*f \n", precision, sqrt(5.0));
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


		
