log_line = "Nov 12 09:41:23 web01 sshd[4821]: Failed password for invalid user admin from 203.0.113.45 port 51234 ssh2"
info = log_line.split()

timestamp = f"{info[0]} {info[1]} {info[2]}"
hostname = info[3]

process_name = info[4].split("[")[0]
process_id = info[4].split("[")[1]
clean_process_id = int(process_id.strip("]:"))

user = info[-6]
source_ip = info[-4]
port = int(info[-2])
is_failed_login = "Failed password" in log_line

print(f"Parsed {len(info)} fields")
print(f"timestamp   :{timestamp}")
print(f"Hostname    :{hostname}")
print(f"process     :{process_name} (pid {clean_process_id})")
print(f"User        :{user}")
print(f"Source IP   :{source_ip}")
print(f"Port        :{port}")
print (f"Failed     :{is_failed_login}")