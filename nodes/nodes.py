from geonodes.core.node import Node

# ----------------------------------------------------------------------------------------------------
# Node NodeAlignEulerToVector for FunctionNodeAlignEulerToVector

class NodeAlignEulerToVector(Node):

    """Node 'Align Euler to Vector' (FunctionNodeAlignEulerToVector)

    Input sockets
    -------------
        rotation        : Vector
        factor          : Float
        vector          : Vector

    Parameters
    ----------
        axis            : 'X' in [ 'X' 'Y' 'Z']
        pivot_axis      : 'AUTO' in [ 'AUTO' 'X' 'Y' 'Z']

    Output sockets
    --------------
        rotation        : Vector
    """

    def __init__(self, rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO', label=None):

        super().__init__('FunctionNodeAlignEulerToVector', name='Align Euler to Vector', label=label)

        # Parameters

        self.bnode.axis            = axis
        self.bnode.pivot_axis      = pivot_axis

        # Input sockets

        self.plug(0, rotation)
        self.plug(1, factor)
        self.plug(2, vector)

        # Output sockets

        self.rotation        = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = [self.rotation]

# ----------------------------------------------------------------------------------------------------
# Node NodeBooleanMath for FunctionNodeBooleanMath

class NodeBooleanMath(Node):

    """Node 'Boolean Math' (FunctionNodeBooleanMath)

    Input sockets
    -------------
        boolean0        : Boolean
        boolean1        : Boolean

    Parameters
    ----------
        operation       : 'AND' in [ 'AND' 'OR' 'NOT' 'NAND' 'NOR' 'XNOR' 'XOR' 'IMPLY' 'NIMPLY']

    Output sockets
    --------------
        boolean         : Boolean
    """

    def __init__(self, boolean0=None, boolean1=None, operation='AND', label=None):

        super().__init__('FunctionNodeBooleanMath', name='Boolean Math', label=label)

        # Parameters

        self.bnode.operation       = operation

        # Input sockets

        self.plug(0, boolean0)
        self.plug(1, boolean1)

        # Output sockets

        self.boolean         = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = [self.boolean]

# ----------------------------------------------------------------------------------------------------
# Node NodeCompare for FunctionNodeCompare

class NodeCompare(Node):

    """Node 'Compare' (FunctionNodeCompare)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA')

        Input sockets     : ['a', 'b']

    Input sockets
    -------------
        a               : data_type dependant
        b               : data_type dependant
        c               : Float
        angle           : Float
        epsilon         : Float

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'VECTOR' 'STRING' 'RGBA']
        mode            : 'ELEMENT' in [ 'ELEMENT' 'LENGTH' 'AVERAGE' 'DOT_PRODUCT' 'DIRECTION']
        operation       : 'GREATER_THAN' in [ 'LESS_THAN' 'LESS_EQUAL' 'GREATER_THAN' 'GREATER_EQUAL' 'EQUAL' 'NOT_EQUAL']

    Output sockets
    --------------
        result          : Boolean
    """

    def __init__(self, a=None, b=None, c=None, angle=None, epsilon=None, data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', label=None):

        super().__init__('FunctionNodeCompare', name='Compare', label=label)

        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.mode            = mode
        self.bnode.operation       = operation

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(0, a)
            self.plug(1, b)
        elif data_type == 'INT':
            self.plug(2, a)
            self.plug(3, b)
        elif data_type == 'VECTOR':
            self.plug(4, a)
            self.plug(5, b)
        elif data_type == 'STRING':
            self.plug(8, a)
            self.plug(9, b)
        elif data_type == 'RGBA':
            self.plug(6, a)
            self.plug(7, b)

        self.plug(10, c)
        self.plug(11, angle)
        self.plug(12, epsilon)


        # Output sockets

        self.result          = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = [self.result]

# ----------------------------------------------------------------------------------------------------
# Node NodeFloatToInteger for FunctionNodeFloatToInt

class NodeFloatToInteger(Node):

    """Node 'Float to Integer' (FunctionNodeFloatToInt)

    Input sockets
    -------------
        float           : Float

    Parameters
    ----------
        rounding_mode   : 'ROUND' in [ 'ROUND' 'FLOOR' 'CEILING' 'TRUNCATE']

    Output sockets
    --------------
        integer         : Integer
    """

    def __init__(self, float=None, rounding_mode='ROUND', label=None):

        super().__init__('FunctionNodeFloatToInt', name='Float to Integer', label=label)

        # Parameters

        self.bnode.rounding_mode   = rounding_mode

        # Input sockets

        self.plug(0, float)

        # Output sockets

        self.integer         = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = [self.integer]

# ----------------------------------------------------------------------------------------------------
# Node NodeBoolean for FunctionNodeInputBool

class NodeBoolean(Node):

    """Node 'Boolean' (FunctionNodeInputBool)

    Parameters
    ----------
        boolean         : (False) bool

    Output sockets
    --------------
        boolean         : Boolean
    """

    def __init__(self, boolean=False, label=None):

        super().__init__('FunctionNodeInputBool', name='Boolean', label=label)

        # Parameters

        self.bnode.boolean         = boolean

        # Output sockets

        self.boolean         = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = [self.boolean]

# ----------------------------------------------------------------------------------------------------
# Node NodeColor for FunctionNodeInputColor

class NodeColor(Node):

    """Node 'Color' (FunctionNodeInputColor)

    Output sockets
    --------------
        color           : Color
    """

    def __init__(self, label=None):

        super().__init__('FunctionNodeInputColor', name='Color', label=label)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.output_sockets  = [self.color]

# ----------------------------------------------------------------------------------------------------
# Node NodeInteger for FunctionNodeInputInt

class NodeInteger(Node):

    """Node 'Integer' (FunctionNodeInputInt)

    Parameters
    ----------
        integer         : (0) int

    Output sockets
    --------------
        integer         : Integer
    """

    def __init__(self, integer=0, label=None):

        super().__init__('FunctionNodeInputInt', name='Integer', label=label)

        # Parameters

        self.bnode.integer         = integer

        # Output sockets

        self.integer         = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = [self.integer]

# ----------------------------------------------------------------------------------------------------
# Node NodeSpecialCharacters for FunctionNodeInputSpecialCharacters

class NodeSpecialCharacters(Node):

    """Node 'Special Characters' (FunctionNodeInputSpecialCharacters)

    Output sockets
    --------------
        line_break      : String
        tab             : String
    """

    def __init__(self, label=None):

        super().__init__('FunctionNodeInputSpecialCharacters', name='Special Characters', label=label)

        # Output sockets

        self.line_break      = self.String(self.bnode.outputs[0])
        self.tab             = self.String(self.bnode.outputs[1])
        self.output_sockets  = [self.line_break, self.tab]

# ----------------------------------------------------------------------------------------------------
# Node NodeString for FunctionNodeInputString

class NodeString(Node):

    """Node 'String' (FunctionNodeInputString)

    Parameters
    ----------
        string          : '' str

    Output sockets
    --------------
        string          : String
    """

    def __init__(self, string='', label=None):

        super().__init__('FunctionNodeInputString', name='String', label=label)

        # Parameters

        self.bnode.string          = string

        # Output sockets

        self.string          = self.String(self.bnode.outputs[0])
        self.output_sockets  = [self.string]

# ----------------------------------------------------------------------------------------------------
# Node NodeVector for FunctionNodeInputVector

class NodeVector(Node):

    """Node 'Vector' (FunctionNodeInputVector)

    Parameters
    ----------
        vector          : ([0.0, 0.0, 0.0]) Vector

    Output sockets
    --------------
        vector          : Vector
    """

    def __init__(self, vector=[0.0, 0.0, 0.0], label=None):

        super().__init__('FunctionNodeInputVector', name='Vector', label=label)

        # Parameters

        self.bnode.vector          = vector

        # Output sockets

        self.vector          = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = [self.vector]

# ----------------------------------------------------------------------------------------------------
# Node NodeRandomValue for FunctionNodeRandomValue

class NodeRandomValue(Node):

    """Node 'Random Value' (FunctionNodeRandomValue)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')

        Input sockets     : ['min', 'max']
        Output sockets    : ['value']

    Input sockets
    -------------
        min             : data_type dependant
        max             : data_type dependant
        probability     : Float
        ID              : Integer
        seed            : Integer

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'BOOLEAN']

    Output sockets
    --------------
        value           : data_type dependant
    """

    def __init__(self, min=None, max=None, probability=None, ID=None, seed=None, data_type='FLOAT', label=None):

        super().__init__('FunctionNodeRandomValue', name='Random Value', label=label)

        # Parameters

        self.bnode.data_type       = data_type

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(2, min)
            self.plug(3, max)
        elif data_type == 'INT':
            self.plug(4, min)
            self.plug(5, max)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(0, min)
            self.plug(1, max)

        self.plug(6, probability)
        self.plug(7, ID)
        self.plug(8, seed)

        # Output sockets

        if data_type == 'FLOAT':
            self.value           = self.Float(self.bnode.outputs[1])
        elif data_type == 'INT':
            self.value           = self.Integer(self.bnode.outputs[2])
        elif data_type == 'FLOAT_VECTOR':
            self.value           = self.Vector(self.bnode.outputs[0])
        elif data_type == 'BOOLEAN':
            self.value           = self.Boolean(self.bnode.outputs[3])

        self.output_sockets  = []

# ----------------------------------------------------------------------------------------------------
# Node NodeReplaceString for FunctionNodeReplaceString

class NodeReplaceString(Node):

    """Node 'Replace String' (FunctionNodeReplaceString)

    Input sockets
    -------------
        string          : String
        find            : String
        replace         : String

    Output sockets
    --------------
        string          : String
    """

    def __init__(self, string=None, find=None, replace=None, label=None):

        super().__init__('FunctionNodeReplaceString', name='Replace String', label=label)

        # Input sockets

        self.plug(0, string)
        self.plug(1, find)
        self.plug(2, replace)

        # Output sockets

        self.string          = self.String(self.bnode.outputs[0])
        self.output_sockets  = [self.string]

# ----------------------------------------------------------------------------------------------------
# Node NodeRotateEuler for FunctionNodeRotateEuler

class NodeRotateEuler(Node):

    """Node 'Rotate Euler' (FunctionNodeRotateEuler)

    Input sockets
    -------------
        rotation        : Vector
        rotate_by       : Vector
        axis            : Vector
        angle           : Float

    Parameters
    ----------
        space           : 'OBJECT' in [ 'OBJECT' 'LOCAL']

    Output sockets
    --------------
        rotation        : Vector
    """

    def __init__(self, rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', label=None):

        super().__init__('FunctionNodeRotateEuler', name='Rotate Euler', label=label)

        # Parameters

        self.bnode.space           = space

        # Input sockets

        self.plug(0, rotation)
        self.plug(1, rotate_by)
        self.plug(2, axis)
        self.plug(3, angle)

        # Output sockets

        self.rotation        = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = [self.rotation]

# ----------------------------------------------------------------------------------------------------
# Node NodeSliceString for FunctionNodeSliceString

class NodeSliceString(Node):

    """Node 'Slice String' (FunctionNodeSliceString)

    Input sockets
    -------------
        string          : String
        position        : Integer
        length          : Integer

    Output sockets
    --------------
        string          : String
    """

    def __init__(self, string=None, position=None, length=None, label=None):

        super().__init__('FunctionNodeSliceString', name='Slice String', label=label)

        # Input sockets

        self.plug(0, string)
        self.plug(1, position)
        self.plug(2, length)

        # Output sockets

        self.string          = self.String(self.bnode.outputs[0])
        self.output_sockets  = [self.string]

# ----------------------------------------------------------------------------------------------------
# Node NodeStringLength for FunctionNodeStringLength

class NodeStringLength(Node):

    """Node 'String Length' (FunctionNodeStringLength)

    Input sockets
    -------------
        string          : String

    Output sockets
    --------------
        length          : Integer
    """

    def __init__(self, string=None, label=None):

        super().__init__('FunctionNodeStringLength', name='String Length', label=label)

        # Input sockets

        self.plug(0, string)

        # Output sockets

        self.length          = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = [self.length]

# ----------------------------------------------------------------------------------------------------
# Node NodeValueToString for FunctionNodeValueToString

class NodeValueToString(Node):

    """Node 'Value to String' (FunctionNodeValueToString)

    Input sockets
    -------------
        value           : Float
        decimals        : Integer

    Output sockets
    --------------
        string          : String
    """

    def __init__(self, value=None, decimals=None, label=None):

        super().__init__('FunctionNodeValueToString', name='Value to String', label=label)

        # Input sockets

        self.plug(0, value)
        self.plug(1, decimals)

        # Output sockets

        self.string          = self.String(self.bnode.outputs[0])
        self.output_sockets  = [self.string]

# ----------------------------------------------------------------------------------------------------
# Node NodeAccumulateField for GeometryNodeAccumulateField

class NodeAccumulateField(Node):

    """Node 'Accumulate Field' (GeometryNodeAccumulateField)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR')

        Input sockets     : ['value']
        Output sockets    : ['leading', 'trailing', 'total']

    Input sockets
    -------------
        value           : data_type dependant
        group_index     : Integer

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR']
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CORNER' 'CURVE' 'INSTANCE']

    Output sockets
    --------------
        leading         : data_type dependant
        trailing        : data_type dependant
        total           : data_type dependant
    """

    def __init__(self, value=None, group_index=None, data_type='FLOAT', domain='POINT', label=None):

        super().__init__('GeometryNodeAccumulateField', name='Accumulate Field', label=label)

        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.domain          = domain

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(1, value)
        elif data_type == 'INT':
            self.plug(2, value)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(0, value)

        self.plug(3, group_index)

        # Output sockets

        if data_type == 'FLOAT':
            self.leading         = self.Float(self.bnode.outputs[1])
            self.trailing        = self.Float(self.bnode.outputs[4])
            self.total           = self.Float(self.bnode.outputs[7])
        elif data_type == 'INT':
            self.leading         = self.Integer(self.bnode.outputs[2])
            self.trailing        = self.Integer(self.bnode.outputs[5])
            self.total           = self.Integer(self.bnode.outputs[8])
        elif data_type == 'FLOAT_VECTOR':
            self.leading         = self.Vector(self.bnode.outputs[0])
            self.trailing        = self.Vector(self.bnode.outputs[3])
            self.total           = self.Vector(self.bnode.outputs[6])

        self.output_sockets  = []

# ----------------------------------------------------------------------------------------------------
# Node NodeDomainSize for GeometryNodeAttributeDomainSize

class NodeDomainSize(Node):

    """Node 'Domain Size' (GeometryNodeAttributeDomainSize)

    Input sockets
    -------------
        geometry        : Geometry

    Parameters
    ----------
        component       : 'MESH' in [ 'MESH' 'POINTCLOUD' 'CURVE' 'INSTANCES']

    Output sockets
    --------------
        point_count     : Integer
        edge_count      : Integer
        face_count      : Integer
        face_corner_count : Integer
        spline_count    : Integer
        instance_count  : Integer
    """

    def __init__(self, geometry=None, component='MESH', label=None):

        super().__init__('GeometryNodeAttributeDomainSize', name='Domain Size', label=label)

        # Parameters

        self.bnode.component       = component

        # Input sockets

        self.plug(0, geometry)

        # Output sockets

        self.point_count     = self.Integer(self.bnode.outputs[0])
        self.edge_count      = self.Integer(self.bnode.outputs[1])
        self.face_count      = self.Integer(self.bnode.outputs[2])
        self.face_corner_count = self.Integer(self.bnode.outputs[3])
        self.spline_count    = self.Integer(self.bnode.outputs[4])
        self.instance_count  = self.Integer(self.bnode.outputs[5])
        self.output_sockets  = [self.point_count, self.edge_count, self.face_count, self.face_corner_count, self.spline_count, self.instance_count]

# ----------------------------------------------------------------------------------------------------
# Node NodeAttributeRemove for GeometryNodeAttributeRemove

class NodeAttributeRemove(Node):

    """Node 'Attribute Remove' (GeometryNodeAttributeRemove)

    Input sockets
    -------------
        geometry        : Geometry
        attribute       : *String

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, *attribute, geometry=None, label=None):

        super().__init__('GeometryNodeAttributeRemove', name='Attribute Remove', label=label)

        # Input sockets

        self.plug(1, *attribute)
        self.plug(0, geometry)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeAttributeStatistic for GeometryNodeAttributeStatistic

class NodeAttributeStatistic(Node):

    """Node 'Attribute Statistic' (GeometryNodeAttributeStatistic)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'FLOAT_VECTOR')

        Input sockets     : ['attribute']
        Output sockets    : ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        attribute       : data_type dependant

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'FLOAT_VECTOR']
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CORNER' 'CURVE' 'INSTANCE']

    Output sockets
    --------------
        mean            : data_type dependant
        median          : data_type dependant
        sum             : data_type dependant
        min             : data_type dependant
        max             : data_type dependant
        range           : data_type dependant
        standard_deviation : data_type dependant
        variance        : data_type dependant
    """

    def __init__(self, geometry=None, selection=None, attribute=None, data_type='FLOAT', domain='POINT', label=None):

        super().__init__('GeometryNodeAttributeStatistic', name='Attribute Statistic', label=label)

        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.domain          = domain

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(2, attribute)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(3, attribute)

        self.plug(0, geometry)
        self.plug(1, selection)

        # Output sockets

        if data_type == 'FLOAT':
            self.mean            = self.Float(self.bnode.outputs[0])
            self.median          = self.Float(self.bnode.outputs[1])
            self.sum             = self.Float(self.bnode.outputs[2])
            self.min             = self.Float(self.bnode.outputs[3])
            self.max             = self.Float(self.bnode.outputs[4])
            self.range           = self.Float(self.bnode.outputs[5])
            self.standard_deviation = self.Float(self.bnode.outputs[6])
            self.variance        = self.Float(self.bnode.outputs[7])
        elif data_type == 'FLOAT_VECTOR':
            self.mean            = self.Vector(self.bnode.outputs[8])
            self.median          = self.Vector(self.bnode.outputs[9])
            self.sum             = self.Vector(self.bnode.outputs[10])
            self.min             = self.Vector(self.bnode.outputs[11])
            self.max             = self.Vector(self.bnode.outputs[12])
            self.range           = self.Vector(self.bnode.outputs[13])
            self.standard_deviation = self.Vector(self.bnode.outputs[14])
            self.variance        = self.Vector(self.bnode.outputs[15])

        self.output_sockets  = []

# ----------------------------------------------------------------------------------------------------
# Node NodeTransferAttribute for GeometryNodeAttributeTransfer

class NodeTransferAttribute(Node):

    """Node 'Transfer Attribute' (GeometryNodeAttributeTransfer)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

        Input sockets     : ['attribute']
        Output sockets    : ['attribute']

    Input sockets
    -------------
        source          : Geometry
        attribute       : data_type dependant
        source_position : Vector
        index           : Integer

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'FLOAT_COLOR' 'BOOLEAN']
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CORNER' 'CURVE' 'INSTANCE']
        mapping         : 'NEAREST_FACE_INTERPOLATED' in [ 'NEAREST_FACE_INTERPOLATED' 'NEAREST' 'INDEX']

    Output sockets
    --------------
        attribute       : data_type dependant
    """

    def __init__(self, source=None, attribute=None, source_position=None, index=None, data_type='FLOAT', domain='POINT', mapping='NEAREST_FACE_INTERPOLATED', label=None):

        super().__init__('GeometryNodeAttributeTransfer', name='Transfer Attribute', label=label)

        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.domain          = domain
        self.bnode.mapping         = mapping

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(2, attribute)
        elif data_type == 'INT':
            self.plug(5, attribute)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(1, attribute)
        elif data_type == 'FLOAT_COLOR':
            self.plug(3, attribute)
        elif data_type == 'BOOLEAN':
            self.plug(4, attribute)

        self.plug(0, source)
        self.plug(6, source_position)
        self.plug(7, index)

        # Output sockets

        if data_type == 'FLOAT':
            self.attribute       = self.Float(self.bnode.outputs[1])
        elif data_type == 'INT':
            self.attribute       = self.Integer(self.bnode.outputs[4])
        elif data_type == 'FLOAT_VECTOR':
            self.attribute       = self.Vector(self.bnode.outputs[0])
        elif data_type == 'FLOAT_COLOR':
            self.attribute       = self.Color(self.bnode.outputs[2])
        elif data_type == 'BOOLEAN':
            self.attribute       = self.Boolean(self.bnode.outputs[3])

        self.output_sockets  = []

# ----------------------------------------------------------------------------------------------------
# Node NodeBoundingBox for GeometryNodeBoundBox

class NodeBoundingBox(Node):

    """Node 'Bounding Box' (GeometryNodeBoundBox)

    Input sockets
    -------------
        geometry        : Geometry

    Output sockets
    --------------
        bounding_box    : Geometry
        min             : Vector
        max             : Vector
    """

    def __init__(self, geometry=None, label=None):

        super().__init__('GeometryNodeBoundBox', name='Bounding Box', label=label)

        # Input sockets

        self.plug(0, geometry)

        # Output sockets

        self.bounding_box    = self.Geometry(self.bnode.outputs[0])
        self.min             = self.Vector(self.bnode.outputs[1])
        self.max             = self.Vector(self.bnode.outputs[2])
        self.output_sockets  = [self.bounding_box, self.min, self.max]

# ----------------------------------------------------------------------------------------------------
# Node NodeCaptureAttribute for GeometryNodeCaptureAttribute

class NodeCaptureAttribute(Node):

    """Node 'Capture Attribute' (GeometryNodeCaptureAttribute)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

        Input sockets     : ['value']
        Output sockets    : ['attribute']

    Input sockets
    -------------
        geometry        : Geometry
        value           : data_type dependant

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'FLOAT_COLOR' 'BOOLEAN']
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CORNER' 'CURVE' 'INSTANCE']

    Output sockets
    --------------
        geometry        : Geometry
        attribute       : data_type dependant
    """

    def __init__(self, geometry=None, value=None, data_type='FLOAT', domain='POINT', label=None):

        super().__init__('GeometryNodeCaptureAttribute', name='Capture Attribute', label=label)

        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.domain          = domain

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(2, value)
        elif data_type == 'INT':
            self.plug(5, value)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(1, value)
        elif data_type == 'FLOAT_COLOR':
            self.plug(3, value)
        elif data_type == 'BOOLEAN':
            self.plug(4, value)

        self.plug(0, geometry)

        # Output sockets

        if data_type == 'FLOAT':
            self.attribute       = self.Float(self.bnode.outputs[2])
        elif data_type == 'INT':
            self.attribute       = self.Integer(self.bnode.outputs[5])
        elif data_type == 'FLOAT_VECTOR':
            self.attribute       = self.Vector(self.bnode.outputs[1])
        elif data_type == 'FLOAT_COLOR':
            self.attribute       = self.Color(self.bnode.outputs[3])
        elif data_type == 'BOOLEAN':
            self.attribute       = self.Boolean(self.bnode.outputs[4])

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeCollectionInfo for GeometryNodeCollectionInfo

class NodeCollectionInfo(Node):

    """Node 'Collection Info' (GeometryNodeCollectionInfo)

    Input sockets
    -------------
        collection      : Collection
        separate_children : Boolean
        reset_children  : Boolean

    Parameters
    ----------
        transform_space : 'ORIGINAL' in [ 'ORIGINAL' 'RELATIVE']

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL', label=None):

        super().__init__('GeometryNodeCollectionInfo', name='Collection Info', label=label)

        # Parameters

        self.bnode.transform_space = transform_space

        # Input sockets

        self.plug(0, collection)
        self.plug(1, separate_children)
        self.plug(2, reset_children)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeConvexHull for GeometryNodeConvexHull

