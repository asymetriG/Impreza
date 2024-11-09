class Graph:
    def __init__(self):
        self.edges = {}  # Düğüm ve bağlantılarını tutacak bir sözlük

    def add_node(self, node):
        # Eğer düğüm yoksa ekle
        if node not in self.edges:
            self.edges[node] = []

    def add_edge(self, node1, node2, weight):
        # Her iki düğüm arasında ağırlıklı bir kenar ekle
        self.add_node(node1)
        self.add_node(node2)
        self.edges[node1].append((node2, weight))
        self.edges[node2].append((node1, weight))  # Çift yönlü bağlantı için

    def display(self):
        # Graf yapısını yazdırarak göster
        for node, connections in self.edges.items():
            connections_str = ', '.join([f"{neighbor} ({weight})" for neighbor, weight in connections])
            print(f"{node} -> {connections_str}")

# Grafı oluştur
g = Graph()

# Kenarları ekle (düğüm1, düğüm2, ağırlık)
edges = [
    ("İzmir", "İstanbul", 10),
    ("İzmir", "Bursa", 6),
    ("İzmir", "Isparta", 9),
    ("İzmir", "Antalya", 13),
    ("Bursa", "İstanbul", 4),
    ("Bursa", "Isparta", 13),
    ("İstanbul", "Kocaeli", 4),
    ("Kocaeli", "Trabzon", 13),
    ("Kocaeli", "Ankara", 10),
    ("Trabzon", "Erzurum", 7),
    ("Trabzon", "Kars", 15),
    ("Erzurum", "Kars", 12),
    ("Erzurum", "Ankara", 16),
    ("Erzurum", "Şanlıurfa", 12),
    ("Şanlıurfa", "Hatay", 7),
    ("Şanlıurfa", "Ankara", 17),
    ("Hatay", "Ankara", 10),
    ("Hatay", "Isparta", 12),
    ("Antalya", "Isparta", 3),
    ("Ankara", "Isparta", 10),
]

if __name__=="__main__":

    for node1, node2, weight in edges:
        g.add_edge(node1, node2, weight)

    g.display()