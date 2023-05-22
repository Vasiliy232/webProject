from rest_framework.pagination import PageNumberPagination


class StructurePagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'


class RegisterPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'


class SubStructurePagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'

