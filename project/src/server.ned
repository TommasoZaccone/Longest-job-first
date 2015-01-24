
package progetto;

simple Server
{
    parameters:
        string queuePolicy=default("FIFO");
		int maxJobs;
        @statistic[numJobs](source="numJobs"; record=timeavg);
    gates:
        input in;
        output out;
}
