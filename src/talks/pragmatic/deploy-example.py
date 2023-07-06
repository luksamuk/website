from diagrams import Cluster, Diagram, Edge

from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ingress, Service
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS
from diagrams.aws.general import Client, MobileClient
from diagrams.aws.compute import ElasticBeanstalkApplication

from diagrams.generic.database import SQL
from diagrams.generic.compute import Rack

attr = {
    "bgcolor": "transparent"
}

with Diagram("", show=False, outformat="png", graph_attr=attr, filename="deploy-example"):
    with Cluster("Amazon Web Services"):
        db = RDS("Relational Database\nService")
        with Cluster("Réplicas"):
            pods = [ElasticBeanstalkApplication("Back-end"), ElasticBeanstalkApplication("Back-end"), ElasticBeanstalkApplication("Back-end")]
            pods - Edge(style="dashed") - db
        lb = ELB("Load Balancer")
        lb >> pods
    with Cluster("Front-ends"):
        clients = [Client("Navegador"), MobileClient("Smartphone")]
        clients >> lb

with Diagram("", show=False, outformat="png", graph_attr=attr, filename="dichotomy"):
    with Cluster("Provedor Cloud"):
        db = SQL("Banco de Dados")
        back = Rack("Back-end")
        back - Edge(style="dashed") - db
    with Cluster("Cliente (Front-end)"):
        clients = [Client("Web"), MobileClient("Mobile")]
        clients >> back
