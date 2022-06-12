import inspect
from typing import Any, Callable, List, Type, TypeVar, Union, get_type_hints

from fastapi import APIRouter, Depends
from pydantic.typing import is_classvar
from starlette.routing import Route, WebSocketRoute
from fastapi_utils.cbv import _init_cbv, _update_cbv_route_endpoint_signature


T = TypeVar("T")

CBV_CLASS_KEY = "__cbv_class__"


"""
extension for cbv route to fix duplicate prefix path
"""
def cbv(router: APIRouter) -> Callable[[Type[T]], Type[T]]:
    """
    This function returns a decorator that converts the decorated into a class-based view for the provided router.

    Any methods of the decorated class that are decorated as endpoints using the router provided to this function
    will become endpoints in the router. The first positional argument to the methods (typically `self`)
    will be populated with an instance created using FastAPI's dependency-injection.

    For more detail, review the documentation at
    https://fastapi-utils.davidmontague.xyz/user-guide/class-based-views/#the-cbv-decorator
    """

    def decorator(cls: Type[T]) -> Type[T]:
        return _cbv(router, cls)

    return decorator


def _cbv(router: APIRouter, cls: Type[T]) -> Type[T]:
    """
    Replaces any methods of the provided class `cls` that are endpoints of routes in `router` with updated
    function calls that will properly inject an instance of `cls`.
    """
    _init_cbv(cls)
    cbv_router = APIRouter()
    function_members = inspect.getmembers(cls, inspect.isfunction)
    functions_set = set(func for _, func in function_members)
    cbv_routes = [
        route
        for route in router.routes
        if isinstance(route, (Route, WebSocketRoute)) and route.endpoint in functions_set
    ]
    for route in cbv_routes:
        _update_cbv_route_endpoint_signature(cls, route)
    router.include_router(cbv_router)
    return cls