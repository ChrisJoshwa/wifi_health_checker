import argparse
import pandas as pd
from utils.ssh_utils import ssh_connect
from utils.parser import parse_output
from concurrent.futures import ThreadPoolExecutor

def check_device(ip, username, password):
    ssh_client = ssh_connect(ip, username, password)
    if not ssh_client:
        return {"IP": ip, "Status": "Connection Failed"}
    
    # Commands to run
    uptime_cmd = "uptime -p"
    cpu_cmd = "top -bn1 | grep 'Cpu(s)'"
    mem_cmd = "free -m"
    process_cmd = "ps | grep 'wifidog' | grep -v grep"

    results = {}
    results["IP"] = ip
    results["Uptime"] = parse_output(ssh_client, uptime_cmd)
    results["CPU_Usage"] = parse_output(ssh_client, cpu_cmd)
    results["Memory_Usage"] = parse_output(ssh_client, mem_cmd)
    results["Process_Status"] = "Running" if parse_output(ssh_client, process_cmd) else "Missing"

    ssh_client.close()
    return results

def main():
    parser = argparse.ArgumentParser(description="WiFi Access Point Health Checker")
    parser.add_argument("--device-list", required=True, help="CSV file with IP, username, password")
    parser.add_argument("--output", default="results.csv", help="Output CSV file")
    args = parser.parse_args()

    devices = pd.read_csv(args.device_list)
    all_results = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(check_device, row["ip"], row["username"], row["password"])
            for _, row in devices.iterrows()
        ]
        for future in futures:
            all_results.append(future.result())

    pd.DataFrame(all_results).to_csv(args.output, index=False)
    print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()

