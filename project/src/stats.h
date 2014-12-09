
#ifndef __PROGETTO_SERVER_H_
#define __PROGETTO_SERVER_H_

#include <omnetpp.h>


class Stats : public cSimpleModule
{
    private:
    simsignal_t s_serviceT;
    simsignal_t s_queueT;
    simsignal_t s_responseT;


  protected:
    virtual void initialize();
    virtual void handleMessage(cMessage *msg);
};

#endif
