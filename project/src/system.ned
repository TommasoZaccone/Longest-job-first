
package progetto;

module System
{
    gates:
        input in;
    submodules:
        server : Server;
        stats: Stats;
        connections:
            in-->server.in;
            server.out --> stats.in;
}
