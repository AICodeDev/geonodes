# Nodes Menus

- [Attribute](#menu-Attribute)
- [Color](#menu-Color)
- [Curve](#menu-Curve)
- [Curve Primitives](#menu-Curve-Primitives)
- [Curve Topology](#menu-Curve-Topology)
- [Geometry](#menu-Geometry)
- [Input](#menu-Input)
- [Instances](#menu-Instances)
- [Material](#menu-Material)
- [Mesh](#menu-Mesh)
- [Mesh Primitives](#menu-Mesh-Primitives)
- [Output](#menu-Output)
- [Point](#menu-Point)
- [Text](#menu-Text)
- [Texture](#menu-Texture)
- [Utilities](#menu-Utilities)
- [UV](#menu-UV)
- [Vector](#menu-Vector)
- [Volume](#menu-Volume)

## Menu Attribute

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Domain](Domain.md) | [attribute_statistic](Domain.md#attribute_statistic) |
|      | [Geometry](Geometry.md) | [attribute_statistic](Geometry.md#attribute_statistic) |
| [Domain Size](GeometryNodeAttributeDomainSize.md) | [CloudPoint](CloudPoint.md) | [count](CloudPoint.md#count) |
|      | [ControlPoint](ControlPoint.md) | [count](ControlPoint.md#count) |
|      | [Corner](Corner.md) | [count](Corner.md#count) |
|      | [Curve](Curve.md) | - [domain_size](Curve.md#domain_size)<br>- [point_count](Curve.md#point_count)<br>- [spline_count](Curve.md#spline_count)|
|      | [Edge](Edge.md) | [count](Edge.md#count) |
|      | [Face](Face.md) | [count](Face.md#count) |
|      | [Geometry](Geometry.md) | [domain_size](Geometry.md#domain_size) |
|      | [Instance](Instance.md) | [count](Instance.md#count) |
|      | [Instances](Instances.md) | [domain_size](Instances.md#domain_size) |
|      | [Mesh](Mesh.md) | [domain_size](Mesh.md#domain_size) / [point_count](Mesh.md#point_count) / [face_count](Mesh.md#face_count) / [edge_count](Mesh.md#edge_count) / [corner_count](Mesh.md#corner_count) / |
|      | [Points](Points.md) | [domain_size](Points.md#domain_size) |
|      | [Spline](Spline.md) | [count](Spline.md#count) |
|      | [Vertex](Vertex.md) | [count](Vertex.md#count) |
| [Blur Attribute](GeometryNodeBlurAttribute.md) | [Domain](Domain.md) | [blur_attribute](Domain.md#blur_attribute) / [blur_float](Domain.md#blur_float) / [blur_integer](Domain.md#blur_integer) / [blur_vector](Domain.md#blur_vector) / [blur_color](Domain.md#blur_color) / |
| [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Domain](Domain.md) | [capture_attribute](Domain.md#capture_attribute) |
|      | [Geometry](Geometry.md) | - [capture_attribute](Geometry.md#capture_attribute)<br>- [capture_attribute_node](Geometry.md#capture_attribute_node)|
| [Remove Named Attribute](GeometryNodeRemoveAttribute.md) | [Domain](Domain.md) | [remove_named_attribute](Domain.md#remove_named_attribute) |
|      | [Geometry](Geometry.md) | [remove_named_attribute](Geometry.md#remove_named_attribute) |
| [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Domain](Domain.md) | [store_named_attribute](Domain.md#store_named_attribute) / [store_named_float](Domain.md#store_named_float) / [store_named_integer](Domain.md#store_named_integer) / [store_named_vector](Domain.md#store_named_vector) / [store_named_color](Domain.md#store_named_color) / [store_named_byte_color](Domain.md#store_named_byte_color) / [store_named_boolean](Domain.md#store_named_boolean) / [store_named_2D_vector](Domain.md#store_named_2D_vector) / |
|      | [Geometry](Geometry.md) | [store_named_attribute](Geometry.md#store_named_attribute) / [store_named_boolean](Geometry.md#store_named_boolean) / [store_named_integer](Geometry.md#store_named_integer) / [store_named_float](Geometry.md#store_named_float) / [store_named_vector](Geometry.md#store_named_vector) / [store_named_color](Geometry.md#store_named_color) / |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Color

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Color Ramp](ShaderNodeValToRGB.md) | [Float](Float.md) | [color_ramp](Float.md#color_ramp) |
|      | [functions](functions.md) | [color_ramp](functions.md#color_ramp) |
| [Combine Color](FunctionNodeCombineColor.md) | [Color](Color.md) | - [RGB](Color.md#RGB)<br>- [HSV](Color.md#HSV)<br>- [HSL](Color.md#HSL)|
|      | [functions](functions.md) | - [combine_rgb](functions.md#combine_rgb)<br>- [combine_hsv](functions.md#combine_hsv)<br>- [combine_hsl](functions.md#combine_hsl)|
| [Mix](ShaderNodeMix.md) | [Color](Color.md) | [mix](Color.md#mix) / [mix_darken](Color.md#mix_darken) / [mix_multiply](Color.md#mix_multiply) / [mix_burn](Color.md#mix_burn) / [mix_lighten](Color.md#mix_lighten) / [mix_screen](Color.md#mix_screen) / [mix_dodge](Color.md#mix_dodge) / [mix_add](Color.md#mix_add) / [mix_overlay](Color.md#mix_overlay) / [mix_soft_light](Color.md#mix_soft_light) / [mix_linear_light](Color.md#mix_linear_light) / [mix_difference](Color.md#mix_difference) / [mix_subtract](Color.md#mix_subtract) / [mix_divide](Color.md#mix_divide) / [mix_hue](Color.md#mix_hue) / [mix_saturation](Color.md#mix_saturation) / [mix_color](Color.md#mix_color) / [mix_value](Color.md#mix_value) / |
|      | [Float](Float.md) | [mix](Float.md#mix) |
|      | [Vector](Vector.md) | - [mix](Vector.md#mix)<br>- [mix_uniform](Vector.md#mix_uniform)<br>- [mix_non_uniform](Vector.md#mix_non_uniform)|
|      | [functions](functions.md) | [float_mix](functions.md#float_mix) / [vector_mix](functions.md#vector_mix) / [color_mix](functions.md#color_mix) / [color_darken](functions.md#color_darken) / [color_multiply](functions.md#color_multiply) / [color_burn](functions.md#color_burn) / [color_lighten](functions.md#color_lighten) / [color_screen](functions.md#color_screen) / [color_dodge](functions.md#color_dodge) / [color_add](functions.md#color_add) / [color_overlay](functions.md#color_overlay) / [color_soft_light](functions.md#color_soft_light) / [color_linear_light](functions.md#color_linear_light) / [color_difference](functions.md#color_difference) / [color_subtract](functions.md#color_subtract) / [color_divide](functions.md#color_divide) / [color_hue](functions.md#color_hue) / [color_saturation](functions.md#color_saturation) / [color_color](functions.md#color_color) / [color_value](functions.md#color_value) / |
| [RGB Curves](ShaderNodeRGBCurve.md) | [Color](Color.md) | [rgb_curves](Color.md#rgb_curves) |
|      | [functions](functions.md) | [rgb_curves](functions.md#rgb_curves) |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Curve

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Curve Length](GeometryNodeCurveLength.md) | [Curve](Curve.md) | [length](Curve.md#length) |
| [Curve to Mesh](GeometryNodeCurveToMesh.md) | [Curve](Curve.md) | [to_mesh](Curve.md#to_mesh) |
| [Curve to Points](GeometryNodeCurveToPoints.md) | [Curve](Curve.md) | - [to_points](Curve.md#to_points)<br>- [to_points_count](Curve.md#to_points_count)<br>- [to_points_length](Curve.md#to_points_length)<br>- [to_points_evaluated](Curve.md#to_points_evaluated)|
| [Deform Curves on Surface](GeometryNodeDeformCurvesOnSurface.md) | [Curve](Curve.md) | [deform_on_surface](Curve.md#deform_on_surface) |
| [Fill Curve](GeometryNodeFillCurve.md) | [Curve](Curve.md) | - [fill](Curve.md#fill)<br>- [fill_triangles](Curve.md#fill_triangles)<br>- [fill_ngons](Curve.md#fill_ngons)|
| [Fillet Curve](GeometryNodeFilletCurve.md) | [Curve](Curve.md) | - [fillet](Curve.md#fillet)<br>- [fillet_bezier](Curve.md#fillet_bezier)<br>- [fillet_poly](Curve.md#fillet_poly)|
| [Resample Curve](GeometryNodeResampleCurve.md) | [Curve](Curve.md) | - [resample](Curve.md#resample)<br>- [resample_count](Curve.md#resample_count)<br>- [resample_length](Curve.md#resample_length)<br>- [resample_evaluated](Curve.md#resample_evaluated)|
|      | [Spline](Spline.md) | - [resample](Spline.md#resample)<br>- [resample_count](Spline.md#resample_count)<br>- [resample_length](Spline.md#resample_length)<br>- [resample_evaluated](Spline.md#resample_evaluated)|
| [Reverse Curve](GeometryNodeReverseCurve.md) | [Curve](Curve.md) | [reverse](Curve.md#reverse) |
| [Sample Curve](GeometryNodeSampleCurve.md) | [Curve](Curve.md) | [sample](Curve.md#sample) |
| [Subdivide Curve](GeometryNodeSubdivideCurve.md) | [Curve](Curve.md) | [subdivide](Curve.md#subdivide) |
| [Trim Curve](GeometryNodeTrimCurve.md) | [Curve](Curve.md) | - [trim](Curve.md#trim)<br>- [trim_factor](Curve.md#trim_factor)<br>- [trim_length](Curve.md#trim_length)|
|      | [Spline](Spline.md) | - [trim](Spline.md#trim)<br>- [trim_factor](Spline.md#trim_factor)<br>- [trim_length](Spline.md#trim_length)|
| [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [ControlPoint](ControlPoint.md) | [handle_positions](ControlPoint.md#handle_positions) / [left_handle_positions](ControlPoint.md#left_handle_positions) / [right_handle_positions](ControlPoint.md#right_handle_positions) / [relative_left_handle_positions](ControlPoint.md#relative_left_handle_positions) / [relative_right_handle_positions](ControlPoint.md#relative_right_handle_positions) / |
| [Curve Tangent](GeometryNodeInputTangent.md) | [ControlPoint](ControlPoint.md) | [tangent](ControlPoint.md#tangent) |
| [Curve Tilt](GeometryNodeInputCurveTilt.md) | [ControlPoint](ControlPoint.md) | [tilt](ControlPoint.md#tilt) |
| [Endpoint Selection](GeometryNodeCurveEndpointSelection.md) | [ControlPoint](ControlPoint.md) | [endpoint_selection](ControlPoint.md#endpoint_selection) |
| [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [ControlPoint](ControlPoint.md) | [handle_type_selection_node](ControlPoint.md#handle_type_selection_node) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / [handle_type_selection](ControlPoint.md#handle_type_selection) / |
| [Is Spline Cyclic](GeometryNodeInputSplineCyclic.md) | [Spline](Spline.md) | [cyclic](Spline.md#cyclic) |
| [Spline Length](GeometryNodeSplineLength.md) | [Spline](Spline.md) | [length](Spline.md#length) |
| [Spline Parameter](GeometryNodeSplineParameter.md) | [ControlPoint](ControlPoint.md) | [parameter](ControlPoint.md#parameter) |
| [Spline Resolution](GeometryNodeInputSplineResolution.md) | [Spline](Spline.md) | [resolution](Spline.md#resolution) |
| [Set Curve Normal](GeometryNodeSetCurveNormal.md) | [Spline](Spline.md) | - [set_normal](Spline.md#set_normal)<br>- [normal](Spline.md#normal)|
| [Set Curve Radius](GeometryNodeSetCurveRadius.md) | [ControlPoint](ControlPoint.md) | - [set_radius](ControlPoint.md#set_radius)<br>- [radius](ControlPoint.md#radius)|
| [Set Curve Tilt](GeometryNodeSetCurveTilt.md) | [ControlPoint](ControlPoint.md) | - [set_tilt](ControlPoint.md#set_tilt)<br>- [tilt](ControlPoint.md#tilt)|
| [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [ControlPoint](ControlPoint.md) | [set_handle_positions](ControlPoint.md#set_handle_positions) / [set_left_handle_positions](ControlPoint.md#set_left_handle_positions) / [set_right_handle_positions](ControlPoint.md#set_right_handle_positions) / [left_handle_positions](ControlPoint.md#left_handle_positions) / [right_handle_positions](ControlPoint.md#right_handle_positions) / [left_handle_offset](ControlPoint.md#left_handle_offset) / [left_handle_offset](ControlPoint.md#left_handle_offset) / [right_handle_offset](ControlPoint.md#right_handle_offset) / [right_handle_offset](ControlPoint.md#right_handle_offset) / |
| [Set Handle Type](GeometryNodeCurveSetHandles.md) | [ControlPoint](ControlPoint.md) | - [set_handle_type_node](ControlPoint.md#set_handle_type_node)<br>- [set_handle_type](ControlPoint.md#set_handle_type)|
| [Set Spline Cyclic](GeometryNodeSetSplineCyclic.md) | [Spline](Spline.md) | - [set_cyclic](Spline.md#set_cyclic)<br>- [cyclic](Spline.md#cyclic)|
| [Set Spline Resolution](GeometryNodeSetSplineResolution.md) | [Spline](Spline.md) | - [set_resolution](Spline.md#set_resolution)<br>- [resolution](Spline.md#resolution)|
| [Set Spline Type](GeometryNodeCurveSplineType.md) | [Spline](Spline.md) | - [set_type](Spline.md#set_type)<br>- [type](Spline.md#type)<br>- [type](Spline.md#type)|
| [Interpolate Curves](GeometryNodeInterpolateCurves.md) | [CloudPoint](CloudPoint.md) | [interpolate](CloudPoint.md#interpolate) |
|      | [ControlPoint](ControlPoint.md) | [interpolate](ControlPoint.md#interpolate) |
|      | [Curve](Curve.md) | [interpolate](Curve.md#interpolate) |
|      | [Points](Points.md) | [interpolate](Points.md#interpolate) |
|      | [Vertex](Vertex.md) | [interpolate](Vertex.md#interpolate) |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Curve Primitives

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Arc](GeometryNodeCurveArc.md) | [Curve](Curve.md) | - [Arc](Curve.md#Arc)<br>- [ArcFromPoints](Curve.md#ArcFromPoints)|
| [Bezier Segment](GeometryNodeCurvePrimitiveBezierSegment.md) | [Curve](Curve.md) | [BezierSegment](Curve.md#BezierSegment) |
| [Curve Circle](GeometryNodeCurvePrimitiveCircle.md) | [Curve](Curve.md) | - [Circle](Curve.md#Circle)<br>- [CircleFromPoints](Curve.md#CircleFromPoints)|
| [Curve Line](GeometryNodeCurvePrimitiveLine.md) | [Curve](Curve.md) | - [Line](Curve.md#Line)<br>- [LineDirection](Curve.md#LineDirection)|
| [Spiral](GeometryNodeCurveSpiral.md) | [Curve](Curve.md) | [Spiral](Curve.md#Spiral) |
| [Quadratic Bezier](GeometryNodeCurveQuadraticBezier.md) | [Curve](Curve.md) | [QuadraticBezier](Curve.md#QuadraticBezier) |
| [Quadrilateral](GeometryNodeCurvePrimitiveQuadrilateral.md) | [Curve](Curve.md) | [Quadrilateral](Curve.md#Quadrilateral) |
| [Star](GeometryNodeCurveStar.md) | [Curve](Curve.md) | [Star](Curve.md#Star) |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Curve Topology

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Offset Point in Curve](GeometryNodeOffsetPointInCurve.md) | [ControlPoint](ControlPoint.md) | [offset](ControlPoint.md#offset) |
|      | [Curve](Curve.md) | [offset_point](Curve.md#offset_point) |
| [Curve of Point](GeometryNodeCurveOfPoint.md) | [ControlPoint](ControlPoint.md) | [curve](ControlPoint.md#curve) |
|      | [Curve](Curve.md) | [curve_of_point](Curve.md#curve_of_point) |
| [Points of Curve](GeometryNodePointsOfCurve.md) | [Curve](Curve.md) | [points_of_curve](Curve.md#points_of_curve) |
|      | [Spline](Spline.md) | [points](Spline.md#points) |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Geometry

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Bounding Box](GeometryNodeBoundBox.md) | [Geometry](Geometry.md) | [bounding_box](Geometry.md#bounding_box) |
| [Convex Hull](GeometryNodeConvexHull.md) | [Geometry](Geometry.md) | [convex_hull](Geometry.md#convex_hull) |
| [Delete Geometry](GeometryNodeDeleteGeometry.md) | [CloudPoint](CloudPoint.md) | [delete](CloudPoint.md#delete) |
|      | [ControlPoint](ControlPoint.md) | [delete](ControlPoint.md#delete) |
|      | [Edge](Edge.md) | - [delete](Edge.md#delete)<br>- [delete_all](Edge.md#delete_all)<br>- [delete_edges](Edge.md#delete_edges)<br>- [delete_faces](Edge.md#delete_faces)|
|      | [Face](Face.md) | - [delete](Face.md#delete)<br>- [delete_all](Face.md#delete_all)<br>- [delete_edges](Face.md#delete_edges)<br>- [delete_faces](Face.md#delete_faces)|
|      | [Geometry](Geometry.md) | [delete](Geometry.md#delete) |
|      | [Instance](Instance.md) | [delete](Instance.md#delete) |
|      | [Mesh](Mesh.md) | - [delete_all](Mesh.md#delete_all)<br>- [delete_edges](Mesh.md#delete_edges)<br>- [delete_faces](Mesh.md#delete_faces)|
|      | [Spline](Spline.md) | [delete](Spline.md#delete) |
|      | [Vertex](Vertex.md) | - [delete](Vertex.md#delete)<br>- [delete_all](Vertex.md#delete_all)<br>- [delete_edges](Vertex.md#delete_edges)<br>- [delete_faces](Vertex.md#delete_faces)|
| [Duplicate Elements](GeometryNodeDuplicateElements.md) | [CloudPoint](CloudPoint.md) | [duplicate](CloudPoint.md#duplicate) |
|      | [ControlPoint](ControlPoint.md) | [duplicate](ControlPoint.md#duplicate) |
|      | [Edge](Edge.md) | [duplicate](Edge.md#duplicate) |
|      | [Face](Face.md) | [duplicate](Face.md#duplicate) |
|      | [Geometry](Geometry.md) | [duplicate](Geometry.md#duplicate) |
|      | [Instance](Instance.md) | [duplicate](Instance.md#duplicate) |
|      | [Spline](Spline.md) | [duplicate](Spline.md#duplicate) |
|      | [Vertex](Vertex.md) | [duplicate](Vertex.md#duplicate) |
| [Geometry to Instance](GeometryNodeGeometryToInstance.md) | [Geometry](Geometry.md) | [to_instance](Geometry.md#to_instance) |
|      | [functions](functions.md) | [geometry_to_instance](functions.md#geometry_to_instance) |
| [Join Geometry](GeometryNodeJoinGeometry.md) | [Geometry](Geometry.md) | [join](Geometry.md#join) |
|      | [functions](functions.md) | [join_geometry](functions.md#join_geometry) |
| [Merge by Distance](GeometryNodeMergeByDistance.md) | [Geometry](Geometry.md) | [merge_by_distance](Geometry.md#merge_by_distance) |
|      | [Vertex](Vertex.md) | - [merge_by_distance](Vertex.md#merge_by_distance)<br>- [merge_by_distance_connected](Vertex.md#merge_by_distance_connected)|
| [Raycast](GeometryNodeRaycast.md) | [Domain](Domain.md) | - [raycast](Domain.md#raycast)<br>- [raycast_interpolated](Domain.md#raycast_interpolated)<br>- [raycast_nearest](Domain.md#raycast_nearest)|
|      | [Geometry](Geometry.md) | - [raycast](Geometry.md#raycast)<br>- [raycast_interpolated](Geometry.md#raycast_interpolated)<br>- [raycast_nearest](Geometry.md#raycast_nearest)|
| [Sample Index](GeometryNodeSampleIndex.md) | [Domain](Domain.md) | [sample_index](Domain.md#sample_index) |
|      | [Geometry](Geometry.md) | [sample_index](Geometry.md#sample_index) |
| [Sample Nearest](GeometryNodeSampleNearest.md) | [Domain](Domain.md) | [sample_nearest](Domain.md#sample_nearest) |
|      | [Geometry](Geometry.md) | [sample_nearest](Geometry.md#sample_nearest) |
| [Separate Components](GeometryNodeSeparateComponents.md) | [Geometry](Geometry.md) | [separate_components](Geometry.md#separate_components) / [mesh_component](Geometry.md#mesh_component) / [curve_component](Geometry.md#curve_component) / [points_component](Geometry.md#points_component) / [volume_component](Geometry.md#volume_component) / [instances_component](Geometry.md#instances_component) / |
| [Separate Geometry](GeometryNodeSeparateGeometry.md) | [ControlPoint](ControlPoint.md) | [separate](ControlPoint.md#separate) |
|      | [Edge](Edge.md) | [separate](Edge.md#separate) |
|      | [Face](Face.md) | [separate](Face.md#separate) |
|      | [Geometry](Geometry.md) | [separate](Geometry.md#separate) |
|      | [Instance](Instance.md) | [separate](Instance.md#separate) |
|      | [Spline](Spline.md) | [separate](Spline.md#separate) |
|      | [Vertex](Vertex.md) | [separate](Vertex.md#separate) |
| [Transform Geometry](GeometryNodeTransform.md) | [Geometry](Geometry.md) | - [transform_geometry](Geometry.md#transform_geometry)<br>- [transform](Geometry.md#transform)|
| [Set ID](GeometryNodeSetID.md) | [Domain](Domain.md) | - [set_ID](Domain.md#set_ID)<br>- [ID](Domain.md#ID)|
|      | [Geometry](Geometry.md) | [set_ID](Geometry.md#set_ID) |
| [Set Position](GeometryNodeSetPosition.md) | [Domain](Domain.md) | - [set_position](Domain.md#set_position)<br>- [position](Domain.md#position)<br>- [position_offset](Domain.md#position_offset)<br>- [position_offset](Domain.md#position_offset)|
|      | [Geometry](Geometry.md) | [set_position](Geometry.md#set_position) |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Input

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Boolean](FunctionNodeInputBool.md) | [Boolean](Boolean.md) | [Boolean](Boolean.md#Boolean) |
| [Collection Info](GeometryNodeCollectionInfo.md) | [Geometry](Geometry.md) | [Collection](Geometry.md#Collection) |
| [Color](FunctionNodeInputColor.md) | [Color](Color.md) | [Color](Color.md#Color) |
| [Integer](FunctionNodeInputInt.md) | [Integer](Integer.md) | [Integer](Integer.md#Integer) |
| [Material](GeometryNodeInputMaterial.md) | [Material](Material.md) | [Material](Material.md#Material) |
| [Object Info](GeometryNodeObjectInfo.md) | [Object](Object.md) | [info](Object.md#info) / [location](Object.md#location) / [rotation](Object.md#rotation) / [scale](Object.md#scale) / [geometry](Object.md#geometry) / |
| [Self Object](GeometryNodeSelfObject.md) | [Object](Object.md) | [Self](Object.md#Self) |
| [String](FunctionNodeInputString.md) | [String](String.md) | [String](String.md#String) |
| [Value](ShaderNodeValue.md) | [Float](Float.md) | [Value](Float.md#Value) |
| [Vector](FunctionNodeInputVector.md) | [Vector](Vector.md) | [Vector](Vector.md#Vector) |
| [ID](GeometryNodeInputID.md) | [Curve](Curve.md) | [ID](Curve.md#ID) |
|      | [Domain](Domain.md) | [ID](Domain.md#ID) |
|      | [Instances](Instances.md) | [ID](Instances.md#ID) |
|      | [Mesh](Mesh.md) | [ID](Mesh.md#ID) |
|      | [Points](Points.md) | [ID](Points.md#ID) |
| [Index](GeometryNodeInputIndex.md) | [Curve](Curve.md) | [index](Curve.md#index) |
|      | [Domain](Domain.md) | - [index](Domain.md#index)<br>- [domain_index](Domain.md#domain_index)|
|      | [Instances](Instances.md) | [index](Instances.md#index) |
|      | [Mesh](Mesh.md) | [index](Mesh.md#index) |
|      | [Points](Points.md) | [index](Points.md#index) |
| [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Curve](Curve.md) | [named_attribute](Curve.md#named_attribute) / [named_float](Curve.md#named_float) / [named_integer](Curve.md#named_integer) / [named_vector](Curve.md#named_vector) / [named_color](Curve.md#named_color) / [named_boolean](Curve.md#named_boolean) / |
|      | [Domain](Domain.md) | [named_attribute](Domain.md#named_attribute) / [named_float](Domain.md#named_float) / [named_integer](Domain.md#named_integer) / [named_vector](Domain.md#named_vector) / [named_color](Domain.md#named_color) / [named_boolean](Domain.md#named_boolean) / |
|      | [Instances](Instances.md) | [named_attribute](Instances.md#named_attribute) / [named_float](Instances.md#named_float) / [named_integer](Instances.md#named_integer) / [named_vector](Instances.md#named_vector) / [named_color](Instances.md#named_color) / [named_boolean](Instances.md#named_boolean) / |
|      | [Mesh](Mesh.md) | [named_attribute](Mesh.md#named_attribute) / [named_float](Mesh.md#named_float) / [named_integer](Mesh.md#named_integer) / [named_vector](Mesh.md#named_vector) / [named_color](Mesh.md#named_color) / [named_boolean](Mesh.md#named_boolean) / |
|      | [Points](Points.md) | [named_attribute](Points.md#named_attribute) / [named_float](Points.md#named_float) / [named_integer](Points.md#named_integer) / [named_vector](Points.md#named_vector) / [named_color](Points.md#named_color) / [named_boolean](Points.md#named_boolean) / |
| [Normal](GeometryNodeInputNormal.md) | [Curve](Curve.md) | [normal](Curve.md#normal) |
|      | [Domain](Domain.md) | [normal](Domain.md#normal) |
|      | [Instances](Instances.md) | [normal](Instances.md#normal) |
|      | [Mesh](Mesh.md) | [normal](Mesh.md#normal) |
|      | [Points](Points.md) | [normal](Points.md#normal) |
|      | [Spline](Spline.md) | [normal](Spline.md#normal) |
| [Position](GeometryNodeInputPosition.md) | [Curve](Curve.md) | [position](Curve.md#position) |
|      | [Domain](Domain.md) | [position](Domain.md#position) |
|      | [Instances](Instances.md) | [position](Instances.md#position) |
|      | [Mesh](Mesh.md) | [position](Mesh.md#position) |
|      | [Points](Points.md) | [position](Points.md#position) |
| [Radius](GeometryNodeInputRadius.md) | [CloudPoint](CloudPoint.md) | [radius](CloudPoint.md#radius) |
|      | [ControlPoint](ControlPoint.md) | [radius](ControlPoint.md#radius) |
|      | [Curve](Curve.md) | [radius](Curve.md#radius) |
|      | [Points](Points.md) | [radius](Points.md#radius) |
| [Scene Time](GeometryNodeInputSceneTime.md) | [Float](Float.md) | - [Seconds](Float.md#Seconds)<br>- [Frame](Float.md#Frame)|
| [Image Info](GeometryNodeImageInfo.md) | [Image](Image.md) | [info](Image.md#info) / [width](Image.md#width) / [height](Image.md#height) / [has_alpha](Image.md#has_alpha) / [frame_count](Image.md#frame_count) / [fps](Image.md#fps) / |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Instances

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Instance on Points](GeometryNodeInstanceOnPoints.md) | [CloudPoint](CloudPoint.md) | [instance_on](CloudPoint.md#instance_on) |
|      | [ControlPoint](ControlPoint.md) | [instance_on](ControlPoint.md#instance_on) |
|      | [Curve](Curve.md) | [instance_on_points](Curve.md#instance_on_points) |
|      | [Instances](Instances.md) | - [InstanceOnPoints](Instances.md#InstanceOnPoints)<br>- [on_points](Instances.md#on_points)|
|      | [Mesh](Mesh.md) | [instance_on_points](Mesh.md#instance_on_points) |
|      | [Points](Points.md) | [instance_on_points](Points.md#instance_on_points) |
|      | [Vertex](Vertex.md) | [instance_on](Vertex.md#instance_on) |
| [Instances to Points](GeometryNodeInstancesToPoints.md) | [Instance](Instance.md) | [to_points](Instance.md#to_points) |
|      | [Instances](Instances.md) | [to_points](Instances.md#to_points) |
| [Realize Instances](GeometryNodeRealizeInstances.md) | [Instances](Instances.md) | [realize](Instances.md#realize) |
| [Rotate Instances](GeometryNodeRotateInstances.md) | [Instance](Instance.md) | [rotate](Instance.md#rotate) |
|      | [Instances](Instances.md) | [rotate](Instances.md#rotate) |
| [Scale Instances](GeometryNodeScaleInstances.md) | [Instance](Instance.md) | [set_scale](Instance.md#set_scale) |
|      | [Instances](Instances.md) | [set_scale](Instances.md#set_scale) |
| [Translate Instances](GeometryNodeTranslateInstances.md) | [Instance](Instance.md) | [translate](Instance.md#translate) |
|      | [Instances](Instances.md) | [translate](Instances.md#translate) |
| [Instance Scale](GeometryNodeInputInstanceScale.md) | [Instance](Instance.md) | [scale](Instance.md#scale) |
|      | [Instances](Instances.md) | [scale](Instances.md#scale) |
| [Instance Rotation](GeometryNodeInputInstanceRotation.md) | [Instance](Instance.md) | [rotation](Instance.md#rotation) |
|      | [Instances](Instances.md) | [rotation](Instances.md#rotation) |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Material

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Replace Material](GeometryNodeReplaceMaterial.md) | [Geometry](Geometry.md) | [replace_material](Geometry.md#replace_material) |
| [Material Index](GeometryNodeInputMaterialIndex.md) | [CloudPoint](CloudPoint.md) | [material_index](CloudPoint.md#material_index) |
|      | [Face](Face.md) | [material_index](Face.md#material_index) |
|      | [Mesh](Mesh.md) | [material_index](Mesh.md#material_index) |
|      | [Points](Points.md) | [material_index](Points.md#material_index) |
| [Material Selection](GeometryNodeMaterialSelection.md) | [Domain](Domain.md) | [material_selection](Domain.md#material_selection) |
|      | [Mesh](Mesh.md) | [material_selection](Mesh.md#material_selection) |
|      | [Points](Points.md) | [material_selection](Points.md#material_selection) |
| [Set Material](GeometryNodeSetMaterial.md) | [CloudPoint](CloudPoint.md) | - [set_material](CloudPoint.md#set_material)<br>- [material](CloudPoint.md#material)<br>- [material](CloudPoint.md#material)|
|      | [Face](Face.md) | - [set_material](Face.md#set_material)<br>- [material](Face.md#material)<br>- [material](Face.md#material)|
|      | [Mesh](Mesh.md) | [set_material](Mesh.md#set_material) |
|      | [Points](Points.md) | [set_material](Points.md#set_material) |
|      | [Volume](Volume.md) | [set_material](Volume.md#set_material) |
| [Set Material Index](GeometryNodeSetMaterialIndex.md) | [CloudPoint](CloudPoint.md) | - [set_material_index](CloudPoint.md#set_material_index)<br>- [material_index](CloudPoint.md#material_index)|
|      | [Face](Face.md) | - [set_material_index](Face.md#set_material_index)<br>- [material_index](Face.md#material_index)|
|      | [Geometry](Geometry.md) | [set_material_index](Geometry.md#set_material_index) |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Mesh

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Dual Mesh](GeometryNodeDualMesh.md) | [Mesh](Mesh.md) | [dual_mesh](Mesh.md#dual_mesh) |
| [Edge Paths to Curves](GeometryNodeEdgePathsToCurves.md) | [Edge](Edge.md) | [edge_paths_to_curves](Edge.md#edge_paths_to_curves) |
|      | [Mesh](Mesh.md) | [edge_paths_to_curves](Mesh.md#edge_paths_to_curves) |
| [Edge Paths to Selection](GeometryNodeEdgePathsToSelection.md) | [Mesh](Mesh.md) | [edge_paths_to_selection](Mesh.md#edge_paths_to_selection) |
| [Extrude Mesh](GeometryNodeExtrudeMesh.md) | [Edge](Edge.md) | [extrude](Edge.md#extrude) |
|      | [Face](Face.md) | [extrude](Face.md#extrude) |
|      | [Mesh](Mesh.md) | [extrude](Mesh.md#extrude) |
|      | [Vertex](Vertex.md) | [extrude](Vertex.md#extrude) |
| [Flip Faces](GeometryNodeFlipFaces.md) | [Face](Face.md) | [flip](Face.md#flip) |
|      | [Mesh](Mesh.md) | [flip_faces](Mesh.md#flip_faces) |
| [Mesh Boolean](GeometryNodeMeshBoolean.md) | [Mesh](Mesh.md) | - [boolean_intersect](Mesh.md#boolean_intersect)<br>- [boolean_union](Mesh.md#boolean_union)<br>- [boolean_difference](Mesh.md#boolean_difference)|
| [Mesh to Curve](GeometryNodeMeshToCurve.md) | [Edge](Edge.md) | [to_curve](Edge.md#to_curve) |
|      | [Mesh](Mesh.md) | [to_curve](Mesh.md#to_curve) |
| [Mesh to Points](GeometryNodeMeshToPoints.md) | [Mesh](Mesh.md) | [to_points](Mesh.md#to_points) |
|      | [Vertex](Vertex.md) | [to_points](Vertex.md#to_points) |
| [Mesh to Volume](GeometryNodeMeshToVolume.md) | [Mesh](Mesh.md) | [to_volume](Mesh.md#to_volume) |
|      | [Vertex](Vertex.md) | [to_volume](Vertex.md#to_volume) |
| [Sample Nearest Surface](GeometryNodeSampleNearestSurface.md) | [Mesh](Mesh.md) | [sample_nearest_surface](Mesh.md#sample_nearest_surface) |
| [Sample UV Surface](GeometryNodeSampleUVSurface.md) | [Mesh](Mesh.md) | [sample_uv_surface](Mesh.md#sample_uv_surface) |
| [Scale Elements](GeometryNodeScaleElements.md) | [Edge](Edge.md) | - [scale_uniform](Edge.md#scale_uniform)<br>- [scale_single_axis](Edge.md#scale_single_axis)|
|      | [Face](Face.md) | - [scale_uniform](Face.md#scale_uniform)<br>- [scale_single_axis](Face.md#scale_single_axis)|
|      | [Mesh](Mesh.md) | - [scale_elements](Mesh.md#scale_elements)<br>- [scale_uniform](Mesh.md#scale_uniform)<br>- [scale_single_axis](Mesh.md#scale_single_axis)|
| [Split Edges](GeometryNodeSplitEdges.md) | [Edge](Edge.md) | [split](Edge.md#split) |
|      | [Mesh](Mesh.md) | [split_edges](Mesh.md#split_edges) |
| [Subdivide Mesh](GeometryNodeSubdivideMesh.md) | [Mesh](Mesh.md) | [subdivide](Mesh.md#subdivide) |
| [Subdivision Surface](GeometryNodeSubdivisionSurface.md) | [Mesh](Mesh.md) | [subdivision_surface](Mesh.md#subdivision_surface) |
| [Triangulate](GeometryNodeTriangulate.md) | [Face](Face.md) | [triangulate](Face.md#triangulate) |
|      | [Mesh](Mesh.md) | [triangulate](Mesh.md#triangulate) |
| [Edge Angle](GeometryNodeInputMeshEdgeAngle.md) | [Edge](Edge.md) | - [angle](Edge.md#angle)<br>- [unsigned_angle](Edge.md#unsigned_angle)<br>- [signed_angle](Edge.md#signed_angle)|
| [Edge Neighbors](GeometryNodeInputMeshEdgeNeighbors.md) | [Edge](Edge.md) | [neighbors](Edge.md#neighbors) |
| [Edge Vertices](GeometryNodeInputMeshEdgeVertices.md) | [Edge](Edge.md) | [vertices](Edge.md#vertices) |
| [Face Area](GeometryNodeInputMeshFaceArea.md) | [Face](Face.md) | [area](Face.md#area) |
| [Face Neighbors](GeometryNodeInputMeshFaceNeighbors.md) | [Face](Face.md) | [neighbors](Face.md#neighbors) |
| [Face Group Boundaries](GeometryNodeMeshFaceSetBoundaries.md) | [Face](Face.md) | [face_group_boundaries](Face.md#face_group_boundaries) |
|      | [Mesh](Mesh.md) | [face_group_boundaries](Mesh.md#face_group_boundaries) |
| [Is Face Planar](GeometryNodeInputMeshFaceIsPlanar.md) | [Face](Face.md) | [is_planar](Face.md#is_planar) |
|      | [Mesh](Mesh.md) | [is_face_planar](Mesh.md#is_face_planar) |
| [Is Shade Smooth](GeometryNodeInputShadeSmooth.md) | [Face](Face.md) | [shade_smooth](Face.md#shade_smooth) |
|      | [Mesh](Mesh.md) | [is_shade_smooth](Mesh.md#is_shade_smooth) |
| [Mesh Island](GeometryNodeInputMeshIsland.md) | [Face](Face.md) | [island](Face.md#island) |
|      | [Mesh](Mesh.md) | [island](Mesh.md#island) |
| [Shortest Edge Paths](GeometryNodeInputShortestEdgePaths.md) | [Mesh](Mesh.md) | [shortest_edge_paths](Mesh.md#shortest_edge_paths) |
|      | [Vertex](Vertex.md) | [shortest_edge_paths](Vertex.md#shortest_edge_paths) |
| [Vertex Neighbors](GeometryNodeInputMeshVertexNeighbors.md) | [Vertex](Vertex.md) | [neighbors](Vertex.md#neighbors) |
| [Set Shade Smooth](GeometryNodeSetShadeSmooth.md) | [Face](Face.md) | - [set_shade_smooth](Face.md#set_shade_smooth)<br>- [shade_smooth](Face.md#shade_smooth)|
|      | [Mesh](Mesh.md) | [set_shade_smooth](Mesh.md#set_shade_smooth) |
| [Edges to Face Groups](GeometryNodeEdgesToFaceGroups.md) | [Edge](Edge.md) | [to_face_groups](Edge.md#to_face_groups) |
|      | [Mesh](Mesh.md) | [edges_to_face_groups](Mesh.md#edges_to_face_groups) |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Mesh Primitives

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Cone](GeometryNodeMeshCone.md) | [Mesh](Mesh.md) | [Cone](Mesh.md#Cone) |
| [Cube](GeometryNodeMeshCube.md) | [Mesh](Mesh.md) | [Cube](Mesh.md#Cube) |
| [Cylinder](GeometryNodeMeshCylinder.md) | [Mesh](Mesh.md) | [Cylinder](Mesh.md#Cylinder) |
| [Grid](GeometryNodeMeshGrid.md) | [Mesh](Mesh.md) | [Grid](Mesh.md#Grid) |
| [Ico Sphere](GeometryNodeMeshIcoSphere.md) | [Mesh](Mesh.md) | [IcoSphere](Mesh.md#IcoSphere) |
| [Mesh Circle](GeometryNodeMeshCircle.md) | [Mesh](Mesh.md) | [Circle](Mesh.md#Circle) |
| [Mesh Line](GeometryNodeMeshLine.md) | [Mesh](Mesh.md) | - [Line](Mesh.md#Line)<br>- [LineEndPoints](Mesh.md#LineEndPoints)<br>- [LineEndPointsResolution](Mesh.md#LineEndPointsResolution)<br>- [LineOffset](Mesh.md#LineOffset)|
| [UV Sphere](GeometryNodeMeshUVSphere.md) | [Mesh](Mesh.md) | [UVSphere](Mesh.md#UVSphere) |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Output

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Viewer](GeometryNodeViewer.md) | [Domain](Domain.md) | - [viewer](Domain.md#viewer)<br>- [view](Domain.md#view)|
|      | [Geometry](Geometry.md) | - [viewer](Geometry.md#viewer)<br>- [view](Geometry.md#view)|

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Point

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Distribute Points in Volume](GeometryNodeDistributePointsInVolume.md) | [Volume](Volume.md) | - [distribute_points](Volume.md#distribute_points)<br>- [distribute_points_random](Volume.md#distribute_points_random)<br>- [distribute_points_grid](Volume.md#distribute_points_grid)|
| [Distribute Points on Faces](GeometryNodeDistributePointsOnFaces.md) | [Face](Face.md) | - [distribute_points](Face.md#distribute_points)<br>- [distribute_points_random](Face.md#distribute_points_random)<br>- [distribute_points_poisson](Face.md#distribute_points_poisson)|
|      | [Mesh](Mesh.md) | [distribute_points_on_faces](Mesh.md#distribute_points_on_faces) |
| [Points](GeometryNodePoints.md) | [Points](Points.md) | [Points](Points.md#Points) |
| [Points to Vertices](GeometryNodePointsToVertices.md) | [CloudPoint](CloudPoint.md) | [to_vertices](CloudPoint.md#to_vertices) |
|      | [Points](Points.md) | [to_vertices](Points.md#to_vertices) |
| [Points to Volume](GeometryNodePointsToVolume.md) | [Points](Points.md) | - [to_volume](Points.md#to_volume)<br>- [to_volume_size](Points.md#to_volume_size)<br>- [to_volume_amount](Points.md#to_volume_amount)|
| [Set Point Radius](GeometryNodeSetPointRadius.md) | [CloudPoint](CloudPoint.md) | [radius](CloudPoint.md#radius) |
|      | [Points](Points.md) | [set_point_radius](Points.md#set_point_radius) |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Text

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Join Strings](GeometryNodeStringJoin.md) | [String](String.md) | - [join](String.md#join)<br>- [string_join](String.md#string_join)|
|      | [functions](functions.md) | [join_strings](functions.md#join_strings) |
| [Replace String](FunctionNodeReplaceString.md) | [String](String.md) | [replace](String.md#replace) |
|      | [functions](functions.md) | [replace_string](functions.md#replace_string) |
| [Slice String](FunctionNodeSliceString.md) | [String](String.md) | [slice](String.md#slice) |
|      | [functions](functions.md) | [slice_string](functions.md#slice_string) |
| [String Length](FunctionNodeStringLength.md) | [String](String.md) | [length](String.md#length) |
|      | [functions](functions.md) | [string_length](functions.md#string_length) |
| [String to Curves](GeometryNodeStringToCurves.md) | [String](String.md) | [to_curves](String.md#to_curves) |
|      | [functions](functions.md) | [string_to_curves](functions.md#string_to_curves) |
| [Value to String](FunctionNodeValueToString.md) | [Float](Float.md) | [to_string](Float.md#to_string) |
|      | [Integer](Integer.md) | [to_string](Integer.md#to_string) |
|      | [functions](functions.md) | [value_to_string](functions.md#value_to_string) |
| [Special Characters](FunctionNodeInputSpecialCharacters.md) | [String](String.md) | - [LineBreak](String.md#LineBreak)<br>- [Tab](String.md#Tab)|

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Texture

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Brick Texture](ShaderNodeTexBrick.md) | [Texture](Texture.md) | [Brick](Texture.md#Brick) |
| [Checker Texture](ShaderNodeTexChecker.md) | [Texture](Texture.md) | [Checker](Texture.md#Checker) |
| [Gradient Texture](ShaderNodeTexGradient.md) | [Texture](Texture.md) | [Gradient](Texture.md#Gradient) / [GradientLinear](Texture.md#GradientLinear) / [GradientQuadratic](Texture.md#GradientQuadratic) / [GradientEeasing](Texture.md#GradientEeasing) / [GradientDiagonal](Texture.md#GradientDiagonal) / [GradientSpherical](Texture.md#GradientSpherical) / [GradientQuadratic_sphere](Texture.md#GradientQuadratic_sphere) / [GradientRadial](Texture.md#GradientRadial) / |
| [Image Texture](GeometryNodeImageTexture.md) | [Image](Image.md) | [texture](Image.md#texture) |
|      | [Texture](Texture.md) | [Image](Texture.md#Image) |
| [Magic Texture](ShaderNodeTexMagic.md) | [Texture](Texture.md) | [Magic](Texture.md#Magic) |
| [Musgrave Texture](ShaderNodeTexMusgrave.md) | [Texture](Texture.md) | [Musgrave](Texture.md#Musgrave) |
| [Noise Texture](ShaderNodeTexNoise.md) | [Texture](Texture.md) | [Noise](Texture.md#Noise) / [Noise1D](Texture.md#Noise1D) / [Noise2D](Texture.md#Noise2D) / [Noise3D](Texture.md#Noise3D) / [Noise4D](Texture.md#Noise4D) / |
| [Voronoi Texture](ShaderNodeTexVoronoi.md) | [Texture](Texture.md) | [Voronoi](Texture.md#Voronoi) / [Voronoi1D](Texture.md#Voronoi1D) / [Voronoi2D](Texture.md#Voronoi2D) / [Voronoi3D](Texture.md#Voronoi3D) / [Voronoi4D](Texture.md#Voronoi4D) / |
| [Wave Texture](ShaderNodeTexWave.md) | [Texture](Texture.md) | [Wave](Texture.md#Wave) / [WaveBands](Texture.md#WaveBands) / [WaveRings](Texture.md#WaveRings) / [WaveBands_sine](Texture.md#WaveBands_sine) / [WaveBands_saw](Texture.md#WaveBands_saw) / [WaveBands_triangle](Texture.md#WaveBands_triangle) / [WaveRings_sine](Texture.md#WaveRings_sine) / [WaveRings_saw](Texture.md#WaveRings_saw) / [WaveRings_triangle](Texture.md#WaveRings_triangle) / |
| [White Noise Texture](ShaderNodeTexWhiteNoise.md) | [Texture](Texture.md) | [WhiteNoise](Texture.md#WhiteNoise) / [WhiteNoise1D](Texture.md#WhiteNoise1D) / [WhiteNoise2D](Texture.md#WhiteNoise2D) / [WhiteNoise3D](Texture.md#WhiteNoise3D) / [WhiteNoise4D](Texture.md#WhiteNoise4D) / |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Utilities

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Accumulate Field](GeometryNodeAccumulateField.md) | [Domain](Domain.md) | [accumulate_field](Domain.md#accumulate_field) |
| [Align Euler to Vector](FunctionNodeAlignEulerToVector.md) | [Vector](Vector.md) | - [align_euler_to_vector](Vector.md#align_euler_to_vector)<br>- [AlignToVector](Vector.md#AlignToVector)|
|      | [functions](functions.md) | [align_euler_to_vector](functions.md#align_euler_to_vector) |
| [Boolean Math](FunctionNodeBooleanMath.md) | [Boolean](Boolean.md) | [b_and](Boolean.md#b_and) / [b_or](Boolean.md#b_or) / [b_not](Boolean.md#b_not) / [nand](Boolean.md#nand) / [nor](Boolean.md#nor) / [xnor](Boolean.md#xnor) / [xor](Boolean.md#xor) / [imply](Boolean.md#imply) / [nimply](Boolean.md#nimply) / |
|      | [functions](functions.md) | [b_and](functions.md#b_and) / [b_or](functions.md#b_or) / [b_not](functions.md#b_not) / [nand](functions.md#nand) / [nor](functions.md#nor) / [xnor](functions.md#xnor) / [xor](functions.md#xor) / [imply](functions.md#imply) / [nimply](functions.md#nimply) / |
| [Clamp](ShaderNodeClamp.md) | [Float](Float.md) | - [clamp](Float.md#clamp)<br>- [clamp_min_max](Float.md#clamp_min_max)<br>- [clamp_range](Float.md#clamp_range)|
|      | [functions](functions.md) | - [clamp](functions.md#clamp)<br>- [clamp_min_max](functions.md#clamp_min_max)<br>- [clamp_range](functions.md#clamp_range)|
| [Compare](FunctionNodeCompare.md) | [Color](Color.md) | - [darker](Color.md#darker)<br>- [brighter](Color.md#brighter)<br>- [equal](Color.md#equal)<br>- [equal](Color.md#equal)|
|      | [Float](Float.md) | [compare](Float.md#compare) / [less_than](Float.md#less_than) / [less_equal](Float.md#less_equal) / [greater_than](Float.md#greater_than) / [greater_equal](Float.md#greater_equal) / [equal](Float.md#equal) / [not_equal](Float.md#not_equal) / |
|      | [Integer](Integer.md) | [compare](Integer.md#compare) / [less_than](Integer.md#less_than) / [less_equal](Integer.md#less_equal) / [greater_than](Integer.md#greater_than) / [greater_equal](Integer.md#greater_equal) / [equal](Integer.md#equal) / [not_equal](Integer.md#not_equal) / |
|      | [String](String.md) | - [equal](String.md#equal)<br>- [not_equal](String.md#not_equal)|
|      | [Vector](Vector.md) | [compare](Vector.md#compare) / [elements_less_than](Vector.md#elements_less_than) / [elements_less_equal](Vector.md#elements_less_equal) / [elements_greater_than](Vector.md#elements_greater_than) / [elements_greater_equal](Vector.md#elements_greater_equal) / [elements_equal](Vector.md#elements_equal) / [elements_not_equal](Vector.md#elements_not_equal) / [length_less_than](Vector.md#length_less_than) / [length_less_equal](Vector.md#length_less_equal) / [length_greater_than](Vector.md#length_greater_than) / [length_greater_equal](Vector.md#length_greater_equal) / [length_equal](Vector.md#length_equal) / [length_not_equal](Vector.md#length_not_equal) / [average_less_than](Vector.md#average_less_than) / [average_less_equal](Vector.md#average_less_equal) / [average_greater_than](Vector.md#average_greater_than) / [average_greater_equal](Vector.md#average_greater_equal) / [average_equal](Vector.md#average_equal) / [average_not_equal](Vector.md#average_not_equal) / [dot_product_less_than](Vector.md#dot_product_less_than) / [dot_product_less_equal](Vector.md#dot_product_less_equal) / [dot_product_greater_than](Vector.md#dot_product_greater_than) / [dot_product_greater_equal](Vector.md#dot_product_greater_equal) / [dot_product_equal](Vector.md#dot_product_equal) / [dot_product_not_equal](Vector.md#dot_product_not_equal) / [direction_less_than](Vector.md#direction_less_than) / [direction_less_equal](Vector.md#direction_less_equal) / [direction_greater_than](Vector.md#direction_greater_than) / [direction_greater_equal](Vector.md#direction_greater_equal) / [direction_equal](Vector.md#direction_equal) / [direction_not_equal](Vector.md#direction_not_equal) / |
|      | [functions](functions.md) | [compare](functions.md#compare) |
| [Float Curve](ShaderNodeFloatCurve.md) | [Float](Float.md) | [float_curve](Float.md#float_curve) |
| [Float to Integer](FunctionNodeFloatToInt.md) | [Float](Float.md) | [to_integer](Float.md#to_integer) / [round](Float.md#round) / [floor](Float.md#floor) / [ceiling](Float.md#ceiling) / [truncate](Float.md#truncate) / |
| [Map Range](ShaderNodeMapRange.md) | [Float](Float.md) | [map_range](Float.md#map_range) / [map_range_linear](Float.md#map_range_linear) / [map_range_stepped](Float.md#map_range_stepped) / [map_range_smooth](Float.md#map_range_smooth) / [map_range_smoother](Float.md#map_range_smoother) / |
|      | [Vector](Vector.md) | [map_range](Vector.md#map_range) / [map_range_linear](Vector.md#map_range_linear) / [map_range_stepped](Vector.md#map_range_stepped) / [map_range_smooth](Vector.md#map_range_smooth) / [map_range_smoother](Vector.md#map_range_smoother) / |
| [Math](ShaderNodeMath.md) | [Float](Float.md) | [multiply_add](Float.md#multiply_add) / [mul_add](Float.md#mul_add) / [power](Float.md#power) / [pow](Float.md#pow) / [logarithm](Float.md#logarithm) / [log](Float.md#log) / [sqrt](Float.md#sqrt) / [inverse_sqrt](Float.md#inverse_sqrt) / [absolute](Float.md#absolute) / [abs](Float.md#abs) / [exponent](Float.md#exponent) / [exp](Float.md#exp) / [minimum](Float.md#minimum) / [min](Float.md#min) / [maximum](Float.md#maximum) / [max](Float.md#max) / [math_less_than](Float.md#math_less_than) / [math_greater_than](Float.md#math_greater_than) / [sign](Float.md#sign) / [math_compare](Float.md#math_compare) / [smooth_minimum](Float.md#smooth_minimum) / [smooth_maximum](Float.md#smooth_maximum) / [math_round](Float.md#math_round) / [math_floor](Float.md#math_floor) / [math_ceil](Float.md#math_ceil) / [math_truncate](Float.md#math_truncate) / [math_trunc](Float.md#math_trunc) / [fraction](Float.md#fraction) / [fact](Float.md#fact) / [modulo](Float.md#modulo) / [wrap](Float.md#wrap) / [snap](Float.md#snap) / [ping_pong](Float.md#ping_pong) / [sine](Float.md#sine) / [sin](Float.md#sin) / [cosine](Float.md#cosine) / [cos](Float.md#cos) / [tangent](Float.md#tangent) / [tan](Float.md#tan) / [arcsine](Float.md#arcsine) / [arcsin](Float.md#arcsin) / [arccosine](Float.md#arccosine) / [arccos](Float.md#arccos) / [arctangent](Float.md#arctangent) / [arctan](Float.md#arctan) / [arctan2](Float.md#arctan2) / [sinh](Float.md#sinh) / [cosh](Float.md#cosh) / [tanh](Float.md#tanh) / [to_radians](Float.md#to_radians) / [to_degrees](Float.md#to_degrees) / |
|      | [Integer](Integer.md) | [multiply_add](Integer.md#multiply_add) / [mul_add](Integer.md#mul_add) / [power](Integer.md#power) / [pow](Integer.md#pow) / [logarithm](Integer.md#logarithm) / [log](Integer.md#log) / [sqrt](Integer.md#sqrt) / [inverse_sqrt](Integer.md#inverse_sqrt) / [absolute](Integer.md#absolute) / [abs](Integer.md#abs) / [exponent](Integer.md#exponent) / [exp](Integer.md#exp) / [minimum](Integer.md#minimum) / [min](Integer.md#min) / [maximum](Integer.md#maximum) / [max](Integer.md#max) / [math_less_than](Integer.md#math_less_than) / [math_greater_than](Integer.md#math_greater_than) / [sign](Integer.md#sign) / [math_compare](Integer.md#math_compare) / [smooth_minimum](Integer.md#smooth_minimum) / [smooth_maximum](Integer.md#smooth_maximum) / [math_round](Integer.md#math_round) / [math_floor](Integer.md#math_floor) / [math_ceil](Integer.md#math_ceil) / [math_truncate](Integer.md#math_truncate) / [math_trunc](Integer.md#math_trunc) / [fraction](Integer.md#fraction) / [fact](Integer.md#fact) / [modulo](Integer.md#modulo) / [wrap](Integer.md#wrap) / [snap](Integer.md#snap) / [ping_pong](Integer.md#ping_pong) / [sine](Integer.md#sine) / [sin](Integer.md#sin) / [cosine](Integer.md#cosine) / [cos](Integer.md#cos) / [tangent](Integer.md#tangent) / [tan](Integer.md#tan) / [arcsine](Integer.md#arcsine) / [arcsin](Integer.md#arcsin) / [arccosine](Integer.md#arccosine) / [arccos](Integer.md#arccos) / [arctangent](Integer.md#arctangent) / [arctan](Integer.md#arctan) / [arctan2](Integer.md#arctan2) / [sinh](Integer.md#sinh) / [cosh](Integer.md#cosh) / [tanh](Integer.md#tanh) / [to_radians](Integer.md#to_radians) / [to_degrees](Integer.md#to_degrees) / |
|      | [functions](functions.md) | [math](functions.md#math) / [multiply_add](functions.md#multiply_add) / [mul_add](functions.md#mul_add) / [power](functions.md#power) / [logarithm](functions.md#logarithm) / [log](functions.md#log) / [sqrt](functions.md#sqrt) / [inverse_sqrt](functions.md#inverse_sqrt) / [absolute](functions.md#absolute) / [abs](functions.md#abs) / [exponent](functions.md#exponent) / [exp](functions.md#exp) / [minimum](functions.md#minimum) / [min](functions.md#min) / [maximum](functions.md#maximum) / [max](functions.md#max) / [math_less_than](functions.md#math_less_than) / [math_greater_than](functions.md#math_greater_than) / [sign](functions.md#sign) / [math_compare](functions.md#math_compare) / [smooth_minimum](functions.md#smooth_minimum) / [smooth_maximum](functions.md#smooth_maximum) / [math_round](functions.md#math_round) / [math_floor](functions.md#math_floor) / [math_ceil](functions.md#math_ceil) / [math_truncate](functions.md#math_truncate) / [math_trun](functions.md#math_trun) / [fraction](functions.md#fraction) / [modulo](functions.md#modulo) / [wrap](functions.md#wrap) / [snap](functions.md#snap) / [ping_pong](functions.md#ping_pong) / [sine](functions.md#sine) / [sin](functions.md#sin) / [cosine](functions.md#cosine) / [cos](functions.md#cos) / [tangent](functions.md#tangent) / [tan](functions.md#tan) / [arcsine](functions.md#arcsine) / [arcsin](functions.md#arcsin) / [arccosine](functions.md#arccosine) / [arccos](functions.md#arccos) / [arctangent](functions.md#arctangent) / [arctan](functions.md#arctan) / [arctan2](functions.md#arctan2) / [sinh](functions.md#sinh) / [cosh](functions.md#cosh) / [tanh](functions.md#tanh) / [to_radians](functions.md#to_radians) / [to_degrees](functions.md#to_degrees) / |
| [Random Value](FunctionNodeRandomValue.md) | [Boolean](Boolean.md) | [Random](Boolean.md#Random) |
|      | [Domain](Domain.md) | - [random_float](Domain.md#random_float)<br>- [random_integer](Domain.md#random_integer)<br>- [random_vector](Domain.md#random_vector)<br>- [random_boolean](Domain.md#random_boolean)|
|      | [Float](Float.md) | [Random](Float.md#Random) |
|      | [Geometry](Geometry.md) | - [random_float](Geometry.md#random_float)<br>- [random_integer](Geometry.md#random_integer)<br>- [random_vector](Geometry.md#random_vector)<br>- [random_boolean](Geometry.md#random_boolean)|
|      | [Integer](Integer.md) | [Random](Integer.md#Random) |
|      | [Vector](Vector.md) | [Random](Vector.md#Random) |
|      | [functions](functions.md) | - [random_float](functions.md#random_float)<br>- [random_integer](functions.md#random_integer)<br>- [random_vector](functions.md#random_vector)<br>- [random_boolean](functions.md#random_boolean)|
| [Rotate Euler](FunctionNodeRotateEuler.md) | [functions](functions.md) | - [rotate_euler](functions.md#rotate_euler)<br>- [rotate_axis_angle](functions.md#rotate_axis_angle)|
| [Switch](GeometryNodeSwitch.md) | [Boolean](Boolean.md) | [switch](Boolean.md#switch) |
|      | [Collection](Collection.md) | [switch](Collection.md#switch) |
|      | [Color](Color.md) | [switch](Color.md#switch) |
|      | [Float](Float.md) | [switch](Float.md#switch) |
|      | [Geometry](Geometry.md) | [switch](Geometry.md#switch) |
|      | [Image](Image.md) | [switch](Image.md#switch) |
|      | [Integer](Integer.md) | [switch](Integer.md#switch) |
|      | [Material](Material.md) | [switch](Material.md#switch) |
|      | [Object](Object.md) | [switch](Object.md#switch) |
|      | [String](String.md) | [switch](String.md#switch) |
|      | [Texture](Texture.md) | [switch](Texture.md#switch) |
|      | [Vector](Vector.md) | [switch](Vector.md#switch) |
|      | [functions](functions.md) | [switch](functions.md#switch) / [switch_float](functions.md#switch_float) / [switch_integer](functions.md#switch_integer) / [switch_boolean](functions.md#switch_boolean) / [switch_vector](functions.md#switch_vector) / [switch_string](functions.md#switch_string) / [switch_color](functions.md#switch_color) / [switch_object](functions.md#switch_object) / [switch_image](functions.md#switch_image) / [switch_geometry](functions.md#switch_geometry) / [switch_collection](functions.md#switch_collection) / [switch_texture](functions.md#switch_texture) / [switch_material](functions.md#switch_material) / |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu UV

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Pack UV Islands](GeometryNodeUVPackIslands.md) | [Face](Face.md) | [pack_uv_islands](Face.md#pack_uv_islands) |
|      | [Mesh](Mesh.md) | [pack_uv_islands](Mesh.md#pack_uv_islands) |
| [UV Unwrap](GeometryNodeUVUnwrap.md) | [Face](Face.md) | [uv_unwrap](Face.md#uv_unwrap) |
|      | [Mesh](Mesh.md) | [uv_unwrap](Mesh.md#uv_unwrap) |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Vector

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Combine XYZ](ShaderNodeCombineXYZ.md) | [Vector](Vector.md) | [Combine](Vector.md#Combine) |
| [Separate XYZ](ShaderNodeSeparateXYZ.md) | [Vector](Vector.md) | [separate](Vector.md#separate) |
| [Vector Curves](ShaderNodeVectorCurve.md) | [Vector](Vector.md) | [curves](Vector.md#curves) |
| [Vector Math](ShaderNodeVectorMath.md) | [Vector](Vector.md) | [add](Vector.md#add) / [subtract](Vector.md#subtract) / [sub](Vector.md#sub) / [multiply](Vector.md#multiply) / [mul](Vector.md#mul) / [divide](Vector.md#divide) / [div](Vector.md#div) / [multiply_add](Vector.md#multiply_add) / [mul_add](Vector.md#mul_add) / [cross_product](Vector.md#cross_product) / [cross](Vector.md#cross) / [project](Vector.md#project) / [reflect](Vector.md#reflect) / [refract](Vector.md#refract) / [face_forward](Vector.md#face_forward) / [dot_product](Vector.md#dot_product) / [dot](Vector.md#dot) / [distance](Vector.md#distance) / [length](Vector.md#length) / [scale](Vector.md#scale) / [normalize](Vector.md#normalize) / [absolute](Vector.md#absolute) / [abs](Vector.md#abs) / [minimum](Vector.md#minimum) / [min](Vector.md#min) / [maximum](Vector.md#maximum) / [max](Vector.md#max) / [floor](Vector.md#floor) / [ceil](Vector.md#ceil) / [fraction](Vector.md#fraction) / [fract](Vector.md#fract) / [modulo](Vector.md#modulo) / [wrap](Vector.md#wrap) / [snap](Vector.md#snap) / [sine](Vector.md#sine) / [sin](Vector.md#sin) / [cosine](Vector.md#cosine) / [cos](Vector.md#cos) / [tangent](Vector.md#tangent) / [tan](Vector.md#tan) / |
| [Vector Rotate](ShaderNodeVectorRotate.md) | [Vector](Vector.md) | [rotate_euler](Vector.md#rotate_euler) / [rotate_axis_angle](Vector.md#rotate_axis_angle) / [rotate_x](Vector.md#rotate_x) / [rotate_y](Vector.md#rotate_y) / [rotate_z](Vector.md#rotate_z) / |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Menu Volume

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

| node | class | method name |
|------|-------|-------------|
| [Volume Cube](GeometryNodeVolumeCube.md) | [Volume](Volume.md) | [Cube](Volume.md#Cube) |
| [Volume to Mesh](GeometryNodeVolumeToMesh.md) | [Volume](Volume.md) | [to_mesh](Volume.md#to_mesh) |

<sub>Go to [top](#nodes-menus) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

