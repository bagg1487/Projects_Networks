import grpc
import logging
from concurrent import futures

import service_pb2
import service_pb2_grpc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ServiceImplementation(service_pb2_grpc.EventsServiceServicer):
    
    def __init__(self):
        self.events = {}
        self.next_id = 1
    
    def CreateEvent(self, request, context):
        logger.info(f"CreateEvent: {request.name}, {request.location}")
        
        event_id = self.next_id
        self.next_id += 1
        
        event = service_pb2.Event(
            id=event_id,
            name=request.name,
            description=request.description,
            location=request.location,
            timestamp=request.timestamp
        )
        
        self.events[event_id] = event
        
        return service_pb2.CreateEventResponse(
            id=event.id,
            name=event.name,
            description=event.description,
            location=event.location,
            timestamp=event.timestamp,
            status="created"
        )
    
    def GetEvent(self, request, context):
        logger.info(f"GetEvent: id={request.id}")
        
        if request.id not in self.events:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"Event with ID {request.id} not found")
            return service_pb2.GetEventResponse()
        
        event = self.events[request.id]
        
        return service_pb2.GetEventResponse(
            id=event.id,
            name=event.name,
            description=event.description,
            location=event.location,
            timestamp=event.timestamp
        )
    
    def ListEvents(self, request, context):
        logger.info(f"ListEvents: page={request.page}, page_size={request.page_size}")
        
        all_events = list(self.events.values())
        total_count = len(all_events)
        
        page = request.page if request.page > 0 else 1
        page_size = request.page_size if request.page_size > 0 else 10
        
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        
        paginated_events = all_events[start_index:end_index]
        
        return service_pb2.ListEventsResponse(
            events=paginated_events,
            total_count=total_count,
            page=page,
            page_size=page_size
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_EventsServiceServicer_to_server(ServiceImplementation(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logger.info("Server started on port 50051")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()