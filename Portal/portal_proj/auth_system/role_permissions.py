class RolePermissions:
    PERMISSIONS = {
        'SuperAdmin': 10,
        'Admin': 8,
        'Manager': 6,
        'Employee': 4,
        'User': 2
    }

    def __init__(self, role):
        self.role = role

    def get_permissions(self):
        return self.PERMISSIONS.get(self.role, 0)
