import networkx as nx
import matplotlib.pyplot as plt
import random
import time

# Ξεκινάμε τη μέτρηση του χρόνου
start_time = time.time()

# Δημιουργία τυχαίου γράφου με n=10 και p=0.3
n = 10000
p = 0.3
G = nx.erdos_renyi_graph(n, p)

# Προσθήκη τυχαίων βαρών στις ακμές (τιμές από 1 έως 10)
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 10)

# Απεικόνιση του γράφου
pos = nx.spring_layout(G)  # Καθορισμός θέσης κόμβων για καλύτερη διάταξη
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=700, font_size=14)

# Προσθήκη των βαρών στις ακμές
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Υπολογισμός και εμφάνιση χρόνου εκτέλεσης
end_time = time.time()
execution_time = end_time - start_time
print(f"Χρόνος εκτέλεσης: {execution_time:.4f} δευτερόλεπτα")

plt.title("Τυχαίος γράφος με βάρη στις ακμές")
plt.show()

#####################################################################

# Ορισμός συνάρτησης DFS με το όνομα dfs_preorder_nodes
def dfs_preorder_nodes(graph, start_node):
    return list(nx.dfs_preorder_nodes(graph, start_node))

# Καλούμε τη συνάρτηση DFS ξεκινώντας από τον κόμβο 0
start_node = 0
dfs_result = dfs_preorder_nodes(G, start_node)

# Τυπώνουμε τα αποτελέσματα της αναζήτησης
print(f"\nΑποτελέσματα Αναζήτησης κατά Βάθος (DFS) από τον κόμβο {start_node}: {dfs_result}")

#######################################################################


# Συνάρτηση BFS για εύρεση BFS δέντρου από κόμβο εκκίνησης
def bfs_tree(graph, start_node):
    # Δημιουργία BFS δέντρου με χρήση της συνάρτησης nx.bfs_tree
    bfs_tree = nx.bfs_tree(graph, start_node)
    bfs_result = list(bfs_tree.nodes())
    return bfs_result, bfs_tree

# Εκτέλεση της BFS από τον κόμβο 0 και εμφάνιση των αποτελεσμάτων
start_node = 0
bfs_result, bfs_tree = bfs_tree(G, start_node)
print(f"\nΑποτελέσματα αναζήτησης κατά πλάτος (BFS) από τον κόμβο {start_node}: {bfs_result}")

##########################################################################

# Συνάρτηση για τον υπολογισμό των ελάχιστων μονοπατιών με τον αλγόριθμο Dijkstra
def shortest_path(G, start_node):
    # Υπολογισμός ελάχιστων μονοπατιών από τον κόμβο start_node
    paths = nx.single_source_dijkstra_path_length(G, start_node, weight='weight')
    return paths

# Χρήση της συνάρτησης για εύρεση ελάχιστων μονοπατιών από τον κόμβο 0
start_node = 0
shortest_paths = shortest_path(G, start_node)

# Εκτύπωση των αποτελεσμάτων
print(f"\nΑποτελέσματα Dijkstra Ελάχιστες αποστάσεις από τον κόμβο {start_node}:")
for target_node, distance in shortest_paths.items():
    print(f"Κόμβος {start_node} -> Κόμβος {target_node}: Απόσταση = {distance}")
    
############################################################################

# Υπολογισμός και απεικόνιση του MST με τον αλγόριθμο Kruskal
mst = nx.minimum_spanning_tree(G, algorithm='kruskal')

# Εκτύπωση των ακμών και των βαρών του MST
print("\nΑλγόριθμος Kruskal: Ακμές του Ελάχιστου Επικαλυπτικού Δένδρου (MST) και τα βάρη τους:")
for u, v, weight in mst.edges(data=True):
    print(f"({u}, {v}) με βάρος {weight['weight']}")

# Απεικόνιση του MST
plt.figure()
nx.draw(mst, pos, with_labels=True, node_color='lightgreen', edge_color='blue', node_size=700, font_size=14)
mst_edge_labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(mst, pos, edge_labels=mst_edge_labels, font_color='blue')

plt.title("Ελάχιστο Επικαλυπτικό Δένδρο (MST) - Αλγόριθμος Kruskal")
plt.show()

###############################################################################


# Υπολογισμός ελάχιστου επικαλυπτικού δένδρου με τον αλγόριθμο Prim
mst = nx.minimum_spanning_tree(G, algorithm='prim')

# Εκτύπωση των ακμών του ελάχιστου επικαλυπτικού δένδρου και των βαρών τους
print("\nΑλγόριθμος Prim: Ακμές του Ελάχιστου Επικαλυπτικού Δένδρου (MST) και τα βάρη τους:")
for (u, v, weight) in mst.edges(data='weight'):
    print(f"({u}, {v}) με βάρος {weight}")
# Απεικόνιση του ελάχιστου επικαλυπτικού δένδρου
plt.figure()
nx.draw(mst, pos, with_labels=True, node_color='lightgreen', edge_color='blue', node_size=700, font_size=14)
nx.draw_networkx_edge_labels(mst, pos, edge_labels=nx.get_edge_attributes(mst, 'weight'), font_color='red')
plt.title("Ελάχιστο Επικαλυπτικό Δένδρο (MST) - Αλγόριθμος Prim")
plt.show()

