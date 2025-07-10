
# 🧠 Fabric Lab

The **Fabric Lab** is a modular, containerized testbed for data-centric industrial architectures. It includes services for message brokering (Kafka), semantic data storage (GraphDB), device simulation (OPC UA servers), and interactive data exploration (JupyterLab). Everything is orchestrated via Docker Compose.

---

## 🔧 Services Overview

| Service                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **Zookeeper**                 | Coordination service used by Kafka                                          |
| **Kafka**                     | Message broker for distributed event streams                               |
| **GraphDB**                   | RDF triple store for semantic data                                         |
| **init_graphdb**              | Initializes a GraphDB repository using a TTL config                        |
| **Kafka UI**                  | Web-based UI for inspecting Kafka topics and brokers                        |
| **Portainer**                 | Web UI for managing Docker containers                                       |
| **OPC UA Assembly Station**   | Simulates an assembly machine via OPC UA                                   |
| **OPC UA CNC Milling**        | Simulates a CNC milling machine via OPC UA                                 |
| **OPC UA Injection Molding**  | Simulates an injection molding machine via OPC UA                          |
| **JupyterLab**                | Interactive Python environment with pre-cloned GitLab repository            |

---

## 🚀 Getting Started

### 1. Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

---

### 2. Startup

To start the entire lab environment:

```bash
docker compose up --build
```

To stop and clean everything:

```bash
docker compose down --remove-orphans --volumes
```

---

## 📂 Project Highlights

### OPC UA Simulation
Three simulated OPC UA devices are started:
- `assembly_station` → port **4841**
- `cnc_milling` → port **4842**
- `injection_molding` → port **4843**

Each is based on the [`opcua_sample_server`](https://hub.docker.com/r/stephantrattnig/opcua_sample_server) Docker image and configured via runtime arguments.

---

### JupyterLab

A JupyterLab container is available on port **8888**, with:
- Tokenless login (`--NotebookApp.token=''`)
- Pre-cloned client repo: [data-fabric/client](https://gitlab.lrz.de/data-fabric/client)
- Persistent volume at `/home/jovyan/work`

---

### Kafka & UI
- Kafka is accessible on **localhost:29092**
- Kafka UI at **http://localhost:8080**

---

### GraphDB

GraphDB is available at **http://localhost:7200**  
It is initialized using a `.ttl` file via the `init_graphdb` service.

---

### Portainer

Portainer UI is available at **http://localhost:9000**  
You can use it to visually manage and monitor your containers, networks, and volumes.

---

## 🧠 Network

All services share the `fabric-lab` network for seamless internal communication.

---

## 📦 Volumes

| Volume Name       | Purpose                            |
|-------------------|------------------------------------|
| `portainer_data`  | Persistent Portainer data storage  |
| `jupyterlab_data` | JupyterLab notebooks and work dir  |

---

## ✅ Notes
- All OPC UA servers expose port `4840` internally but are mapped externally to unique ports.
- JupyterLab is launched as root to allow volume folder creation.
- Git repository cloning in JupyterLab is done on container startup.

---

## 📮 Contact

For issues or contributions, feel free to open a ticket or fork the repo. Happy experimenting with your data fabric!
```

Let me know if you'd like this as a file directly or if you want to tweak the wording/format!







###### deprecated
This is a lab for the data fabric architecture. It includes a mock that shows all the relevant components in interplay, including

- A central message broker kafka instance
- exemplary mock OPC UA data sources (3x)
- OPC UA Connectors
- a Graph Database storing the central knowledge graph
- a python environment for the execution of the client or the agent



starting

```commandline
docker compose up -d
```

stopping and removing all containers:
```commandline
docker compose down
```
add a -v flag if the volumes may be destroyed too


portainer setting:
local username: admin
