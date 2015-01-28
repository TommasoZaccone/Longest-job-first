#ifndef __PROGETTO_PRODUCER_H_
#define __PROGETTO_PRODUCER_H_

#include "job_m.h"
#include <queue>
class Queue
{
    public :
        virtual void push(Job* elem)=0;
        virtual void pop ()=0;
        virtual int size()=0;
        virtual bool empty()=0;
        virtual Job* top()=0;
};


class FifoQueue: public Queue
{
    public :
        virtual void push(Job* elem);
        virtual void pop ();
        virtual int size();
        virtual bool empty();
        virtual Job* top();
    private:
        std::queue <Job*> q;

};

class PriorityQueue: public Queue
{
    public :
        virtual void push(Job* elem);
        virtual void pop ();
        virtual int size();
        virtual bool empty();
        virtual Job* top();
    private:
        //compare functor class for stl comparison
        //la compare di libreria vuole una funz x decidere il minoreinternamente alla struttura
        class jobLessThen {
        	public:
				bool operator () (Job *a, Job* b) {
					return a->getServiceT() < b->getServiceT() ;
				}
		} ;
        std::priority_queue <Job* , std::vector<Job*>, jobLessThen> q ;
};

#endif
