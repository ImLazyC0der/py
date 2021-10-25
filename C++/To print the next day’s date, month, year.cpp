#include <iostream>
using namespace std;

int main()
{
	int d, m, y;
	cout << "Enter today's date in the format:DD MM YYYY\n";
	cin >> d >> m >> y;
	if (d > 0 && d < 28)	//checking for day from 0 to 27
		d += 1;
	if (d == 28)
	{
		if (m == 2)	//checking for february
		{
			if ((y % 400 == 0) || (y % 100 != 0 || y % 4 == 0))	//leap year check in case of feb
			{
				d = 29;
			}
			else
			{
				d = 1;
				m = 3;
			}
		}
		else	//when its not feb
			d += 1;
	}
	if (d == 29)	//last day check for feb
	{
		if (m == 2)
		{
			d = 1;
			m = 3;
		}
		else
			d += 1;
	}
	if (d == 30)	//last day check for april,june,September,November
	{
		if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12)
			d += 1;
		else
		{
			d = 1;
			m += 1;
		}
	}
	if (d == 31)	//last day of the month
	{
		d = 1;
		if (m == 12)	//checking for last day of the year
		{
			y += 1;
			m = 1;
		}
		else
			m += 1;
	}
	cout << "Tomorrow's date:\n";
	if (d < 10)	//checking if day needs to be preceded by 0
	{
		cout << "0" << d << " ";
	}
	else
		cout << d << " ";
	if (m < 10)	//checking if month needs to be preceded by 0
	{
		cout << "0" << m << " ";
	}
	else
		cout << m << " ";
	cout << y;
	return 0;
}
