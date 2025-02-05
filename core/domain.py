#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:57:33 2022

@author: alain
"""

from geonodes.core.socket import Socket
from geonodes.core.node import Node


import logging
logger = logging.getLogger('geonodes')

# =============================================================================================================================
# Domain selector
#
# Domain uses selector property which can be used to get the selection or the index
# - selection: selector.selection
# - index:     selector.index

class Selector:
    
    def __init__(self, domain, value):
        self.domain     = domain
        self.value      = value
        self._selection = None
        
    def __repr__(self):
        return f"<{self.value}>"
        
    @property
    def is_index(self):
        return isinstance(self.value, int) or Socket.is_socket(self.value)
            
    @property
    def index(self):
        
        if self.value is None:
            raise Exception(f"{self} index error: the selection is not an Integer. Use {type(self).__name__}[Integer] to have a valid index.")
            #return self.domain.domain_index

        # ----- Index is an int or a socket (different from Boolean addressed above)
        
        elif self.is_index:
            return self.value
        
        else:
            raise Exception(f"Invalid domain index: {self.value}. Only Int is a valid type to get an index from domain[value].")
            
    @property
    def selection(self):
        
        import geonodes as gn
        
        if self.value is None:
            return True
        
        # ----- Index is a boolean
        
        elif isinstance(self.value, (bool, gn.Boolean)):
            return self.value

        # ----- Index is an int or a socket (different from Boolean addressed above)
        
        elif isinstance(self.value, int) or Socket.is_socket(self.value):
            return self.domain.domain_index.equal(self.value)

        # ----- Index is slice
        
        elif isinstance(self.value, slice):
            if self.value.start is None:
                return self.domain.domain_index.less_equal(self.value.stop)
            
            elif self.value.stop is None:
                return self.domain.domain_index.greater_equal(self.value.start)
            
            else:
                center = (self.value.start + self.value.stop - 1)/2
                amp    = (self.value.stop - self.value.start - 1)/2
                return gn.Float(self.domain.domain_index).equal(center, epsilon=amp+0.1)
            
        # ----- Index is an array of indices
        
        elif hasattr(self.value, '__len__'):
            sel = None
            for i in self.value[:10]:
                if sel is None:
                    sel = self.domain.domain_index.equal(i)
                else:
                    sel = sel.b_or(self.domain.domain_index.equal(i))
            return sel
        
        else:
            msg = f"Invalid domain index: {self.value}. Only bool, int, slice and array are valid."
            if hasattr(self.value, 'is_Node'):
                msg += f"\nThe value is a Node, you certainly want to use one output socket in {list(self.value.outsockets.keys())}."
                
            raise Exception(msg)
            


# =============================================================================================================================
# Root class for domains
#    
# Fields are properties of domains.
#   
# Components and domains
# ----------------------
#
# - Mesh component
#     - Point   : point (or points, verts)
#     - Edge    : edge  (or edges)
#     - Face    : face  (or faces)
#     - Corner  : face_corner (or corner or corners)
# - Curve component
#     - Point   : point (or points)
#     - Spline  : spline (or splines)
# - Points
#     - Point   : point (or points)
# - Instances components
#     - Instance : instances (or insts)
#
# POINT domain is share between Mesh, Curve and Points but has not the same methods
#
# The inheritance diagram is the following:
#
# - Interfaces
#   - PointInterface      : common to points : Vertex, ControlPoint and CloudPoint
#   - MeshInterface       : common to all mesh domains: Vertex, Edge, Face, Corner
#   - PEFInterface        : common to Mesh domains except Corner: Vertex, Edge and Face
#
# - Classes
#   - Domain
#     - Vertex          : POINT
#     - Edge            : EDGE
#     - Face            : FACE
#     - Corner          : CORNER
#     - ControlPoint    : POINT
#     - Spline          : CURVE
#     - CloudPoint      : POINT
#     - Instance        : INSTANCE


class Domain:
    """ 
    **Domain** is the root class for:
    - [Vertex](Vertex.md), node domain *'POINT'*
    - [Edge](Edge.md), node domain *'EDGE'*
    - [Face](Face.md), node domain *'FACE'*
    - [Corner](Corner.md), node domain *'CORNER'*
    - [ControlPoint](ControlPoint.md), node domain *'POINT'*
    - [Spline](Spline.md), node domain *'SPLINE' (or *'CURVE'*)
    - [CloudPoint](CloudPoint.md), node domain *'POINT'*
    - [Instance](Instance.md), node domain *'INSTANCE'*
    
    
    **Domain** provides mechanism to keep the context, by maintaining:
    - the `selection`
    - the node domain value in *'POINT'*, *'EDGE'*, *'FACE'*, *'CORNER'*, *'SPLINE'*, *'INSTANCE'*
    - the geometry it is a domain of
    
    > By keeping the context geometry, it is not necessary to explicitly create **Capture Attribute**.
      **Domain** class determines if it is necessary or not to create this node.
    
    **Domains** are not initialized directly but by geometries:
    - [Mesh](Mesh.md) initializes 4 domains:
      - `verts` property of type [Vertex](Vertex.md)
      - `edges` property of type [Edge](Edge.md)
      - `faces` property of type [Face](Face.md)
      - `corners` property of type [Corner](Corner.md)
    - [Curve](Curve.md) initializes 2 domains:
      - `points` property of type [ControlPoint](ControlPoint.md)
      - `splines` property of type [Spline](Spline.md)
    - [Instances](Instances.md) initializes 1 domain: 
      - `insts` property of type [Instance](Instance.md)
    - [Points](Points.md) initializes 1 domain: 
      - `points` property of type [CloudPoint](CloudPoint.md)
    
    > Note that the node domain *'POINT'* is used by 3 **Domains**.
    
    ## Selection mechanism
    
    One important feature of **Domain** is the selection mechanism. The selection is expressed using the array syntax:
    - `mesh.verts[1]` : select the `index == 1`
    - `mesh.faces[10:20]` : select the `index` in the range 10 to 20 (exc)
    - `mesh.faces[8, 17]` : select the `index` equal to 8 or 17
    - `mesh.edges[(mesh.edges.index % 2).equal(0)]` : select the even `index`
    
    Nodes having a **Selection** socket use the **Domain** selection initialized with this syntax.
    
    In the following example, two vertices selected by the user are moved upwards:
    
    ```python
    import geonodes as gn
    
    with gn.Tree("Test") as tree:
        
        index1 = gn.Integer.Input(0, "Index 1")
        index2 = gn.Integer.Input(1, "Index 2")
        
        cube = gn.Mesh.Cube()
        
        cube.verts[index1, index2].position += (0, 0, .2)
        
        tree.og = cube
    ```
    """
    
    def __init__(self, data_socket, selection=None):
        """
        Args:
            - data_socket (DataSocket): the data class the domain belongs to
            - selection (any): the selection to use
        """
        self._data_socket = data_socket
        self.selector     = None if selection is None else Selector(self, selection)
        
    @classmethod
    @property
    def domain(cls):
        """ Gives the **Geometry Nodes** domain string to use in the generated nodes.
        
        - Vertex        : 'POINT',
        - Edge          : 'EDGE',
        - Face          : 'FACE',
        - Corner        : 'CORNER',
        - ControlPoint  : 'POINT',
        - Spline        : 'CURVE',
        - CloudPoint    : 'POINT',
        - Instance      : 'INSTANCE',
        
        Returns:
            domain string (str)
        """
        return {
            'Vertex'        : 'POINT',
            'Edge'          : 'EDGE',
            'Face'          : 'FACE',
            'Corner'        : 'CORNER',
            'ControlPoint'  : 'POINT',
            'Spline'        : 'CURVE',
            'CloudPoint'    : 'POINT',
            'Instance'      : 'INSTANCE',
            }[cls.__name__]
        
    # ----------------------------------------------------------------------------------------------------
    # Data socket
    
    @property
    def data_socket(self):
        """ Returns the data socket it belongs to.       
        
        Returns:
            DataSocket
        """
        return self if self._data_socket is None else self._data_socket
    
    # ----------------------------------------------------------------------------------------------------
    # Node
    
    @property
    def node(self):
        return self.data_socket.node
        
    # ----------------------------------------------------------------------------------------------------
    # Return bool selection
        
    @property
    def selection(self):
        """ Returns the selection value to use in nodes with a **Selection** socket.  
        
        Returns:
            Boolean
        """
        return None if self.selector is None else self.selector.selection
    
    @property
    def selection_index(self):
        """ Returns the selection index.
        
        > CAUTION: raise an error if the selection is not a integer.
        
        Returns:
            Integer
        """
        return None if self.selector is None else self.selector.index
    
    def index_for_sample(self, default=None):
        """ Return default if not None or Input index socket.
        
        The node 'Sample Index' has an input with default value to 0.
        If mehod argument is None, create a node 'Input Index' as input.
        
        **sample_index** method is implemented:
            
        ```python
        def sample_index(self, value=None, index=None, clamp=False):
            return nodes.SampleIndex(..., index=self.index_for_sample(index), ...)
        ```
        
        Returns:
            default or Input index
        """
        if default is not None:
            return default
        else:
            return self.data_socket.index
        
    @staticmethod
    def is_domain_class():
        return True
    
    # ----------------------------------------------------------------------------------------------------
    # Select domain either by a bool or by int(s)
    
    @staticmethod
    def value_data_type(socket, default=None, color='FLOAT_COLOR'):
        return Socket.value_data_type(socket, default=default, color=color)

    # ----------------------------------------------------------------------------------------------------
    # Select domain either by a bool or by int(s)
        
    def select(self, selection):
        """ Select the domain
        
        If the method is called on a **Domain** which already has a selection, the two selections are combined:
            
        ```python
        verts = mesh.verts[10:20] # Selection of vertices from 10 to 20
        v = verts.select((verts.index % 2).equal(0)) # Even indices in the previous selection
        ```
        
        Args:
            - selection (Boolean or Integer): The selection condition
            
        Returns:
            Domain with the given selection (Domain)
        
        If a selection is existing, the resulting selection is a logical and betwenn the two
        """
        
        if self.selector is None:
            sel = selection
            
        elif selection is None:
            sel = self.selector.value
            
        else:
            other = Selector(self, selection)
            sel = self.selector.selection.b_and(other.selection)
            
        return type(self)(self.data_socket, selection=sel)
    
    # ----------------------------------------------------------------------------------------------------
    # Representation
    
    def __repr__(self):
        sel = "" if self.selector is None else f" [{self.selector}]"
        return f"[Domain {self.domain} of {self.data_socket}{sel}]"
    
    # ----------------------------------------------------------------------------------------------------
    # Reset the cache
    
    def reset_cache(self):        
        cache = set()
        for name in dir(self):
            if name[:3] == '_c_':
                cache.add(name)
                
        for name in cache:
            delattr(self, name)
    
    # ----------------------------------------------------------------------------------------------------
    # Stack
    
    def socket_stack(self, node, socket_name=None):
        """ Make the owning socket jump to the output socket of the node passed in argumment.
        
        Args:
            - node (Node): The node to jump to
            - socket_name: The name of the output socket (first one if None)
        """
        self.reset_cache()
        return self.data_socket.stack(node, socket_name=socket_name)
    
    # ----------------------------------------------------------------------------------------------------
    # Def a node as attribute node
    
    def attribute_node(self, node):
        """ Define an input node as attribute

        Called when creating an input node in a property getter. Performs two actions:
            
            - Call the method :func:`Node.as_attribute` to tag the node as being an attribute.
              This will allow the :func:`Tree.check_attributes` to see if it is necessary to create
              a *Capture Attribute* for this field.
            - Set the node property :attr:`attr_domain` to self in order to implement the transfer attribute
              mechanism.
        
        Args:
            - node (Node): The node created by the domain
            
        Returns:
            The node argument        
        """
        
        return self.data_socket.attribute_node(node, domain=self)

    # ----------------------------------------------------------------------------------------------------
    # Access by index
    
    def __getitem__(self, index):
        
        return self.select(index)

    # ----------------------------------------------------------------------------------------------------
    # To viewer
    
    def view(self, socket=None, label=None, node_color=None):
        """ To viewer.
        
        Create a **Viewer** node with the domain geometry as input and the provided socket.
        
        Args:
            socket (DataSocket): The value to view  
        """
        return self.data_socket.node.tree.view(geometry=self.data_socket, socket=socket, domain=self.domain, label=label, node_color=node_color)
    
    # ----------------------------------------------------------------------------------------------------
    # Force a domain change
    #
    # For instance, it can be used to manage the faces of instances of meshes
    
    @property
    def as_verts(self):
        """ Type cast to Vertex."""
        from geonodes.nodes.classes import Vertex
        return Vertex(self.data_socket)
        
    @property
    def as_edges(self):
        """ Type cast to Edge."""
        from geonodes.nodes.classes import Edge
        return Edge(self.data_socket)
        
    @property
    def as_faces(self):
        """ Type cast to Face."""
        from geonodes.nodes.classes import Face
        return Face(self.data_socket)
        
    @property
    def as_corners(self):
        """ Type cast to Corner."""
        from geonodes.nodes.classes import Corner
        return Corner(self.data_socket)
        
    @property
    def as_control_points(self):
        """ Type cast to ControlPoint."""
        from geonodes.nodes.classes import ControlPoint
        return ControlPoint(self.data_socket)

    @property
    def as_splines(self):
        """ Type cast to Spline."""
        from geonodes.nodes.classes import Spline
        return Spline(self.data_socket)
        
    @property
    def as_cloud_points(self):
        """ Type cast to CloudPoint."""
        from geonodes.nodes.classes import CloudPoint
        return CloudPoint(self.data_socket)
        
    @property
    def as_insts(self):
        """ Type cast to Instance."""
        from geonodes.nodes.classes import Instance
        return Instance(self.data_socket)
    
    # ----------------------------------------------------------------------------------------------------
    # Geometry domain
    
    @staticmethod
    def geo_dom(geometry, domain='POINT'):
        """ Split a domain into (geometry, domain code)
        
        Nodes such as 'sample_index' or 'sample_nearest' need a geometry and a domain code:
            
        ``` python
        def sample_index(self, geometry=None, value=None, index=None, clamp=False, domain='POINT'):
        ```
        
        One can pass a domain rather that a geometry. In that case, this utility get the proper domain code
        to pass to the node.
        
        ``` python
            return self.default_domain.attribute_node(nodes.SampleNearest(
                geometry         = Domain.geo_dom(geometry, domain)[0],
                sample_position  = sample_position, 
                domain           = Domain.geo_dom(geometry, domain)[1]
                )).index
        ``` 
        """
        
        if hasattr(geometry, 'is_domain_class'):
            return geometry.data_socket, geometry.domain
        else:
            return geometry, domain
    
    
    # ----------------------------------------------------------------------------------------------------
    # Points matrix
    
    def matrix(self, points=None):
        """ Return a PointsMatrix with another POINT geometry.
        
        This geometry is the x geometry and the points geometry is the y axis.
        
        Raises an error if one of these two geometries as no POINT domain.
        
        See [PointsMatrix](PointsMatrix.md) for more documentation.
        
        Args:
        - points (Mesh, Points, Curve) : the y geometry of the matrix to build
        
        Returns:
        - instance of PointsMatrix
        """
        
        import geonodes as gn
        
        return gn.PointsMatrix(self.data_socket, points)
    
    # ====================================================================================================
    # Methods implemented manually
    
    # ----------------------------------------------------------------------------------------------------
    # Geometry proximity
    
    def geometry_proximity(self, target=None, source_position=None, target_element='FACES'):
        """

        > Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

        #### Args:
        - target: Geometry
        - source_position: Vector
        - target_element (str): 'FACES' in [POINTS, EDGES, FACES]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeProximity.webp)

        #### Returns:
        - node with sockets ['position', 'distance']


        """
        
        from geonodes.nodes import nodes
        
        geo, dom = self.geo_dom(target, target_element)
        if dom == 'POINT':
            dom = 'POINTS'
        elif dom == 'EDGE':
            dom = 'EDGES'
        elif dom == 'FACE':
            dom == 'FACESS'
        else:
            raise Exception(f"geometry proximity error: the domain of the target {target} must be POINTS, EDGES or FACES, not '{dom}'.")

        return self.attribute_node(nodes.GeometryProximity(target=geo, source_position=source_position, target_element=dom))

    

    
    

    
    


    