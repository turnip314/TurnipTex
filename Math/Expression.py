class Type:
    EXPR = "expr"
    TEXT = "text"
    WORD = "word"
    FRACTION = "frac"
    SUM = "sum"
    POWER = "pow"
    SUB = "sub"


class AXIS:
    VERTICAL = 1
    HORIZONTAL = 2


class RESTRICTION:
    TOP = 1
    BOTTOM = 2
    LEFT = 3


class Expression:
    def __init__(self, expr_type):
        self.TYPE = expr_type
        self.scale = 1
        self.width = None
        self.height = None
        self.height_below_origin = None
        self.height_above_origin = None
        self.height_of_main_component = None

    def __str__(self):
        raise Exception("__str__ not implemented for %s" % self.TYPE)

    @property
    def is_center_align(self):
        """
        Whether or not to align with other expressions by center of main component
        :return:
        """
        return True

    @property
    def is_top_align(self):
        """
        Exponents for example
        :return:
        """
        return False

    def initialize(self):
        """
        Initializes size fields
        Must be called in this order
        :return:
        """
        self.initialize_width()
        self.initialize_height()
        self.initialize_height_below_origin()
        self.initialize_height_of_main_component()
        self.initialize_height_above_origin()

    def initialize_width(self):
        raise Exception("Width initialization not implemented for " + str(type(self)))

    def initialize_height(self):
        raise Exception("Height initialization not implemented for " + str(type(self)))

    def initialize_height_below_origin(self):
        raise Exception("Initialize height below origin not implemented for " + str(type(self)))

    def initialize_height_of_main_component(self):
        raise Exception("Initialize height of main component not implemented for " + str(type(self)))

    def initialize_height_above_origin(self):
        self.height_above_origin = self.get_height - self.get_height_below_origin

    def set_scale(self, scale=1):
        raise Exception("Scale not implemented for " + str(type(self)))

    @property
    def get_width(self):
        return self.width

    @property
    def get_height(self):
        return self.height

    @property
    def get_height_below_origin(self):
        return self.height_below_origin

    @property
    def get_height_above_origin(self):
        return self.height_above_origin

    @property
    def get_height_of_main_component(self):
        return self.height_of_main_component

    def draw(self, handler):
        raise Exception("Draw not implemented for " + str(type(self)))
        pass


