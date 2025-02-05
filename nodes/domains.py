from geonodes.nodes import nodes
import geonodes.core.domain as geodom

class Domain(geodom.Domain):
    @property
    def ID(self):
        """

        > Node: [ID](GeometryNodeInputID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

        #### Returns:
        - socket `ID`


        """

        return self.attribute_node(nodes.ID()).ID


    @ID.setter
    def ID(self, attr_value):
        """

        > Node: [Set ID](GeometryNodeSetID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: ID



        """

        self.socket_stack(nodes.SetID(geometry=self.data_socket, selection=self.selection, ID=attr_value))


    def accumulate_field(self, value=None, group_id=None):
        """

        > Node: [Accumulate Field](GeometryNodeAccumulateField.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)

        #### Args:
        - value: ['Vector', 'Float', 'Integer']
        - group_id: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        #### Returns:
        - node with sockets ['leading', 'trailing', 'total']


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.attribute_node(nodes.AccumulateField(value=value, group_id=group_id, data_type=data_type_, domain=self.domain))


    def attribute_statistic(self, attribute=None):
        """

        > Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

        #### Args:
        - attribute: ['Float', 'Vector']

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        #### Returns:
        - node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']


        """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return nodes.AttributeStatistic(geometry=self.data_socket, selection=self.selection, attribute=attribute, data_type=data_type_, domain=self.domain)


    def blur_attribute(self, value=None, iterations=None, weight=None):
        """

        > Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

        #### Args:
        - value: ['Float', 'Integer', 'Vector', 'Color']
        - iterations: Integer
        - weight: Float

        #### Returns:
        - socket `value`


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.attribute_node(nodes.BlurAttribute(value=value, iterations=iterations, weight=weight, data_type=data_type_)).value


    def blur_color(self, value=None, iterations=None, weight=None):
        """

        > Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

        #### Args:
        - value: ['Float', 'Integer', 'Vector', 'Color']
        - iterations: Integer
        - weight: Float

        #### Returns:
        - socket `value`


        """

        return self.attribute_node(nodes.BlurAttribute(value=value, iterations=iterations, weight=weight, data_type='FLOAT_COLOR')).value


    def blur_float(self, value=None, iterations=None, weight=None):
        """

        > Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

        #### Args:
        - value: ['Float', 'Integer', 'Vector', 'Color']
        - iterations: Integer
        - weight: Float

        #### Returns:
        - socket `value`


        """

        return self.attribute_node(nodes.BlurAttribute(value=value, iterations=iterations, weight=weight, data_type='FLOAT')).value


    def blur_integer(self, value=None, iterations=None, weight=None):
        """

        > Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

        #### Args:
        - value: ['Float', 'Integer', 'Vector', 'Color']
        - iterations: Integer
        - weight: Float

        #### Returns:
        - socket `value`


        """

        return self.attribute_node(nodes.BlurAttribute(value=value, iterations=iterations, weight=weight, data_type='INT')).value


    def blur_vector(self, value=None, iterations=None, weight=None):
        """

        > Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

        #### Args:
        - value: ['Float', 'Integer', 'Vector', 'Color']
        - iterations: Integer
        - weight: Float

        #### Returns:
        - socket `value`


        """

        return self.attribute_node(nodes.BlurAttribute(value=value, iterations=iterations, weight=weight, data_type='FLOAT_VECTOR')).value


    def capture_attribute(self, value=None):
        """

        > Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

        #### Args:
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        #### Returns:
        - socket `attribute`


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.socket_stack(nodes.CaptureAttribute(geometry=self.data_socket, value=value, data_type=data_type_, domain=self.domain)).node.attribute


    @property
    def domain_index(self):
        """

        > Node: [Index](GeometryNodeInputIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

        #### Returns:
        - socket `index`


        """

        return self.attribute_node(nodes.Index()).index


    @property
    def index(self):
        """

        > Node: [Index](GeometryNodeInputIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

        #### Returns:
        - socket `index`


        """

        return self.attribute_node(nodes.Index()).index


    def index_of_nearest(self, position=None, group_id=None):
        """

        > Node: [Index of Nearest](GeometryNodeIndexOfNearest.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/n.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeIndexOfNearest.html)

        #### Args:
        - position: Vector
        - group_id: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeIndexOfNearest.webp)

        #### Returns:
        - node with sockets ['index', 'has_neighbor']


        """

        return self.attribute_node(nodes.IndexOfNearest(position=position, group_id=group_id))


    def material_selection(self, material=None):
        """

        > Node: [Material Selection](GeometryNodeMaterialSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

        #### Args:
        - material: Material

        #### Returns:
        - socket `selection`


        """

        return self.attribute_node(nodes.MaterialSelection(material=material)).selection


    def named_attribute(self, name=None, data_type='FLOAT'):
        """

        > Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        #### Args:
        - name: String
        - data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputNamedAttribute.webp)

        #### Returns:
        - node with sockets ['attribute', 'exists']


        """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type=data_type))


    def named_boolean(self, name=None):
        """

        > Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        #### Args:
        - name: String

        #### Returns:
        - socket `attribute`


        """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='BOOLEAN')).attribute


    def named_color(self, name=None):
        """

        > Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        #### Args:
        - name: String

        #### Returns:
        - socket `attribute`


        """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT_COLOR')).attribute


    def named_float(self, name=None):
        """

        > Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        #### Args:
        - name: String

        #### Returns:
        - socket `attribute`


        """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT')).attribute


    def named_integer(self, name=None):
        """

        > Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        #### Args:
        - name: String

        #### Returns:
        - socket `attribute`


        """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='INT')).attribute


    def named_vector(self, name=None):
        """

        > Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

        #### Args:
        - name: String

        #### Returns:
        - socket `attribute`


        """

        return self.attribute_node(nodes.NamedAttribute(name=name, data_type='FLOAT_VECTOR')).attribute


    @property
    def normal(self):
        """

        > Node: [Normal](GeometryNodeInputNormal.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

        #### Returns:
        - socket `normal`


        """

        return self.attribute_node(nodes.Normal()).normal


    @property
    def position(self):
        """

        > Node: [Position](GeometryNodeInputPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

        #### Returns:
        - socket `position`


        """

        return self.attribute_node(nodes.Position()).position


    @position.setter
    def position(self, attr_value):
        """

        > Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: position



        """

        if attr_value is None: return self

        self.socket_stack(nodes.SetPosition(geometry=self.data_socket, selection=self.selection, position=attr_value, offset=None))


    @property
    def position_offset(self):
        """

        > Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

        'position_offset' is a write only property.
        Raise an exception if attempt to read.



        """

        raise Exception("Error: 'position_offset' is a write only property of class Domain!")


    @position_offset.setter
    def position_offset(self, attr_value):
        """

        > Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: offset



        """

        self.socket_stack(nodes.SetPosition(geometry=self.data_socket, selection=self.selection, position=None, offset=attr_value))


    @staticmethod
    def random_boolean(probability=None, ID=None, seed=None):
        """

        > Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        #### Args:
        - probability: Float
        - ID: Integer
        - seed: Integer

        #### Returns:
        - socket `value`


        """

        return nodes.RandomValue(min=None, max=None, probability=probability, ID=ID, seed=seed, data_type='BOOLEAN').value


    @staticmethod
    def random_float(min=None, max=None, ID=None, seed=None):
        """

        > Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        #### Args:
        - min: ['Vector', 'Float', 'Integer']
        - max: ['Vector', 'Float', 'Integer']
        - ID: Integer
        - seed: Integer

        #### Returns:
        - socket `value`


        """

        return nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT').value


    @staticmethod
    def random_integer(min=None, max=None, ID=None, seed=None):
        """

        > Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        #### Args:
        - min: ['Vector', 'Float', 'Integer']
        - max: ['Vector', 'Float', 'Integer']
        - ID: Integer
        - seed: Integer

        #### Returns:
        - socket `value`


        """

        return nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='INT').value


    @staticmethod
    def random_vector(min=None, max=None, ID=None, seed=None):
        """

        > Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

        #### Args:
        - min: ['Vector', 'Float', 'Integer']
        - max: ['Vector', 'Float', 'Integer']
        - ID: Integer
        - seed: Integer

        #### Returns:
        - socket `value`


        """

        return nodes.RandomValue(min=min, max=max, probability=None, ID=ID, seed=seed, data_type='FLOAT_VECTOR').value


    def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """

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


        """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return self.attribute_node(nodes.Raycast(target_geometry=target_geometry, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type_, mapping=mapping))


    def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):
        """

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


        """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return self.attribute_node(nodes.Raycast(target_geometry=target_geometry, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type_, mapping='INTERPOLATED'))


    def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None):
        """

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


        """

        data_type_ = self.value_data_type(attribute, 'FLOAT')
        return self.attribute_node(nodes.Raycast(target_geometry=target_geometry, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length, data_type=data_type_, mapping='NEAREST'))


    def remove_named_attribute(self, name=None):
        """

        > Node: [Remove Named Attribute](GeometryNodeRemoveAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

        #### Args:
        - name: String

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.RemoveNamedAttribute(geometry=self.data_socket, name=name))


    def sample_index(self, geometry=None, value=None, index=None, clamp=False, domain='POINT'):
        """

        > Node: [Sample Index](GeometryNodeSampleIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

        #### Args:
        - geometry: Geometry
        - value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
        - index: Integer
        - clamp (bool): False
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

        #### Returns:
        - socket `value`


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.attribute_node(nodes.SampleIndex(geometry=self.geo_dom(geometry, domain)[0], value=value, index=index, clamp=clamp, data_type=data_type_, domain=self.geo_dom(geometry, domain)[1])).value


    def sample_nearest(self, geometry=None, sample_position=None, domain='POINT'):
        """

        > Node: [Sample Nearest](GeometryNodeSampleNearest.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

        #### Args:
        - geometry: Geometry
        - sample_position: Vector
        - domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER]

        #### Returns:
        - socket `index`


        """

        return self.attribute_node(nodes.SampleNearest(geometry=self.geo_dom(geometry, domain)[0], sample_position=sample_position, domain=self.geo_dom(geometry, domain)[1])).index


    def set_ID(self, ID=None):
        """

        > Node: [Set ID](GeometryNodeSetID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

        #### Args:
        - ID: Integer

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetID(geometry=self.data_socket, selection=self.selection, ID=ID))


    def set_position(self, position=None, offset=None):
        """

        > Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

        #### Args:
        - position: Vector
        - offset: Vector

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetPosition(geometry=self.data_socket, selection=self.selection, position=position, offset=offset))


    def store_named_2D_vector(self, name=None, value=None):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, selection=self.selection, name=name, value=value, data_type='FLOAT2', domain=self.domain))


    def store_named_attribute(self, name=None, value=None):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        #### Returns:
        - self


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, selection=self.selection, name=name, value=value, data_type=data_type_, domain=self.domain))


    def store_named_boolean(self, name=None, value=None):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, selection=self.selection, name=name, value=value, data_type='BOOLEAN', domain=self.domain))


    def store_named_byte_color(self, name=None, value=None):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, selection=self.selection, name=name, value=value, data_type='BYTE_COLOR', domain=self.domain))


    def store_named_color(self, name=None, value=None):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, selection=self.selection, name=name, value=value, data_type='FLOAT_COLOR', domain=self.domain))


    def store_named_float(self, name=None, value=None):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, selection=self.selection, name=name, value=value, data_type='FLOAT', domain=self.domain))


    def store_named_integer(self, name=None, value=None):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, selection=self.selection, name=name, value=value, data_type='INT', domain=self.domain))


    def store_named_vector(self, name=None, value=None):
        """

        > Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

        #### Args:
        - name: String
        - value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.StoreNamedAttribute(geometry=self.data_socket, selection=self.selection, name=name, value=value, data_type='FLOAT_VECTOR', domain=self.domain))


    def view(self, value=None):
        """

        > Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

        #### Args:
        - value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']

        #### Returns:
        - node with sockets []


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return nodes.Viewer(geometry=self.data_socket, value=value, data_type=data_type_, domain=self.domain)


    def viewer(self, value=None):
        """

        > Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

        #### Args:
        - value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']

        #### Returns:
        - node with sockets []


        """

        data_type_ = self.value_data_type(value, 'FLOAT')
        return nodes.Viewer(geometry=self.data_socket, value=value, data_type=data_type_, domain=self.domain)




class Vertex(Domain):
    def corners(self, weights=None, sort_index=None):
        """

        > Node: [Corners of Vertex](GeometryNodeCornersOfVertex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_vertex.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfVertex.html)

        #### Args:
        - weights: Float
        - sort_index: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfVertex.webp)

        #### Returns:
        - node with sockets ['corner_index', 'total']


        """

        return self.attribute_node(nodes.CornersOfVertex(vertex_index=self.selection_index, weights=weights, sort_index=sort_index))


    @property
    def count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `point_count`


        """

        return nodes.DomainSize(geometry=self.data_socket, component='MESH').point_count


    def delete(self, mode='ALL'):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Args:
        - mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def delete_all(self):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ALL'))


    def delete_edges(self):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='EDGE_FACE'))


    def delete_faces(self):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ONLY_FACE'))


    def duplicate(self, amount=None):
        """

        > Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

        #### Args:
        - amount: Integer

        #### Returns:
        - socket `duplicate_index`


        """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def edges(self, weights=None, sort_index=None):
        """

        > Node: [Edges of Vertex](GeometryNodeEdgesOfVertex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_vertex.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)

        #### Args:
        - weights: Float
        - sort_index: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfVertex.webp)

        #### Returns:
        - node with sockets ['edge_index', 'total']


        """

        return self.attribute_node(nodes.EdgesOfVertex(vertex_index=self.selection_index, weights=weights, sort_index=sort_index))


    def extrude(self, offset=None, offset_scale=None, individual=None):
        """

        > Node: [Extrude Mesh](GeometryNodeExtrudeMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

        #### Args:
        - offset: Vector
        - offset_scale: Float
        - individual: Boolean

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

        #### Returns:
        - node with sockets ['mesh', 'top', 'side']


        """

        return self.socket_stack(nodes.ExtrudeMesh(mesh=self.data_socket, selection=self.selection, offset=offset, offset_scale=offset_scale, individual=individual, mode='VERTICES')).node


    def instance_on(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

        > Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

        #### Args:
        - instance: Geometry
        - pick_instance: Boolean
        - instance_index: Integer
        - rotation: Vector
        - scale: Vector

        #### Returns:
        - socket `instances`


        """

        return nodes.InstanceOnPoints(points=self.data_socket, selection=self.selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances


    def interpolate(self, guide_curves=None, guide_up=None, guide_group_id=None, point_up=None, point_group_id=None, max_neighbors=None):
        """

        > Node: [Interpolate Curves](GeometryNodeInterpolateCurves.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/n.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInterpolateCurves.html)

        #### Args:
        - guide_curves: Geometry
        - guide_up: Vector
        - guide_group_id: Integer
        - point_up: Vector
        - point_group_id: Integer
        - max_neighbors: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateCurves.webp)

        #### Returns:
        - node with sockets ['curves', 'closest_index', 'closest_weight']


        """

        return nodes.InterpolateCurves(guide_curves=guide_curves, guide_up=guide_up, guide_group_id=guide_group_id, points=self.data_socket, point_up=point_up, point_group_id=point_group_id, max_neighbors=max_neighbors)


    def merge_by_distance(self, distance=None, mode='ALL'):
        """

        > Node: [Merge by Distance](GeometryNodeMergeByDistance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)

        #### Args:
        - distance: Float
        - mode (str): 'ALL' in [ALL, CONNECTED]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.MergeByDistance(geometry=self.data_socket, selection=self.selection, distance=distance, mode=mode))


    def merge_by_distance_connected(self, distance=None):
        """

        > Node: [Merge by Distance](GeometryNodeMergeByDistance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)

        #### Args:
        - distance: Float

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.MergeByDistance(geometry=self.data_socket, selection=self.selection, distance=distance, mode='CONNECTED'))


    @property
    def neighbors(self):
        """

        > Node: [Vertex Neighbors](GeometryNodeInputMeshVertexNeighbors.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshVertexNeighbors.webp)

        #### Returns:
        - node with sockets ['vertex_count', 'face_count']


        """

        return self.attribute_node(nodes.VertexNeighbors())


    def separate(self):
        """

        > Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        #### Returns:
        - node with sockets ['selection', 'inverted']


        """

        return nodes.SeparateGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain)


    def shortest_edge_paths(self, end_vertex=None, edge_cost=None):
        """

        > Node: [Shortest Edge Paths](GeometryNodeInputShortestEdgePaths.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/shortest_edge_paths.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html)

        #### Args:
        - end_vertex: Boolean
        - edge_cost: Float

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputShortestEdgePaths.webp)

        #### Returns:
        - node with sockets ['next_vertex_index', 'total_cost']


        """

        return self.attribute_node(nodes.ShortestEdgePaths(end_vertex=end_vertex, edge_cost=edge_cost))


    def to_points(self, position=None, radius=None, mode='VERTICES'):
        """

        > Node: [Mesh to Points](GeometryNodeMeshToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)

        #### Args:
        - position: Vector
        - radius: Float
        - mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

        #### Returns:
        - socket `points` of class Points


        """

        import geonodes as gn
        return gn.Points(nodes.MeshToPoints(mesh=self.data_socket, selection=self.selection, position=position, radius=radius, mode=mode).points)


    def to_sdf_volume(self, voxel_size=None, voxel_amount=None, half_band_width=None, resolution_mode='VOXEL_AMOUNT'):
        """

        > Node: [Mesh to SDF Volume](GeometryNodeMeshToSDFVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/e.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToSDFVolume.html)

        #### Args:
        - voxel_size: Float
        - voxel_amount: Float
        - half_band_width: Float
        - resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

        #### Returns:
        - socket `volume` of class Volume


        """

        import geonodes as gn
        return gn.Volume(nodes.MeshToSdfVolume(mesh=self.data_socket, voxel_size=voxel_size, voxel_amount=voxel_amount, half_band_width=half_band_width, resolution_mode=resolution_mode).volume)


    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):
        """

        > Node: [Mesh to Volume](GeometryNodeMeshToVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)

        #### Args:
        - density: Float
        - voxel_size: Float
        - voxel_amount: Float
        - exterior_band_width: Float
        - interior_band_width: Float
        - fill_volume: Boolean
        - resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

        #### Returns:
        - socket `volume` of class Volume


        """

        import geonodes as gn
        return gn.Volume(nodes.MeshToVolume(mesh=self.data_socket, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, exterior_band_width=exterior_band_width, interior_band_width=interior_band_width, fill_volume=fill_volume, resolution_mode=resolution_mode).volume)




class Face(Domain):
    @property
    def area(self):
        """

        > Node: [Face Area](GeometryNodeInputMeshFaceArea.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_area.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html)

        #### Returns:
        - node with sockets ['area']


        """

        return self.attribute_node(nodes.FaceArea())


    def corners(self, weights=None, sort_index=None):
        """

        > Node: [Corners of Face](GeometryNodeCornersOfFace.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_face.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfFace.html)

        #### Args:
        - weights: Float
        - sort_index: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfFace.webp)

        #### Returns:
        - node with sockets ['corner_index', 'total']


        """

        return self.attribute_node(nodes.CornersOfFace(face_index=self.selection_index, weights=weights, sort_index=sort_index))


    @property
    def count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `face_count`


        """

        return nodes.DomainSize(geometry=self.data_socket, component='MESH').face_count


    def delete(self, mode='ALL'):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Args:
        - mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def delete_all(self):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ALL'))


    def delete_edges(self):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='EDGE_FACE'))


    def delete_faces(self):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ONLY_FACE'))


    def distribute_points(self, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', use_legacy_normal=False):
        """

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


        """

        return nodes.DistributePointsOnFaces(mesh=self.data_socket, selection=self.selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method, use_legacy_normal=use_legacy_normal)


    def distribute_points_poisson(self, distance_min=None, density_max=None, density_factor=None, seed=None, use_legacy_normal=False):
        """

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


        """

        return nodes.DistributePointsOnFaces(mesh=self.data_socket, selection=self.selection, distance_min=distance_min, density_max=density_max, density=None, density_factor=density_factor, seed=seed, distribute_method='POISSON', use_legacy_normal=use_legacy_normal)


    def distribute_points_random(self, density=None, seed=None, use_legacy_normal=False):
        """

        > Node: [Distribute Points on Faces](GeometryNodeDistributePointsOnFaces.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)

        #### Args:
        - density: Float
        - seed: Integer
        - use_legacy_normal (bool): False

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsOnFaces.webp)

        #### Returns:
        - node with sockets ['points', 'normal', 'rotation']


        """

        return nodes.DistributePointsOnFaces(mesh=self.data_socket, selection=self.selection, distance_min=None, density_max=None, density=density, density_factor=None, seed=seed, distribute_method='RANDOM', use_legacy_normal=use_legacy_normal)


    def duplicate(self, amount=None):
        """

        > Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

        #### Args:
        - amount: Integer

        #### Returns:
        - socket `duplicate_index`


        """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def extrude(self, offset=None, offset_scale=None, individual=None):
        """

        > Node: [Extrude Mesh](GeometryNodeExtrudeMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

        #### Args:
        - offset: Vector
        - offset_scale: Float
        - individual: Boolean

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

        #### Returns:
        - node with sockets ['mesh', 'top', 'side']


        """

        return self.socket_stack(nodes.ExtrudeMesh(mesh=self.data_socket, selection=self.selection, offset=offset, offset_scale=offset_scale, individual=individual, mode='FACES')).node


    def face_group_boundaries(self, face_group_id=None):
        """

        > Node: [Face Group Boundaries](GeometryNodeMeshFaceSetBoundaries.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/a.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)

        #### Args:
        - face_group_id: Integer

        #### Returns:
        - socket `boundary_edges`


        """

        return self.attribute_node(nodes.FaceGroupBoundaries(face_group_id=face_group_id)).boundary_edges


    def flip(self):
        """

        > Node: [Flip Faces](GeometryNodeFlipFaces.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.FlipFaces(mesh=self.data_socket, selection=self.selection))


    def is_planar(self, threshold=None):
        """

        > Node: [Is Face Planar](GeometryNodeInputMeshFaceIsPlanar.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/s.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)

        #### Args:
        - threshold: Float

        #### Returns:
        - socket `planar`


        """

        return self.attribute_node(nodes.IsFacePlanar(threshold=threshold)).planar


    @property
    def island(self):
        """

        > Node: [Mesh Island](GeometryNodeInputMeshIsland.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshIsland.webp)

        #### Returns:
        - node with sockets ['island_index', 'island_count']


        """

        return self.attribute_node(nodes.MeshIsland())


    @property
    def material(self):
        """

        > Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        'material' is a write only property.
        Raise an exception if attempt to read.



        """

        raise Exception("Error: 'material' is a write only property of class Domain!")


    @material.setter
    def material(self, attr_value):
        """

        > Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: material



        """

        self.socket_stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=attr_value))


    @property
    def material_index(self):
        """

        > Node: [Material Index](GeometryNodeInputMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

        #### Returns:
        - socket `material_index`


        """

        return self.attribute_node(nodes.MaterialIndex()).material_index


    @material_index.setter
    def material_index(self, attr_value):
        """

        > Node: [Set Material Index](GeometryNodeSetMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: material_index



        """

        self.socket_stack(nodes.SetMaterialIndex(geometry=self.data_socket, selection=self.selection, material_index=attr_value))


    @property
    def neighbors(self):
        """

        > Node: [Face Neighbors](GeometryNodeInputMeshFaceNeighbors.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshFaceNeighbors.webp)

        #### Returns:
        - node with sockets ['vertex_count', 'face_count']


        """

        return self.attribute_node(nodes.FaceNeighbors())


    def pack_uv_islands(self, uv=None, margin=None, rotate=None):
        """

        > Node: [Pack UV Islands](GeometryNodeUVPackIslands.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)

        #### Args:
        - uv: Vector
        - margin: Float
        - rotate: Boolean

        #### Returns:
        - socket `uv`


        """

        return self.attribute_node(nodes.PackUvIslands(uv=uv, selection=self.selection, margin=margin, rotate=rotate)).uv


    def scale_single_axis(self, scale=None, center=None, axis=None):
        """

        > Node: [Scale Elements](GeometryNodeScaleElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

        #### Args:
        - scale: Float
        - center: Vector
        - axis: Vector

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=axis, domain=self.domain, scale_mode='SINGLE_AXIS'))


    def scale_uniform(self, scale=None, center=None):
        """

        > Node: [Scale Elements](GeometryNodeScaleElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

        #### Args:
        - scale: Float
        - center: Vector

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=None, domain=self.domain, scale_mode='UNIFORM'))


    def separate(self):
        """

        > Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        #### Returns:
        - node with sockets ['selection', 'inverted']


        """

        return nodes.SeparateGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain)


    def set_material(self, material=None):
        """

        > Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        #### Args:
        - material: Material

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=material))


    def set_material_index(self, material_index=None):
        """

        > Node: [Set Material Index](GeometryNodeSetMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

        #### Args:
        - material_index: Integer

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetMaterialIndex(geometry=self.data_socket, selection=self.selection, material_index=material_index))


    def set_shade_smooth(self, shade_smooth=None):
        """

        > Node: [Set Shade Smooth](GeometryNodeSetShadeSmooth.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)

        #### Args:
        - shade_smooth: Boolean

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetShadeSmooth(geometry=self.data_socket, selection=self.selection, shade_smooth=shade_smooth))


    @property
    def shade_smooth(self):
        """

        > Node: [Is Shade Smooth](GeometryNodeInputShadeSmooth.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)

        #### Returns:
        - socket `smooth`


        """

        return self.attribute_node(nodes.IsShadeSmooth()).smooth


    @shade_smooth.setter
    def shade_smooth(self, attr_value):
        """

        > Node: [Set Shade Smooth](GeometryNodeSetShadeSmooth.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: shade_smooth



        """

        self.socket_stack(nodes.SetShadeSmooth(geometry=self.data_socket, selection=self.selection, shade_smooth=attr_value))


    def triangulate(self, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):
        """

        > Node: [Triangulate](GeometryNodeTriangulate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)

        #### Args:
        - minimum_vertices: Integer
        - ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
        - quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.Triangulate(mesh=self.data_socket, selection=self.selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method))


    def uv_unwrap(self, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):
        """

        > Node: [UV Unwrap](GeometryNodeUVUnwrap.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)

        #### Args:
        - seam: Boolean
        - margin: Float
        - fill_holes: Boolean
        - method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]

        #### Returns:
        - socket `uv`


        """

        return self.attribute_node(nodes.UvUnwrap(selection=self.selection, seam=seam, margin=margin, fill_holes=fill_holes, method=method)).uv




class Edge(Domain):
    @property
    def angle(self):
        """

        > Node: [Edge Angle](GeometryNodeInputMeshEdgeAngle.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshEdgeAngle.webp)

        #### Returns:
        - node with sockets ['unsigned_angle', 'signed_angle']


        """

        return self.attribute_node(nodes.EdgeAngle())


    @property
    def count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `edge_count`


        """

        return nodes.DomainSize(geometry=self.data_socket, component='MESH').edge_count


    def delete(self, mode='ALL'):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Args:
        - mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def delete_all(self):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ALL'))


    def delete_edges(self):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='EDGE_FACE'))


    def delete_faces(self):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode='ONLY_FACE'))


    def duplicate(self, amount=None):
        """

        > Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

        #### Args:
        - amount: Integer

        #### Returns:
        - socket `duplicate_index`


        """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):
        """

        > Node: [Edge Paths to Curves](GeometryNodeEdgePathsToCurves.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)

        #### Args:
        - start_vertices: Boolean
        - next_vertex_index: Integer

        #### Returns:
        - socket `curves` of class Curve


        """

        import geonodes as gn
        return gn.Curve(nodes.EdgePathsToCurves(mesh=self.data_socket, start_vertices=start_vertices, next_vertex_index=next_vertex_index).curves)


    def extrude(self, offset=None, offset_scale=None, individual=None):
        """

        > Node: [Extrude Mesh](GeometryNodeExtrudeMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

        #### Args:
        - offset: Vector
        - offset_scale: Float
        - individual: Boolean

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

        #### Returns:
        - node with sockets ['mesh', 'top', 'side']


        """

        return self.socket_stack(nodes.ExtrudeMesh(mesh=self.data_socket, selection=self.selection, offset=offset, offset_scale=offset_scale, individual=individual, mode='EDGES')).node


    @property
    def neighbors(self):
        """

        > Node: [Edge Neighbors](GeometryNodeInputMeshEdgeNeighbors.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_neighbors.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)

        #### Returns:
        - socket `face_count`


        """

        return self.attribute_node(nodes.EdgeNeighbors()).face_count


    def scale_single_axis(self, scale=None, center=None, axis=None):
        """

        > Node: [Scale Elements](GeometryNodeScaleElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

        #### Args:
        - scale: Float
        - center: Vector
        - axis: Vector

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=axis, domain=self.domain, scale_mode='SINGLE_AXIS'))


    def scale_uniform(self, scale=None, center=None):
        """

        > Node: [Scale Elements](GeometryNodeScaleElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

        #### Args:
        - scale: Float
        - center: Vector

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.ScaleElements(geometry=self.data_socket, selection=self.selection, scale=scale, center=center, axis=None, domain=self.domain, scale_mode='UNIFORM'))


    def separate(self):
        """

        > Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        #### Returns:
        - node with sockets ['selection', 'inverted']


        """

        return nodes.SeparateGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain)


    @property
    def signed_angle(self):
        """

        > Node: [Edge Angle](GeometryNodeInputMeshEdgeAngle.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)

        #### Returns:
        - socket `signed_angle`


        """

        return self.attribute_node(nodes.EdgeAngle()).signed_angle


    def split(self):
        """

        > Node: [Split Edges](GeometryNodeSplitEdges.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SplitEdges(mesh=self.data_socket, selection=self.selection))


    def to_curve(self):
        """

        > Node: [Mesh to Curve](GeometryNodeMeshToCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)

        #### Returns:
        - socket `curve` of class Curve


        """

        import geonodes as gn
        return gn.Curve(nodes.MeshToCurve(mesh=self.data_socket, selection=self.selection).curve)


    @property
    def to_face_groups(self):
        """

        > Node: [Edges to Face Groups](GeometryNodeEdgesToFaceGroups.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/d.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesToFaceGroups.html)

        #### Returns:
        - socket `face_group_id`


        """

        return self.attribute_node(nodes.EdgesToFaceGroups(boundary_edges=self.selection)).face_group_id


    @property
    def unsigned_angle(self):
        """

        > Node: [Edge Angle](GeometryNodeInputMeshEdgeAngle.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)

        #### Returns:
        - socket `unsigned_angle`


        """

        return self.attribute_node(nodes.EdgeAngle()).unsigned_angle


    @property
    def vertices(self):
        """

        > Node: [Edge Vertices](GeometryNodeInputMeshEdgeVertices.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshEdgeVertices.webp)

        #### Returns:
        - node with sockets ['vertex_index_1', 'vertex_index_2', 'position_1', 'position_2']


        """

        return self.attribute_node(nodes.EdgeVertices())




class Corner(Domain):
    @property
    def count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `face_corner_count`


        """

        return nodes.DomainSize(geometry=self.data_socket, component='MESH').face_corner_count


    def edges(self):
        """

        > Node: [Edges of Corner](GeometryNodeEdgesOfCorner.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_corner.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfCorner.webp)

        #### Returns:
        - node with sockets ['next_edge_index', 'previous_edge_index']


        """

        return self.attribute_node(nodes.EdgesOfCorner(corner_index=self.selection_index))


    def face(self):
        """

        > Node: [Face of Corner](GeometryNodeFaceOfCorner.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/face_of_corner.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFaceOfCorner.webp)

        #### Returns:
        - node with sockets ['face_index', 'index_in_face']


        """

        return self.attribute_node(nodes.FaceOfCorner(corner_index=self.selection_index))


    def offset_in_face(self, offset=None):
        """

        > Node: [Offset Corner in Face](GeometryNodeOffsetCornerInFace.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/offset_corner_in_face.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetCornerInFace.html)

        #### Args:
        - offset: Integer

        #### Returns:
        - socket `corner_index`


        """

        return self.attribute_node(nodes.OffsetCornerInFace(corner_index=self.selection_index, offset=offset)).corner_index


    @property
    def vertex_index(self):
        """

        > Node: [Vertex of Corner](GeometryNodeVertexOfCorner.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/vertex_of_corner.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVertexOfCorner.html)

        #### Returns:
        - socket `vertex_index`


        """

        return self.attribute_node(nodes.VertexOfCorner(corner_index=self.selection_index)).vertex_index