class NodeConvexHull(Node):

    """Node 'Convex Hull' (GeometryNodeConvexHull)

    Input sockets
    -------------
        geometry        : Geometry

    Output sockets
    --------------
        convex_hull     : Geometry
    """

    def __init__(self, geometry=None, label=None):

        super().__init__('GeometryNodeConvexHull', name='Convex Hull', label=label)

        # Input sockets

        self.plug(0, geometry)

        # Output sockets

        self.convex_hull     = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.convex_hull]

# ----------------------------------------------------------------------------------------------------
# Node NodeArc for GeometryNodeCurveArc

class NodeArc(Node):

    """Node 'Arc' (GeometryNodeCurveArc)

    Input sockets
    -------------
        resolution      : Integer
        start           : Vector
        middle          : Vector
        end             : Vector
        radius          : Float
        start_angle     : Float
        sweep_angle     : Float
        offset_angle    : Float
        connect_center  : Boolean
        invert_arc      : Boolean

    Parameters
    ----------
        mode            : 'RADIUS' in [ 'POINTS' 'RADIUS']

    Output sockets
    --------------
        curve           : Geometry
        center          : Vector
        normal          : Vector
        radius          : Float
    """

    def __init__(self, resolution=None, start=None, middle=None, end=None, radius=None, start_angle=None, sweep_angle=None, offset_angle=None, connect_center=None, invert_arc=None, mode='RADIUS', label=None):

        super().__init__('GeometryNodeCurveArc', name='Arc', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, resolution)
        self.plug(1, start)
        self.plug(2, middle)
        self.plug(3, end)
        self.plug(4, radius)
        self.plug(5, start_angle)
        self.plug(6, sweep_angle)
        self.plug(7, offset_angle)
        self.plug(8, connect_center)
        self.plug(9, invert_arc)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.center          = self.Vector(self.bnode.outputs[1])
        self.normal          = self.Vector(self.bnode.outputs[2])
        self.radius          = self.Float(self.bnode.outputs[3])
        self.output_sockets  = [self.curve, self.center, self.normal, self.radius]

# ----------------------------------------------------------------------------------------------------
# Node NodeEndpointSelection for GeometryNodeCurveEndpointSelection

class NodeEndpointSelection(Node):

    """Node 'Endpoint Selection' (GeometryNodeCurveEndpointSelection)

    Input sockets
    -------------
        start_size      : Integer
        end_size        : Integer

    Output sockets
    --------------
        selection       : Boolean
    """

    def __init__(self, start_size=None, end_size=None, label=None):

        super().__init__('GeometryNodeCurveEndpointSelection', name='Endpoint Selection', label=label)

        # Input sockets

        self.plug(0, start_size)
        self.plug(1, end_size)

        # Output sockets

        self.selection       = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = [self.selection]

# ----------------------------------------------------------------------------------------------------
# Node NodeHandleTypeSelection for GeometryNodeCurveHandleTypeSelection

class NodeHandleTypeSelection(Node):

    """Node 'Handle Type Selection' (GeometryNodeCurveHandleTypeSelection)

    Parameters
    ----------
        handle_type     : 'AUTO' in [ 'FREE' 'AUTO' 'VECTOR' 'ALIGN']
        mode            : ({'LEFT', 'RIGHT'}) set

    Output sockets
    --------------
        selection       : Boolean
    """

    def __init__(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None):

        super().__init__('GeometryNodeCurveHandleTypeSelection', name='Handle Type Selection', label=label)

        # Parameters

        self.bnode.handle_type     = handle_type
        self.bnode.mode            = mode

        # Output sockets

        self.selection       = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = [self.selection]

# ----------------------------------------------------------------------------------------------------
# Node NodeCurveLength for GeometryNodeCurveLength

class NodeCurveLength(Node):

    """Node 'Curve Length' (GeometryNodeCurveLength)

    Input sockets
    -------------
        curve           : Geometry

    Output sockets
    --------------
        length          : Float
    """

    def __init__(self, curve=None, label=None):

        super().__init__('GeometryNodeCurveLength', name='Curve Length', label=label)

        # Input sockets

        self.plug(0, curve)

        # Output sockets

        self.length          = self.Float(self.bnode.outputs[0])
        self.output_sockets  = [self.length]

# ----------------------------------------------------------------------------------------------------
# Node NodeBezierSegment for GeometryNodeCurvePrimitiveBezierSegment

class NodeBezierSegment(Node):

    """Node 'Bezier Segment' (GeometryNodeCurvePrimitiveBezierSegment)

    Input sockets
    -------------
        resolution      : Integer
        start           : Vector
        start_handle    : Vector
        end_handle      : Vector
        end             : Vector

    Parameters
    ----------
        mode            : 'POSITION' in [ 'POSITION' 'OFFSET']

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', label=None):

        super().__init__('GeometryNodeCurvePrimitiveBezierSegment', name='Bezier Segment', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, resolution)
        self.plug(1, start)
        self.plug(2, start_handle)
        self.plug(3, end_handle)
        self.plug(4, end)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeCurveCircle for GeometryNodeCurvePrimitiveCircle

class NodeCurveCircle(Node):

    """Node 'Curve Circle' (GeometryNodeCurvePrimitiveCircle)

    Input sockets
    -------------
        resolution      : Integer
        point_1         : Vector
        point_2         : Vector
        point_3         : Vector
        radius          : Float

    Parameters
    ----------
        mode            : 'RADIUS' in [ 'POINTS' 'RADIUS']

    Output sockets
    --------------
        curve           : Geometry
        center          : Vector
    """

    def __init__(self, resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS', label=None):

        super().__init__('GeometryNodeCurvePrimitiveCircle', name='Curve Circle', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, resolution)
        self.plug(1, point_1)
        self.plug(2, point_2)
        self.plug(3, point_3)
        self.plug(4, radius)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.center          = self.Vector(self.bnode.outputs[1])
        self.output_sockets  = [self.curve, self.center]

# ----------------------------------------------------------------------------------------------------
# Node NodeCurveLine for GeometryNodeCurvePrimitiveLine

class NodeCurveLine(Node):

    """Node 'Curve Line' (GeometryNodeCurvePrimitiveLine)

    Input sockets
    -------------
        start           : Vector
        end             : Vector
        direction       : Vector
        length          : Float

    Parameters
    ----------
        mode            : 'POINTS' in [ 'POINTS' 'DIRECTION']

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, start=None, end=None, direction=None, length=None, mode='POINTS', label=None):

        super().__init__('GeometryNodeCurvePrimitiveLine', name='Curve Line', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, start)
        self.plug(1, end)
        self.plug(2, direction)
        self.plug(3, length)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeQuadrilateral for GeometryNodeCurvePrimitiveQuadrilateral

class NodeQuadrilateral(Node):

    """Node 'Quadrilateral' (GeometryNodeCurvePrimitiveQuadrilateral)

    Input sockets
    -------------
        width           : Float
        height          : Float
        bottom_width    : Float
        top_width       : Float
        offset          : Float
        bottom_height   : Float
        top_height      : Float
        point_1         : Vector
        point_2         : Vector
        point_3         : Vector
        point_4         : Vector

    Parameters
    ----------
        mode            : 'RECTANGLE' in [ 'RECTANGLE' 'PARALLELOGRAM' 'TRAPEZOID' 'KITE' 'POINTS']

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE', label=None):

        super().__init__('GeometryNodeCurvePrimitiveQuadrilateral', name='Quadrilateral', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, width)
        self.plug(1, height)
        self.plug(2, bottom_width)
        self.plug(3, top_width)
        self.plug(4, offset)
        self.plug(5, bottom_height)
        self.plug(6, top_height)
        self.plug(7, point_1)
        self.plug(8, point_2)
        self.plug(9, point_3)
        self.plug(10, point_4)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeQuadraticBezier for GeometryNodeCurveQuadraticBezier

class NodeQuadraticBezier(Node):

    """Node 'Quadratic Bezier' (GeometryNodeCurveQuadraticBezier)

    Input sockets
    -------------
        resolution      : Integer
        start           : Vector
        middle          : Vector
        end             : Vector

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, resolution=None, start=None, middle=None, end=None, label=None):

        super().__init__('GeometryNodeCurveQuadraticBezier', name='Quadratic Bezier', label=label)

        # Input sockets

        self.plug(0, resolution)
        self.plug(1, start)
        self.plug(2, middle)
        self.plug(3, end)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetHandleType for GeometryNodeCurveSetHandles

