from graphviz import Digraph

def create_class_diagram():
    dot = Digraph(comment='UML Class Diagram - Student Management System', format='png')
    dot.attr(rankdir='TB', splines='ortho', nodesep='0.5', ranksep='1.2')
    
    # Define class structure with fields and methods
    
    # CustomUser Class
    custom_user_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="lightblue"><B>CustomUser</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ username: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ password: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ email: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ first_name: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ last_name: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ user_type: int (1/2/3)</TD></TR>
        <TR><TD ALIGN="LEFT">+ is_staff: bool</TD></TR>
        <TR><TD ALIGN="LEFT">+ is_active: bool</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ get_full_name(): str</TD></TR>
        <TR><TD ALIGN="LEFT">+ set_password(): void</TD></TR>
    </TABLE>>'''
    
    # AdminHOD Class
    admin_hod_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="lightgreen"><B>AdminHOD</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ admin: CustomUser (1:1)</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ create_course(): void</TD></TR>
        <TR><TD ALIGN="LEFT">+ manage_staff(): void</TD></TR>
        <TR><TD ALIGN="LEFT">+ approve_leave(): void</TD></TR>
        <TR><TD ALIGN="LEFT">+ generate_report(): void</TD></TR>
    </TABLE>>'''
    
    # Staffs Class
    staffs_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="lightgreen"><B>Staffs</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ admin: CustomUser (1:1)</TD></TR>
        <TR><TD ALIGN="LEFT">+ address: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ mark_attendance(): void</TD></TR>
        <TR><TD ALIGN="LEFT">+ upload_marks(): void</TD></TR>
        <TR><TD ALIGN="LEFT">+ manage_subjects(): void</TD></TR>
        <TR><TD ALIGN="LEFT">+ submit_feedback(): void</TD></TR>
    </TABLE>>'''
    
    # Students Class
    students_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="lightcyan"><B>Students</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ admin: CustomUser (1:1)</TD></TR>
        <TR><TD ALIGN="LEFT">+ gender: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ profile_pic: file</TD></TR>
        <TR><TD ALIGN="LEFT">+ address: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ course_id: Courses (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ session_year_id: SessionYearModel (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ view_attendance(): list</TD></TR>
        <TR><TD ALIGN="LEFT">+ view_marks(): list</TD></TR>
        <TR><TD ALIGN="LEFT">+ submit_leave(): void</TD></TR>
        <TR><TD ALIGN="LEFT">+ submit_feedback(): void</TD></TR>
    </TABLE>>'''
    
    # Courses Class
    courses_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Courses</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ course_name: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ get_subjects(): list</TD></TR>
        <TR><TD ALIGN="LEFT">+ get_students(): list</TD></TR>
    </TABLE>>'''
    
    # SessionYearModel Class
    session_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>SessionYearModel</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ session_start_year: date</TD></TR>
        <TR><TD ALIGN="LEFT">+ session_end_year: date</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ get_duration(): str</TD></TR>
    </TABLE>>'''
    
    # Subjects Class
    subjects_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Subjects</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ subject_name: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ course_id: Courses (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ staff_id: CustomUser (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ get_attendance(): list</TD></TR>
        <TR><TD ALIGN="LEFT">+ get_results(): list</TD></TR>
    </TABLE>>'''
    
    # Attendance Class
    attendance_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="lightcoral"><B>Attendance</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ subject_id: Subjects (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ attendance_date: date</TD></TR>
        <TR><TD ALIGN="LEFT">+ session_year_id: SessionYearModel (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ mark_present(): void</TD></TR>
        <TR><TD ALIGN="LEFT">+ mark_absent(): void</TD></TR>
    </TABLE>>'''
    
    # AttendanceReport Class
    attendance_report_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="lightcoral"><B>AttendanceReport</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ student_id: Students (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ attendance_id: Attendance (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ status: bool</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ is_present(): bool</TD></TR>
    </TABLE>>'''
    
    # StudentResult Class
    result_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="plum"><B>StudentResult</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ student_id: Students (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ subject_id: Subjects (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ subject_exam_marks: float</TD></TR>
        <TR><TD ALIGN="LEFT">+ subject_assignment_marks: float</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ calculate_total(): float</TD></TR>
        <TR><TD ALIGN="LEFT">+ get_grade(): str</TD></TR>
    </TABLE>>'''
    
    # LeaveReportStudent Class
    leave_student_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="peachpuff"><B>LeaveReportStudent</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ student_id: Students (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ leave_date: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ leave_message: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ leave_status: int (0/1/-1)</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ is_approved(): bool</TD></TR>
    </TABLE>>'''
    
    # LeaveReportStaff Class
    leave_staff_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="peachpuff"><B>LeaveReportStaff</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ staff_id: Staffs (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ leave_date: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ leave_message: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ leave_status: int (0/1/-1)</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ is_approved(): bool</TD></TR>
    </TABLE>>'''
    
    # FeedBackStudent Class
    feedback_student_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="lavender"><B>FeedBackStudent</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ student_id: Students (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ feedback: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ feedback_reply: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ has_reply(): bool</TD></TR>
    </TABLE>>'''
    
    # FeedBackStaffs Class
    feedback_staff_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="lavender"><B>FeedBackStaffs</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ staff_id: Staffs (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ feedback: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ feedback_reply: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ has_reply(): bool</TD></TR>
    </TABLE>>'''
    
    # NotificationStudent Class
    notification_student_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="honeydew"><B>NotificationStudent</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ student_id: Students (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ message: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ send_notification(): void</TD></TR>
    </TABLE>>'''
    
    # NotificationStaffs Class
    notification_staff_class = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR><TD COLSPAN="1" BGCOLOR="honeydew"><B>NotificationStaffs</B></TD></TR>
        <TR><TD ALIGN="LEFT"><U>+ id: int</U></TD></TR>
        <TR><TD ALIGN="LEFT">+ stafff_id: Staffs (FK)</TD></TR>
        <TR><TD ALIGN="LEFT">+ message: str</TD></TR>
        <TR><TD ALIGN="LEFT">+ created_at: datetime</TD></TR>
        <TR><TD ALIGN="LEFT">+ updated_at: datetime</TD></TR>
        <TR><TD COLSPAN="1" BGCOLOR="lightyellow"><B>Methods</B></TD></TR>
        <TR><TD ALIGN="LEFT">+ send_notification(): void</TD></TR>
    </TABLE>>'''
    
    # Create nodes
    dot.node('CustomUser', custom_user_class, shape='plaintext')
    dot.node('AdminHOD', admin_hod_class, shape='plaintext')
    dot.node('Staffs', staffs_class, shape='plaintext')
    dot.node('Students', students_class, shape='plaintext')
    dot.node('Courses', courses_class, shape='plaintext')
    dot.node('SessionYearModel', session_class, shape='plaintext')
    dot.node('Subjects', subjects_class, shape='plaintext')
    dot.node('Attendance', attendance_class, shape='plaintext')
    dot.node('AttendanceReport', attendance_report_class, shape='plaintext')
    dot.node('StudentResult', result_class, shape='plaintext')
    dot.node('LeaveReportStudent', leave_student_class, shape='plaintext')
    dot.node('LeaveReportStaff', leave_staff_class, shape='plaintext')
    dot.node('FeedBackStudent', feedback_student_class, shape='plaintext')
    dot.node('FeedBackStaffs', feedback_staff_class, shape='plaintext')
    dot.node('NotificationStudent', notification_student_class, shape='plaintext')
    dot.node('NotificationStaffs', notification_staff_class, shape='plaintext')
    
    # One-to-One Relationships
    dot.edge('CustomUser', 'AdminHOD', label='1:1', arrowhead='none', arrowtail='none', style='dashed')
    dot.edge('CustomUser', 'Staffs', label='1:1', arrowhead='none', arrowtail='none', style='dashed')
    dot.edge('CustomUser', 'Students', label='1:1', arrowhead='none', arrowtail='none', style='dashed')
    
    # One-to-Many Relationships
    # Courses relationships
    dot.edge('Courses', 'Subjects', label='1:N', arrowhead='crow', arrowtail='none')
    dot.edge('Courses', 'Students', label='1:N', arrowhead='crow', arrowtail='none')
    
    # SessionYearModel relationships
    dot.edge('SessionYearModel', 'Attendance', label='1:N', arrowhead='crow', arrowtail='none')
    dot.edge('SessionYearModel', 'Students', label='1:N', arrowhead='crow', arrowtail='none')
    
    # Subjects relationships
    dot.edge('Subjects', 'Attendance', label='1:N', arrowhead='crow', arrowtail='none')
    dot.edge('Subjects', 'StudentResult', label='1:N', arrowhead='crow', arrowtail='none')
    
    # CustomUser (Staff) to Subjects
    dot.edge('CustomUser', 'Subjects', label='1:N\n(staff)', arrowhead='crow', arrowtail='none', style='dashed')
    
    # Students relationships
    dot.edge('Students', 'AttendanceReport', label='1:N', arrowhead='crow', arrowtail='none')
    dot.edge('Students', 'LeaveReportStudent', label='1:N', arrowhead='crow', arrowtail='none')
    dot.edge('Students', 'FeedBackStudent', label='1:N', arrowhead='crow', arrowtail='none')
    dot.edge('Students', 'NotificationStudent', label='1:N', arrowhead='crow', arrowtail='none')
    dot.edge('Students', 'StudentResult', label='1:N', arrowhead='crow', arrowtail='none')
    
    # Staffs relationships
    dot.edge('Staffs', 'LeaveReportStaff', label='1:N', arrowhead='crow', arrowtail='none')
    dot.edge('Staffs', 'FeedBackStaffs', label='1:N', arrowhead='crow', arrowtail='none')
    dot.edge('Staffs', 'NotificationStaffs', label='1:N', arrowhead='crow', arrowtail='none')
    
    # Attendance relationships
    dot.edge('Attendance', 'AttendanceReport', label='1:N', arrowhead='crow', arrowtail='none')
    
    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/class_diagram'
    dot.render(output_path, cleanup=True)
    print(f"Class Diagram generated successfully: {output_path}.png")

# Generate class diagram
create_class_diagram()
