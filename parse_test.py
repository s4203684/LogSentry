log_line = "Nov 12 09:41:23 web01 sshd[4821]: Failed password for invalid user admin from 203.0.113.45 port 51234 ssh2"
info = log_line.split()
print(len(info))
for word in info:
    print(word)