def get_dashboard_content(role):
    """Returns dashboard content based on user role"""
    content = {
        "SuperAdmin": [
            "Dashboard",
            "Request",
            "Admin",
            "Manager",
            "Employee",
            "Users",
            "Sales",
            "Students",
            "Colleges",
            "Question",
        ],
        "Admin": [
            "Dashboard",
            "Request",
            "Manager",
            "Employee",
            "Users",
            "Sales",
            "Students",
            "Colleges",
            "Question",
        ],
        "Manager": [
            "Dashboard",
            "Request",
            "Employee",
            "Users",
            "Sales",
            "Students",
            "Colleges",
            "Question",
        ],
        "Employee": [
            "Dashboard",
            "Request",
            "Users",
            "Sales",
            "Students",
            "Colleges",
            "Question",
        ],
        "User": [
            "Dashboard",
            "Request",
            "Users",
            "Sales",
            "Students",
            "Colleges",
            "Question",
        ],
    }

    return content.get(role, [])  # Default to an empty list if the role is missing
