import json
import socket
import salt.client


with open('/var/tmp/test.json') as json_data:
    d = json.load(json_data)

inspec_data = d.get('profiles', None).pop().get('controls', None)
hostname = socket.gethostname()
influx_return = []

for line in inspec_data:
    id = line.get('id', None)
    title = line.get('title', None)
    desc = line.get('desc', None)
    category = line.get('tags', {}).get('category', "NA")
    technology = line.get('tags', {}).get('technology', "NA")

    status = []
    for check_results in line['results']:
        status.append(check_results.get('status', None))

    if "failed" in status:
       check_status = "failed"
    else:
       check_status = "passed"


    input_json = { 
                    "measurement": "custom_returns",
                    "tags": { 
                          "id": id,
                          "title": title,
                          "hostname": hostname,
                          "status": check_status,
                          "category": category,
                          "technology": technology
                    },
                    "fields": {
                          "desc": desc
                    } 
                 }

    
    influx_return.append(input_json)

caller = salt.client.Caller('/etc/salt/minion')
caller.sminion.functions['event.send'](
    'inspec/tests/results',
    {
       'results': influx_return,
    }
)
