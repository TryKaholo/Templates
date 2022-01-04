import socket
import json
import logging
from datetime import datetime
import sys
import pandas as pd
import os

print("starting to send data to Elastic search")
# Create TCP/IP socket
print("Creating TCP/IP socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
message = []
try:
    # Connect to port where server is running
    file_name = sys.argv[1]
    file_type = os.path.splitext(file_name)[1][1:]
    counter = 0
    server_address = ('localhost', 50504)
    sock.connect(server_address)
    if file_type == 'csv':
        df = pd.read_csv(file_name)
        df['json_doc'] = df.apply(lambda x: x.to_json(), axis=1)
        for index, row in df.iterrows():
            counter = counter + 1
            sock.sendall(row['json_doc'].encode())
            sock.send('\n'.encode())
    elif file_type == 'json':
        f = open(file_name)
        docs = json.load(f)
        for doc in docs:
            counter = counter + 1
            sock.sendall(json.dumps(doc).encode())
            sock.send('\n'.encode())

    sock.close()
    print("Total Records: {0}".format(counter))
except socket.error as e:
    sys.stderr.write(str(e))
finally:
    sock.close()