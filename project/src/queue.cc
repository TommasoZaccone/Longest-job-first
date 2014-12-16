#include "queue.h"

void FifoQueue::push(Job* elem) {
        q.push(elem);
}

void FifoQueue::pop(){
    q.pop();
}

Job* FifoQueue::top(){
    return q.front();
}

bool FifoQueue::empty() {
    return q.empty();
}

int FifoQueue::size(){
   return q.size();

}

void PriorityQueue::push(Job* elem) {
        q.push(elem);
}

void PriorityQueue::pop(){
    q.pop();
}

Job* PriorityQueue::top(){
    return q.top();
}

bool PriorityQueue::empty() {
    return q.empty();
}

int PriorityQueue::size(){
   return q.size();

}
