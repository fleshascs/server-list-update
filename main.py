import requests
from bs4 import BeautifulSoup

servers = [
    # fleshas
    "91.211.246.7:27015",
    "91.211.246.7:27018",
    "91.211.246.7:27019",
    "91.211.246.7:27021",
    "91.211.246.7:27022",

    # omonas
    "91.211.247.221:27015",
    "91.211.247.222:27015",
    "78.56.9.125:27020",
    "91.211.247.230:27024",

    # procs
    "185.80.129.86:27015",
    "91.225.107.149:27017",
    "91.225.107.149:27019",
    "91.225.107.149:27020",
    "91.225.107.149:27015",
    "91.225.107.149:27016",
]

def get_top50_servers():
    URL = "https://www.gametracker.com/search/cs/?&searchipp=50#search"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("table", class_="table_lst table_lst_srs")
    results = results.find_all("tr")
    servers = []
    for row in results:
        ip = row.find(class_="ip")
        port = row.find(class_="port")
        if ip and port:
            ip = ip.text.strip()
            port = port.text.strip()
            servers.append(ip + port)
    return servers

f = open("serverscs.txt", "w")
f.write("\n".join(servers + get_top50_servers()))
f.close()



