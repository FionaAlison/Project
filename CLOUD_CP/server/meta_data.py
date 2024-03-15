import requests

# server meta data ( fetch dns and IP)
host_server = 'ec2-54-236-191-88.compute-1.amazonaws.com'
ip_sever = '127.0.0.1'

metadata_url: str = "http://169.254.169.254/latest/meta-data/"
metadata: str = ''
try:
    response = requests.get(metadata_url)
    response.raise_for_status()
    metadata = response.text
except requests.exceptions.RequestException as e:
    print("Error fetching instance metadata:", e)
    metadata = None

# Get instance public DNS name and IP address
if metadata:
    lines = metadata.split('\n')
    host_server = requests.get(metadata_url + 'public-hostname').text
    ip_sever = requests.get(metadata_url + 'local-ipv4').text
    print("Public DNS Name:", host_server)
    print("Local IP Address:", ip_sever)

# client meta data
host_client: str = 'my-LB-291696e941a0fa1d.elb.us-east-1.amazonaws.com'
ip_client: str = '127.0.0.1'

# Other static configurations
port = 8080
buffer_size = 1024
cwd = '/'.join(__file__.split("/")[:-1])

# old config
host_server: str = 'localhost' 
host_client: str = 'localhost' 
ip_server = '127.0.0.1'
ip_client = '127.0.0.1'
port = 8080
buffer_size = 1024
cwd = '/'.join(__file__.split("/")[:-1])