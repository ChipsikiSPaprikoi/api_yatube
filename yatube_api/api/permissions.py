from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Кастомное разрешение для предоставления прав на редактирование
    только автору объекта.
    """

    def has_object_permission(self, request, view, obj):
        # Права на чтение предоставляются всем аутентифицированным
        # пользователям
        if request.method in permissions.SAFE_METHODS:
            return True

        # Права на изменение предоставляются только автору объекта
        return obj.author == request.user
