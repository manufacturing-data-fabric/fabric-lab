import time
import requests
import os

graphdb_url = "http://graphdb:7200/rest/repositories"
config_file_path = "/init/repo-config.ttl"
df_file_path = "/init/df_full.ttl"
repo_id = "fabric-lab" # todo: make this an .env variable?

boundary = "myBoundary"
with open(config_file_path, "rb") as file:
    payload = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="config"; filename="repo-config.ttl"\r\n'
        "Content-Type: text/turtle\r\n\r\n"
    )
    payload += file.read().decode('utf-8')
    payload += f"\r\n--{boundary}--"

files = {"config": (None, payload, "text/turtle")}
headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}

# Wait for GraphDB to become available
created = False
for i in range(20):
    try:
        r = requests.post(graphdb_url, files=files, headers=headers)
        if r.status_code in (200, 201) and r.text == "":
            print("Repository created successfully.")
            created = True
            break
        else:
            print(f"Attempt {i}: Status {r.status_code}, response: {r.text}")
    except Exception as e:
        print(f"Attempt {i}: GraphDB not ready, retrying... {e}")
    time.sleep(5)

if not created:
    print("Proceeding anyway (repository may already exist).")

for i in range(10):
    try:
        with open(df_file_path, "rb") as f:
            resp = requests.post(
                url = f"http://graphdb:7200/repositories/{repo_id}/statements",
                params = {"context": "<http://stephantrattnig.org/grraphs/ontology/df_full>"}, # TODO: potentially make this a .env or else
                data = f.read(),
                headers={"Content-Type": "text/turtle"},
            )
        if resp.status_code == 204:
            print(f"Ontology '{df_file_path}' uploaded successfully")
            break
        else:
            print(f"Upload attempt {i}: HTTP {resp.status_code}, response: {resp.text}")
    except Exception as e:
        print(f"Upload attempt {i}: error {e}")
    time.sleep(3)

