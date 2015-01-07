
package progetto;


simple Stats
{
    parameters:
        @statistic[queueT](source="queueT"; record=vector);
    	@statistic[responseT](source="responseT"; record=vector);
        gates:
        input in;
}
