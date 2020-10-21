def add_variable_to_context(request):
    if request.COOKIES.get('uuid') is not None:
        return {
            'uuid': request.COOKIES.get('uuid')
        }
    else:
        return {
            'uuid': '000'
        }
