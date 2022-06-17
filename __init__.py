version = "1.0"name = f"geonodes version {version}"pi = 3.141592653589793import geonodes.core as coreimport geonodes.core.colors as colorsfrom geonodes.core.node import DataSocket, Tree, Node, Groupfrom geonodes.core.domains import PointDomain, EdgeDomain, FaceDomain, CornerDomain, CurveDomain, InstanceDomainfrom geonodes.nodes import nodesfrom geonodes.sockets.boolean    import Booleanfrom geonodes.sockets.integer    import Integerfrom geonodes.sockets.float      import Floatfrom geonodes.sockets.vector     import Vectorfrom geonodes.sockets.color      import Colorfrom geonodes.sockets.string     import Stringfrom geonodes.sockets.geometry   import Geometryfrom geonodes.sockets.spline     import Splinefrom geonodes.sockets.curve      import Curvefrom geonodes.sockets.mesh       import Meshfrom geonodes.sockets.points     import Pointsfrom geonodes.sockets.instances  import Instancesfrom geonodes.sockets.volume     import Volumefrom geonodes.sockets.material   import Materialfrom geonodes.sockets.image      import Imagefrom geonodes.sockets.texture    import Texturefrom geonodes.sockets.collection import Collectionfrom geonodes.sockets.object     import Objectfrom geonodes.sockets.functions import abs, add, arccos, arcsin, arctan, arctan2, b_and, b_not, b_or, ceilfrom geonodes.sockets.functions import color_add, color_burn, color_darken, color_difference, color_dividefrom geonodes.sockets.functions import color_dodge, color_hue, color_lighten, color_linear_light, color_mixfrom geonodes.sockets.functions import color_mix_color, color_multiply, color_overlay, color_saturationfrom geonodes.sockets.functions import color_screen, color_soft_light, color_subtract, color_value, comparefrom geonodes.sockets.functions import compare, cos, cosh, cross, degrees, distance, divide, dot, expfrom geonodes.sockets.functions import faceforward, floor, fract, fraction, greater_than, imply, inverse_sqrtfrom geonodes.sockets.functions import join_strings, length, less_than, log, max, min, modulo, multiplyfrom geonodes.sockets.functions import multiply_add, nand, nimply, nor, normalize, pingpong, pow, projectfrom geonodes.sockets.functions import radians, reflect, refract, round, scale, scene, sign, sin, sinhfrom geonodes.sockets.functions import smooth_max, smooth_min, snap, sqrt, subtract, switch, tan, tanhfrom geonodes.sockets.functions import trunc, vector_absolute, vector_add, vector_ceil, vector_cos, vector_dividefrom geonodes.sockets.functions import vector_floor, vector_max, vector_min, vector_modulo, vector_multiplyfrom geonodes.sockets.functions import vector_multiply_add, vector_sin, vector_snap, vector_subtract, vector_tanfrom geonodes.sockets.functions import vector_wrap, wrap, xnor, xor    