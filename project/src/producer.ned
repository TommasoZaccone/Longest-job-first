 

package progetto;


simple Producer
{
	parameters:
	     @statistic[interArrival](source="interArrival"; record=vector);
	     @statistic[serviceT](source="serviceT"; record=vector);
	     double iaMean @unit(s);
	     double stMean @unit(s);
	     string iaDist=default("exp");
	     string stDist=default("exp");
        gates:
        output out;
}
