import plotly.graph_objects as go
import os
import pandas as pd
import networkx as nx

def plotGraph(df, Gprob, startingNode, startingProbability, text, filename):
    G = nx.from_pandas_adjacency(df)
    pos = nx.fruchterman_reingold_layout(G) #A dictionary of positions keyed by node

    edge_x = []
    edge_y = []
    xtp = []
    ytp = []
    etext = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)
        xtp.append(0.5 * (x0 + x1))
        ytp.append(0.5 * (y0 + y1))
        etext.append(f"{G[edge[0]][edge[1]]['weight']}")


    eweights_trace = go.Scatter(x=xtp, y=ytp, mode='text',
                                marker_size=0.5,
                                text=etext,
                                textposition='top center',
                                hovertemplate='weight: %{text}<extra></extra>')

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='text',
        mode='lines')


    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=False,
            # colorscale options
            #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            colorscale='Hot',
            reversescale=True,
            color=[],
            size=10,
            line_width=2))

    node_probabilities = []
    node_text = []
    for node, probability in Gprob.items():
        if (node == startingNode):
            node_text.append(f'Starting node: {node} p: {startingProbability}')
            node_probabilities.append(startingProbability * 100)
        else:
            node_text.append(f'Node: {node} p: {probability}')
            node_probabilities.append(probability * 100)

    #node_trace.marker.color = node_probabilities
    node_trace.text = node_text
    node_trace.marker.size = node_probabilities

    fig = go.Figure(data=[edge_trace, node_trace, eweights_trace],
                 layout=go.Layout(
                    title=f'{text} ',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[ dict(
                        text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002 ) ],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    fig.show()
    # directory = os.path.dirname(os.path.abspath("plotting.py"))
    # dest = f"{directory}/plots"
    # fig.write_image(f"{dest}/{filename}.png")


if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath("plotting.py"))
    dest = f"{directory}/graphs"
    for filename in os.listdir(dest):
        df = pd.read_csv(f"{dest}/{filename}")
        print(filename)
    #plotGraph()