class Spline(Domain):
    @property
    def count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `spline_count`


        """

        return nodes.DomainSize(geometry=self.data_socket, component='CURVE').spline_count


    @property
    def cyclic(self):
        """

        > Node: [Is Spline Cyclic](GeometryNodeInputSplineCyclic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/is_spline_cyclic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html)

        #### Returns:
        - socket `cyclic`


        """

        return self.attribute_node(nodes.IsSplineCyclic()).cyclic


    @cyclic.setter
    def cyclic(self, attr_value):
        """

        > Node: [Set Spline Cyclic](GeometryNodeSetSplineCyclic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: cyclic



        """

        self.socket_stack(nodes.SetSplineCyclic(geometry=self.data_socket, selection=self.selection, cyclic=attr_value))


    def delete(self, mode='ALL'):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Args:
        - mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def duplicate(self, amount=None):
        """

        > Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

        #### Args:
        - amount: Integer

        #### Returns:
        - socket `duplicate_index`


        """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain='SPLINE')).node.duplicate_index


    @property
    def length(self):
        """

        > Node: [Spline Length](GeometryNodeSplineLength.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_length.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSplineLength.webp)

        #### Returns:
        - node with sockets ['length', 'point_count']


        """

        return self.attribute_node(nodes.SplineLength())


    @property
    def normal(self):
        """

        > Node: [Normal](GeometryNodeInputNormal.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

        #### Returns:
        - socket `normal`


        """

        return self.attribute_node(nodes.Normal()).normal


    @normal.setter
    def normal(self, attr_value):
        """

        > Node: [Set Curve Normal](GeometryNodeSetCurveNormal.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: mode



        """

        self.socket_stack(nodes.SetCurveNormal(curve=self.data_socket, selection=self.selection, mode=attr_value))


    def points(self, weights=None, sort_index=None):
        """

        > Node: [Points of Curve](GeometryNodePointsOfCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)

        #### Args:
        - weights: Float
        - sort_index: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsOfCurve.webp)

        #### Returns:
        - node with sockets ['point_index', 'total']


        """

        return self.attribute_node(nodes.PointsOfCurve(curve_index=self.selection_index, weights=weights, sort_index=sort_index))


    def resample(self, count=None, length=None, mode='COUNT'):
        """

        > Node: [Resample Curve](GeometryNodeResampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

        #### Args:
        - count: Integer
        - length: Float
        - mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=count, length=length, mode=mode))


    def resample_count(self, count=None):
        """

        > Node: [Resample Curve](GeometryNodeResampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

        #### Args:
        - count: Integer

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=count, length=0.1, mode='COUNT'))


    def resample_evaluated(self):
        """

        > Node: [Resample Curve](GeometryNodeResampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=10, length=0.1, mode='EVALUATED'))


    def resample_length(self, length=None):
        """

        > Node: [Resample Curve](GeometryNodeResampleCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

        #### Args:
        - length: Float

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.ResampleCurve(curve=self.data_socket, selection=self.selection, count=10, length=length, mode='LENGTH'))


    @property
    def resolution(self):
        """

        > Node: [Spline Resolution](GeometryNodeInputSplineResolution.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_resolution.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html)

        #### Returns:
        - socket `resolution`


        """

        return self.attribute_node(nodes.SplineResolution()).resolution


    @resolution.setter
    def resolution(self, attr_value):
        """

        > Node: [Set Spline Resolution](GeometryNodeSetSplineResolution.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: resolution



        """

        self.socket_stack(nodes.SetSplineResolution(geometry=self.data_socket, selection=self.selection, resolution=attr_value))


    def separate(self):
        """

        > Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        #### Returns:
        - node with sockets ['selection', 'inverted']


        """

        return nodes.SeparateGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain)


    def set_cyclic(self, cyclic=None):
        """

        > Node: [Set Spline Cyclic](GeometryNodeSetSplineCyclic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)

        #### Args:
        - cyclic: Boolean

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetSplineCyclic(geometry=self.data_socket, selection=self.selection, cyclic=cyclic))


    def set_normal(self, mode='MINIMUM_TWIST'):
        """

        > Node: [Set Curve Normal](GeometryNodeSetCurveNormal.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)

        #### Args:
        - mode (str): 'MINIMUM_TWIST' in [MINIMUM_TWIST, Z_UP]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetCurveNormal(curve=self.data_socket, selection=self.selection, mode=mode))


    def set_resolution(self, resolution=None):
        """

        > Node: [Set Spline Resolution](GeometryNodeSetSplineResolution.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)

        #### Args:
        - resolution: Integer

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetSplineResolution(geometry=self.data_socket, selection=self.selection, resolution=resolution))


    def set_type(self, spline_type='POLY'):
        """

        > Node: [Set Spline Type](GeometryNodeCurveSplineType.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)

        #### Args:
        - spline_type (str): 'POLY' in [CATMULL_ROM, POLY, BEZIER, NURBS]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetSplineType(curve=self.data_socket, selection=self.selection, spline_type=spline_type))


    def trim(self, start=None, end=None, mode='FACTOR'):
        """

        > Node: [Trim Curve](GeometryNodeTrimCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)

        #### Args:
        - mode (str): 'FACTOR' in [FACTOR, LENGTH]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.TrimCurve(curve=self.data_socket, selection=self.selection, start0=start, start1=start, end0=end, end1=end, mode=mode))


    def trim_factor(self, start=None, end=None):
        """

        > Node: [Trim Curve](GeometryNodeTrimCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)

        #### Args:
        - start: Float
        - end: Float

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.TrimCurve(curve=self.data_socket, selection=self.selection, start0=start, start1=None, end0=end, end1=None, mode='FACTOR'))


    def trim_length(self, start=None, end=None):
        """

        > Node: [Trim Curve](GeometryNodeTrimCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/trim_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)

        #### Args:
        - start: Float
        - end: Float

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.TrimCurve(curve=self.data_socket, selection=self.selection, start0=None, start1=start, end0=None, end1=end, mode='LENGTH'))


    @property
    def type(self):
        """

        > Node: [Set Spline Type](GeometryNodeCurveSplineType.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)

        'type' is a write only property.
        Raise an exception if attempt to read.



        """

        raise Exception("Error: 'type' is a write only property of class Curve!")


    @type.setter
    def type(self, attr_value):
        """

        > Node: [Set Spline Type](GeometryNodeCurveSplineType.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: spline_type



        """

        self.socket_stack(nodes.SetSplineType(curve=self.data_socket, selection=self.selection, spline_type=attr_value))




