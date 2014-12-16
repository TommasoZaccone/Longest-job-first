
package progetto;

simple Server
{
    parameters:
        string queuePolicy=default("FIFO");
        @statistic[numJobs](source="numJobs"; record=vector);
    gates:
        input in;
        output out;
}
