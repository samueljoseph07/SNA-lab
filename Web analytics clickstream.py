import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

data = {
    'user_id': [1,1,2,3,3],
    'page': ['home', 'product', 'home', 'home', 'checkout'],
    'duration': [10, 30, 20, 15, 25]
}

df = pd.DataFrame(data)
usage = df.groupby('page')['duration'].mean()
print("Average Time on pages: \n", usage)
G= nx.DiGraph()
links = [('home','product'),('product', 'checkout'),('checkout', 'home')]
G.add_edges_from(links)
nx.draw(G, with_labels = True, node_color= 'lightblue', node_size = 2800)
plt.show()
