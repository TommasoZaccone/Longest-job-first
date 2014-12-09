//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with this program.  If not, see http://www.gnu.org/licenses/.
// 

#include "server.h"
#include "define.h"

Define_Module(Server);

void Server::initialize()
{
    currentJob=0;
    timer=new cMessage; //in caso da deallocare con la finish()
    stats_timer= new cMessage;
    stats_timer->setKind(STATS_TIMER);
    s_numJobs = registerSignal("numJobs");
    //schedulo il timer per le statistiche
    scheduleAt(simTime()+0.1,stats_timer);
}

void Server::handleMessage(cMessage *msg)
{

    switch(msg->getKind()) {

            case TIMER :
                //ho gia aspettato lenght del precedente top cio� currentJob
                handleTimer(msg);
                        break;

            case JOB :
                //mi arriva un job nuovo
                handleJob(msg);
                        break;
            case STATS_TIMER :
                //conto i pacchetti in coda
                int numJobs = q.size();
                emit(s_numJobs,numJobs);
                scheduleAt(simTime()+0.1,stats_timer);
                break;
    }
}

void Server::handleTimer(cMessage* msg){
    Job *mex = check_and_cast<Job*>(currentJob);
    mex->setExitSystemT(simTime());
    send(currentJob,"out");
    if(q.empty()) {
        currentJob=0;
    }
    else {
        currentJob=q.top();
        q.pop();
        scheduleAt(currentJob->getServiceT() + simTime(),timer);
    }
}

void Server::handleJob(cMessage* msg){
    Job *mex = check_and_cast<Job*>(msg);
    mex->setEnterSystemT(simTime());
    if(currentJob==0) {
        currentJob=mex;
        scheduleAt(currentJob->getServiceT() + simTime(),timer);
    }
    else
        q.push(mex);
}
