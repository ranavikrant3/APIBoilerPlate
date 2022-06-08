class Pagination:
    """
    This class is used for paging in the restful object. It is an optional field that can be set in the routes.py file
    """
    def __init__(self):
        """
        :param limit: Limit number of item in the page
        :type limit: Integer, default=50
        :param offset: Integer from which item to start from the list
        :type offset: Integer, default=0
        :param totat_count: Total number of item in the list
        :type totat_count: Integer, default=0
        """
        self.limit = 50
        self.offset = 0
        self.total_count = 0
