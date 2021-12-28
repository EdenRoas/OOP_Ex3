#  Ex3_OOP

## Overview:
Writing an algorithm and creating a link graph.
the data structure that the assignment is built on is an directional weighted graph. 
for info about this type of graph you can visit: [https://en.wikipedia.org/wiki/Directed_graph].
the process of building this data structrue was to implement and program the interfaces sent by Boaz-Ben-Moshe.
here are the classes of this data structure:

| Class      | Description |
| :------------| :------------|
| NodeData  | represents a vertices on the grap |
| Point3D      |    represents a 3 coordinates point|
| DiGraph      |    represents an graph based on the vertices and edges |
| GraphAlgo      |    a data structure based on the DirectedWeightedGraph structrue that offers variuos algorithms | 

## NodeData
+ Represents a vertice on the graph.
   + **id:** specific key associated with this node.
   + **Location:** the location of the node in 3D.
    
## Point3D
+ Represents a location in 3D.
  + **X:** x value.
  + **Y:** y value.
  + **Z:** z value.

## DiGraph
+ Represents an graph based on the nodes and edges.
  + **_vertices_dict:** a dictionary contains all the vertices of the graph.
  + **_src_edge_dict:** a nested dictionary containing the edges of the graph according to the scource vertax.
  + **_dest_edge_dict:** a nested dictionary containing the edges of the graph according to the destination vertax.
  + **_mc:** counts the changes in the graph.
  + **edges_size:** the amount of edges.

## GraphAlgo
+ The class that contains the whole algorithms that can be used on a graph.
     + **graph:** the graph that the algorithms being used on. 

![image](https://user-images.githubusercontent.com/92533182/145768109-4e0bff58-b817-4ef4-8a83-1eecc66e04a6.png)

## The algorithems we used:
+ in order to calculate the shortest path between two given edges on the graph, we used dijkstra's algorithm.
  for info about this specific algorithm please visit: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm.
+ in order to calculate the center in the graph, we used Floyd–Warshall algorithm.
  for info about this algorithem please visit: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm.
+ in order to find if the graph is strongly connected  we used DFS algorithem.
  for info about this specific algorithm please visit: https://en.wikipedia.org/wiki/Depth-first_search
  
 
  
  ***in this assignment we also asked to build a GUI were we could load graphs using a JSON file.***

# GUI
### G1.json

![G1](https://user-images.githubusercontent.com/92533182/146030677-c54ef26d-b1eb-4374-ade6-fa93d922ef33.png)
##### Center - 8
##### isConnected - true
##### ShortestPathDist(5,16) - 8.335654448747263

## Tests
**1000 nodes-**
  + is connected - true
  + center - 362

**10000 nodes-**
  + is connected - true
  + center -

**100000 nodes-**
  + is connected - true
  + center - 

## About
 we used swing for the GUI and build three classes that got used for the GUI: 
   + **GraphPanel-** the class is used to draw a graph.
   + **PathPanel**- the class is used to draw the shortest path between two vertices and the path for the Tsp.
   + **GUI_runnner** - this class creat a frame that runs all the function needed and in general runs all the gui.
## How to run
  + in the folder "Ex2/out/artifacts/Ex2_Jar" there is a jar file
  + open the terminal and type the command : java -jar Ex2.jar (optinal-)"a file name.json"

### Collaborators
  + **HADAR BITAN**
  + **EDEN ROAS**
