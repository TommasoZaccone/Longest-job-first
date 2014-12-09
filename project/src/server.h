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

#ifndef __PROGETTO_QUEUE_H_
#define __PROGETTO_QUEUE_H_

#include <omnetpp.h>
#include <queue>
#include "job_m.h"

//compare functor class for stl comparison
//la compare di libreria vuole una funz x decidere il minoreinternamente alla struttura
class jobLessThen {
public:
   bool operator () (Job *a, Job* b) {

      return a->getServiceT() < b->getServiceT() ;
      }

    } ;

class Server : public cSimpleModule
{
private:
    Job* currentJob;
    cMessage* timer;
    cMessage* stats_timer;
    simsignal_t s_numJobs;

    std::priority_queue <Job* , std::vector<Job*>, jobLessThen> q ;

    void handleTimer(cMessage* msg);
    void handleJob(cMessage*msg);
  protected:
    virtual void initialize();
    virtual void handleMessage(cMessage *msg);
};

#endif