class ControlPoint(Domain):
    @property
    def count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `point_count`


        """

        return nodes.DomainSize(geometry=self.data_socket, component='CURVE').point_count


    def curve(self):
        """

        > Node: [Curve of Point](GeometryNodeCurveOfPoint.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveOfPoint.webp)

        #### Returns:
        - node with sockets ['curve_index', 'index_in_curve']


        """

        return self.attribute_node(nodes.CurveOfPoint(point_index=self.selection_index))


    def delete(self, mode='ALL'):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Args:
        - mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def duplicate(self, amount=None):
        """

        > Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

        #### Args:
        - amount: Integer

        #### Returns:
        - socket `duplicate_index`


        """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def endpoint_selection(self, start_size=None, end_size=None):
        """

        > Node: [Endpoint Selection](GeometryNodeCurveEndpointSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)

        #### Args:
        - start_size: Integer
        - end_size: Integer

        #### Returns:
        - socket `selection`


        """

        return self.attribute_node(nodes.EndpointSelection(start_size=start_size, end_size=end_size)).selection


    def handle_positions(self, relative=None):
        """

        > Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

        #### Args:
        - relative: Boolean

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputCurveHandlePositions.webp)

        #### Returns:
        - node with sockets ['left', 'right']


        """

        return self.attribute_node(nodes.CurveHandlePositions(relative=relative))


    def handle_type_selection(self, left=True, right=True, handle_type='AUTO'):
        """

        > Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        #### Args:
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - node with sockets ['selection']


        """

        mode={'LEFT'} if left else {}
        if right: mode.add('RIGHT')
        return self.handle_type_selection_node(handle_type=handle_type, mode=mode)


    def handle_type_selection_free(self, left=True, right=True):
        """

        > Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        #### Args:
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - node with sockets ['selection']


        """

        return self.handle_type_selection(left=left, right=right, handle_type='FREE')


    def handle_type_selection_auto(self, left=True, right=True):
        """

        > Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        #### Args:
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - node with sockets ['selection']


        """

        return self.handle_type_selection(left=left, right=right, handle_type='AUTO')


    def handle_type_selection_vector(self, left=True, right=True):
        """

        > Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        #### Args:
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - node with sockets ['selection']


        """

        return self.handle_type_selection(left=left, right=right, handle_type='VECTOR')


    def handle_type_selection_align(self, left=True, right=True):
        """

        > Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        #### Args:
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - node with sockets ['selection']


        """

        return self.handle_type_selection(left=left, right=right, handle_type='ALIGN')


    def capture_handle_type_selection(self, left=True, right=True, handle_type='AUTO'):
        """

        > Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        #### Args:
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - node with sockets ['selection']


        """

        return self.capture_node(self.capture_handle_type_selection(left=left, right=right, handle_type=handle_type))


    def capture_handle_type_selection_free(self, left=True, right=True):
        """

        > Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        #### Args:
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - node with sockets ['selection']


        """

        return self.capture_handle_type_selection(left=left, right=right, handle_type='FREE')


    def capture_handle_type_selection_auto(self, left=True, right=True):
        """

        > Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        #### Args:
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - node with sockets ['selection']


        """

        return self.capture_handle_type_selection(left=left, right=right, handle_type='AUTO')


    def capture_handle_type_selection_vector(self, left=True, right=True):
        """

        > Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        #### Args:
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - node with sockets ['selection']


        """

        return self.capture_handle_type_selection(left=left, right=right, handle_type='VECTOR')


    def capture_handle_type_selection_align(self, left=True, right=True):
        """

        > Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        #### Args:
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - node with sockets ['selection']


        """

        return self.capture_handle_type_selection(left=left, right=right, handle_type='ALIGN')


    def handle_type_selection_node(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """

        > Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

        #### Args:
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - socket `selection`


        """

        return self.attribute_node(nodes.HandleTypeSelection(handle_type=handle_type, mode=mode)).selection


    def instance_on(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

        > Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

        #### Args:
        - instance: Geometry
        - pick_instance: Boolean
        - instance_index: Integer
        - rotation: Vector
        - scale: Vector

        #### Returns:
        - socket `instances`


        """

        return nodes.InstanceOnPoints(points=self.data_socket, selection=self.selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances


    def interpolate(self, guide_curves=None, guide_up=None, guide_group_id=None, point_up=None, point_group_id=None, max_neighbors=None):
        """

        > Node: [Interpolate Curves](GeometryNodeInterpolateCurves.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/n.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInterpolateCurves.html)

        #### Args:
        - guide_curves: Geometry
        - guide_up: Vector
        - guide_group_id: Integer
        - point_up: Vector
        - point_group_id: Integer
        - max_neighbors: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateCurves.webp)

        #### Returns:
        - node with sockets ['curves', 'closest_index', 'closest_weight']


        """

        return nodes.InterpolateCurves(guide_curves=guide_curves, guide_up=guide_up, guide_group_id=guide_group_id, points=self.data_socket, point_up=point_up, point_group_id=point_group_id, max_neighbors=max_neighbors)


    @property
    def left_handle_offset(self):
        """

        > Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        'left_handle_offset' is a write only property.
        Raise an exception if attempt to read.



        """

        raise Exception("Error: 'left_handle_offset' is a write only property of class ControlPoint!")


    @left_handle_offset.setter
    def left_handle_offset(self, attr_value):
        """

        > Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: offset



        """

        self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=None, offset=attr_value, mode='LEFT'))


    @property
    def left_handle_positions(self):
        """

        > Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

        #### Returns:
        - socket `left`


        """

        return self.attribute_node(nodes.CurveHandlePositions(relative=False)).left


    @left_handle_positions.setter
    def left_handle_positions(self, attr_value):
        """

        > Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: position



        """

        self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=attr_value, offset=None, mode='LEFT'))


    def offset(self, offset=None):
        """

        > Node: [Offset Point in Curve](GeometryNodeOffsetPointInCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)

        #### Args:
        - offset: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeOffsetPointInCurve.webp)

        #### Returns:
        - node with sockets ['is_valid_offset', 'point_index']


        """

        return self.attribute_node(nodes.OffsetPointInCurve(point_index=self.selection_index, offset=offset))


    @property
    def parameter(self):
        """

        > Node: [Spline Parameter](GeometryNodeSplineParameter.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSplineParameter.webp)

        #### Returns:
        - node with sockets ['factor', 'length', 'index']


        """

        if not hasattr(self, '_c_geometrynodesplineparameter'):
            self._c_geometrynodesplineparameter = self.attribute_node(nodes.SplineParameter())
        return self._c_geometrynodesplineparameter


    @property
    def radius(self):
        """

        > Node: [Radius](GeometryNodeInputRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

        #### Returns:
        - socket `radius`


        """

        return self.attribute_node(nodes.Radius()).radius


    @radius.setter
    def radius(self, attr_value):
        """

        > Node: [Set Curve Radius](GeometryNodeSetCurveRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: radius



        """

        self.socket_stack(nodes.SetCurveRadius(curve=self.data_socket, selection=self.selection, radius=attr_value))


    @property
    def relative_left_handle_positions(self):
        """

        > Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

        #### Returns:
        - socket `left`


        """

        return self.attribute_node(nodes.CurveHandlePositions(relative=True)).left


    @property
    def relative_right_handle_positions(self):
        """

        > Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

        #### Returns:
        - socket `right`


        """

        return self.attribute_node(nodes.CurveHandlePositions(relative=True)).right


    @property
    def right_handle_offset(self):
        """

        > Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        'right_handle_offset' is a write only property.
        Raise an exception if attempt to read.



        """

        raise Exception("Error: 'right_handle_offset' is a write only property of class ControlPoint!")


    @right_handle_offset.setter
    def right_handle_offset(self, attr_value):
        """

        > Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: offset



        """

        self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=None, offset=attr_value, mode='RIGHT'))


    @property
    def right_handle_positions(self):
        """

        > Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

        #### Returns:
        - socket `right`


        """

        return self.attribute_node(nodes.CurveHandlePositions(relative=False)).right


    @right_handle_positions.setter
    def right_handle_positions(self, attr_value):
        """

        > Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: position



        """

        self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=attr_value, offset=None, mode='RIGHT'))


    def separate(self):
        """

        > Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        #### Returns:
        - node with sockets ['selection', 'inverted']


        """

        return nodes.SeparateGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain)


    def set_handle_positions(self, position=None, offset=None, mode='LEFT'):
        """

        > Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        #### Args:
        - position: Vector
        - offset: Vector
        - mode (str): 'LEFT' in [LEFT, RIGHT]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=position, offset=offset, mode=mode))


    def set_handle_type(self, left=True, right=True, handle_type='AUTO'):
        """

        > Node: [Set Handle Type](GeometryNodeCurveSetHandles.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)

        #### Args:
        - curve: Curve
        - selection: Boolean
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - node with sockets ['curve']


        """

        mode={'LEFT'} if left else {}
        if right: mode.add('RIGHT')
        return self.set_handle_type_node(handle_type=handle_type, mode=mode)


    def set_handle_type_node(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """

        > Node: [Set Handle Type](GeometryNodeCurveSetHandles.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)

        #### Args:
        - handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
        - mode (set): {'LEFT', 'RIGHT'}

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetHandleType(curve=self.data_socket, selection=self.selection, handle_type=handle_type, mode=mode))


    def set_left_handle_positions(self, position=None, offset=None):
        """

        > Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        #### Args:
        - position: Vector
        - offset: Vector

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=position, offset=offset, mode='LEFT'))


    def set_radius(self, radius=None):
        """

        > Node: [Set Curve Radius](GeometryNodeSetCurveRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)

        #### Args:
        - radius: Float

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetCurveRadius(curve=self.data_socket, selection=self.selection, radius=radius))


    def set_right_handle_positions(self, position=None, offset=None):
        """

        > Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

        #### Args:
        - position: Vector
        - offset: Vector

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetHandlePositions(curve=self.data_socket, selection=self.selection, position=position, offset=offset, mode='RIGHT'))


    def set_tilt(self, tilt=None):
        """

        > Node: [Set Curve Tilt](GeometryNodeSetCurveTilt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)

        #### Args:
        - tilt: Float

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetCurveTilt(curve=self.data_socket, selection=self.selection, tilt=tilt))


    @property
    def tangent(self):
        """

        > Node: [Curve Tangent](GeometryNodeInputTangent.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tangent.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)

        #### Returns:
        - socket `tangent`


        """

        return self.attribute_node(nodes.CurveTangent()).tangent


    @property
    def tilt(self):
        """

        > Node: [Curve Tilt](GeometryNodeInputCurveTilt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tilt.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html)

        #### Returns:
        - socket `tilt`


        """

        return self.attribute_node(nodes.CurveTilt()).tilt


    @tilt.setter
    def tilt(self, attr_value):
        """

        > Node: [Set Curve Tilt](GeometryNodeSetCurveTilt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: tilt



        """

        self.socket_stack(nodes.SetCurveTilt(curve=self.data_socket, selection=self.selection, tilt=attr_value))




