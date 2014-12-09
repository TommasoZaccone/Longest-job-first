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
    iaMean=par("iaMean");
    stMean=par("stMean");
    s_interArrival = registerSignal("interArrival");
    s_serviceT = registerSignal("serviceT");
    scheduleAt(simTime(),new cMessage);
}

void Producer::handleMessage(cMessage *msg)
{
    Job *mex = new Job;
    simtime_t interArrival = exponential(iaMean,0);
    emit(s_interArrival,interArrival);
    simtime_t serviceT = exponential(stMean,1);
    emit(s_serviceT,serviceT);
    mex->setServiceT(serviceT);
    mex->setId(id++);
    mex->setKind(JOB);
    send(mex,"out");
    scheduleAt(simTime()+interArrival,msg);


}