class NodeSetHandleType(Node):

    """Node 'Set Handle Type' (GeometryNodeCurveSetHandles)

    Input sockets
    -------------
        curve           : Geometry
        selection       : Boolean

    Parameters
    ----------
        handle_type     : 'AUTO' in [ 'FREE' 'AUTO' 'VECTOR' 'ALIGN']
        mode            : ({'LEFT', 'RIGHT'}) set

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, curve=None, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}, label=None):

        super().__init__('GeometryNodeCurveSetHandles', name='Set Handle Type', label=label)

        # Parameters

        self.bnode.handle_type     = handle_type
        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeSpiral for GeometryNodeCurveSpiral

class NodeSpiral(Node):

    """Node 'Spiral' (GeometryNodeCurveSpiral)

    Input sockets
    -------------
        resolution      : Integer
        rotations       : Float
        start_radius    : Float
        end_radius      : Float
        height          : Float
        reverse         : Boolean

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None, label=None):

        super().__init__('GeometryNodeCurveSpiral', name='Spiral', label=label)

        # Input sockets

        self.plug(0, resolution)
        self.plug(1, rotations)
        self.plug(2, start_radius)
        self.plug(3, end_radius)
        self.plug(4, height)
        self.plug(5, reverse)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetSplineType for GeometryNodeCurveSplineType

class NodeSetSplineType(Node):

    """Node 'Set Spline Type' (GeometryNodeCurveSplineType)

    Input sockets
    -------------
        curve           : Geometry
        selection       : Boolean

    Parameters
    ----------
        spline_type     : 'POLY' in [ 'BEZIER' 'NURBS' 'POLY']

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, curve=None, selection=None, spline_type='POLY', label=None):

        super().__init__('GeometryNodeCurveSplineType', name='Set Spline Type', label=label)

        # Parameters

        self.bnode.spline_type     = spline_type

        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeStar for GeometryNodeCurveStar

class NodeStar(Node):

    """Node 'Star' (GeometryNodeCurveStar)

    Input sockets
    -------------
        points          : Integer
        inner_radius    : Float
        outer_radius    : Float
        twist           : Float

    Output sockets
    --------------
        curve           : Geometry
        outer_points    : Boolean
    """

    def __init__(self, points=None, inner_radius=None, outer_radius=None, twist=None, label=None):

        super().__init__('GeometryNodeCurveStar', name='Star', label=label)

        # Input sockets

        self.plug(0, points)
        self.plug(1, inner_radius)
        self.plug(2, outer_radius)
        self.plug(3, twist)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.outer_points    = self.Boolean(self.bnode.outputs[1])
        self.output_sockets  = [self.curve, self.outer_points]

# ----------------------------------------------------------------------------------------------------
# Node NodeCurveToMesh for GeometryNodeCurveToMesh

class NodeCurveToMesh(Node):

    """Node 'Curve to Mesh' (GeometryNodeCurveToMesh)

    Input sockets
    -------------
        curve           : Geometry
        profile_curve   : Geometry
        fill_caps       : Boolean

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, curve=None, profile_curve=None, fill_caps=None, label=None):

        super().__init__('GeometryNodeCurveToMesh', name='Curve to Mesh', label=label)

        # Input sockets

        self.plug(0, curve)
        self.plug(1, profile_curve)
        self.plug(2, fill_caps)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeCurveToPoints for GeometryNodeCurveToPoints

class NodeCurveToPoints(Node):

    """Node 'Curve to Points' (GeometryNodeCurveToPoints)

    Input sockets
    -------------
        curve           : Geometry
        count           : Integer
        length          : Float

    Parameters
    ----------
        mode            : 'COUNT' in [ 'EVALUATED' 'COUNT' 'LENGTH']

    Output sockets
    --------------
        points          : Geometry
        tangent         : Vector
        normal          : Vector
        rotation        : Vector
    """

    def __init__(self, curve=None, count=None, length=None, mode='COUNT', label=None):

        super().__init__('GeometryNodeCurveToPoints', name='Curve to Points', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, count)
        self.plug(2, length)

        # Output sockets

        self.points          = self.Geometry(self.bnode.outputs[0])
        self.tangent         = self.Vector(self.bnode.outputs[1])
        self.normal          = self.Vector(self.bnode.outputs[2])
        self.rotation        = self.Vector(self.bnode.outputs[3])
        self.output_sockets  = [self.points, self.tangent, self.normal, self.rotation]

# ----------------------------------------------------------------------------------------------------
# Node NodeDeleteGeometry for GeometryNodeDeleteGeometry

class NodeDeleteGeometry(Node):

    """Node 'Delete Geometry' (GeometryNodeDeleteGeometry)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean

    Parameters
    ----------
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CURVE' 'INSTANCE']
        mode            : 'ALL' in [ 'ALL' 'EDGE_FACE' 'ONLY_FACE']

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, selection=None, domain='POINT', mode='ALL', label=None):

        super().__init__('GeometryNodeDeleteGeometry', name='Delete Geometry', label=label)

        # Parameters

        self.bnode.domain          = domain
        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeDistributePointsOnFaces for GeometryNodeDistributePointsOnFaces

class NodeDistributePointsOnFaces(Node):

    """Node 'Distribute Points on Faces' (GeometryNodeDistributePointsOnFaces)

    Input sockets
    -------------
        mesh            : Geometry
        selection       : Boolean
        distance_min    : Float
        density_max     : Float
        density         : Float
        density_factor  : Float
        seed            : Integer

    Parameters
    ----------
        distribute_method : 'RANDOM' in [ 'RANDOM' 'POISSON']

    Output sockets
    --------------
        points          : Geometry
        normal          : Vector
        rotation        : Vector
    """

    def __init__(self, mesh=None, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM', label=None):

        super().__init__('GeometryNodeDistributePointsOnFaces', name='Distribute Points on Faces', label=label)

        # Parameters

        self.bnode.distribute_method = distribute_method

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)
        self.plug(2, distance_min)
        self.plug(3, density_max)
        self.plug(4, density)
        self.plug(5, density_factor)
        self.plug(6, seed)

        # Output sockets

        self.points          = self.Geometry(self.bnode.outputs[0])
        self.normal          = self.Vector(self.bnode.outputs[1])
        self.rotation        = self.Vector(self.bnode.outputs[2])
        self.output_sockets  = [self.points, self.normal, self.rotation]

# ----------------------------------------------------------------------------------------------------
# Node NodeDualMesh for GeometryNodeDualMesh

class NodeDualMesh(Node):

    """Node 'Dual Mesh' (GeometryNodeDualMesh)

    Input sockets
    -------------
        mesh            : Geometry
        keep_boundaries : Boolean

    Output sockets
    --------------
        dual_mesh       : Geometry
    """

    def __init__(self, mesh=None, keep_boundaries=None, label=None):

        super().__init__('GeometryNodeDualMesh', name='Dual Mesh', label=label)

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, keep_boundaries)

        # Output sockets

        self.dual_mesh       = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.dual_mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeExtrudeMesh for GeometryNodeExtrudeMesh

class NodeExtrudeMesh(Node):

    """Node 'Extrude Mesh' (GeometryNodeExtrudeMesh)

    Input sockets
    -------------
        mesh            : Geometry
        selection       : Boolean
        offset          : Vector
        offset_scale    : Float
        individual      : Boolean

    Parameters
    ----------
        mode            : 'FACES' in [ 'VERTICES' 'EDGES' 'FACES']

    Output sockets
    --------------
        mesh            : Geometry
        top             : Boolean
        side            : Boolean
    """

    def __init__(self, mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES', label=None):

        super().__init__('GeometryNodeExtrudeMesh', name='Extrude Mesh', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)
        self.plug(2, offset)
        self.plug(3, offset_scale)
        self.plug(4, individual)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.top             = self.Boolean(self.bnode.outputs[1])
        self.side            = self.Boolean(self.bnode.outputs[2])
        self.output_sockets  = [self.mesh, self.top, self.side]

# ----------------------------------------------------------------------------------------------------
# Node NodeFieldAtIndex for GeometryNodeFieldAtIndex

class NodeFieldAtIndex(Node):

    """Node 'Field at Index' (GeometryNodeFieldAtIndex)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

        Input sockets     : ['value']
        Output sockets    : ['value']

    Input sockets
    -------------
        index           : Integer
        value           : data_type dependant

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'FLOAT_COLOR' 'BOOLEAN']
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CORNER' 'CURVE' 'INSTANCE']

    Output sockets
    --------------
        value           : data_type dependant
    """

    def __init__(self, index=None, value=None, data_type='FLOAT', domain='POINT', label=None):

        super().__init__('GeometryNodeFieldAtIndex', name='Field at Index', label=label)

        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.domain          = domain

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(1, value)
        elif data_type == 'INT':
            self.plug(2, value)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(3, value)
        elif data_type == 'FLOAT_COLOR':
            self.plug(4, value)
        elif data_type == 'BOOLEAN':
            self.plug(5, value)

        self.plug(0, index)

        # Output sockets

        if data_type == 'FLOAT':
            self.value           = self.Float(self.bnode.outputs[0])
        elif data_type == 'INT':
            self.value           = self.Integer(self.bnode.outputs[1])
        elif data_type == 'FLOAT_VECTOR':
            self.value           = self.Vector(self.bnode.outputs[2])
        elif data_type == 'FLOAT_COLOR':
            self.value           = self.Color(self.bnode.outputs[3])
        elif data_type == 'BOOLEAN':
            self.value           = self.Boolean(self.bnode.outputs[4])

        self.output_sockets  = []

# ----------------------------------------------------------------------------------------------------
# Node NodeFillCurve for GeometryNodeFillCurve

class NodeFillCurve(Node):

    """Node 'Fill Curve' (GeometryNodeFillCurve)

    Input sockets
    -------------
        curve           : Geometry

    Parameters
    ----------
        mode            : 'TRIANGLES' in [ 'TRIANGLES' 'NGONS']

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, curve=None, mode='TRIANGLES', label=None):

        super().__init__('GeometryNodeFillCurve', name='Fill Curve', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeFilletCurve for GeometryNodeFilletCurve

class NodeFilletCurve(Node):

    """Node 'Fillet Curve' (GeometryNodeFilletCurve)

    Input sockets
    -------------
        curve           : Geometry
        count           : Integer
        radius          : Float
        limit_radius    : Boolean

    Parameters
    ----------
        mode            : 'BEZIER' in [ 'BEZIER' 'POLY']

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER', label=None):

        super().__init__('GeometryNodeFilletCurve', name='Fillet Curve', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, count)
        self.plug(2, radius)
        self.plug(3, limit_radius)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeFlipFaces for GeometryNodeFlipFaces

class NodeFlipFaces(Node):

    """Node 'Flip Faces' (GeometryNodeFlipFaces)

    Input sockets
    -------------
        mesh            : Geometry
        selection       : Boolean

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, mesh=None, selection=None, label=None):

        super().__init__('GeometryNodeFlipFaces', name='Flip Faces', label=label)

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeGeometryToInstance for GeometryNodeGeometryToInstance

class NodeGeometryToInstance(Node):

    """Node 'Geometry to Instance' (GeometryNodeGeometryToInstance)

    Input sockets
    -------------
        geometry        : *Geometry

    Output sockets
    --------------
        instances       : Geometry
    """

    def __init__(self, *geometry, label=None):

        super().__init__('GeometryNodeGeometryToInstance', name='Geometry to Instance', label=label)

        # Input sockets

        self.plug(0, *geometry)

        # Output sockets

        self.instances       = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.instances]

# ----------------------------------------------------------------------------------------------------
# Node NodeGroup for GeometryNodeGroup

class NodeGroup(Node):

    """Node 'Group' (GeometryNodeGroup)

    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeGroup', name='Group', label=label)

        self.output_sockets  = []

# ----------------------------------------------------------------------------------------------------
# Node NodeImageTexture for GeometryNodeImageTexture

class NodeImageTexture(Node):

    """Node 'Image Texture' (GeometryNodeImageTexture)

    Input sockets
    -------------
        image           : Image
        vector          : Vector
        frame           : Integer

    Parameters
    ----------
        extension       : 'REPEAT' in [ 'REPEAT' 'EXTEND' 'CLIP']
        interpolation   : 'Linear' in [ 'Linear' 'Closest' 'Cubic']

    Output sockets
    --------------
        color           : Color
        alpha           : Float
    """

    def __init__(self, image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear', label=None):

        super().__init__('GeometryNodeImageTexture', name='Image Texture', label=label)

        # Parameters

        self.bnode.extension       = extension
        self.bnode.interpolation   = interpolation

        # Input sockets

        self.plug(0, image)
        self.plug(1, vector)
        self.plug(2, frame)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.alpha           = self.Float(self.bnode.outputs[1])
        self.output_sockets  = [self.color, self.alpha]

# ----------------------------------------------------------------------------------------------------
# Node NodeCurveHandlePositions for GeometryNodeInputCurveHandlePositions

class NodeCurveHandlePositions(Node):

    """Node 'Curve Handle Positions' (GeometryNodeInputCurveHandlePositions)

    Input sockets
    -------------
        relative        : Boolean

    Output sockets
    --------------
        left            : Vector
        right           : Vector
    """

    def __init__(self, relative=None, label=None):

        super().__init__('GeometryNodeInputCurveHandlePositions', name='Curve Handle Positions', label=label)

        # Input sockets

        self.plug(0, relative)

        # Output sockets

        self.left            = self.Vector(self.bnode.outputs[0])
        self.right           = self.Vector(self.bnode.outputs[1])
        self.output_sockets  = [self.left, self.right]

# ----------------------------------------------------------------------------------------------------
# Node NodeCurveTilt for GeometryNodeInputCurveTilt

class NodeCurveTilt(Node):

    """Node 'Curve Tilt' (GeometryNodeInputCurveTilt)

    Output sockets
    --------------
        tilt            : Float
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputCurveTilt', name='Curve Tilt', label=label)

        # Output sockets

        self.tilt            = self.Float(self.bnode.outputs[0])
        self.output_sockets  = [self.tilt]

# ----------------------------------------------------------------------------------------------------
# Node NodeID for GeometryNodeInputID

class NodeID(Node):

    """Node 'ID' (GeometryNodeInputID)

    Output sockets
    --------------
        ID              : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputID', name='ID', label=label)

        # Output sockets

        self.ID              = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = [self.ID]

# ----------------------------------------------------------------------------------------------------
# Node NodeIndex for GeometryNodeInputIndex

class NodeIndex(Node):

    """Node 'Index' (GeometryNodeInputIndex)

    Output sockets
    --------------
        index           : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputIndex', name='Index', label=label)

        # Output sockets

        self.index           = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = [self.index]

# ----------------------------------------------------------------------------------------------------
# Node NodeMaterial for GeometryNodeInputMaterial

class NodeMaterial(Node):

    """Node 'Material' (GeometryNodeInputMaterial)

    Output sockets
    --------------
        material        : Material
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMaterial', name='Material', label=label)

        # Output sockets

        self.material        = self.Material(self.bnode.outputs[0])
        self.output_sockets  = [self.material]

# ----------------------------------------------------------------------------------------------------
# Node NodeMaterialIndex for GeometryNodeInputMaterialIndex

class NodeMaterialIndex(Node):

    """Node 'Material Index' (GeometryNodeInputMaterialIndex)

    Output sockets
    --------------
        material_index  : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMaterialIndex', name='Material Index', label=label)

        # Output sockets

        self.material_index  = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = [self.material_index]

# ----------------------------------------------------------------------------------------------------
# Node NodeEdgeAngle for GeometryNodeInputMeshEdgeAngle

