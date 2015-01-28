
package progetto;


simple Stats
{
    parameters:
        @statistic[queueT](source="queueT"; record=vector,mean);
    	@statistic[responseT](source="responseT"; record=vector,mean);
    gates:
        input in;
}
