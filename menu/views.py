from django.core.exceptions import FieldError
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from django.db.models import Prefetch

from .models import FoodCategory, Food
from .serializers import DishSerializer


class DishViewSet(viewsets.ViewSet):
    """
        A simple ViewSet for get dishes.
    """

    def list(self, request: Request, *args, **kwargs):
        type_filter = request.query_params.get("filter")  # example: 'is_vegan', 'topping__name', 'is_special'
        value_filter = request.query_params.get("value")  # example: '0' - '1',  'Банан'           '0' - '1'

        qs_filter = Food.objects.filter(is_publish=True)
        if type_filter and value_filter:
            # quickly solution
            try:
                qs_filter = qs_filter.filter(**{type_filter: value_filter})
            except FieldError:
                return Response(status=422)

        queryset = FoodCategory.objects.prefetch_related(Prefetch('foods', queryset=qs_filter))
        serializer = DishSerializer(queryset, many=True)
        return Response(serializer.data)
