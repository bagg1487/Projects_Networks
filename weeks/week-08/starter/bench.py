import time
import requests
import grpc
import service_pb2
import service_pb2_grpc

PROJECT_CODE = "users-s14"

def run_rest_bench():
    print("Starting REST benchmark...")
    
    for _ in range(100):
        try:
            requests.get("http://localhost:8000/items", timeout=5)
        except Exception as e:
            print(f"REST warmup error: {e}")
            return
    
    print("Running REST benchmark (1000 requests)...")
    start = time.time()
    
    for i in range(1000):
        try:
            response = requests.get("http://localhost:8000/items", timeout=5)
            if i % 100 == 0:
                print(f"REST: {i} requests completed")
        except Exception as e:
            print(f"REST request {i} failed: {e}")
    
    end = time.time()
    total_time = end - start
    avg_time = (total_time / 1000) * 1000
    rps = 1000 / total_time
    
    print(f"\n=== REST Results ===")
    print(f"Total time: {total_time:.4f} sec")
    print(f"Average per request: {avg_time:.2f} ms")
    print(f"Requests per second: {rps:.2f} req/sec")
    print(f"===================\n")

def run_grpc_bench():
    print("Starting gRPC benchmark...")
    
    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = service_pb2_grpc.MyServiceStub(channel)
        
        for _ in range(100):
            try:
                stub.MyMethod(service_pb2.MyRequest(id="1"))
            except Exception as e:
                print(f"gRPC warmup error: {e}")
                return
        
        print("Running gRPC benchmark (1000 requests)...")
        start = time.time()
        
        for i in range(1000):
            try:
                stub.MyMethod(service_pb2.MyRequest(id="1"))
                if i % 100 == 0:
                    print(f"gRPC: {i} requests completed")
            except Exception as e:
                print(f"gRPC request {i} failed: {e}")
        
        end = time.time()
        total_time = end - start
        avg_time = (total_time / 1000) * 1000
        rps = 1000 / total_time
        
        print(f"\n=== gRPC Results ===")
        print(f"Total time: {total_time:.4f} sec")
        print(f"Average per request: {avg_time:.2f} ms")
        print(f"Requests per second: {rps:.2f} req/sec")
        print(f"===================\n")
        
    except Exception as e:
        print(f"gRPC benchmark failed: {e}")
    finally:
        channel.close()

if __name__ == "__main__":
    run_rest_bench()
    run_grpc_bench()