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
#include <string>

Define_Module(Server);

void Server::initialize()
{
    std::string qPolicy = par("queuePolicy");
    if(qPolicy=="LJF"){
        q= new PriorityQueue;
    }
    else{
        q=new FifoQueue;
	}
    currentJob=0;
    timer=new cMessage; //in caso da deallocare con la finish()
    s_numJobs = registerSignal("numJobs");
	minTime = par("minTime");
}

void Server::handleMessage(cMessage *msg)
{

	switch(msg->getKind()) {

		case TIMER :
			//service time ended
			handleTimer(msg);
			break;
		case JOB :
			//new job
			handleJob(msg);
			break;
	}
	int numJobs= q->size()+(currentJob!=0);
	emit(s_numJobs,numJobs);
}

void Server::handleTimer(cMessage* msg){
    currentJob->setExitSystemT(simTime());
    send(currentJob,"out");
    if(q->empty()) {
        currentJob=0;
		if(simTime()>minTime){
			endSimulation();
		}
    }
    else {
        currentJob=q->top();
        q->pop();
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
    else{
        q->push(mex);
	}
}

void Server::finish() {
    cancelEvent(timer);
    delete timer;
    if(currentJob!=0){
        delete currentJob;
	}
    EV<<"ELEMENTS IN QUEUE "<<q->size()<<endl;
    while(!q->empty()){
        delete q->top();
        q->pop();
	}
}

