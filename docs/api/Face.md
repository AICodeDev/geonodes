# Class Face

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 > **Face** is one of the four [domains](Domain.md) of [Mesh](Mesh.md).

It uses the *'FACE'* string domain.




### Constructor

```python
Face(self, data_socket, selection=None)
```


#### Args:
- data_socket (DataSocket): the data class the domain belongs to
- selection (any): the selection to use



## Content

**Properties**

[ID](#ID) | [area](#area) | [as_cloud_points](#as_cloud_points) | [as_control_points](#as_control_points) | [as_corners](#as_corners) | [as_edges](#as_edges) | [as_faces](#as_faces) | [as_insts](#as_insts) | [as_splines](#as_splines) | [as_verts](#as_verts) | [count](#count) | [data_socket](#data_socket) | [domain](#domain) | [domain_index](#domain_index) | [index](#index) | [island](#island) | [material](#material) | [material_index](#material_index) | [neighbors](#neighbors) | [normal](#normal) | [position](#position) | [position_offset](#position_offset) | [selection](#selection) | [selection_index](#selection_index) | [shade_smooth](#shade_smooth)

**Class and static methods**

[geo_dom](#geo_dom) | [random_boolean](#random_boolean) | [random_float](#random_float) | [random_integer](#random_integer) | [random_vector](#random_vector)

**Methods**

[accumulate_field](#accumulate_field) | [attribute_node](#attribute_node) | [attribute_statistic](#attribute_statistic) | [blur_attribute](#blur_attribute) | [blur_color](#blur_color) | [blur_float](#blur_float) | [blur_integer](#blur_integer) | [blur_vector](#blur_vector) | [capture_attribute](#capture_attribute) | [corners](#corners) | [delete](#delete) | [delete_all](#delete_all) | [delete_edges](#delete_edges) | [delete_faces](#delete_faces) | [distribute_points](#distribute_points) | [distribute_points_poisson](#distribute_points_poisson) | [distribute_points_random](#distribute_points_random) | [duplicate](#duplicate) | [extrude](#extrude) | [face_group_boundaries](#face_group_boundaries) | [flip](#flip) | [geometry_proximity](#geometry_proximity) | [index_for_sample](#index_for_sample) | [index_of_nearest](#index_of_nearest) | [is_planar](#is_planar) | [material_selection](#material_selection) | [matrix](#matrix) | [named_attribute](#named_attribute) | [named_boolean](#named_boolean) | [named_color](#named_color) | [named_float](#named_float) | [named_integer](#named_integer) | [named_vector](#named_vector) | [pack_uv_islands](#pack_uv_islands) | [raycast](#raycast) | [raycast_interpolated](#raycast_interpolated) | [raycast_nearest](#raycast_nearest) | [remove_named_attribute](#remove_named_attribute) | [sample_index](#sample_index) | [sample_nearest](#sample_nearest) | [scale_single_axis](#scale_single_axis) | [scale_uniform](#scale_uniform) | [select](#select) | [separate](#separate) | [set_ID](#set_ID) | [set_material](#set_material) | [set_material_index](#set_material_index) | [set_position](#set_position) | [set_shade_smooth](#set_shade_smooth) | [socket_stack](#socket_stack) | [store_named_2D_vector](#store_named_2D_vector) | [store_named_attribute](#store_named_attribute) | [store_named_boolean](#store_named_boolean) | [store_named_byte_color](#store_named_byte_color) | [store_named_color](#store_named_color) | [store_named_float](#store_named_float) | [store_named_integer](#store_named_integer) | [store_named_vector](#store_named_vector) | [triangulate](#triangulate) | [uv_unwrap](#uv_unwrap) | [view](#view) | [viewer](#viewer)

## Properties

### ID



> Node: [ID](GeometryNodeInputID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

#### Returns:
- socket `ID`






Setter



> Node: [Set ID](GeometryNodeSetID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

Node implemented as property setter.

#### Args:
- attr_value: ID







<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### area



> Node: [Face Area](GeometryNodeInputMeshFaceArea.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_area.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html)

#### Returns:
- node with sockets ['area']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_cloud_points

 Type cast to CloudPoint.


<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_control_points

 Type cast to ControlPoint.


<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_corners

 Type cast to Corner.


<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_edges

 Type cast to Edge.


<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_faces

 Type cast to Face.


<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_insts

 Type cast to Instance.


<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_splines

 Type cast to Spline.


<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_verts

 Type cast to Vertex.


<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### count



> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `face_count`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### data_socket

 Returns the data socket it belongs to.       

#### Returns:
- DataSocket



<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### domain

 Gives the **Geometry Nodes** domain string to use in the generated nodes.

- Vertex        : 'POINT',
- Edge          : 'EDGE',
- Face          : 'FACE',
- Corner        : 'CORNER',
- ControlPoint  : 'POINT',
- Spline        : 'CURVE',
- CloudPoint    : 'POINT',
- Instance      : 'INSTANCE',

#### Returns:
- domain string (str)



<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### domain_index



> Node: [Index](GeometryNodeInputIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### index



> Node: [Index](GeometryNodeInputIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### island



> Node: [Mesh Island](GeometryNodeInputMeshIsland.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshIsland.webp)

#### Returns:
- node with sockets ['island_index', 'island_count']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### material



> Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

'material' is a write only property.
Raise an exception if attempt to read.







Setter



> Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

Node implemented as property setter.

#### Args:
- attr_value: material







<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### material_index



> Node: [Material Index](GeometryNodeInputMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

#### Returns:
- socket `material_index`






Setter



> Node: [Set Material Index](GeometryNodeSetMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

Node implemented as property setter.

#### Args:
- attr_value: material_index







<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### neighbors



> Node: [Face Neighbors](GeometryNodeInputMeshFaceNeighbors.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshFaceNeighbors.webp)

#### Returns:
- node with sockets ['vertex_count', 'face_count']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### normal



> Node: [Normal](GeometryNodeInputNormal.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

#### Returns:
- socket `normal`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### position



> Node: [Position](GeometryNodeInputPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

#### Returns:
- socket `position`






Setter



> Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

Node implemented as property setter.

#### Args:
- attr_value: position







<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### position_offset



> Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

'position_offset' is a write only property.
Raise an exception if attempt to read.







Setter



> Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

Node implemented as property setter.

#### Args:
- attr_value: offset







<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### selection

 Returns the selection value to use in nodes with a **Selection** socket.  

#### Returns:
- Boolean



<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### selection_index

 Returns the selection index.

> CAUTION: raise an error if the selection is not a integer.

#### Returns:
- Integer



<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### shade_smooth



> Node: [Is Shade Smooth](GeometryNodeInputShadeSmooth.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)

#### Returns:
- socket `smooth`






Setter



> Node: [Set Shade Smooth](GeometryNodeSetShadeSmooth.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)

Node implemented as property setter.

#### Args:
- attr_value: shade_smooth







<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Class and static methods

### geo_dom

```python
@staticmethod
def geo_dom(geometry, domain='POINT')
```

 Split a domain into (geometry, domain code)

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




<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_boolean

```python
@staticmethod
def random_boolean(probability=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- probability: Float
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_float

```python
@staticmethod
def random_float(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_integer

```python
@staticmethod
def random_integer(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_vector

```python
@staticmethod
def random_vector(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### accumulate_field

```python
def accumulate_field(self, value=None, group_id=None)
```



> Node: [Accumulate Field](GeometryNodeAccumulateField.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)

#### Args:
- value: ['Vector', 'Float', 'Integer']
- group_id: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

#### Returns:
- node with sockets ['leading', 'trailing', 'total']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_node

```python
def attribute_node(self, node)
```

 Define an input node as attribute

Called when creating an input node in a property getter. Performs two actions:
    
    - Call the method :func:`Node.as_attribute` to tag the node as being an attribute.
      This will allow the :func:`Tree.check_attributes` to see if it is necessary to create
      a *Capture Attribute* for this field.
    - Set the node property :attr:`attr_domain` to self in order to implement the transfer attribute
      mechanism.

#### Args:
- node (Node): The node created by the domain
    
#### Returns:
- The node argument




<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_statistic

```python
def attribute_statistic(self, attribute=None)
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

#### Returns:
- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### blur_attribute

```python
def blur_attribute(self, value=None, iterations=None, weight=None)
```



> Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color']
- iterations: Integer
- weight: Float

#### Returns:
- socket `value`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### blur_color

```python
def blur_color(self, value=None, iterations=None, weight=None)
```



> Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color']
- iterations: Integer
- weight: Float

#### Returns:
- socket `value`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### blur_float

```python
def blur_float(self, value=None, iterations=None, weight=None)
```



> Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color']
- iterations: Integer
- weight: Float

#### Returns:
- socket `value`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### blur_integer

```python
def blur_integer(self, value=None, iterations=None, weight=None)
```



> Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color']
- iterations: Integer
- weight: Float

#### Returns:
- socket `value`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### blur_vector

```python
def blur_vector(self, value=None, iterations=None, weight=None)
```



> Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color']
- iterations: Integer
- weight: Float

#### Returns:
- socket `value`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_attribute

```python
def capture_attribute(self, value=None)
```



> Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### corners

```python
def corners(self, weights=None, sort_index=None)
```



> Node: [Corners of Face](GeometryNodeCornersOfFace.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_face.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfFace.html)

#### Args:
- weights: Float
- sort_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfFace.webp)

#### Returns:
- node with sockets ['corner_index', 'total']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete

```python
def delete(self, mode='ALL')
```



> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete_all

```python
def delete_all(self)
```



> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete_edges

```python
def delete_edges(self)
```



> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete_faces

```python
def delete_faces(self)
```



> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### distribute_points

```python
def distribute_points(self, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', use_legacy_normal=False)
```



> Node: [Distribute Points on Faces](GeometryNodeDistributePointsOnFaces.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)

#### Args:
- distance_min: Float
- density_max: Float
- density: Float
- density_factor: Float
- seed: Integer
- distribute_method (str): 'RANDOM' in [RANDOM, POISSON]
- use_legacy_normal (bool): False

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsOnFaces.webp)

#### Returns:
- node with sockets ['points', 'normal', 'rotation']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### distribute_points_poisson

```python
def distribute_points_poisson(self, distance_min=None, density_max=None, density_factor=None, seed=None, use_legacy_normal=False)
```



> Node: [Distribute Points on Faces](GeometryNodeDistributePointsOnFaces.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)

#### Args:
- distance_min: Float
- density_max: Float
- density_factor: Float
- seed: Integer
- use_legacy_normal (bool): False

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsOnFaces.webp)

#### Returns:
- node with sockets ['points', 'normal', 'rotation']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### distribute_points_random

```python
def distribute_points_random(self, density=None, seed=None, use_legacy_normal=False)
```



> Node: [Distribute Points on Faces](GeometryNodeDistributePointsOnFaces.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)

#### Args:
- density: Float
- seed: Integer
- use_legacy_normal (bool): False

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsOnFaces.webp)

#### Returns:
- node with sockets ['points', 'normal', 'rotation']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### duplicate

```python
def duplicate(self, amount=None)
```



> Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- amount: Integer

#### Returns:
- socket `duplicate_index`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### extrude

```python
def extrude(self, offset=None, offset_scale=None, individual=None)
```



> Node: [Extrude Mesh](GeometryNodeExtrudeMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

#### Args:
- offset: Vector
- offset_scale: Float
- individual: Boolean

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

#### Returns:
- node with sockets ['mesh', 'top', 'side']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### face_group_boundaries

```python
def face_group_boundaries(self, face_group_id=None)
```



> Node: [Face Group Boundaries](GeometryNodeMeshFaceSetBoundaries.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/a.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)

#### Args:
- face_group_id: Integer

#### Returns:
- socket `boundary_edges`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### flip

```python
def flip(self)
```



> Node: [Flip Faces](GeometryNodeFlipFaces.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### geometry_proximity

```python
def geometry_proximity(self, target=None, source_position=None, target_element='FACES')
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector
- target_element (str): 'FACES' in [POINTS, EDGES, FACES]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeProximity.webp)

#### Returns:
- node with sockets ['position', 'distance']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### index_for_sample

```python
def index_for_sample(self, default=None)
```

 Return default if not None or Input index socket.

The node 'Sample Index' has an input with default value to 0.
If mehod argument is None, create a node 'Input Index' as input.

**sample_index** method is implemented:
    
```python
def sample_index(self, value=None, index=None, clamp=False):
    return nodes.SampleIndex(..., index=self.index_for_sample(index), ...)
```

#### Returns:
- default or Input index



<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### index_of_nearest

```python
def index_of_nearest(self, position=None, group_id=None)
```



> Node: [Index of Nearest](GeometryNodeIndexOfNearest.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/n.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeIndexOfNearest.html)

#### Args:
- position: Vector
- group_id: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeIndexOfNearest.webp)

#### Returns:
- node with sockets ['index', 'has_neighbor']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_planar

```python
def is_planar(self, threshold=None)
```



> Node: [Is Face Planar](GeometryNodeInputMeshFaceIsPlanar.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/s.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)

#### Args:
- threshold: Float

#### Returns:
- socket `planar`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### material_selection

```python
def material_selection(self, material=None)
```



> Node: [Material Selection](GeometryNodeMaterialSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

#### Args:
- material: Material

#### Returns:
- socket `selection`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### matrix

```python
def matrix(self, points=None)
```

 Return a PointsMatrix with another POINT geometry.

This geometry is the x geometry and the points geometry is the y axis.

Raises an error if one of these two geometries as no POINT domain.

See [PointsMatrix](PointsMatrix.md) for more documentation.

#### Args:
- points (Mesh, Points, Curve) : the y geometry of the matrix to build

#### Returns:
- instance of PointsMatrix




<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_attribute

```python
def named_attribute(self, name=None, data_type='FLOAT')
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputNamedAttribute.webp)

#### Returns:
- node with sockets ['attribute', 'exists']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_boolean

```python
def named_boolean(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_color

```python
def named_color(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_float

```python
def named_float(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_integer

```python
def named_integer(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_vector

```python
def named_vector(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### pack_uv_islands

```python
def pack_uv_islands(self, uv=None, margin=None, rotate=None)
```



> Node: [Pack UV Islands](GeometryNodeUVPackIslands.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)

#### Args:
- uv: Vector
- margin: Float
- rotate: Boolean

#### Returns:
- socket `uv`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast

```python
def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED')
```



> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float
- mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast_interpolated

```python
def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```



> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast_nearest

```python
def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```



> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### remove_named_attribute

```python
def remove_named_attribute(self, name=None)
```



> Node: [Remove Named Attribute](GeometryNodeRemoveAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

#### Args:
- name: String

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_index

```python
def sample_index(self, geometry=None, value=None, index=None, clamp=False, domain='POINT')
```



> Node: [Sample Index](GeometryNodeSampleIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

#### Args:
- geometry: Geometry
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_nearest

```python
def sample_nearest(self, geometry=None, sample_position=None, domain='POINT')
```



> Node: [Sample Nearest](GeometryNodeSampleNearest.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

#### Args:
- geometry: Geometry
- sample_position: Vector
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER]

#### Returns:
- socket `index`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### scale_single_axis

```python
def scale_single_axis(self, scale=None, center=None, axis=None)
```



> Node: [Scale Elements](GeometryNodeScaleElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- scale: Float
- center: Vector
- axis: Vector

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### scale_uniform

```python
def scale_uniform(self, scale=None, center=None)
```



> Node: [Scale Elements](GeometryNodeScaleElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- scale: Float
- center: Vector

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### select

```python
def select(self, selection)
```

 Select the domain

If the method is called on a **Domain** which already has a selection, the two selections are combined:
    
```python
verts = mesh.verts[10:20] # Selection of vertices from 10 to 20
v = verts.select((verts.index % 2).equal(0)) # Even indices in the previous selection
```

#### Args:
- selection (Boolean or Integer): The selection condition
    
#### Returns:
- Domain with the given selection (Domain)

If a selection is existing, the resulting selection is a logical and betwenn the two




<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate

```python
def separate(self)
```



> Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

#### Returns:
- node with sockets ['selection', 'inverted']






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_ID

```python
def set_ID(self, ID=None)
```



> Node: [Set ID](GeometryNodeSetID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

#### Args:
- ID: Integer

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_material

```python
def set_material(self, material=None)
```



> Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

#### Args:
- material: Material

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_material_index

```python
def set_material_index(self, material_index=None)
```



> Node: [Set Material Index](GeometryNodeSetMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

#### Args:
- material_index: Integer

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_position

```python
def set_position(self, position=None, offset=None)
```



> Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

#### Args:
- position: Vector
- offset: Vector

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_shade_smooth

```python
def set_shade_smooth(self, shade_smooth=None)
```



> Node: [Set Shade Smooth](GeometryNodeSetShadeSmooth.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)

#### Args:
- shade_smooth: Boolean

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### socket_stack

```python
def socket_stack(self, node, socket_name=None)
```

 Make the owning socket jump to the output socket of the node passed in argumment.

#### Args:
- node (Node): The node to jump to
- socket_name: The name of the output socket (first one if None)



<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_2D_vector

```python
def store_named_2D_vector(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_attribute

```python
def store_named_attribute(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_boolean

```python
def store_named_boolean(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_byte_color

```python
def store_named_byte_color(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_color

```python
def store_named_color(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_float

```python
def store_named_float(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_integer

```python
def store_named_integer(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_vector

```python
def store_named_vector(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### triangulate

```python
def triangulate(self, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL')
```



> Node: [Triangulate](GeometryNodeTriangulate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)

#### Args:
- minimum_vertices: Integer
- ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
- quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]

#### Returns:
- self






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### uv_unwrap

```python
def uv_unwrap(self, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED')
```



> Node: [UV Unwrap](GeometryNodeUVUnwrap.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)

#### Args:
- seam: Boolean
- margin: Float
- fill_holes: Boolean
- method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]

#### Returns:
- socket `uv`






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### view

```python
def view(self, value=None)
```



> Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

#### Args:
- value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']

#### Returns:
- node with sockets []






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### viewer

```python
def viewer(self, value=None)
```



> Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

#### Args:
- value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']

#### Returns:
- node with sockets []






<sub>Go to [top](#class-Face) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