class NodeEdgeAngle(Node):

    """Node 'Edge Angle' (GeometryNodeInputMeshEdgeAngle)

    Output sockets
    --------------
        unsigned_angle  : Float
        signed_angle    : Float
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshEdgeAngle', name='Edge Angle', label=label)

        # Output sockets

        self.unsigned_angle  = self.Float(self.bnode.outputs[0])
        self.signed_angle    = self.Float(self.bnode.outputs[1])
        self.output_sockets  = [self.unsigned_angle, self.signed_angle]

# ----------------------------------------------------------------------------------------------------
# Node NodeEdgeNeighbors for GeometryNodeInputMeshEdgeNeighbors

class NodeEdgeNeighbors(Node):

    """Node 'Edge Neighbors' (GeometryNodeInputMeshEdgeNeighbors)

    Output sockets
    --------------
        face_count      : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshEdgeNeighbors', name='Edge Neighbors', label=label)

        # Output sockets

        self.face_count      = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = [self.face_count]

# ----------------------------------------------------------------------------------------------------
# Node NodeEdgeVertices for GeometryNodeInputMeshEdgeVertices

class NodeEdgeVertices(Node):

    """Node 'Edge Vertices' (GeometryNodeInputMeshEdgeVertices)

    Output sockets
    --------------
        vertex_index_1  : Integer
        vertex_index_2  : Integer
        position_1      : Vector
        position_2      : Vector
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshEdgeVertices', name='Edge Vertices', label=label)

        # Output sockets

        self.vertex_index_1  = self.Integer(self.bnode.outputs[0])
        self.vertex_index_2  = self.Integer(self.bnode.outputs[1])
        self.position_1      = self.Vector(self.bnode.outputs[2])
        self.position_2      = self.Vector(self.bnode.outputs[3])
        self.output_sockets  = [self.vertex_index_1, self.vertex_index_2, self.position_1, self.position_2]

# ----------------------------------------------------------------------------------------------------
# Node NodeFaceArea for GeometryNodeInputMeshFaceArea

class NodeFaceArea(Node):

    """Node 'Face Area' (GeometryNodeInputMeshFaceArea)

    Output sockets
    --------------
        area            : Float
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshFaceArea', name='Face Area', label=label)

        # Output sockets

        self.area            = self.Float(self.bnode.outputs[0])
        self.output_sockets  = [self.area]

# ----------------------------------------------------------------------------------------------------
# Node NodeFaceNeighbors for GeometryNodeInputMeshFaceNeighbors

class NodeFaceNeighbors(Node):

    """Node 'Face Neighbors' (GeometryNodeInputMeshFaceNeighbors)

    Output sockets
    --------------
        vertex_count    : Integer
        face_count      : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshFaceNeighbors', name='Face Neighbors', label=label)

        # Output sockets

        self.vertex_count    = self.Integer(self.bnode.outputs[0])
        self.face_count      = self.Integer(self.bnode.outputs[1])
        self.output_sockets  = [self.vertex_count, self.face_count]

# ----------------------------------------------------------------------------------------------------
# Node NodeMeshIsland for GeometryNodeInputMeshIsland

class NodeMeshIsland(Node):

    """Node 'Mesh Island' (GeometryNodeInputMeshIsland)

    Output sockets
    --------------
        island_index    : Integer
        island_count    : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshIsland', name='Mesh Island', label=label)

        # Output sockets

        self.island_index    = self.Integer(self.bnode.outputs[0])
        self.island_count    = self.Integer(self.bnode.outputs[1])
        self.output_sockets  = [self.island_index, self.island_count]

# ----------------------------------------------------------------------------------------------------
# Node NodeVertexNeighbors for GeometryNodeInputMeshVertexNeighbors

class NodeVertexNeighbors(Node):

    """Node 'Vertex Neighbors' (GeometryNodeInputMeshVertexNeighbors)

    Output sockets
    --------------
        vertex_count    : Integer
        face_count      : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputMeshVertexNeighbors', name='Vertex Neighbors', label=label)

        # Output sockets

        self.vertex_count    = self.Integer(self.bnode.outputs[0])
        self.face_count      = self.Integer(self.bnode.outputs[1])
        self.output_sockets  = [self.vertex_count, self.face_count]

# ----------------------------------------------------------------------------------------------------
# Node NodeNormal for GeometryNodeInputNormal

class NodeNormal(Node):

    """Node 'Normal' (GeometryNodeInputNormal)

    Output sockets
    --------------
        normal          : Vector
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputNormal', name='Normal', label=label)

        # Output sockets

        self.normal          = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = [self.normal]

# ----------------------------------------------------------------------------------------------------
# Node NodePosition for GeometryNodeInputPosition

class NodePosition(Node):

    """Node 'Position' (GeometryNodeInputPosition)

    Output sockets
    --------------
        position        : Vector
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputPosition', name='Position', label=label)

        # Output sockets

        self.position        = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = [self.position]

# ----------------------------------------------------------------------------------------------------
# Node NodeRadius for GeometryNodeInputRadius

class NodeRadius(Node):

    """Node 'Radius' (GeometryNodeInputRadius)

    Output sockets
    --------------
        radius          : Float
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputRadius', name='Radius', label=label)

        # Output sockets

        self.radius          = self.Float(self.bnode.outputs[0])
        self.output_sockets  = [self.radius]

# ----------------------------------------------------------------------------------------------------
# Node NodeSceneTime for GeometryNodeInputSceneTime

class NodeSceneTime(Node):

    """Node 'Scene Time' (GeometryNodeInputSceneTime)

    Output sockets
    --------------
        seconds         : Float
        frame           : Float
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputSceneTime', name='Scene Time', label=label)

        # Output sockets

        self.seconds         = self.Float(self.bnode.outputs[0])
        self.frame           = self.Float(self.bnode.outputs[1])
        self.output_sockets  = [self.seconds, self.frame]

# ----------------------------------------------------------------------------------------------------
# Node NodeIsShadeSmooth for GeometryNodeInputShadeSmooth

class NodeIsShadeSmooth(Node):

    """Node 'Is Shade Smooth' (GeometryNodeInputShadeSmooth)

    Output sockets
    --------------
        smooth          : Boolean
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputShadeSmooth', name='Is Shade Smooth', label=label)

        # Output sockets

        self.smooth          = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = [self.smooth]

# ----------------------------------------------------------------------------------------------------
# Node NodeIsSplineCyclic for GeometryNodeInputSplineCyclic

class NodeIsSplineCyclic(Node):

    """Node 'Is Spline Cyclic' (GeometryNodeInputSplineCyclic)

    Output sockets
    --------------
        cyclic          : Boolean
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputSplineCyclic', name='Is Spline Cyclic', label=label)

        # Output sockets

        self.cyclic          = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = [self.cyclic]

# ----------------------------------------------------------------------------------------------------
# Node NodeSplineResolution for GeometryNodeInputSplineResolution

class NodeSplineResolution(Node):

    """Node 'Spline Resolution' (GeometryNodeInputSplineResolution)

    Output sockets
    --------------
        resolution      : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputSplineResolution', name='Spline Resolution', label=label)

        # Output sockets

        self.resolution      = self.Integer(self.bnode.outputs[0])
        self.output_sockets  = [self.resolution]

# ----------------------------------------------------------------------------------------------------
# Node NodeCurveTangent for GeometryNodeInputTangent

class NodeCurveTangent(Node):

    """Node 'Curve Tangent' (GeometryNodeInputTangent)

    Output sockets
    --------------
        tangent         : Vector
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeInputTangent', name='Curve Tangent', label=label)

        # Output sockets

        self.tangent         = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = [self.tangent]

# ----------------------------------------------------------------------------------------------------
# Node NodeInstanceOnPoints for GeometryNodeInstanceOnPoints

class NodeInstanceOnPoints(Node):

    """Node 'Instance on Points' (GeometryNodeInstanceOnPoints)

    Input sockets
    -------------
        points          : Geometry
        selection       : Boolean
        instance        : Geometry
        pick_instance   : Boolean
        instance_index  : Integer
        rotation        : Vector
        scale           : Vector

    Output sockets
    --------------
        instances       : Geometry
    """

    def __init__(self, points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None, label=None):

        super().__init__('GeometryNodeInstanceOnPoints', name='Instance on Points', label=label)

        # Input sockets

        self.plug(0, points)
        self.plug(1, selection)
        self.plug(2, instance)
        self.plug(3, pick_instance)
        self.plug(4, instance_index)
        self.plug(5, rotation)
        self.plug(6, scale)

        # Output sockets

        self.instances       = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.instances]

# ----------------------------------------------------------------------------------------------------
# Node NodeInstancesToPoints for GeometryNodeInstancesToPoints

class NodeInstancesToPoints(Node):

    """Node 'Instances to Points' (GeometryNodeInstancesToPoints)

    Input sockets
    -------------
        instances       : Geometry
        selection       : Boolean
        position        : Vector
        radius          : Float

    Output sockets
    --------------
        points          : Geometry
    """

    def __init__(self, instances=None, selection=None, position=None, radius=None, label=None):

        super().__init__('GeometryNodeInstancesToPoints', name='Instances to Points', label=label)

        # Input sockets

        self.plug(0, instances)
        self.plug(1, selection)
        self.plug(2, position)
        self.plug(3, radius)

        # Output sockets

        self.points          = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.points]

# ----------------------------------------------------------------------------------------------------
# Node NodeIsViewport for GeometryNodeIsViewport

class NodeIsViewport(Node):

    """Node 'Is Viewport' (GeometryNodeIsViewport)

    Output sockets
    --------------
        is_viewport     : Boolean
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeIsViewport', name='Is Viewport', label=label)

        # Output sockets

        self.is_viewport     = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = [self.is_viewport]

# ----------------------------------------------------------------------------------------------------
# Node NodeJoinGeometry for GeometryNodeJoinGeometry

class NodeJoinGeometry(Node):

    """Node 'Join Geometry' (GeometryNodeJoinGeometry)

    Input sockets
    -------------
        geometry        : *Geometry

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, *geometry, label=None):

        super().__init__('GeometryNodeJoinGeometry', name='Join Geometry', label=label)

        # Input sockets

        self.plug(0, *geometry)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeMaterialSelection for GeometryNodeMaterialSelection

class NodeMaterialSelection(Node):

    """Node 'Material Selection' (GeometryNodeMaterialSelection)

    Input sockets
    -------------
        material        : Material

    Output sockets
    --------------
        selection       : Boolean
    """

    def __init__(self, material=None, label=None):

        super().__init__('GeometryNodeMaterialSelection', name='Material Selection', label=label)

        # Input sockets

        self.plug(0, material)

        # Output sockets

        self.selection       = self.Boolean(self.bnode.outputs[0])
        self.output_sockets  = [self.selection]

# ----------------------------------------------------------------------------------------------------
# Node NodeMergeByDistance for GeometryNodeMergeByDistance

class NodeMergeByDistance(Node):

    """Node 'Merge by Distance' (GeometryNodeMergeByDistance)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        distance        : Float

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, selection=None, distance=None, label=None):

        super().__init__('GeometryNodeMergeByDistance', name='Merge by Distance', label=label)

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, distance)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeMeshBoolean for GeometryNodeMeshBoolean

class NodeMeshBoolean(Node):

    """Node 'Mesh Boolean' (GeometryNodeMeshBoolean)

    Input sockets
    -------------
        mesh_1          : Geometry
        mesh_2          : *Geometry
        self_intersection : Boolean
        hole_tolerant   : Boolean

    Parameters
    ----------
        operation       : 'DIFFERENCE' in [ 'INTERSECT' 'UNION' 'DIFFERENCE']

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, *mesh_2, mesh_1=None, self_intersection=None, hole_tolerant=None, operation='DIFFERENCE', label=None):

        super().__init__('GeometryNodeMeshBoolean', name='Mesh Boolean', label=label)

        # Parameters

        self.bnode.operation       = operation

        # Input sockets

        self.plug(1, *mesh_2)
        self.plug(0, mesh_1)
        self.plug(2, self_intersection)
        self.plug(3, hole_tolerant)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeMeshCircle for GeometryNodeMeshCircle

class NodeMeshCircle(Node):

    """Node 'Mesh Circle' (GeometryNodeMeshCircle)

    Input sockets
    -------------
        vertices        : Integer
        radius          : Float

    Parameters
    ----------
        fill_type       : 'NONE' in [ 'NONE' 'NGON' 'TRIANGLE_FAN']

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, vertices=None, radius=None, fill_type='NONE', label=None):

        super().__init__('GeometryNodeMeshCircle', name='Mesh Circle', label=label)

        # Parameters

        self.bnode.fill_type       = fill_type

        # Input sockets

        self.plug(0, vertices)
        self.plug(1, radius)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeCone for GeometryNodeMeshCone

class NodeCone(Node):

    """Node 'Cone' (GeometryNodeMeshCone)

    Input sockets
    -------------
        vertices        : Integer
        side_segments   : Integer
        fill_segments   : Integer
        radius_top      : Float
        radius_bottom   : Float
        depth           : Float

    Parameters
    ----------
        fill_type       : 'NGON' in [ 'NONE' 'NGON' 'TRIANGLE_FAN']

    Output sockets
    --------------
        mesh            : Geometry
        top             : Boolean
        bottom          : Boolean
        side            : Boolean
    """

    def __init__(self, vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON', label=None):

        super().__init__('GeometryNodeMeshCone', name='Cone', label=label)

        # Parameters

        self.bnode.fill_type       = fill_type

        # Input sockets

        self.plug(0, vertices)
        self.plug(1, side_segments)
        self.plug(2, fill_segments)
        self.plug(3, radius_top)
        self.plug(4, radius_bottom)
        self.plug(5, depth)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.top             = self.Boolean(self.bnode.outputs[1])
        self.bottom          = self.Boolean(self.bnode.outputs[2])
        self.side            = self.Boolean(self.bnode.outputs[3])
        self.output_sockets  = [self.mesh, self.top, self.bottom, self.side]

# ----------------------------------------------------------------------------------------------------
# Node NodeCube for GeometryNodeMeshCube

class NodeCube(Node):

    """Node 'Cube' (GeometryNodeMeshCube)

    Input sockets
    -------------
        size            : Vector
        vertices_x      : Integer
        vertices_y      : Integer
        vertices_z      : Integer

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, size=None, vertices_x=None, vertices_y=None, vertices_z=None, label=None):

        super().__init__('GeometryNodeMeshCube', name='Cube', label=label)

        # Input sockets

        self.plug(0, size)
        self.plug(1, vertices_x)
        self.plug(2, vertices_y)
        self.plug(3, vertices_z)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeCylinder for GeometryNodeMeshCylinder

class NodeCylinder(Node):

    """Node 'Cylinder' (GeometryNodeMeshCylinder)

    Input sockets
    -------------
        vertices        : Integer
        side_segments   : Integer
        fill_segments   : Integer
        radius          : Float
        depth           : Float

    Parameters
    ----------
        fill_type       : 'NGON' in [ 'NONE' 'NGON' 'TRIANGLE_FAN']

    Output sockets
    --------------
        mesh            : Geometry
        top             : Boolean
        side            : Boolean
        bottom          : Boolean
    """

    def __init__(self, vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON', label=None):

        super().__init__('GeometryNodeMeshCylinder', name='Cylinder', label=label)

        # Parameters

        self.bnode.fill_type       = fill_type

        # Input sockets

        self.plug(0, vertices)
        self.plug(1, side_segments)
        self.plug(2, fill_segments)
        self.plug(3, radius)
        self.plug(4, depth)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.top             = self.Boolean(self.bnode.outputs[1])
        self.side            = self.Boolean(self.bnode.outputs[2])
        self.bottom          = self.Boolean(self.bnode.outputs[3])
        self.output_sockets  = [self.mesh, self.top, self.side, self.bottom]

# ----------------------------------------------------------------------------------------------------
# Node NodeGrid for GeometryNodeMeshGrid

class NodeGrid(Node):

    """Node 'Grid' (GeometryNodeMeshGrid)

    Input sockets
    -------------
        size_x          : Float
        size_y          : Float
        vertices_x      : Integer
        vertices_y      : Integer

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, size_x=None, size_y=None, vertices_x=None, vertices_y=None, label=None):

        super().__init__('GeometryNodeMeshGrid', name='Grid', label=label)

        # Input sockets

        self.plug(0, size_x)
        self.plug(1, size_y)
        self.plug(2, vertices_x)
        self.plug(3, vertices_y)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeIcoSphere for GeometryNodeMeshIcoSphere