class CloudPoint(Domain):
    @property
    def count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `point_count`


        """

        return nodes.DomainSize(geometry=self.data_socket, component='POINTCLOUD').point_count


    def delete(self, mode='ALL'):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Args:
        - mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def duplicate(self, amount=None):
        """

        > Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

        #### Args:
        - amount: Integer

        #### Returns:
        - socket `duplicate_index`


        """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def instance_on(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """

        > Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

        #### Args:
        - instance: Geometry
        - pick_instance: Boolean
        - instance_index: Integer
        - rotation: Vector
        - scale: Vector

        #### Returns:
        - socket `instances`


        """

        return nodes.InstanceOnPoints(points=self.data_socket, selection=self.selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances


    def interpolate(self, guide_curves=None, guide_up=None, guide_group_id=None, point_up=None, point_group_id=None, max_neighbors=None):
        """

        > Node: [Interpolate Curves](GeometryNodeInterpolateCurves.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/n.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInterpolateCurves.html)

        #### Args:
        - guide_curves: Geometry
        - guide_up: Vector
        - guide_group_id: Integer
        - point_up: Vector
        - point_group_id: Integer
        - max_neighbors: Integer

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateCurves.webp)

        #### Returns:
        - node with sockets ['curves', 'closest_index', 'closest_weight']


        """

        return nodes.InterpolateCurves(guide_curves=guide_curves, guide_up=guide_up, guide_group_id=guide_group_id, points=self.data_socket, point_up=point_up, point_group_id=point_group_id, max_neighbors=max_neighbors)


    @property
    def material(self):
        """

        > Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        'material' is a write only property.
        Raise an exception if attempt to read.



        """

        raise Exception("Error: 'material' is a write only property of class Domain!")


    @material.setter
    def material(self, attr_value):
        """

        > Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: material



        """

        self.socket_stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=attr_value))


    @property
    def material_index(self):
        """

        > Node: [Material Index](GeometryNodeInputMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

        #### Returns:
        - socket `material_index`


        """

        return self.attribute_node(nodes.MaterialIndex()).material_index


    @material_index.setter
    def material_index(self, attr_value):
        """

        > Node: [Set Material Index](GeometryNodeSetMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: material_index



        """

        self.socket_stack(nodes.SetMaterialIndex(geometry=self.data_socket, selection=self.selection, material_index=attr_value))


    @property
    def radius(self):
        """

        > Node: [Radius](GeometryNodeInputRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

        #### Returns:
        - socket `radius`


        """

        return self.attribute_node(nodes.Radius()).radius


    @radius.setter
    def radius(self, attr_value):
        """

        > Node: [Set Point Radius](GeometryNodeSetPointRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)

        Node implemented as property setter.

        #### Args:
        - attr_value: radius



        """

        self.socket_stack(nodes.SetPointRadius(points=self.data_socket, selection=self.selection, radius=attr_value))


    def set_material(self, material=None):
        """

        > Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

        #### Args:
        - material: Material

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetMaterial(geometry=self.data_socket, selection=self.selection, material=material))


    def set_material_index(self, material_index=None):
        """

        > Node: [Set Material Index](GeometryNodeSetMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

        #### Args:
        - material_index: Integer

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.SetMaterialIndex(geometry=self.data_socket, selection=self.selection, material_index=material_index))


    def to_sdf_volume(self, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """

        > Node: [Points to SDF Volume](GeometryNodePointsToSDFVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/o.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToSDFVolume.html)

        #### Args:
        - voxel_size: Float
        - voxel_amount: Float
        - radius: Float
        - resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

        #### Returns:
        - socket `volume` of class Volume


        """

        import geonodes as gn
        return gn.Volume(nodes.PointsToSdfVolume(points=self.data_socket, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode).volume)


    def to_vertices(self):
        """

        > Node: [Points to Vertices](GeometryNodePointsToVertices.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)

        #### Returns:
        - socket `mesh` of class Mesh


        """

        import geonodes as gn
        return gn.Mesh(nodes.PointsToVertices(points=self.data_socket, selection=self.selection).mesh)




class Instance(Domain):
    @property
    def count(self):
        """

        > Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

        #### Returns:
        - socket `instance_count`


        """

        return nodes.DomainSize(geometry=self.data_socket, component='INSTANCES').instance_count


    def delete(self, mode='ALL'):
        """

        > Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

        #### Args:
        - mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.DeleteGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain, mode=mode))


    def duplicate(self, amount=None):
        """

        > Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

        #### Args:
        - amount: Integer

        #### Returns:
        - socket `duplicate_index`


        """

        return self.socket_stack(nodes.DuplicateElements(geometry=self.data_socket, selection=self.selection, amount=amount, domain=self.domain)).node.duplicate_index


    def rotate(self, rotation=None, pivot_point=None, local_space=None):
        """

        > Node: [Rotate Instances](GeometryNodeRotateInstances.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)

        #### Args:
        - rotation: Vector
        - pivot_point: Vector
        - local_space: Boolean

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.RotateInstances(instances=self.data_socket, selection=self.selection, rotation=rotation, pivot_point=pivot_point, local_space=local_space))


    @property
    def rotation(self):
        """

        > Node: [Instance Rotation](GeometryNodeInputInstanceRotation.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html)

        #### Returns:
        - socket `rotation`


        """

        return self.attribute_node(nodes.InstanceRotation()).rotation


    @property
    def scale(self):
        """

        > Node: [Instance Scale](GeometryNodeInputInstanceScale.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html)

        #### Returns:
        - socket `scale`


        """

        return self.attribute_node(nodes.InstanceScale()).scale


    def separate(self):
        """

        > Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

        ![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        #### Returns:
        - node with sockets ['selection', 'inverted']


        """

        return nodes.SeparateGeometry(geometry=self.data_socket, selection=self.selection, domain=self.domain)


    def set_scale(self, scale=None, center=None, local_space=None):
        """

        > Node: [Scale Instances](GeometryNodeScaleInstances.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)

        #### Args:
        - scale: Vector
        - center: Vector
        - local_space: Boolean

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.ScaleInstances(instances=self.data_socket, selection=self.selection, scale=scale, center=center, local_space=local_space))


    def to_points(self, position=None, radius=None):
        """

        > Node: [Instances to Points](GeometryNodeInstancesToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)

        #### Args:
        - position: Vector
        - radius: Float

        #### Returns:
        - socket `points` of class Points


        """

        import geonodes as gn
        return gn.Points(nodes.InstancesToPoints(instances=self.data_socket, selection=self.selection, position=position, radius=radius).points)


    def translate(self, translation=None, local_space=None):
        """

        > Node: [Translate Instances](GeometryNodeTranslateInstances.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html)

        #### Args:
        - translation: Vector
        - local_space: Boolean

        #### Returns:
        - self


        """

        return self.socket_stack(nodes.TranslateInstances(instances=self.data_socket, selection=self.selection, translation=translation, local_space=local_space))




