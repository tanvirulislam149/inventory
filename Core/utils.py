from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    """
    Returns custom error response format for all exceptions.
    """
    # Call DRF's default handler first
    response = exception_handler(exc, context)
    message = None
    if response is not None:
        if response.status_code == 400:
            message = "Validation failed"
        elif response.status_code == 403:
            message = "Permission denied"
        elif response.status_code == 404:
            message = "Resource not found"
        else:
            message = getattr(response.data, "detail", "An error occurred")
        # Standardize response
        customized_response = {
            "success": False,
            "errors": response.data,  # raw errors
            "message": message,
            "status_code": response.status_code
        }
        return Response(customized_response, status=response.status_code)

    # Unhandled exceptions fallback
    return Response({
        "success": False,
        "errors": str(exc),
        "message": "Internal server error",
        "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