class NodeIcoSphere(Node):

    """Node 'Ico Sphere' (GeometryNodeMeshIcoSphere)

    Input sockets
    -------------
        radius          : Float
        subdivisions    : Integer

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, radius=None, subdivisions=None, label=None):

        super().__init__('GeometryNodeMeshIcoSphere', name='Ico Sphere', label=label)

        # Input sockets

        self.plug(0, radius)
        self.plug(1, subdivisions)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeMeshLine for GeometryNodeMeshLine

class NodeMeshLine(Node):

    """Node 'Mesh Line' (GeometryNodeMeshLine)

    Input sockets
    -------------
        count           : Integer
        resolution      : Float
        start_location  : Vector
        offset          : Vector

    Parameters
    ----------
        count_mode      : 'TOTAL' in [ 'TOTAL' 'RESOLUTION']
        mode            : 'OFFSET' in [ 'OFFSET' 'END_POINTS']

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET', label=None):

        super().__init__('GeometryNodeMeshLine', name='Mesh Line', label=label)

        # Parameters

        self.bnode.count_mode      = count_mode
        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, count)
        self.plug(1, resolution)
        self.plug(2, start_location)
        self.plug(3, offset)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeMeshToCurve for GeometryNodeMeshToCurve

class NodeMeshToCurve(Node):

    """Node 'Mesh to Curve' (GeometryNodeMeshToCurve)

    Input sockets
    -------------
        mesh            : Geometry
        selection       : Boolean

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, mesh=None, selection=None, label=None):

        super().__init__('GeometryNodeMeshToCurve', name='Mesh to Curve', label=label)

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeMeshToPoints for GeometryNodeMeshToPoints

class NodeMeshToPoints(Node):

    """Node 'Mesh to Points' (GeometryNodeMeshToPoints)

    Input sockets
    -------------
        mesh            : Geometry
        selection       : Boolean
        position        : Vector
        radius          : Float

    Parameters
    ----------
        mode            : 'VERTICES' in [ 'VERTICES' 'EDGES' 'FACES' 'CORNERS']

    Output sockets
    --------------
        points          : Geometry
    """

    def __init__(self, mesh=None, selection=None, position=None, radius=None, mode='VERTICES', label=None):

        super().__init__('GeometryNodeMeshToPoints', name='Mesh to Points', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)
        self.plug(2, position)
        self.plug(3, radius)

        # Output sockets

        self.points          = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.points]

# ----------------------------------------------------------------------------------------------------
# Node NodeUvSphere for GeometryNodeMeshUVSphere

class NodeUvSphere(Node):

    """Node 'UV Sphere' (GeometryNodeMeshUVSphere)

    Input sockets
    -------------
        segments        : Integer
        rings           : Integer
        radius          : Float

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, segments=None, rings=None, radius=None, label=None):

        super().__init__('GeometryNodeMeshUVSphere', name='UV Sphere', label=label)

        # Input sockets

        self.plug(0, segments)
        self.plug(1, rings)
        self.plug(2, radius)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeObjectInfo for GeometryNodeObjectInfo

class NodeObjectInfo(Node):

    """Node 'Object Info' (GeometryNodeObjectInfo)

    Input sockets
    -------------
        object          : Object
        as_instance     : Boolean

    Parameters
    ----------
        transform_space : 'ORIGINAL' in [ 'ORIGINAL' 'RELATIVE']

    Output sockets
    --------------
        location        : Vector
        rotation        : Vector
        scale           : Vector
        geometry        : Geometry
    """

    def __init__(self, object=None, as_instance=None, transform_space='ORIGINAL', label=None):

        super().__init__('GeometryNodeObjectInfo', name='Object Info', label=label)

        # Parameters

        self.bnode.transform_space = transform_space

        # Input sockets

        self.plug(0, object)
        self.plug(1, as_instance)

        # Output sockets

        self.location        = self.Vector(self.bnode.outputs[0])
        self.rotation        = self.Vector(self.bnode.outputs[1])
        self.scale           = self.Vector(self.bnode.outputs[2])
        self.geometry        = self.Geometry(self.bnode.outputs[3])
        self.output_sockets  = [self.location, self.rotation, self.scale, self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodePointsToVertices for GeometryNodePointsToVertices

class NodePointsToVertices(Node):

    """Node 'Points to Vertices' (GeometryNodePointsToVertices)

    Input sockets
    -------------
        points          : Geometry
        selection       : Boolean

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, points=None, selection=None, label=None):

        super().__init__('GeometryNodePointsToVertices', name='Points to Vertices', label=label)

        # Input sockets

        self.plug(0, points)
        self.plug(1, selection)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodePointsToVolume for GeometryNodePointsToVolume

class NodePointsToVolume(Node):

    """Node 'Points to Volume' (GeometryNodePointsToVolume)

    Input sockets
    -------------
        points          : Geometry
        density         : Float
        voxel_size      : Float
        voxel_amount    : Float
        radius          : Float

    Parameters
    ----------
        resolution_mode : 'VOXEL_AMOUNT' in [ 'VOXEL_AMOUNT' 'VOXEL_SIZE']

    Output sockets
    --------------
        volume          : Geometry
    """

    def __init__(self, points=None, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT', label=None):

        super().__init__('GeometryNodePointsToVolume', name='Points to Volume', label=label)

        # Parameters

        self.bnode.resolution_mode = resolution_mode

        # Input sockets

        self.plug(0, points)
        self.plug(1, density)
        self.plug(2, voxel_size)
        self.plug(3, voxel_amount)
        self.plug(4, radius)

        # Output sockets

        self.volume          = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.volume]

# ----------------------------------------------------------------------------------------------------
# Node NodeGeometryProximity for GeometryNodeProximity

class NodeGeometryProximity(Node):

    """Node 'Geometry Proximity' (GeometryNodeProximity)

    Input sockets
    -------------
        target          : Geometry
        source_position : Vector

    Parameters
    ----------
        target_element  : 'FACES' in [ 'POINTS' 'EDGES' 'FACES']

    Output sockets
    --------------
        position        : Vector
        distance        : Float
    """

    def __init__(self, target=None, source_position=None, target_element='FACES', label=None):

        super().__init__('GeometryNodeProximity', name='Geometry Proximity', label=label)

        # Parameters

        self.bnode.target_element  = target_element

        # Input sockets

        self.plug(0, target)
        self.plug(1, source_position)

        # Output sockets

        self.position        = self.Vector(self.bnode.outputs[0])
        self.distance        = self.Float(self.bnode.outputs[1])
        self.output_sockets  = [self.position, self.distance]

# ----------------------------------------------------------------------------------------------------
# Node NodeRaycast for GeometryNodeRaycast

class NodeRaycast(Node):

    """Node 'Raycast' (GeometryNodeRaycast)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

        Input sockets     : ['attribute']
        Output sockets    : ['attribute']

    Input sockets
    -------------
        target_geometry : Geometry
        attribute       : data_type dependant
        source_position : Vector
        ray_direction   : Vector
        ray_length      : Float

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'FLOAT_COLOR' 'BOOLEAN']
        mapping         : 'INTERPOLATED' in [ 'INTERPOLATED' 'NEAREST']

    Output sockets
    --------------
        is_hit          : Boolean
        hit_position    : Vector
        hit_normal      : Vector
        hit_distance    : Float
        attribute       : data_type dependant
    """

    def __init__(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, data_type='FLOAT', mapping='INTERPOLATED', label=None):

        super().__init__('GeometryNodeRaycast', name='Raycast', label=label)

        # Parameters

        self.bnode.data_type       = data_type
        self.bnode.mapping         = mapping

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(2, attribute)
        elif data_type == 'INT':
            self.plug(5, attribute)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(1, attribute)
        elif data_type == 'FLOAT_COLOR':
            self.plug(3, attribute)
        elif data_type == 'BOOLEAN':
            self.plug(4, attribute)

        self.plug(0, target_geometry)
        self.plug(6, source_position)
        self.plug(7, ray_direction)
        self.plug(8, ray_length)

        # Output sockets

        if data_type == 'FLOAT':
            self.attribute       = self.Float(self.bnode.outputs[5])
        elif data_type == 'INT':
            self.attribute       = self.Integer(self.bnode.outputs[8])
        elif data_type == 'FLOAT_VECTOR':
            self.attribute       = self.Vector(self.bnode.outputs[4])
        elif data_type == 'FLOAT_COLOR':
            self.attribute       = self.Color(self.bnode.outputs[6])
        elif data_type == 'BOOLEAN':
            self.attribute       = self.Boolean(self.bnode.outputs[7])

        self.is_hit          = self.Boolean(self.bnode.outputs[0])
        self.hit_position    = self.Vector(self.bnode.outputs[1])
        self.hit_normal      = self.Vector(self.bnode.outputs[2])
        self.hit_distance    = self.Float(self.bnode.outputs[3])
        self.output_sockets  = [self.is_hit, self.hit_position, self.hit_normal, self.hit_distance]

# ----------------------------------------------------------------------------------------------------
# Node NodeRealizeInstances for GeometryNodeRealizeInstances

class NodeRealizeInstances(Node):

    """Node 'Realize Instances' (GeometryNodeRealizeInstances)

    Input sockets
    -------------
        geometry        : Geometry

    Parameters
    ----------
        legacy_behavior : (False) bool

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, legacy_behavior=False, label=None):

        super().__init__('GeometryNodeRealizeInstances', name='Realize Instances', label=label)

        # Parameters

        self.bnode.legacy_behavior = legacy_behavior

        # Input sockets

        self.plug(0, geometry)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeReplaceMaterial for GeometryNodeReplaceMaterial

class NodeReplaceMaterial(Node):

    """Node 'Replace Material' (GeometryNodeReplaceMaterial)

    Input sockets
    -------------
        geometry        : Geometry
        old             : Material
        new             : Material

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, old=None, new=None, label=None):

        super().__init__('GeometryNodeReplaceMaterial', name='Replace Material', label=label)

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, old)
        self.plug(2, new)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeResampleCurve for GeometryNodeResampleCurve

class NodeResampleCurve(Node):

    """Node 'Resample Curve' (GeometryNodeResampleCurve)

    Input sockets
    -------------
        curve           : Geometry
        selection       : Boolean
        count           : Integer
        length          : Float

    Parameters
    ----------
        mode            : 'COUNT' in [ 'EVALUATED' 'COUNT' 'LENGTH']

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, curve=None, selection=None, count=None, length=None, mode='COUNT', label=None):

        super().__init__('GeometryNodeResampleCurve', name='Resample Curve', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)
        self.plug(2, count)
        self.plug(3, length)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeReverseCurve for GeometryNodeReverseCurve

class NodeReverseCurve(Node):

    """Node 'Reverse Curve' (GeometryNodeReverseCurve)

    Input sockets
    -------------
        curve           : Geometry
        selection       : Boolean

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, curve=None, selection=None, label=None):

        super().__init__('GeometryNodeReverseCurve', name='Reverse Curve', label=label)

        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeRotateInstances for GeometryNodeRotateInstances

class NodeRotateInstances(Node):

    """Node 'Rotate Instances' (GeometryNodeRotateInstances)

    Input sockets
    -------------
        instances       : Geometry
        selection       : Boolean
        rotation        : Vector
        pivot_point     : Vector
        local_space     : Boolean

    Output sockets
    --------------
        instances       : Geometry
    """

    def __init__(self, instances=None, selection=None, rotation=None, pivot_point=None, local_space=None, label=None):

        super().__init__('GeometryNodeRotateInstances', name='Rotate Instances', label=label)

        # Input sockets

        self.plug(0, instances)
        self.plug(1, selection)
        self.plug(2, rotation)
        self.plug(3, pivot_point)
        self.plug(4, local_space)

        # Output sockets

        self.instances       = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.instances]

# ----------------------------------------------------------------------------------------------------
# Node NodeSampleCurve for GeometryNodeSampleCurve

class NodeSampleCurve(Node):

    """Node 'Sample Curve' (GeometryNodeSampleCurve)

    Input sockets
    -------------
        curve           : Geometry
        factor          : Float
        length          : Float

    Parameters
    ----------
        mode            : 'LENGTH' in [ 'FACTOR' 'LENGTH']

    Output sockets
    --------------
        position        : Vector
        tangent         : Vector
        normal          : Vector
    """

    def __init__(self, curve=None, factor=None, length=None, mode='LENGTH', label=None):

        super().__init__('GeometryNodeSampleCurve', name='Sample Curve', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, factor)
        self.plug(2, length)

        # Output sockets

        self.position        = self.Vector(self.bnode.outputs[0])
        self.tangent         = self.Vector(self.bnode.outputs[1])
        self.normal          = self.Vector(self.bnode.outputs[2])
        self.output_sockets  = [self.position, self.tangent, self.normal]

# ----------------------------------------------------------------------------------------------------
# Node NodeScaleElements for GeometryNodeScaleElements

class NodeScaleElements(Node):

    """Node 'Scale Elements' (GeometryNodeScaleElements)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        scale           : Float
        center          : Vector
        axis            : Vector

    Parameters
    ----------
        domain          : 'FACE' in [ 'FACE' 'EDGE']
        scale_mode      : 'UNIFORM' in [ 'UNIFORM' 'SINGLE_AXIS']

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM', label=None):

        super().__init__('GeometryNodeScaleElements', name='Scale Elements', label=label)

        # Parameters

        self.bnode.domain          = domain
        self.bnode.scale_mode      = scale_mode

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, scale)
        self.plug(3, center)
        self.plug(4, axis)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeScaleInstances for GeometryNodeScaleInstances

class NodeScaleInstances(Node):

    """Node 'Scale Instances' (GeometryNodeScaleInstances)

    Input sockets
    -------------
        instances       : Geometry
        selection       : Boolean
        scale           : Vector
        center          : Vector
        local_space     : Boolean

    Output sockets
    --------------
        instances       : Geometry
    """

    def __init__(self, instances=None, selection=None, scale=None, center=None, local_space=None, label=None):

        super().__init__('GeometryNodeScaleInstances', name='Scale Instances', label=label)

        # Input sockets

        self.plug(0, instances)
        self.plug(1, selection)
        self.plug(2, scale)
        self.plug(3, center)
        self.plug(4, local_space)

        # Output sockets

        self.instances       = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.instances]

# ----------------------------------------------------------------------------------------------------
# Node NodeSeparateComponents for GeometryNodeSeparateComponents

class NodeSeparateComponents(Node):

    """Node 'Separate Components' (GeometryNodeSeparateComponents)

    Input sockets
    -------------
        geometry        : Geometry

    Output sockets
    --------------
        mesh            : Geometry
        point_cloud     : Geometry
        curve           : Geometry
        volume          : Geometry
        instances       : Geometry
    """

    def __init__(self, geometry=None, label=None):

        super().__init__('GeometryNodeSeparateComponents', name='Separate Components', label=label)

        # Input sockets

        self.plug(0, geometry)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.point_cloud     = self.Geometry(self.bnode.outputs[1])
        self.curve           = self.Geometry(self.bnode.outputs[2])
        self.volume          = self.Geometry(self.bnode.outputs[3])
        self.instances       = self.Geometry(self.bnode.outputs[4])
        self.output_sockets  = [self.mesh, self.point_cloud, self.curve, self.volume, self.instances]

