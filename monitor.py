import os 
from datetime import datetime

directory = r"C:\Users\kamas\OneDrive\Desktop\Test"

def monitor_directory(directory, log_file="log.txt"): 
    try: 
        with open(log_file, "a") as log:
            for filename in os.listdir(directory):
                filepath = os.path.join(directory, filename)
                if os.path.isfile(filepath):
                    size_kb = os.path.getsize(filepath) / 1024
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    entry = f"{filename} | {size_kb: .2f} KB | {timestamp}\n"
                    log.write(entry)
                    print(entry.strip())
        print(f"\nScan complete. Results saved to {log_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_to_monitor = r"C:\Users\kamas\OneDrive\Desktop\Test"
    monitor_directory(directory_to_monitor)