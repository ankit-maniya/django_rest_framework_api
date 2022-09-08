from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class StudentStandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'
    page_size_query_param = 'records'
    # max_page_size = 2

class StudentLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5

class StudentCursorPagination(CursorPagination):
    ordering = 'name'
    page_size = 6
    cursor_query_param = 'cu'