
package progetto;

simple Server
{
    parameters:
        @statistic[numJobs](source="numJobs"; record=vector);
    gates:
        input in;
        output out;
}
