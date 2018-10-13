import meetup.api
import json
import networkx as nx
import datetime
from networkx.readwrite import json_graph
import operator


if __name__ == '__main__':

    g = nx.Graph()
    client = meetup.api.Client()

    groups = client.GetFindGroups({'text': 'graphs'})

    for group in groups:

        group_name = group.name
        g.add_node(group_name)
        g.node[group_name]['type'] = 'group'
        g.node[group_name]['id'] = group_name
        g.node[group_name]['members'] = group.members
        g.node[group_name]['city'] = group.city

        if group.key_photo:
            g.node[group_name]['image'] = group.key_photo["photo_link"]

        members = client.GetMembers({'group_urlname': group.urlname})

        for member in members.results:

            member_name = member['name']
            year_visited = datetime.datetime.fromtimestamp(member["visited"]/1000.0).year

            if member['status'] == 'active' and member_name not in g and 'photo' in member.keys() and year_visited >= 2017 and "topics" in member.keys():

                g.add_node(member_name)
                g.node[member_name]['type'] = 'member'
                g.node[member_name]['id'] = member_name
                g.node[member_name]['image'] = member['photo']['photo_link']
                #g.node[member_name]['year_joined'] = member["joined"]
                g.node[member_name]['url'] = member['link']

                g.add_edge(group_name, member_name)

                for topic in member["topics"]:

                    topic_name = topic["name"]

                    if "danc" in topic["urlkey"] \
                            or "cult" in topic["urlkey"] \
                            or "photo" in topic["urlkey"] \
                            or "fitn" in topic["urlkey"] \
                            or "natu" in topic["urlkey"] \
                            or "cook" in topic["urlkey"] \
                            or "food" in topic["urlkey"] \
                            or "music" in topic["urlkey"] \
                            or "cinem" in topic["urlkey"] \
                            or "trave" in topic["urlkey"]\
                            or "book" in topic["urlkey"]\
                            or "read" in topic["urlkey"]\
                            or "sport" in topic["urlkey"]:

                        if topic_name not in g:
                            g.add_node(topic_name)
                            g.node[topic_name]['type'] = 'topic'
                            g.node[topic_name]['id'] = topic['name']

                        g.add_edge(member_name, topic_name)


    for i, comp in enumerate(nx.connected_component_subgraphs(g)):
        print('Component ', i+1 , ': ')
        print('\tSize:', len(comp.nodes()))
        if len(comp.nodes()) > 1:

            closeness = nx.closeness_centrality(comp)
            print('\tCloseness:', closeness)
            print('\tMAX CLOSENESS: ', max(closeness.items(), key=operator.itemgetter(1)))

            for key, value in closeness.items():
                g.node[key]['closeness'] = value


    with open("./Data/salida.json", "w") as f:

        g2 = nx.convert_node_labels_to_integers(g, label_attribute="Name")
        json_data = json_graph.node_link_data(g2)
        json.dump(json_data, f)

