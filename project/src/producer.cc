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

#include "producer.h"
#include <job_m.h>
#include "define.h"

Define_Module(Producer);

void Producer::initialize()
{
    id=0;
    timer = new cMessage;
	s_interArrivalT = registerSignal("interArrivalT");
    s_serviceT = registerSignal("serviceT");
    scheduleAt(simTime(),timer);
}

void Producer::handleMessage(cMessage *msg)
{
    Job *mex = new Job;

    simtime_t interArrivalT = par("interArrivalDist");
    emit(s_interArrivalT,interArrivalT);
    
	simtime_t serviceT = par("serviceDist");
    emit(s_serviceT,serviceT);
    
	mex->setServiceT(serviceT);
    mex->setId(id++);
    mex->setKind(JOB);
    send(mex,"out");
    
	scheduleAt(simTime()+interArrivalT,msg);


}

void Producer::finish(){
    cancelEvent(timer);
    delete timer;
}

