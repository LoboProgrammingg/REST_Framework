from rest_framework import permissions

class GenrePermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # Permission Logic
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            #genres(nome do app), view(oque voce ta liberando), genre(nome do model)
            return request.user.has_perm('genres.view_genre')
        
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        if request.method in ['PATH', 'PUT']:
            return request.user.has_perm('genres.change_genre')
        
        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')
        
        return False