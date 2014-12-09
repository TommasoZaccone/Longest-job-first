package progetto;

network Network {
    submodules:
    producer: Producer;
	system : System;
	connections:
	    producer.out --> system.in;
}