# ----------------------------------------------------------------------------------------------------
# Node NodeSeparateGeometry for GeometryNodeSeparateGeometry

class NodeSeparateGeometry(Node):

    """Node 'Separate Geometry' (GeometryNodeSeparateGeometry)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean

    Parameters
    ----------
        domain          : 'POINT' in [ 'POINT' 'EDGE' 'FACE' 'CURVE' 'INSTANCE']

    Output sockets
    --------------
        selection       : Geometry
        inverted        : Geometry
    """

    def __init__(self, geometry=None, selection=None, domain='POINT', label=None):

        super().__init__('GeometryNodeSeparateGeometry', name='Separate Geometry', label=label)

        # Parameters

        self.bnode.domain          = domain

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)

        # Output sockets

        self.selection       = self.Geometry(self.bnode.outputs[0])
        self.inverted        = self.Geometry(self.bnode.outputs[1])
        self.output_sockets  = [self.selection, self.inverted]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetHandlePositions for GeometryNodeSetCurveHandlePositions

class NodeSetHandlePositions(Node):

    """Node 'Set Handle Positions' (GeometryNodeSetCurveHandlePositions)

    Input sockets
    -------------
        curve           : Geometry
        selection       : Boolean
        position        : Vector
        offset          : Vector

    Parameters
    ----------
        mode            : 'LEFT' in [ 'LEFT' 'RIGHT']

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, curve=None, selection=None, position=None, offset=None, mode='LEFT', label=None):

        super().__init__('GeometryNodeSetCurveHandlePositions', name='Set Handle Positions', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)
        self.plug(2, position)
        self.plug(3, offset)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetCurveRadius for GeometryNodeSetCurveRadius

class NodeSetCurveRadius(Node):

    """Node 'Set Curve Radius' (GeometryNodeSetCurveRadius)

    Input sockets
    -------------
        curve           : Geometry
        selection       : Boolean
        radius          : Float

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, curve=None, selection=None, radius=None, label=None):

        super().__init__('GeometryNodeSetCurveRadius', name='Set Curve Radius', label=label)

        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)
        self.plug(2, radius)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetCurveTilt for GeometryNodeSetCurveTilt

class NodeSetCurveTilt(Node):

    """Node 'Set Curve Tilt' (GeometryNodeSetCurveTilt)

    Input sockets
    -------------
        curve           : Geometry
        selection       : Boolean
        tilt            : Float

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, curve=None, selection=None, tilt=None, label=None):

        super().__init__('GeometryNodeSetCurveTilt', name='Set Curve Tilt', label=label)

        # Input sockets

        self.plug(0, curve)
        self.plug(1, selection)
        self.plug(2, tilt)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetID for GeometryNodeSetID

class NodeSetID(Node):

    """Node 'Set ID' (GeometryNodeSetID)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        ID              : Integer

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, selection=None, ID=None, label=None):

        super().__init__('GeometryNodeSetID', name='Set ID', label=label)

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, ID)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetMaterial for GeometryNodeSetMaterial

class NodeSetMaterial(Node):

    """Node 'Set Material' (GeometryNodeSetMaterial)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        material        : Material

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, selection=None, material=None, label=None):

        super().__init__('GeometryNodeSetMaterial', name='Set Material', label=label)

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, material)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetMaterialIndex for GeometryNodeSetMaterialIndex

class NodeSetMaterialIndex(Node):

    """Node 'Set Material Index' (GeometryNodeSetMaterialIndex)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        material_index  : Integer

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, selection=None, material_index=None, label=None):

        super().__init__('GeometryNodeSetMaterialIndex', name='Set Material Index', label=label)

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, material_index)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetPointRadius for GeometryNodeSetPointRadius

class NodeSetPointRadius(Node):

    """Node 'Set Point Radius' (GeometryNodeSetPointRadius)

    Input sockets
    -------------
        points          : Geometry
        selection       : Boolean
        radius          : Float

    Output sockets
    --------------
        points          : Geometry
    """

    def __init__(self, points=None, selection=None, radius=None, label=None):

        super().__init__('GeometryNodeSetPointRadius', name='Set Point Radius', label=label)

        # Input sockets

        self.plug(0, points)
        self.plug(1, selection)
        self.plug(2, radius)

        # Output sockets

        self.points          = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.points]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetPosition for GeometryNodeSetPosition

class NodeSetPosition(Node):

    """Node 'Set Position' (GeometryNodeSetPosition)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        position        : Vector
        offset          : Vector

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, selection=None, position=None, offset=None, label=None):

        super().__init__('GeometryNodeSetPosition', name='Set Position', label=label)

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, position)
        self.plug(3, offset)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetShadeSmooth for GeometryNodeSetShadeSmooth

class NodeSetShadeSmooth(Node):

    """Node 'Set Shade Smooth' (GeometryNodeSetShadeSmooth)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        shade_smooth    : Boolean

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, selection=None, shade_smooth=None, label=None):

        super().__init__('GeometryNodeSetShadeSmooth', name='Set Shade Smooth', label=label)

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, shade_smooth)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetSplineCyclic for GeometryNodeSetSplineCyclic

class NodeSetSplineCyclic(Node):

    """Node 'Set Spline Cyclic' (GeometryNodeSetSplineCyclic)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        cyclic          : Boolean

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, selection=None, cyclic=None, label=None):

        super().__init__('GeometryNodeSetSplineCyclic', name='Set Spline Cyclic', label=label)

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, cyclic)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeSetSplineResolution for GeometryNodeSetSplineResolution

class NodeSetSplineResolution(Node):

    """Node 'Set Spline Resolution' (GeometryNodeSetSplineResolution)

    Input sockets
    -------------
        geometry        : Geometry
        selection       : Boolean
        resolution      : Integer

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, selection=None, resolution=None, label=None):

        super().__init__('GeometryNodeSetSplineResolution', name='Set Spline Resolution', label=label)

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, selection)
        self.plug(2, resolution)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeSplineLength for GeometryNodeSplineLength

class NodeSplineLength(Node):

    """Node 'Spline Length' (GeometryNodeSplineLength)

    Output sockets
    --------------
        length          : Float
        point_count     : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeSplineLength', name='Spline Length', label=label)

        # Output sockets

        self.length          = self.Float(self.bnode.outputs[0])
        self.point_count     = self.Integer(self.bnode.outputs[1])
        self.output_sockets  = [self.length, self.point_count]

# ----------------------------------------------------------------------------------------------------
# Node NodeSplineParameter for GeometryNodeSplineParameter

class NodeSplineParameter(Node):

    """Node 'Spline Parameter' (GeometryNodeSplineParameter)

    Output sockets
    --------------
        factor          : Float
        length          : Float
        index           : Integer
    """

    def __init__(self, label=None):

        super().__init__('GeometryNodeSplineParameter', name='Spline Parameter', label=label)

        # Output sockets

        self.factor          = self.Float(self.bnode.outputs[0])
        self.length          = self.Float(self.bnode.outputs[1])
        self.index           = self.Integer(self.bnode.outputs[2])
        self.output_sockets  = [self.factor, self.length, self.index]

# ----------------------------------------------------------------------------------------------------
# Node NodeSplitEdges for GeometryNodeSplitEdges

class NodeSplitEdges(Node):

    """Node 'Split Edges' (GeometryNodeSplitEdges)

    Input sockets
    -------------
        mesh            : Geometry
        selection       : Boolean

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, mesh=None, selection=None, label=None):

        super().__init__('GeometryNodeSplitEdges', name='Split Edges', label=label)

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeJoinStrings for GeometryNodeStringJoin

class NodeJoinStrings(Node):

    """Node 'Join Strings' (GeometryNodeStringJoin)

    Input sockets
    -------------
        delimiter       : String
        strings         : *String

    Output sockets
    --------------
        string          : String
    """

    def __init__(self, *strings, delimiter=None, label=None):

        super().__init__('GeometryNodeStringJoin', name='Join Strings', label=label)

        # Input sockets

        self.plug(1, *strings)
        self.plug(0, delimiter)

        # Output sockets

        self.string          = self.String(self.bnode.outputs[0])
        self.output_sockets  = [self.string]

# ----------------------------------------------------------------------------------------------------
# Node NodeStringToCurves for GeometryNodeStringToCurves

class NodeStringToCurves(Node):

    """Node 'String to Curves' (GeometryNodeStringToCurves)

    Input sockets
    -------------
        string          : String
        size            : Float
        character_spacing : Float
        word_spacing    : Float
        line_spacing    : Float
        text_box_width  : Float
        text_box_height : Float

    Parameters
    ----------
        align_x         : 'LEFT' in [ 'LEFT' 'CENTER' 'RIGHT' 'JUSTIFY' 'FLUSH']
        align_y         : 'TOP_BASELINE' in [ 'TOP_BASELINE' 'TOP' 'MIDDLE' 'BOTTOM_BASELINE' 'BOTTOM']
        overflow        : 'OVERFLOW' in [ 'OVERFLOW' 'SCALE_TO_FIT' 'TRUNCATE']
        pivot_mode      : 'BOTTOM_LEFT' in [ 'MIDPOINT' 'TOP_LEFT' 'TOP_CENTER' 'TOP_RIGHT' 'BOTTOM_LEFT' 'BOTTOM_CENTER' 'BOTTOM_RIGHT']

    Output sockets
    --------------
        curve_instances : Geometry
        remainder       : String
        line            : Integer
        pivot_point     : Vector
    """

    def __init__(self, string=None, size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', label=None):

        super().__init__('GeometryNodeStringToCurves', name='String to Curves', label=label)

        # Parameters

        self.bnode.align_x         = align_x
        self.bnode.align_y         = align_y
        self.bnode.overflow        = overflow
        self.bnode.pivot_mode      = pivot_mode

        # Input sockets

        self.plug(0, string)
        self.plug(1, size)
        self.plug(2, character_spacing)
        self.plug(3, word_spacing)
        self.plug(4, line_spacing)
        self.plug(5, text_box_width)
        self.plug(6, text_box_height)

        # Output sockets

        self.curve_instances = self.Geometry(self.bnode.outputs[0])
        self.remainder       = self.String(self.bnode.outputs[1])
        self.line            = self.Integer(self.bnode.outputs[2])
        self.pivot_point     = self.Vector(self.bnode.outputs[3])
        self.output_sockets  = [self.curve_instances, self.remainder, self.line, self.pivot_point]

# ----------------------------------------------------------------------------------------------------
# Node NodeSubdivideCurve for GeometryNodeSubdivideCurve

class NodeSubdivideCurve(Node):

    """Node 'Subdivide Curve' (GeometryNodeSubdivideCurve)

    Input sockets
    -------------
        curve           : Geometry
        cuts            : Integer

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, curve=None, cuts=None, label=None):

        super().__init__('GeometryNodeSubdivideCurve', name='Subdivide Curve', label=label)

        # Input sockets

        self.plug(0, curve)
        self.plug(1, cuts)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeSubdivideMesh for GeometryNodeSubdivideMesh

class NodeSubdivideMesh(Node):

    """Node 'Subdivide Mesh' (GeometryNodeSubdivideMesh)

    Input sockets
    -------------
        mesh            : Geometry
        level           : Integer

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, mesh=None, level=None, label=None):

        super().__init__('GeometryNodeSubdivideMesh', name='Subdivide Mesh', label=label)

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, level)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeSubdivisionSurface for GeometryNodeSubdivisionSurface

class NodeSubdivisionSurface(Node):

    """Node 'Subdivision Surface' (GeometryNodeSubdivisionSurface)

    Input sockets
    -------------
        mesh            : Geometry
        level           : Integer
        crease          : Float

    Parameters
    ----------
        boundary_smooth : 'ALL' in [ 'PRESERVE_CORNERS' 'ALL']
        uv_smooth       : 'PRESERVE_BOUNDARIES' in [ 'NONE' 'PRESERVE_CORNERS' 'PRESERVE_CORNERS_AND_JUNCTIONS' 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE',
                             'PRESERVE_BOUNDARIES' 'SMOOTH_ALL']

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, mesh=None, level=None, crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', label=None):

        super().__init__('GeometryNodeSubdivisionSurface', name='Subdivision Surface', label=label)

        # Parameters

        self.bnode.boundary_smooth = boundary_smooth
        self.bnode.uv_smooth       = uv_smooth

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, level)
        self.plug(2, crease)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeSwitch for GeometryNodeSwitch

class NodeSwitch(Node):

    """Node 'Switch' (GeometryNodeSwitch)

    Data type dependant sockets
    ---------------------------

        Driving parameter : input_type in ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')

        Input sockets     : ['false', 'true']
        Output sockets    : ['output']

    Input sockets
    -------------
        switch0         : Boolean
        switch1         : Boolean
        false           : input_type dependant
        true            : input_type dependant

    Parameters
    ----------
        input_type      : 'GEOMETRY' in [ 'FLOAT' 'INT' 'BOOLEAN' 'VECTOR' 'STRING' 'RGBA' 'OBJECT' 'IMAGE' 'GEOMETRY' 'COLLECTION' 'TEXTURE',
                             'MATERIAL']

    Output sockets
    --------------
        output          : input_type dependant
    """

    def __init__(self, switch0=None, switch1=None, false=None, true=None, input_type='GEOMETRY', label=None):

        super().__init__('GeometryNodeSwitch', name='Switch', label=label)

        # Parameters

        self.bnode.input_type      = input_type

        # Input sockets

        if input_type == 'FLOAT':
            self.plug(2, false)
            self.plug(3, true)
        elif input_type == 'INT':
            self.plug(4, false)
            self.plug(5, true)
        elif input_type == 'BOOLEAN':
            self.plug(6, false)
            self.plug(7, true)
        elif input_type == 'VECTOR':
            self.plug(8, false)
            self.plug(9, true)
        elif input_type == 'STRING':
            self.plug(12, false)
            self.plug(13, true)
        elif input_type == 'RGBA':
            self.plug(10, false)
            self.plug(11, true)
        elif input_type == 'OBJECT':
            self.plug(16, false)
            self.plug(17, true)
        elif input_type == 'IMAGE':
            self.plug(24, false)
            self.plug(25, true)
        elif input_type == 'GEOMETRY':
            self.plug(14, false)
            self.plug(15, true)
        elif input_type == 'COLLECTION':
            self.plug(18, false)
            self.plug(19, true)
        elif input_type == 'TEXTURE':
            self.plug(20, false)
            self.plug(21, true)
        elif input_type == 'MATERIAL':
            self.plug(22, false)
            self.plug(23, true)

        self.plug(0, switch0)
        self.plug(1, switch1)

        # Output sockets

        if input_type == 'FLOAT':
            self.output          = self.Float(self.bnode.outputs[0])
        elif input_type == 'INT':
            self.output          = self.Integer(self.bnode.outputs[1])
        elif input_type == 'BOOLEAN':
            self.output          = self.Boolean(self.bnode.outputs[2])
        elif input_type == 'VECTOR':
            self.output          = self.Vector(self.bnode.outputs[3])
        elif input_type == 'STRING':
            self.output          = self.String(self.bnode.outputs[5])
        elif input_type == 'RGBA':
            self.output          = self.Color(self.bnode.outputs[4])
        elif input_type == 'OBJECT':
            self.output          = self.Object(self.bnode.outputs[7])
        elif input_type == 'IMAGE':
            self.output          = self.Image(self.bnode.outputs[11])
        elif input_type == 'GEOMETRY':
            self.output          = self.Geometry(self.bnode.outputs[6])
        elif input_type == 'COLLECTION':
            self.output          = self.Collection(self.bnode.outputs[8])
        elif input_type == 'TEXTURE':
            self.output          = self.Texture(self.bnode.outputs[9])
        elif input_type == 'MATERIAL':
            self.output          = self.Material(self.bnode.outputs[10])

        self.output_sockets  = []

# ----------------------------------------------------------------------------------------------------
# Node NodeTransform for GeometryNodeTransform

class NodeTransform(Node):

    """Node 'Transform' (GeometryNodeTransform)

    Input sockets
    -------------
        geometry        : Geometry
        translation     : Vector
        rotation        : Vector
        scale           : Vector

    Output sockets
    --------------
        geometry        : Geometry
    """

    def __init__(self, geometry=None, translation=None, rotation=None, scale=None, label=None):

        super().__init__('GeometryNodeTransform', name='Transform', label=label)

        # Input sockets

        self.plug(0, geometry)
        self.plug(1, translation)
        self.plug(2, rotation)
        self.plug(3, scale)

        # Output sockets

        self.geometry        = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.geometry]

# ----------------------------------------------------------------------------------------------------
# Node NodeTranslateInstances for GeometryNodeTranslateInstances

class NodeTranslateInstances(Node):

    """Node 'Translate Instances' (GeometryNodeTranslateInstances)

    Input sockets
    -------------
        instances       : Geometry
        selection       : Boolean
        translation     : Vector
        local_space     : Boolean

    Output sockets
    --------------
        instances       : Geometry
    """

    def __init__(self, instances=None, selection=None, translation=None, local_space=None, label=None):

        super().__init__('GeometryNodeTranslateInstances', name='Translate Instances', label=label)

        # Input sockets

        self.plug(0, instances)
        self.plug(1, selection)
        self.plug(2, translation)
        self.plug(3, local_space)

        # Output sockets

        self.instances       = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.instances]

# ----------------------------------------------------------------------------------------------------
# Node NodeTriangulate for GeometryNodeTriangulate

class NodeTriangulate(Node):

    """Node 'Triangulate' (GeometryNodeTriangulate)

    Input sockets
    -------------
        mesh            : Geometry
        selection       : Boolean
        minimum_vertices : Integer

    Parameters
    ----------
        ngon_method     : 'BEAUTY' in [ 'BEAUTY' 'CLIP']
        quad_method     : 'SHORTEST_DIAGONAL' in [ 'BEAUTY' 'FIXED' 'FIXED_ALTERNATE' 'SHORTEST_DIAGONAL' 'LONGEST_DIAGONAL']

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, mesh=None, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', label=None):

        super().__init__('GeometryNodeTriangulate', name='Triangulate', label=label)

        # Parameters

        self.bnode.ngon_method     = ngon_method
        self.bnode.quad_method     = quad_method

        # Input sockets

        self.plug(0, mesh)
        self.plug(1, selection)
        self.plug(2, minimum_vertices)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeTrimCurve for GeometryNodeTrimCurve

