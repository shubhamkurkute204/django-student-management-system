from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Student Management System ER Diagram', format='png')
dot.attr(rankdir='TB', splines='ortho', nodesep='0.5', ranksep='0.7')

# Define node attributes
dot.attr('node', shape='box', style='filled', fillcolor='lightblue', fontname='Arial', fontsize='10')

# Define tables
tables = {
    'CustomUser': {
        'fields': [
            'id (PK)',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'user_type (1/2/3)',
            'is_staff',
            'is_active'
        ],
        'color': 'lightcoral'
    },
    'AdminHOD': {
        'fields': ['id (PK)', 'admin_id (FK)', 'created_at', 'updated_at'],
        'color': 'lightgreen'
    },
    'Staffs': {
        'fields': ['id (PK)', 'admin_id (FK)', 'address', 'created_at', 'updated_at'],
        'color': 'lightgreen'
    },
    'Students': {
        'fields': ['id (PK)', 'admin_id (FK)', 'gender', 'profile_pic', 'address', 'course_id (FK)', 'session_year_id (FK)', 'created_at', 'updated_at'],
        'color': 'lightgreen'
    },
    'Courses': {
        'fields': ['id (PK)', 'course_name', 'created_at', 'updated_at'],
        'color': 'lightyellow'
    },
    'SessionYearModel': {
        'fields': ['id (PK)', 'session_start_year', 'session_end_year'],
        'color': 'lightyellow'
    },
    'Subjects': {
        'fields': ['id (PK)', 'subject_name', 'course_id (FK)', 'staff_id (FK)', 'created_at', 'updated_at'],
        'color': 'lightyellow'
    },
    'Attendance': {
        'fields': ['id (PK)', 'subject_id (FK)', 'attendance_date', 'session_year_id (FK)', 'created_at', 'updated_at'],
        'color': 'lightcyan'
    },
    'AttendanceReport': {
        'fields': ['id (PK)', 'student_id (FK)', 'attendance_id (FK)', 'status', 'created_at', 'updated_at'],
        'color': 'lightcyan'
    },
    'StudentResult': {
        'fields': ['id (PK)', 'student_id (FK)', 'subject_id (FK)', 'subject_exam_marks', 'subject_assignment_marks', 'created_at', 'updated_at'],
        'color': 'plum'
    },
    'LeaveReportStudent': {
        'fields': ['id (PK)', 'student_id (FK)', 'leave_date', 'leave_message', 'leave_status', 'created_at', 'updated_at'],
        'color': 'peachpuff'
    },
    'LeaveReportStaff': {
        'fields': ['id (PK)', 'staff_id (FK)', 'leave_date', 'leave_message', 'leave_status', 'created_at', 'updated_at'],
        'color': 'peachpuff'
    },
    'FeedBackStudent': {
        'fields': ['id (PK)', 'student_id (FK)', 'feedback', 'feedback_reply', 'created_at', 'updated_at'],
        'color': 'lavender'
    },
    'FeedBackStaffs': {
        'fields': ['id (PK)', 'staff_id (FK)', 'feedback', 'feedback_reply', 'created_at', 'updated_at'],
        'color': 'lavender'
    },
    'NotificationStudent': {
        'fields': ['id (PK)', 'student_id (FK)', 'message', 'created_at', 'updated_at'],
        'color': 'honeydew'
    },
    'NotificationStaffs': {
        'fields': ['id (PK)', 'stafff_id (FK)', 'message', 'created_at', 'updated_at'],
        'color': 'honeydew'
    }
}

# Create nodes for each table
for table_name, table_info in tables.items():
    fields_str = '\n'.join(table_info['fields'])
    label = f"{{{table_name}|{fields_str}}}"
    dot.node(table_name, label, shape='record', fillcolor=table_info['color'])

# Define relationships (edges)
relationships = [
    # CustomUser relationships (1:1)
    ('CustomUser', 'AdminHOD', '1:1'),
    ('CustomUser', 'Staffs', '1:1'),
    ('CustomUser', 'Students', '1:1'),
    
    # Courses relationships (1:N)
    ('Courses', 'Subjects', '1:N'),
    ('Courses', 'Students', '1:N'),
    
    # SessionYearModel relationships (1:N)
    ('SessionYearModel', 'Attendance', '1:N'),
    ('SessionYearModel', 'Students', '1:N'),
    
    # Subjects relationships (1:N)
    ('Subjects', 'Attendance', '1:N'),
    ('Subjects', 'StudentResult', '1:N'),
    
    # CustomUser (Staff) to Subjects (1:N)
    ('CustomUser', 'Subjects', '1:N', 'staff_id'),
    
    # Students relationships (1:N)
    ('Students', 'AttendanceReport', '1:N'),
    ('Students', 'LeaveReportStudent', '1:N'),
    ('Students', 'FeedBackStudent', '1:N'),
    ('Students', 'NotificationStudent', '1:N'),
    ('Students', 'StudentResult', '1:N'),
    
    # Staffs relationships (1:N)
    ('Staffs', 'LeaveReportStaff', '1:N'),
    ('Staffs', 'FeedBackStaffs', '1:N'),
    ('Staffs', 'NotificationStaffs', '1:N'),
    
    # Attendance relationships (1:N)
    ('Attendance', 'AttendanceReport', '1:N'),
]

# Add edges
for relationship in relationships:
    if len(relationship) == 3:
        from_table, to_table, rel_type = relationship
        label = rel_type
    else:
        from_table, to_table, rel_type, fk_name = relationship
        label = f"{rel_type}\n({fk_name})"
    
    dot.edge(from_table, to_table, label=label, fontsize='9')

# Save the diagram
output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/er_diagram'
dot.render(output_path, cleanup=True)

print(f"ER Diagram generated successfully: {output_path}.png")
