def user_roles(request):
    if not request.user.is_authenticated:
        return {
            'is_organizer': False,
            'is_admin': False,
            'is_participant': False,
        }
    
    return {
        'is_organizer': request.user.groups.filter(name='organizer').exists(),
        'is_admin': request.user.is_superuser or request.user.groups.filter(name='admin').exists(),
        'is_participant': request.user.groups.filter(name='participant').exists(),
    }