class NodeTrimCurve(Node):

    """Node 'Trim Curve' (GeometryNodeTrimCurve)

    Input sockets
    -------------
        curve           : Geometry
        start0          : Float
        start1          : Float
        end0            : Float
        end1            : Float

    Parameters
    ----------
        mode            : 'FACTOR' in [ 'FACTOR' 'LENGTH']

    Output sockets
    --------------
        curve           : Geometry
    """

    def __init__(self, curve=None, start0=None, start1=None, end0=None, end1=None, mode='FACTOR', label=None):

        super().__init__('GeometryNodeTrimCurve', name='Trim Curve', label=label)

        # Parameters

        self.bnode.mode            = mode

        # Input sockets

        self.plug(0, curve)
        self.plug(1, start0)
        self.plug(3, start1)
        self.plug(2, end0)
        self.plug(4, end1)

        # Output sockets

        self.curve           = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.curve]

# ----------------------------------------------------------------------------------------------------
# Node NodeViewer for GeometryNodeViewer

class NodeViewer(Node):

    """Node 'Viewer' (GeometryNodeViewer)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')

        Input sockets     : ['value']

    Input sockets
    -------------
        geometry        : Geometry
        value           : data_type dependant

    Parameters
    ----------
        data_type       : 'FLOAT' in [ 'FLOAT' 'INT' 'FLOAT_VECTOR' 'FLOAT_COLOR' 'BOOLEAN']

    """

    def __init__(self, geometry=None, value=None, data_type='FLOAT', label=None):

        super().__init__('GeometryNodeViewer', name='Viewer', label=label)

        # Parameters

        self.bnode.data_type       = data_type

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(1, value)
        elif data_type == 'INT':
            self.plug(4, value)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(2, value)
        elif data_type == 'FLOAT_COLOR':
            self.plug(3, value)
        elif data_type == 'BOOLEAN':
            self.plug(5, value)

        self.plug(0, geometry)


        self.output_sockets  = []

# ----------------------------------------------------------------------------------------------------
# Node NodeVolumeToMesh for GeometryNodeVolumeToMesh

