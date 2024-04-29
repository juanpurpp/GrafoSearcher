from graph.Graph import Graph

gr = Graph('La paloma')


a = gr.add_node(-41.45624108733179, -72.93056270579201, 'A')
b = gr.add_node(-41.45698815570631, -72.9279256634943, 'B')
c = gr.add_node(-41.45694301205481, -72.9265286480675, 'C')
d = gr.add_node(-41.455785131815134, -72.93049831708267, 'D')
e = gr.add_node(-41.45634799284079, -72.92789121014977, 'E')
f = gr.add_node(-41.45638819701288, -72.92650719041995, 'F')
g = gr.add_node(-41.45638015618045, -72.9253162897222, 'G')
h = gr.add_node(-41.4553267985148, -72.93048758824754, 'H')
i = gr.add_node(-41.45592182708473, -72.92790193898487, 'I')
j = gr.add_node(-41.45597007240521, -72.92506952651458, 'J')

a.connect_to(b, 3)
b.connect_to(c, 3)

d.connect_to(e, 1)
e.connect_to(f, 1)
f.connect_to(g, 1)

h.connect_to(i, 1)
j.connect_to(i, 1, False)

a.connect_to(d,2)
d.connect_to(h,2)

b.connect_to(e, 2)
e.connect_to(i,2)

c.connect_to(f, 1)

g.connect_to(c, 3, False) #non bidirectional
j.connect_to(g, 3, False) #non bidirectional

problem_map = gr