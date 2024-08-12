import socket
import concurrent.futures
def get_sdomain_prefixes():
    sdomain_prefixes = []
    with open("sdomains.txt", 'r') as domains_file:
        for line in domains_file:
            sdomain_prefixes.append(line.strip())  
        
    return sdomain_prefixes

def check_subdomain(subdomain_name):
    try:
        ip_addr = socket.gethostbyname(subdomain_name)
        print(f"Subdomain found: {subdomain_name} -> IP: {ip_addr}")
        return subdomain_name
    except socket.gaierror:
        print(f"Subdomain not found: {subdomain_name}")
        return None

def try_subdomainlist(domain_name):
    prefixes = get_sdomain_prefixes()
    valid_subdomains = []
  
    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
        futures = {executor.submit(check_subdomain, f"{prefix}.{domain_name}"): prefix for prefix in prefixes}     
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                valid_subdomains.append(result)
            
    return valid_subdomains

def main():
    domain = input("Enter the domain name (e.g., example.com): ")
    valid_domains = try_subdomainlist(domain)
    print("Valid subdomains:")
    print(valid_domains)
    print("Count:", len(valid_domains))

if __name__ == "__main__":
    main()
