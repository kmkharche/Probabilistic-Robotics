#include <iostream>
#include <ctime>

using namespace std;

/*
	Pss=P(Day2=sunny|Day1=sunny)
	Pcs=P(Day2=cloudy|Day1=sunny)
	Prs=P(Day2=rainy|Day1=sunny)

	Similarly for the other cases
*/

double getRandomNumber(int min, int max)
{
	static const double fraction = 1.0 / (static_cast<double>(RAND_MAX) + 1.0);  // static used for efficiency, so we only calculate this value once
	// evenly distribute the random number across our range
	return (rand() * fraction * (max - min) + min);
}

int main()
{

	srand(static_cast<unsigned int>(time(0)));

	double Pss = 0.8;
	double Pcs = 0.2;
	double Prs = 0;
	double Psc = 0.4;
	double Pcc = 0.4;
	double Prc = 0.2;
	double Psr = 0.2;
	double Pcr = 0.6;
	double Prr = 0.2;

	int day = 0;
	while (day<=0)
	{
		cout << "Enter the number of days for which you want the weather prediction: ";
		cin >> day;
	}

	//If day1 is sunny
	double Ps=1;
	double Pc=0;
	double Pr=0;

	cout << "sunny ";

	for (int i=1;i<day;++i)
	{
		double PsNew = Pss*Ps + Psc*Pc + Psr*Pr;
		double PcNew = Pcs*Ps + Pcc*Pc + Pcr*Pr;
		double PrNew = Prs*Ps + Prc*Pc + Prr*Pr;

		Ps = PsNew;
		Pc = PcNew;
		Pr = PrNew;

		double sample = getRandomNumber(0,1);
		if (sample < Ps)
			cout << "sunny ";
		else if(sample < (Ps+Pc))
			cout << "cloudy ";
		else
			cout << "rainy ";

	}
	
	cout << endl;

	return 0;
}