class NodeVolumeToMesh(Node):

    """Node 'Volume to Mesh' (GeometryNodeVolumeToMesh)

    Input sockets
    -------------
        volume          : Geometry
        voxel_size      : Float
        voxel_amount    : Float
        threshold       : Float
        adaptivity      : Float

    Parameters
    ----------
        resolution_mode : 'GRID' in [ 'GRID' 'VOXEL_AMOUNT' 'VOXEL_SIZE']

    Output sockets
    --------------
        mesh            : Geometry
    """

    def __init__(self, volume=None, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID', label=None):

        super().__init__('GeometryNodeVolumeToMesh', name='Volume to Mesh', label=label)

        # Parameters

        self.bnode.resolution_mode = resolution_mode

        # Input sockets

        self.plug(0, volume)
        self.plug(1, voxel_size)
        self.plug(2, voxel_amount)
        self.plug(3, threshold)
        self.plug(4, adaptivity)

        # Output sockets

        self.mesh            = self.Geometry(self.bnode.outputs[0])
        self.output_sockets  = [self.mesh]

# ----------------------------------------------------------------------------------------------------
# Node NodeClamp for ShaderNodeClamp

class NodeClamp(Node):

    """Node 'Clamp' (ShaderNodeClamp)

    Input sockets
    -------------
        value           : Float
        min             : Float
        max             : Float

    Parameters
    ----------
        clamp_type      : 'MINMAX' in [ 'MINMAX' 'RANGE']

    Output sockets
    --------------
        result          : Float
    """

    def __init__(self, value=None, min=None, max=None, clamp_type='MINMAX', label=None):

        super().__init__('ShaderNodeClamp', name='Clamp', label=label)

        # Parameters

        self.bnode.clamp_type      = clamp_type

        # Input sockets

        self.plug(0, value)
        self.plug(1, min)
        self.plug(2, max)

        # Output sockets

        self.result          = self.Float(self.bnode.outputs[0])
        self.output_sockets  = [self.result]

# ----------------------------------------------------------------------------------------------------
# Node NodeCombineRgb for ShaderNodeCombineRGB

class NodeCombineRgb(Node):

    """Node 'Combine RGB' (ShaderNodeCombineRGB)

    Input sockets
    -------------
        r               : Float
        g               : Float
        b               : Float

    Output sockets
    --------------
        image           : Color
    """

    def __init__(self, r=None, g=None, b=None, label=None):

        super().__init__('ShaderNodeCombineRGB', name='Combine RGB', label=label)

        # Input sockets

        self.plug(0, r)
        self.plug(1, g)
        self.plug(2, b)

        # Output sockets

        self.image           = self.Color(self.bnode.outputs[0])
        self.output_sockets  = [self.image]

# ----------------------------------------------------------------------------------------------------
# Node NodeCombineXyz for ShaderNodeCombineXYZ

class NodeCombineXyz(Node):

    """Node 'Combine XYZ' (ShaderNodeCombineXYZ)

    Input sockets
    -------------
        x               : Float
        y               : Float
        z               : Float

    Output sockets
    --------------
        vector          : Vector
    """

    def __init__(self, x=None, y=None, z=None, label=None):

        super().__init__('ShaderNodeCombineXYZ', name='Combine XYZ', label=label)

        # Input sockets

        self.plug(0, x)
        self.plug(1, y)
        self.plug(2, z)

        # Output sockets

        self.vector          = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = [self.vector]

# ----------------------------------------------------------------------------------------------------
# Node NodeFloatCurve for ShaderNodeFloatCurve

class NodeFloatCurve(Node):

    """Node 'Float Curve' (ShaderNodeFloatCurve)

    Input sockets
    -------------
        factor          : Float
        value           : Float

    Output sockets
    --------------
        value           : Float
    """

    def __init__(self, factor=None, value=None, label=None):

        super().__init__('ShaderNodeFloatCurve', name='Float Curve', label=label)

        # Input sockets

        self.plug(0, factor)
        self.plug(1, value)

        # Output sockets

        self.value           = self.Float(self.bnode.outputs[0])
        self.output_sockets  = [self.value]

# ----------------------------------------------------------------------------------------------------
# Node NodeMapRange for ShaderNodeMapRange

class NodeMapRange(Node):

    """Node 'Map Range' (ShaderNodeMapRange)

    Data type dependant sockets
    ---------------------------

        Driving parameter : data_type in ('FLOAT', 'FLOAT_VECTOR')

        Input sockets     : ['from_min', 'from_max', 'to_min', 'to_max', 'steps']

    Input sockets
    -------------
        value           : Float
        from_min        : data_type dependant
        from_max        : data_type dependant
        to_min          : data_type dependant
        to_max          : data_type dependant
        steps           : data_type dependant
        vector          : Vector

    Parameters
    ----------
        clamp           : (True) bool
        data_type       : 'FLOAT' in [ 'FLOAT' 'FLOAT_VECTOR']
        interpolation_type : 'LINEAR' in [ 'LINEAR' 'STEPPED' 'SMOOTHSTEP' 'SMOOTHERSTEP']

    Output sockets
    --------------
        result          : Float
        vector          : Vector
    """

    def __init__(self, value=None, from_min=None, from_max=None, to_min=None, to_max=None, steps=None, vector=None, clamp=True, data_type='FLOAT', interpolation_type='LINEAR', label=None):

        super().__init__('ShaderNodeMapRange', name='Map Range', label=label)

        # Parameters

        self.bnode.clamp           = clamp
        self.bnode.data_type       = data_type
        self.bnode.interpolation_type = interpolation_type

        # Input sockets

        if data_type == 'FLOAT':
            self.plug(1, from_min)
            self.plug(2, from_max)
            self.plug(3, to_min)
            self.plug(4, to_max)
        elif data_type == 'FLOAT_VECTOR':
            self.plug(7, from_min)
            self.plug(8, from_max)
            self.plug(9, to_min)
            self.plug(10, to_max)

        self.plug(0, value)
        self.plug(6, vector)


        # Output sockets

        self.result          = self.Float(self.bnode.outputs[0])
        self.vector          = self.Vector(self.bnode.outputs[1])
        self.output_sockets  = [self.result, self.vector]

# ----------------------------------------------------------------------------------------------------
# Node NodeMath for ShaderNodeMath

class NodeMath(Node):

    """Node 'Math' (ShaderNodeMath)

    Input sockets
    -------------
        value0          : Float
        value1          : Float
        value2          : Float

    Parameters
    ----------
        operation       : 'ADD' in [ 'ADD' 'SUBTRACT' 'MULTIPLY' 'DIVIDE' 'MULTIPLY_ADD' 'POWER' 'LOGARITHM' 'SQRT' 'INVERSE_SQRT' 'ABSOLUTE',
                             'EXPONENT' 'MINIMUM' 'MAXIMUM' 'LESS_THAN' 'GREATER_THAN' 'SIGN' 'COMPARE' 'SMOOTH_MIN' 'SMOOTH_MAX',
                             'ROUND' 'FLOOR' 'CEIL' 'TRUNC' 'FRACT' 'MODULO' 'WRAP' 'SNAP' 'PINGPONG' 'SINE' 'COSINE' 'TANGENT' 'ARCSINE',
                             'ARCCOSINE' 'ARCTANGENT' 'ARCTAN2' 'SINH' 'COSH' 'TANH' 'RADIANS' 'DEGREES']

    Output sockets
    --------------
        value           : Float
    """

    def __init__(self, value0=None, value1=None, value2=None, operation='ADD', label=None):

        super().__init__('ShaderNodeMath', name='Math', label=label)

        # Parameters

        self.bnode.operation       = operation

        # Input sockets

        self.plug(0, value0)
        self.plug(1, value1)
        self.plug(2, value2)

        # Output sockets

        self.value           = self.Float(self.bnode.outputs[0])
        self.output_sockets  = [self.value]

# ----------------------------------------------------------------------------------------------------
# Node NodeMix for ShaderNodeMixRGB

class NodeMix(Node):

    """Node 'Mix' (ShaderNodeMixRGB)

    Input sockets
    -------------
        fac             : Float
        color1          : Color
        color2          : Color

    Parameters
    ----------
        blend_type      : 'MIX' in [ 'MIX' 'DARKEN' 'MULTIPLY' 'BURN' 'LIGHTEN' 'SCREEN' 'DODGE' 'ADD' 'OVERLAY' 'SOFT_LIGHT' 'LINEAR_LIGHT',
                             'DIFFERENCE' 'SUBTRACT' 'DIVIDE' 'HUE' 'SATURATION' 'COLOR' 'VALUE']
        use_alpha       : (False) bool

    Output sockets
    --------------
        color           : Color
    """

    def __init__(self, fac=None, color1=None, color2=None, blend_type='MIX', use_alpha=False, label=None):

        super().__init__('ShaderNodeMixRGB', name='Mix', label=label)

        # Parameters

        self.bnode.blend_type      = blend_type
        self.bnode.use_alpha       = use_alpha

        # Input sockets

        self.plug(0, fac)
        self.plug(1, color1)
        self.plug(2, color2)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.output_sockets  = [self.color]

# ----------------------------------------------------------------------------------------------------
# Node NodeRgbCurves for ShaderNodeRGBCurve

class NodeRgbCurves(Node):

    """Node 'RGB Curves' (ShaderNodeRGBCurve)

    Input sockets
    -------------
        fac             : Float
        color           : Color

    Output sockets
    --------------
        color           : Color
    """

    def __init__(self, fac=None, color=None, label=None):

        super().__init__('ShaderNodeRGBCurve', name='RGB Curves', label=label)

        # Input sockets

        self.plug(0, fac)
        self.plug(1, color)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.output_sockets  = [self.color]

# ----------------------------------------------------------------------------------------------------
# Node NodeSeparateRgb for ShaderNodeSeparateRGB

class NodeSeparateRgb(Node):

    """Node 'Separate RGB' (ShaderNodeSeparateRGB)

    Input sockets
    -------------
        image           : Color

    Output sockets
    --------------
        r               : Float
        g               : Float
        b               : Float
    """

    def __init__(self, image=None, label=None):

        super().__init__('ShaderNodeSeparateRGB', name='Separate RGB', label=label)

        # Input sockets

        self.plug(0, image)

        # Output sockets

        self.r               = self.Float(self.bnode.outputs[0])
        self.g               = self.Float(self.bnode.outputs[1])
        self.b               = self.Float(self.bnode.outputs[2])
        self.output_sockets  = [self.r, self.g, self.b]

# ----------------------------------------------------------------------------------------------------
# Node NodeSeparateXyz for ShaderNodeSeparateXYZ

class NodeSeparateXyz(Node):

    """Node 'Separate XYZ' (ShaderNodeSeparateXYZ)

    Input sockets
    -------------
        vector          : Vector

    Output sockets
    --------------
        x               : Float
        y               : Float
        z               : Float
    """

    def __init__(self, vector=None, label=None):

        super().__init__('ShaderNodeSeparateXYZ', name='Separate XYZ', label=label)

        # Input sockets

        self.plug(0, vector)

        # Output sockets

        self.x               = self.Float(self.bnode.outputs[0])
        self.y               = self.Float(self.bnode.outputs[1])
        self.z               = self.Float(self.bnode.outputs[2])
        self.output_sockets  = [self.x, self.y, self.z]

# ----------------------------------------------------------------------------------------------------
# Node NodeBrickTexture for ShaderNodeTexBrick

class NodeBrickTexture(Node):

    """Node 'Brick Texture' (ShaderNodeTexBrick)

    Input sockets
    -------------
        vector          : Vector
        color1          : Color
        color2          : Color
        mortar          : Color
        scale           : Float
        mortar_size     : Float
        mortar_smooth   : Float
        bias            : Float
        brick_width     : Float
        row_height      : Float

    Parameters
    ----------
        offset          : (0.5) float
        offset_frequency : (2) int
        squash          : (1.0) float
        squash_frequency : (2) int

    Output sockets
    --------------
        color           : Color
        fac             : Float
    """

    def __init__(self, vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, label=None):

        super().__init__('ShaderNodeTexBrick', name='Brick Texture', label=label)

        # Parameters

        self.bnode.offset          = offset
        self.bnode.offset_frequency = offset_frequency
        self.bnode.squash          = squash
        self.bnode.squash_frequency = squash_frequency

        # Input sockets

        self.plug(0, vector)
        self.plug(1, color1)
        self.plug(2, color2)
        self.plug(3, mortar)
        self.plug(4, scale)
        self.plug(5, mortar_size)
        self.plug(6, mortar_smooth)
        self.plug(7, bias)
        self.plug(8, brick_width)
        self.plug(9, row_height)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.fac             = self.Float(self.bnode.outputs[1])
        self.output_sockets  = [self.color, self.fac]

# ----------------------------------------------------------------------------------------------------
# Node NodeCheckerTexture for ShaderNodeTexChecker

class NodeCheckerTexture(Node):

    """Node 'Checker Texture' (ShaderNodeTexChecker)

    Input sockets
    -------------
        vector          : Vector
        color1          : Color
        color2          : Color
        scale           : Float

    Output sockets
    --------------
        color           : Color
        fac             : Float
    """

    def __init__(self, vector=None, color1=None, color2=None, scale=None, label=None):

        super().__init__('ShaderNodeTexChecker', name='Checker Texture', label=label)

        # Input sockets

        self.plug(0, vector)
        self.plug(1, color1)
        self.plug(2, color2)
        self.plug(3, scale)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.fac             = self.Float(self.bnode.outputs[1])
        self.output_sockets  = [self.color, self.fac]

# ----------------------------------------------------------------------------------------------------
# Node NodeGradientTexture for ShaderNodeTexGradient

class NodeGradientTexture(Node):

    """Node 'Gradient Texture' (ShaderNodeTexGradient)

    Input sockets
    -------------
        vector          : Vector

    Parameters
    ----------
        gradient_type   : 'LINEAR' in [ 'LINEAR' 'QUADRATIC' 'EASING' 'DIAGONAL' 'SPHERICAL' 'QUADRATIC_SPHERE' 'RADIAL']

    Output sockets
    --------------
        color           : Color
        fac             : Float
    """

    def __init__(self, vector=None, gradient_type='LINEAR', label=None):

        super().__init__('ShaderNodeTexGradient', name='Gradient Texture', label=label)

        # Parameters

        self.bnode.gradient_type   = gradient_type

        # Input sockets

        self.plug(0, vector)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.fac             = self.Float(self.bnode.outputs[1])
        self.output_sockets  = [self.color, self.fac]

# ----------------------------------------------------------------------------------------------------
# Node NodeMagicTexture for ShaderNodeTexMagic

class NodeMagicTexture(Node):

    """Node 'Magic Texture' (ShaderNodeTexMagic)

    Input sockets
    -------------
        vector          : Vector
        scale           : Float
        distortion      : Float

    Parameters
    ----------
        turbulence_depth : (2) int

    Output sockets
    --------------
        color           : Color
        fac             : Float
    """

    def __init__(self, vector=None, scale=None, distortion=None, turbulence_depth=2, label=None):

        super().__init__('ShaderNodeTexMagic', name='Magic Texture', label=label)

        # Parameters

        self.bnode.turbulence_depth = turbulence_depth

        # Input sockets

        self.plug(0, vector)
        self.plug(1, scale)
        self.plug(2, distortion)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.fac             = self.Float(self.bnode.outputs[1])
        self.output_sockets  = [self.color, self.fac]

# ----------------------------------------------------------------------------------------------------
# Node NodeMusgraveTexture for ShaderNodeTexMusgrave

class NodeMusgraveTexture(Node):

    """Node 'Musgrave Texture' (ShaderNodeTexMusgrave)

    Input sockets
    -------------
        vector          : Vector
        w               : Float
        scale           : Float
        detail          : Float
        dimension       : Float
        lacunarity      : Float
        offset          : Float
        gain            : Float

    Parameters
    ----------
        musgrave_dimensions : '3D' in [ '1D' '2D' '3D' '4D']
        musgrave_type   : 'FBM' in [ 'MULTIFRACTAL' 'RIDGED_MULTIFRACTAL' 'HYBRID_MULTIFRACTAL' 'FBM' 'HETERO_TERRAIN']

    Output sockets
    --------------
        fac             : Float
    """

    def __init__(self, vector=None, w=None, scale=None, detail=None, dimension=None, lacunarity=None, offset=None, gain=None, musgrave_dimensions='3D', musgrave_type='FBM', label=None):

        super().__init__('ShaderNodeTexMusgrave', name='Musgrave Texture', label=label)

        # Parameters

        self.bnode.musgrave_dimensions = musgrave_dimensions
        self.bnode.musgrave_type   = musgrave_type

        # Input sockets

        self.plug(0, vector)
        self.plug(1, w)
        self.plug(2, scale)
        self.plug(3, detail)
        self.plug(4, dimension)
        self.plug(5, lacunarity)
        self.plug(6, offset)
        self.plug(7, gain)

        # Output sockets

        self.fac             = self.Float(self.bnode.outputs[0])
        self.output_sockets  = [self.fac]

# ----------------------------------------------------------------------------------------------------
# Node NodeNoiseTexture for ShaderNodeTexNoise

class NodeNoiseTexture(Node):

    """Node 'Noise Texture' (ShaderNodeTexNoise)

    Input sockets
    -------------
        vector          : Vector
        w               : Float
        scale           : Float
        detail          : Float
        roughness       : Float
        distortion      : Float

    Parameters
    ----------
        noise_dimensions : '3D' in [ '1D' '2D' '3D' '4D']

    Output sockets
    --------------
        fac             : Float
        color           : Color
    """

    def __init__(self, vector=None, w=None, scale=None, detail=None, roughness=None, distortion=None, noise_dimensions='3D', label=None):

        super().__init__('ShaderNodeTexNoise', name='Noise Texture', label=label)

        # Parameters

        self.bnode.noise_dimensions = noise_dimensions

        # Input sockets

        self.plug(0, vector)
        self.plug(1, w)
        self.plug(2, scale)
        self.plug(3, detail)
        self.plug(4, roughness)
        self.plug(5, distortion)

        # Output sockets

        self.fac             = self.Float(self.bnode.outputs[0])
        self.color           = self.Color(self.bnode.outputs[1])
        self.output_sockets  = [self.fac, self.color]

# ----------------------------------------------------------------------------------------------------
# Node NodeVoronoiTexture for ShaderNodeTexVoronoi

class NodeVoronoiTexture(Node):

    """Node 'Voronoi Texture' (ShaderNodeTexVoronoi)

    Input sockets
    -------------
        vector          : Vector
        w               : Float
        scale           : Float
        smoothness      : Float
        exponent        : Float
        randomness      : Float

    Parameters
    ----------
        distance        : 'EUCLIDEAN' in [ 'EUCLIDEAN' 'MANHATTAN' 'CHEBYCHEV' 'MINKOWSKI']
        feature         : 'F1' in [ 'F1' 'F2' 'SMOOTH_F1' 'DISTANCE_TO_EDGE' 'N_SPHERE_RADIUS']
        voronoi_dimensions : '3D' in [ '1D' '2D' '3D' '4D']

    Output sockets
    --------------
        distance        : Float
        color           : Color
        position        : Vector
        w               : Float
        radius          : Float
    """

    def __init__(self, vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D', label=None):

        super().__init__('ShaderNodeTexVoronoi', name='Voronoi Texture', label=label)

        # Parameters

        self.bnode.distance        = distance
        self.bnode.feature         = feature
        self.bnode.voronoi_dimensions = voronoi_dimensions

        # Input sockets

        self.plug(0, vector)
        self.plug(1, w)
        self.plug(2, scale)
        self.plug(3, smoothness)
        self.plug(4, exponent)
        self.plug(5, randomness)

        # Output sockets

        self.distance        = self.Float(self.bnode.outputs[0])
        self.color           = self.Color(self.bnode.outputs[1])
        self.position        = self.Vector(self.bnode.outputs[2])
        self.w               = self.Float(self.bnode.outputs[3])
        self.radius          = self.Float(self.bnode.outputs[4])
        self.output_sockets  = [self.distance, self.color, self.position, self.w, self.radius]

# ----------------------------------------------------------------------------------------------------
# Node NodeWaveTexture for ShaderNodeTexWave

class NodeWaveTexture(Node):

    """Node 'Wave Texture' (ShaderNodeTexWave)

    Input sockets
    -------------
        vector          : Vector
        scale           : Float
        distortion      : Float
        detail          : Float
        detail_scale    : Float
        detail_roughness : Float
        phase_offset    : Float

    Parameters
    ----------
        bands_direction : 'X' in [ 'X' 'Y' 'Z' 'DIAGONAL']
        rings_direction : 'X' in [ 'X' 'Y' 'Z' 'SPHERICAL']
        wave_profile    : 'SIN' in [ 'SIN' 'SAW' 'TRI']
        wave_type       : 'BANDS' in [ 'BANDS' 'RINGS']

    Output sockets
    --------------
        color           : Color
        fac             : Float
    """

    def __init__(self, vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS', label=None):

        super().__init__('ShaderNodeTexWave', name='Wave Texture', label=label)

        # Parameters

        self.bnode.bands_direction = bands_direction
        self.bnode.rings_direction = rings_direction
        self.bnode.wave_profile    = wave_profile
        self.bnode.wave_type       = wave_type

        # Input sockets

        self.plug(0, vector)
        self.plug(1, scale)
        self.plug(2, distortion)
        self.plug(3, detail)
        self.plug(4, detail_scale)
        self.plug(5, detail_roughness)
        self.plug(6, phase_offset)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.fac             = self.Float(self.bnode.outputs[1])
        self.output_sockets  = [self.color, self.fac]

# ----------------------------------------------------------------------------------------------------
# Node NodeWhiteNoiseTexture for ShaderNodeTexWhiteNoise

class NodeWhiteNoiseTexture(Node):

    """Node 'White Noise Texture' (ShaderNodeTexWhiteNoise)

    Input sockets
    -------------
        vector          : Vector
        w               : Float

    Parameters
    ----------
        noise_dimensions : '3D' in [ '1D' '2D' '3D' '4D']

    Output sockets
    --------------
        value           : Float
        color           : Color
    """

    def __init__(self, vector=None, w=None, noise_dimensions='3D', label=None):

        super().__init__('ShaderNodeTexWhiteNoise', name='White Noise Texture', label=label)

        # Parameters

        self.bnode.noise_dimensions = noise_dimensions

        # Input sockets

        self.plug(0, vector)
        self.plug(1, w)

        # Output sockets

        self.value           = self.Float(self.bnode.outputs[0])
        self.color           = self.Color(self.bnode.outputs[1])
        self.output_sockets  = [self.value, self.color]

# ----------------------------------------------------------------------------------------------------
# Node NodeColorramp for ShaderNodeValToRGB

class NodeColorramp(Node):

    """Node 'ColorRamp' (ShaderNodeValToRGB)

    Input sockets
    -------------
        fac             : Float

    Output sockets
    --------------
        color           : Color
        alpha           : Float
    """

    def __init__(self, fac=None, label=None):

        super().__init__('ShaderNodeValToRGB', name='ColorRamp', label=label)

        # Input sockets

        self.plug(0, fac)

        # Output sockets

        self.color           = self.Color(self.bnode.outputs[0])
        self.alpha           = self.Float(self.bnode.outputs[1])
        self.output_sockets  = [self.color, self.alpha]

# ----------------------------------------------------------------------------------------------------
# Node NodeValue for ShaderNodeValue

class NodeValue(Node):

    """Node 'Value' (ShaderNodeValue)

    Output sockets
    --------------
        value           : Float
    """

    def __init__(self, label=None):

        super().__init__('ShaderNodeValue', name='Value', label=label)

        # Output sockets

        self.value           = self.Float(self.bnode.outputs[0])
        self.output_sockets  = [self.value]

# ----------------------------------------------------------------------------------------------------
# Node NodeVectorCurves for ShaderNodeVectorCurve

class NodeVectorCurves(Node):

    """Node 'Vector Curves' (ShaderNodeVectorCurve)

    Input sockets
    -------------
        fac             : Float
        vector          : Vector

    Output sockets
    --------------
        vector          : Vector
    """

    def __init__(self, fac=None, vector=None, label=None):

        super().__init__('ShaderNodeVectorCurve', name='Vector Curves', label=label)

        # Input sockets

        self.plug(0, fac)
        self.plug(1, vector)

        # Output sockets

        self.vector          = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = [self.vector]

# ----------------------------------------------------------------------------------------------------
# Node NodeVectorMath for ShaderNodeVectorMath

class NodeVectorMath(Node):

    """Node 'Vector Math' (ShaderNodeVectorMath)

    Input sockets
    -------------
        vector0         : Vector
        vector1         : Vector
        vector2         : Vector
        scale           : Float

    Parameters
    ----------
        operation       : 'ADD' in [ 'ADD' 'SUBTRACT' 'MULTIPLY' 'DIVIDE' 'MULTIPLY_ADD' 'CROSS_PRODUCT' 'PROJECT' 'REFLECT' 'REFRACT' 'FACEFORWARD',
                             'DOT_PRODUCT' 'DISTANCE' 'LENGTH' 'SCALE' 'NORMALIZE' 'ABSOLUTE' 'MINIMUM' 'MAXIMUM' 'FLOOR' 'CEIL',
                             'FRACTION' 'MODULO' 'WRAP' 'SNAP' 'SINE' 'COSINE' 'TANGENT']

    Output sockets
    --------------
        vector          : Vector
        value           : Float
    """

    def __init__(self, vector0=None, vector1=None, vector2=None, scale=None, operation='ADD', label=None):

        super().__init__('ShaderNodeVectorMath', name='Vector Math', label=label)

        # Parameters

        self.bnode.operation       = operation

        # Input sockets

        self.plug(0, vector0)
        self.plug(1, vector1)
        self.plug(2, vector2)
        self.plug(3, scale)

        # Output sockets

        self.vector          = self.Vector(self.bnode.outputs[0])
        self.value           = self.Float(self.bnode.outputs[1])
        self.output_sockets  = [self.vector, self.value]

# ----------------------------------------------------------------------------------------------------
# Node NodeVectorRotate for ShaderNodeVectorRotate

class NodeVectorRotate(Node):

    """Node 'Vector Rotate' (ShaderNodeVectorRotate)

    Input sockets
    -------------
        vector          : Vector
        center          : Vector
        axis            : Vector
        angle           : Float
        rotation        : Vector

    Parameters
    ----------
        invert          : (False) bool
        rotation_type   : 'AXIS_ANGLE' in [ 'AXIS_ANGLE' 'X_AXIS' 'Y_AXIS' 'Z_AXIS' 'EULER_XYZ']

    Output sockets
    --------------
        vector          : Vector
    """

    def __init__(self, vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE', label=None):

        super().__init__('ShaderNodeVectorRotate', name='Vector Rotate', label=label)

        # Parameters

        self.bnode.invert          = invert
        self.bnode.rotation_type   = rotation_type

        # Input sockets

        self.plug(0, vector)
        self.plug(1, center)
        self.plug(2, axis)
        self.plug(3, angle)
        self.plug(4, rotation)

        # Output sockets

        self.vector          = self.Vector(self.bnode.outputs[0])
        self.output_sockets  = [self.vector]
