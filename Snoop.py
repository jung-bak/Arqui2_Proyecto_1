class Subscriber:
    def __init__(self, processor):
        self.processor = processor
        self.processorList = []
        self.memory = processor.memory
        self.identifier = processor.identifier

    def update(self,senderId,message, direccionMemoria):
        self.moesi(self.processorList[senderId], self.processor, self.memory, message, direccionMemoria)
        return

    def moesi(self, senderProcessor, processor, memory, message, direccionMemoria):
        if (message == "read miss"):
            if(processor.estadoCacheGet(direccionMemoria) == "E"):
                senderProcessor.writeCache(direccionMemoria, processor.readCache(direccionMemoria))
                senderProcessor.estadoCacheSet(direccionMemoria,"S")
                processor.estadoCacheSet(direccionMemoria,"S")
            elif(processor.estadoCacheGet(direccionMemoria) == "S"):
                senderProcessor.writeCache(direccionMemoria, processor.readCache(direccionMemoria))
                senderProcessor.estadoCacheSet(direccionMemoria,"S")
            elif(processor.estadoCacheGet(direccionMemoria) == "M"):
                senderProcessor.writeCache(direccionMemoria, processor.readCache(direccionMemoria))
                senderProcessor.estadoCacheSet(direccionMemoria, "S")
                processor.estadoCacheSet(direccionMemoria,"O")
        elif (message == "write miss"):
            if(processor.estadoCacheGet(direccionMemoria) != "I"):
                processor.estadoCacheSet(direccionMemoria,"I")
        elif (message == "write hit"):
            if(processor.estadoCacheGet(direccionMemoria) != "I"):
                processor.estadoCacheSet(direccionMemoria,"I")
        return


class Publisher:
    def __init__(self,identifier):
        self.identifier = identifier
        self.subscriber = []

    def register(self,subscriberName):
        self.subscriber.append(subscriberName)
    
    def broadcast(self, senderId, message, direccionMemoria):
        for subscriber in self.subscriber:
            subscriber.update(senderId,message,direccionMemoria)

