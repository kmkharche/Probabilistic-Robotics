#include <iostream>
#include <ctime>

using namespace std;

/*
	Pss=P(Day2=sunny|Day1=sunny)
	Pcs=P(Day2=cloudy|Day1=sunny)
	Prs=P(Day2=rainy|Day1=sunny)

	Similarly for the other cases
*/

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

	//If day1 is sunny
	double Ps=1;
	double Pc=0;
	double Pr=0;

	//Standard Distribution
	///For standard distribution i.e. steady state,  use a large number of days
	int day = 10000;

	for (int i=1;i<day;++i)
	{
		double PsNew = Pss*Ps + Psc*Pc + Psr*Pr;
		double PcNew = Pcs*Ps + Pcc*Pc + Pcr*Pr;
		double PrNew = Prs*Ps + Prc*Pc + Prr*Pr;

		Ps = PsNew;
		Pc = PcNew;
		Pr = PrNew;
	}
	cout << "The standard distribution probability that a day is sunny is " << Ps << "." << endl;
	cout << "The standard distribution probability that a day is cloudy is " << Pc << "." << endl;
	cout << "The standard distribution probability that a day is rainy is " << Pr << "." << endl;

	return 0;
}