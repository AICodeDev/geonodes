# Class Volume

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 > **Volume** sub class of [Geometry](Geometry.md)

**Volume** has no [Domain](Domain.md)




### Constructor

```python
Volume(self, socket, node=None, label=None)
```

## Content

**Properties**

[bounding_box](#bounding_box) | [convex_hull](#convex_hull) | [curve_component](#curve_component) | [domain_size](#domain_size) | [instances_component](#instances_component) | [mesh_component](#mesh_component) | [points_component](#points_component) | [separate_components](#separate_components) | [volume_component](#volume_component)

***Inherited***

[bl_idname](DataSocket.md#bl_idname) | [bnode](DataSocket.md#bnode) | [is_multi_input](DataSocket.md#is_multi_input) | [is_output](DataSocket.md#is_output) | [is_plugged](DataSocket.md#is_plugged) | [links](DataSocket.md#links) | [name](DataSocket.md#name) | [node_chain_label](DataSocket.md#node_chain_label) | [socket_index](DataSocket.md#socket_index)

**Class and static methods**

[Collection](#Collection) | [Cube](#Cube) | [FromCollection](#FromCollection) | [Input](#Input) | [SdfSphere](#SdfSphere) | [capture_attribute_node](#capture_attribute_node) | [random_boolean](#random_boolean) | [random_float](#random_float) | [random_integer](#random_integer) | [random_vector](#random_vector)

***Inherited***

[geo_dom](DataSocket.md#geo_dom) | [get_bl_idname](DataSocket.md#get_bl_idname) | [get_class_name](DataSocket.md#get_class_name) | [gives_bsocket](DataSocket.md#gives_bsocket) | [is_socket](DataSocket.md#is_socket) | [is_vector](DataSocket.md#is_vector) | [python_type_to_socket](DataSocket.md#python_type_to_socket) | [value_data_type](DataSocket.md#value_data_type)

**Methods**

[attribute_node](#attribute_node) | [attribute_statistic](#attribute_statistic) | [capture_attribute](#capture_attribute) | [delete](#delete) | [distribute_points](#distribute_points) | [distribute_points_grid](#distribute_points_grid) | [distribute_points_random](#distribute_points_random) | [duplicate](#duplicate) | [instantiate](#instantiate) | [join](#join) | [matrix](#matrix) | [mean_filter_sdf_volume](#mean_filter_sdf_volume) | [merge_by_distance](#merge_by_distance) | [offset_sdf_volume](#offset_sdf_volume) | [raycast](#raycast) | [raycast_interpolated](#raycast_interpolated) | [raycast_nearest](#raycast_nearest) | [remove_named_attribute](#remove_named_attribute) | [replace_material](#replace_material) | [sample](#sample) | [sample_boolean](#sample_boolean) | [sample_float](#sample_float) | [sample_index](#sample_index) | [sample_integer](#sample_integer) | [sample_nearest](#sample_nearest) | [sample_vector](#sample_vector) | [separate](#separate) | [set_ID](#set_ID) | [set_material](#set_material) | [set_material_index](#set_material_index) | [set_position](#set_position) | [show_handles](#show_handles) | [store_named_attribute](#store_named_attribute) | [store_named_boolean](#store_named_boolean) | [store_named_color](#store_named_color) | [store_named_float](#store_named_float) | [store_named_integer](#store_named_integer) | [store_named_vector](#store_named_vector) | [switch](#switch) | [to_instance](#to_instance) | [to_mesh](#to_mesh) | [transform](#transform) | [transform_geometry](#transform_geometry) | [view](#view) | [viewer](#viewer)

***Inherited***

[capture](DataSocket.md#capture) | [connected_sockets](DataSocket.md#connected_sockets) | [geometry_proximity](DataSocket.md#geometry_proximity) | [get_blender_socket](DataSocket.md#get_blender_socket) | [init_domains](DataSocket.md#init_domains) | [init_socket](DataSocket.md#init_socket) | [plug](DataSocket.md#plug) | [reroute](DataSocket.md#reroute) | [reset_properties](DataSocket.md#reset_properties) | [stack](DataSocket.md#stack) | [to_output](DataSocket.md#to_output)

## Properties

### bounding_box



> Node: [Bounding Box](GeometryNodeBoundBox.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeBoundBox.webp)

#### Returns:
- node with sockets ['bounding_box', 'min', 'max']






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### convex_hull



> Node: [Convex Hull](GeometryNodeConvexHull.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)

#### Returns:
- socket `convex_hull` of class Mesh






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### curve_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `curve` of class Curve






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### domain_size



> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeDomainSize.webp)

#### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instances_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `instances` of class Instances






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mesh_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `mesh` of class Mesh






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### points_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `point_cloud` of class Points






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate_components



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateComponents.webp)

#### Returns:
- node with sockets ['mesh', 'curve', 'point_cloud', 'volume', 'instances']






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### volume_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `volume` of class Volume






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Class and static methods

### Collection

```python
@classmethod
def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL')
```



> Node: [Collection Info](GeometryNodeCollectionInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)

#### Args:
- collection: Collection
- separate_children: Boolean
- reset_children: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `instances`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Cube

```python
@classmethod
def Cube(cls, density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None)
```



> Node: [Volume Cube](GeometryNodeVolumeCube.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_cube.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeCube.html)

#### Args:
- density: Float
- background: Float
- min: Vector
- max: Vector
- resolution_x: Integer
- resolution_y: Integer
- resolution_z: Integer

#### Returns:
- socket `volume`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### FromCollection

```python
@classmethod
def FromCollection(cls, collection=None, separate_children
```

 Get the geometry from a collection



<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Input

```python
@classmethod
def Input(cls, name = None, description = "")
```

 Create a Geometry input socket in the Group Input Node

#### Args:
- name: The socket name
- description: User tip
    
#### Returns:
- Geometry: The Geometry data socket
    
> Note: This method create a new input socket in the Group Input node. To get the **default** input geometry,
  use [Tree.input_geometry](#Tree.md#input_geometry) property.
    



<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### SdfSphere

```python
@classmethod
def SdfSphere(cls, radius=None, voxel_size=None, half_band_width=None)
```



> Node: [SDF Volume Sphere](GeometryNodeSDFVolumeSphere.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/d.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSDFVolumeSphere.html)

#### Args:
- radius: Float
- voxel_size: Float
- half_band_width: Float

#### Returns:
- socket `volume`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_attribute_node

```python
@staticmethod
def capture_attribute_node(geometry=None, value=None, data_type='FLOAT', domain='POINT')
```



> Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- geometry: Geometry
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

#### Returns:
- node with sockets ['geometry', 'attribute']






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### attribute_node

```python
def attribute_node(self, node, domain=None)
```

 Set the node as being an attribute of the geometry.

All the output sockets of the node will have their 'attr_bsocket' property set to this geometry.        

#### Args:
- node: the attribute node of the geometry
- domain (node): the domain of the attribute. If None, the default domain is taken

#### Returns:
- The attribute node




<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_statistic

```python
def attribute_statistic(self, selection=None, attribute=None, domain='POINT')
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- selection: Boolean
- attribute: ['Float', 'Vector']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

#### Returns:
- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_attribute

```python
def capture_attribute(self, value=None, domain='POINT')
```



> Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete

```python
def delete(self, selection=None, domain='POINT', mode='ALL')
```



> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### distribute_points

```python
def distribute_points(self, density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM')
```



> Node: [Distribute Points in Volume](GeometryNodeDistributePointsInVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)

#### Args:
- density: Float
- seed: Integer
- spacing: Vector
- threshold: Float
- mode (str): 'DENSITY_RANDOM' in [DENSITY_RANDOM, DENSITY_GRID]

#### Returns:
- socket `points` of class Points






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### distribute_points_grid

```python
def distribute_points_grid(self, spacing=None, threshold=None)
```



> Node: [Distribute Points in Volume](GeometryNodeDistributePointsInVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)

#### Args:
- spacing: Vector
- threshold: Float

#### Returns:
- socket `points` of class Points






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### distribute_points_random

```python
def distribute_points_random(self, density=None, seed=None)
```



> Node: [Distribute Points in Volume](GeometryNodeDistributePointsInVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)

#### Args:
- density: Float
- seed: Integer

#### Returns:
- socket `points` of class Points






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### duplicate

```python
def duplicate(self, selection=None, amount=None, domain='POINT')
```



> Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- selection: Boolean
- amount: Integer
- domain (str): 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]

#### Returns:
- socket `duplicate_index`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instantiate

```python
def instantiate(self, count = 1, realize = False)
```

 Instantiate the geometry

#### Args:
- count: Number of instances to create
- realize: True to realize the instances
    
#### Returns:
- Instances or Geometry
    
The duplication is performed by instantiating the geometry along the vertices
of a Mesh Line initialized with `count` points.

The operator ``*`` can be used to operate this method with `realize = False`:
    
```python
    
curves = curve * 10

# is equivalent to

curves = curve.duplicate(10, realize=False)
```




<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### join

```python
def join(*geometry)
```



> Node: [Join Geometry](GeometryNodeJoinGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)

#### Args:
- geometry: <m>Geometry

#### Returns:
- socket `geometry`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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




<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mean_filter_sdf_volume

```python
def mean_filter_sdf_volume(self, iterations=None, width=None)
```



> Node: [Mean Filter SDF Volume](GeometryNodeMeanFilterSDFVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/e.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeanFilterSDFVolume.html)

#### Args:
- iterations: Integer
- width: Integer

#### Returns:
- socket `volume` of class Volume






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### merge_by_distance

```python
def merge_by_distance(self, selection=None, distance=None, mode='ALL')
```



> Node: [Merge by Distance](GeometryNodeMergeByDistance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)

#### Args:
- selection: Boolean
- distance: Float
- mode (str): 'ALL' in [ALL, CONNECTED]

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### offset_sdf_volume

```python
def offset_sdf_volume(self, distance=None)
```



> Node: [Offset SDF Volume](GeometryNodeOffsetSDFVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/f.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetSDFVolume.html)

#### Args:
- distance: Float

#### Returns:
- socket `volume`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### remove_named_attribute

```python
def remove_named_attribute(self, name=None)
```



> Node: [Remove Named Attribute](GeometryNodeRemoveAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

#### Args:
- name: String

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### replace_material

```python
def replace_material(self, old=None, new=None)
```



> Node: [Replace Material](GeometryNodeReplaceMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)

#### Args:
- old: Material
- new: Material

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample

```python
def sample(self, grid=None, position=None, grid_type='FLOAT', interpolation_mode='TRILINEAR')
```



> Node: [Sample Volume](GeometryNodeSampleVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/a.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleVolume.html)

#### Args:
- grid: ['Vector', 'Float', 'Boolean', 'Integer']
- position: Vector
- grid_type (str): 'FLOAT' in [FLOAT, FLOAT_VECTOR, INT, BOOLEAN]
- interpolation_mode (str): 'TRILINEAR' in [NEAREST, TRILINEAR, TRIQUADRATIC]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_boolean

```python
def sample_boolean(self, grid=None, position=None, interpolation_mode='TRILINEAR')
```



> Node: [Sample Volume](GeometryNodeSampleVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/a.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleVolume.html)

#### Args:
- grid: ['Vector', 'Float', 'Boolean', 'Integer']
- position: Vector
- interpolation_mode (str): 'TRILINEAR' in [NEAREST, TRILINEAR, TRIQUADRATIC]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_float

```python
def sample_float(self, grid=None, position=None, interpolation_mode='TRILINEAR')
```



> Node: [Sample Volume](GeometryNodeSampleVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/a.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleVolume.html)

#### Args:
- grid: ['Vector', 'Float', 'Boolean', 'Integer']
- position: Vector
- interpolation_mode (str): 'TRILINEAR' in [NEAREST, TRILINEAR, TRIQUADRATIC]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_integer

```python
def sample_integer(self, grid=None, position=None, interpolation_mode='TRILINEAR')
```



> Node: [Sample Volume](GeometryNodeSampleVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/a.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleVolume.html)

#### Args:
- grid: ['Vector', 'Float', 'Boolean', 'Integer']
- position: Vector
- interpolation_mode (str): 'TRILINEAR' in [NEAREST, TRILINEAR, TRIQUADRATIC]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_vector

```python
def sample_vector(self, grid=None, position=None, interpolation_mode='TRILINEAR')
```



> Node: [Sample Volume](GeometryNodeSampleVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/a.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleVolume.html)

#### Args:
- grid: ['Vector', 'Float', 'Boolean', 'Integer']
- position: Vector
- interpolation_mode (str): 'TRILINEAR' in [NEAREST, TRILINEAR, TRIQUADRATIC]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate

```python
def separate(self, selection=None, domain='POINT')
```



> Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

#### Returns:
- node with sockets ['selection', 'inverted']






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_ID

```python
def set_ID(self, selection=None, ID=None)
```



> Node: [Set ID](GeometryNodeSetID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

#### Args:
- selection: Boolean
- ID: Integer

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_material

```python
def set_material(self, selection=None, material=None)
```



> Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

#### Args:
- selection: Boolean
- material: Material

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_material_index

```python
def set_material_index(self, selection=None, material_index=None)
```



> Node: [Set Material Index](GeometryNodeSetMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

#### Args:
- selection: Boolean
- material_index: Integer

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_position

```python
def set_position(self, selection=None, position=None, offset=None)
```



> Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

#### Args:
- selection: Boolean
- position: Vector
- offset: Vector

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### show_handles

```python
def show_handles(self)
```

 Generate a mesh and cloud points to visualize the control points and handles

#### Returns:
- Geometry: The geometry can be joined to the output
    
Example:
    
```python
curve = ... # Curve initialization

visu = curve.show_handles()

tree.output_geometry = curve + visu
```
    




<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_attribute

```python
def store_named_attribute(self, selection=None, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- selection: Boolean
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_boolean

```python
def store_named_boolean(self, selection=None, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- selection: Boolean
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_color

```python
def store_named_color(self, selection=None, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- selection: Boolean
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_float

```python
def store_named_float(self, selection=None, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- selection: Boolean
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_integer

```python
def store_named_integer(self, selection=None, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- selection: Boolean
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_vector

```python
def store_named_vector(self, selection=None, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- selection: Boolean
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Geometry

#### Returns:
- socket `output`






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_instance

```python
def to_instance(*geometry)
```



> Node: [Geometry to Instance](GeometryNodeGeometryToInstance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)

#### Args:
- geometry: <m>Geometry

#### Returns:
- socket `instances` of class Instances






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_mesh

```python
def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID')
```



> Node: [Volume to Mesh](GeometryNodeVolumeToMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_to_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeToMesh.html)

#### Args:
- voxel_size: Float
- voxel_amount: Float
- threshold: Float
- adaptivity: Float
- resolution_mode (str): 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE]

#### Returns:
- socket `mesh` of class Mesh






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### transform

```python
def transform(self, translation=None, rotation=None, scale=None)
```



> Node: [Transform Geometry](GeometryNodeTransform.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/r.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)

#### Args:
- translation: Vector
- rotation: Vector
- scale: Vector

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### transform_geometry

```python
def transform_geometry(self, translation=None, rotation=None, scale=None)
```



> Node: [Transform Geometry](GeometryNodeTransform.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/r.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)

#### Args:
- translation: Vector
- rotation: Vector
- scale: Vector

#### Returns:
- self






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### view

```python
def view(self, value=None, domain='AUTO')
```



> Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

#### Args:
- value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']
- domain (str): 'AUTO' in [AUTO, POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets []






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### viewer

```python
def viewer(self, value=None, domain='AUTO')
```



> Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

#### Args:
- value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']
- domain (str): 'AUTO' in [AUTO, POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets []






<sub>Go to [top](#class-Volume) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

