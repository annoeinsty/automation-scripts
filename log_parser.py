# Parses log file and prints error lines
def parse_logs(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if "ERROR" in line or "WARN" in line:
                print(line.strip())

if __name__ == "__main__":
    parse_logs("app.log")
