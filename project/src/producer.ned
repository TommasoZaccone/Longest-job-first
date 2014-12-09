 

package progetto;


simple Producer
{
	parameters:
	     @statistic[interArrivalT](source="interArrivalT"; record=vector);
	     @statistic[serviceT](source="serviceT"; record=vector);

	     volatile double interArrivalDist=default(exponential(2));
	     volatile double serviceDist=default(exponential(1));
    gates:
        output out;
}
