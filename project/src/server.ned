
package progetto;

simple Server
{
    parameters:
        string queuePolicy=default("FIFO");
		double minTime;
        @statistic[numJobs](source="numJobs"; record=timeavg);
    gates:
        input in;
        output out;
}
