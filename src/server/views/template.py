import collections
from src.server.views.pagination import Pagination


class Template:
    """
    The Restful class is used for the gathering specific information using the URL

    Each field will be parsed by the method in :py:meth:`src.server.views.restful`
    """
    def __init__(self):
        """
        The fields are the following one :

        :param fields: The fields that want to be in the output
        :type fields: List
        :param filters: The queriable field from DB
        :type filters: Dictionary
        :param order_by: Order the items that are query
        :type order_by: Dictionary
        :param pagination: Pagination information
        :type pagination: Dictionary
        :param q: Direct query
        :type q: String
        """
        self.fields = []
        self.filters = {}
        self.order_by = collections.OrderedDict()
        self.pagination = Pagination()
        self.q = None
