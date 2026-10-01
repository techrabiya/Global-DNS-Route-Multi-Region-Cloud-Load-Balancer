print("--- Cloud Challenge 4 Initialized: Global Load Balancer 🌐 ---")

def route_global_traffic_packet(routing_metrics):
    print(f"Evaluating user request packet from region: {routing_metrics.get('client_region')}")
    
    latency_ms = routing_metrics.get('latency_ms', 120.0)
    server_status = routing_metrics.get('primary_server_active', True)
    
    try:
        if not server_status:
            print("DNS Alert: Primary regional cluster is offline.")
            return "reroute global traffic instantly to secondary backup cluster"
        
        if latency_ms > 300.0:
            print("DNS Latency Log: High network lag detected on primary route.")
            return "redirect traffic via optimized edge caching proxy"
        else:
            print("DNS Status: Routing path is optimal and direct.")
            return "deliver low-latency response to client successfully"
            
    except Exception as exc:
        print(f"DNS Routing Exception: Unexpected network error -> {exc}")
        return "global traffic routing fallback engaged"

mock_dns_payload = {"client_region": "Asia-Mumbai", "latency_ms": 110.0, "primary_server_active": True}
print("\nRunning Cloud Test 4:")
print(route_global_traffic_packet(mock_dns_payload))
