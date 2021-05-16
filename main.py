import requests
from requests.auth import HTTPBasicAuth
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


vcsa_admin="administrator@vsphere.local"
vcsa_passwd="VMware1!"
vcsa_session=requests.session()
vcsa_session.auth=(vcsa_admin,vcsa_passwd)
url_cis="https://scafg-vcsa.scafg.kr/rest/com/vmware/cis/session"
session=vcsa_session.post(url_cis,verify=False)
vcsa_key=json.loads(session.text)["value"]
vcsa_header={"vmware-api-session-id":vcsa_key}
vcsa_session.headers.update(vcsa_header)

url_vms="https://scafg-vcsa.scafg.kr/rest/vcenter/vm/vm-1061"
vms=vcsa_session.get(url_vms,verify=False).json()