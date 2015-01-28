
#include "stats.h"
#include "job_m.h"

Define_Module(Stats);

void Stats::initialize()
{
	s_queueT=registerSignal("queueT");
	s_responseT=registerSignal("responseT");

}

void Stats::handleMessage(cMessage *msg)
{
    Job *mex = check_and_cast<Job*>(msg);
    simtime_t serviceT= mex->getServiceT();
    simtime_t responseT=mex->getExitSystemT()-mex->getEnterSystemT();
    simtime_t queueT=responseT-serviceT;
    emit(s_queueT,queueT);
    emit(s_responseT,responseT);
    delete mex;
}
