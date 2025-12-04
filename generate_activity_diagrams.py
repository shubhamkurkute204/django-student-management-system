from graphviz import Digraph

def create_activity_diagram_student_login():
    """Activity Diagram for Student Login Process"""
    dot = Digraph(comment='Activity Diagram - Student Login', format='png')
    dot.attr(rankdir='TB', splines='ortho', nodesep='0.5', ranksep='0.8')
    dot.attr('node', shape='box', style='rounded', fontname='Arial', fontsize='9')
    
    # Start and End nodes
    dot.node('start', '', shape='circle', style='filled', fillcolor='black', width='0.3')
    dot.node('end', '', shape='circle', style='filled', fillcolor='black', width='0.3', 
             peripheries='2')
    
    # Activities
    dot.node('a1', 'Enter Username\nand Password', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a2', 'Submit Credentials', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a3', 'Verify User\nin Database', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('d1', 'Credentials\nValid?', shape='diamond', style='filled', 
             fillcolor='#FFFACD')
    dot.node('a4', 'Check User Type', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('d2', 'User Type\n= Student?', shape='diamond', style='filled', 
             fillcolor='#FFFACD')
    dot.node('a5', 'Load Student\nDashboard', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a6', 'Display Error\nMessage', shape='box', style='rounded,filled', 
             fillcolor='#FFB6C6')
    dot.node('a7', 'Redirect to\nWrong Portal', shape='box', style='rounded,filled', 
             fillcolor='#FFB6C6')
    dot.node('a8', 'Log Login Activity', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    
    # Transitions
    dot.edge('start', 'a1')
    dot.edge('a1', 'a2')
    dot.edge('a2', 'a3')
    dot.edge('a3', 'd1')
    dot.edge('d1', 'a4', label='Yes')
    dot.edge('d1', 'a6', label='No')
    dot.edge('a4', 'd2')
    dot.edge('d2', 'a5', label='Yes')
    dot.edge('d2', 'a7', label='No')
    dot.edge('a5', 'a8')
    dot.edge('a6', 'a1', style='dashed')
    dot.edge('a7', 'a1', style='dashed')
    dot.edge('a8', 'end')
    
    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/activity_student_login'
    dot.render(output_path, cleanup=True)
    print(f"Activity Diagram (Student Login) generated: {output_path}.png")

def create_activity_diagram_attendance():
    """Activity Diagram for Attendance Marking Process"""
    dot = Digraph(comment='Activity Diagram - Attendance Marking', format='png')
    dot.attr(rankdir='TB', splines='ortho', nodesep='0.5', ranksep='0.8')
    dot.attr('node', shape='box', style='rounded', fontname='Arial', fontsize='9')
    
    # Start and End
    dot.node('start', '', shape='circle', style='filled', fillcolor='black', width='0.3')
    dot.node('end', '', shape='circle', style='filled', fillcolor='black', width='0.3', 
             peripheries='2')
    
    # Activities
    dot.node('a1', 'Staff Opens\nAttendance Module', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a2', 'Select Subject\nand Date', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a3', 'Load Student\nList', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a4', 'Mark Attendance\n(Present/Absent)', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('d1', 'All Students\nMarked?', shape='diamond', style='filled', 
             fillcolor='#FFFACD')
    dot.node('a5', 'Verify Attendance\nRecord', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a6', 'Submit Attendance', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('d2', 'Verified\nSuccessfully?', shape='diamond', style='filled', 
             fillcolor='#FFFACD')
    dot.node('a7', 'Save to Database', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a8', 'Display Error\nMessage', shape='box', style='rounded,filled', 
             fillcolor='#FFB6C6')
    dot.node('a9', 'Send Notification\nto Students', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    
    # Transitions
    dot.edge('start', 'a1')
    dot.edge('a1', 'a2')
    dot.edge('a2', 'a3')
    dot.edge('a3', 'a4')
    dot.edge('a4', 'd1')
    dot.edge('d1', 'a4', label='No')
    dot.edge('d1', 'a5', label='Yes')
    dot.edge('a5', 'a6')
    dot.edge('a6', 'd2')
    dot.edge('d2', 'a7', label='Yes')
    dot.edge('d2', 'a8', label='No')
    dot.edge('a8', 'a4', style='dashed')
    dot.edge('a7', 'a9')
    dot.edge('a9', 'end')
    
    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/activity_attendance'
    dot.render(output_path, cleanup=True)
    print(f"Activity Diagram (Attendance) generated: {output_path}.png")

def create_activity_diagram_marks():
    """Activity Diagram for Marks Upload and View"""
    dot = Digraph(comment='Activity Diagram - Marks Management', format='png')
    dot.attr(rankdir='TB', splines='ortho', nodesep='0.5', ranksep='0.8')
    dot.attr('node', shape='box', style='rounded', fontname='Arial', fontsize='9')
    
    # Start and End
    dot.node('start', '', shape='circle', style='filled', fillcolor='black', width='0.3')
    dot.node('end', '', shape='circle', style='filled', fillcolor='black', width='0.3', 
             peripheries='2')
    
    # Activities
    dot.node('a1', 'Staff/HOD Opens\nMarks Module', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a2', 'Select Subject\nand Class', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a3', 'Upload/Enter\nStudent Marks', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a4', 'Validate Marks', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('d1', 'Valid?', shape='diamond', style='filled', 
             fillcolor='#FFFACD')
    dot.node('a5', 'Calculate Grades', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a6', 'Save Results', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a7', 'Display Error', shape='box', style='rounded,filled', 
             fillcolor='#FFB6C6')
    dot.node('a8', 'Send Notification', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    
    # Transitions
    dot.edge('start', 'a1')
    dot.edge('a1', 'a2')
    dot.edge('a2', 'a3')
    dot.edge('a3', 'a4')
    dot.edge('a4', 'd1')
    dot.edge('d1', 'a7', label='No')
    dot.edge('d1', 'a5', label='Yes')
    dot.edge('a7', 'a3', style='dashed')
    dot.edge('a5', 'a6')
    dot.edge('a6', 'a8')
    dot.edge('a8', 'end')
    dot.edge('a7', 'end')
    
    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/activity_marks'
    dot.render(output_path, cleanup=True)
    print(f"Activity Diagram (Marks) generated: {output_path}.png")

def create_activity_diagram_leave():
    """Activity Diagram for Leave Request Process"""
    dot = Digraph(comment='Activity Diagram - Leave Request', format='png')
    dot.attr(rankdir='TB', splines='curved', nodesep='0.5', ranksep='0.8')
    dot.attr('node', shape='box', style='rounded', fontname='Arial', fontsize='9')
    
    # Start and End
    dot.node('start', '', shape='circle', style='filled', fillcolor='black', width='0.3')
    dot.node('end', '', shape='circle', style='filled', fillcolor='black', width='0.3', 
             peripheries='2')
    
    # Activities
    dot.node('a1', 'Student Submits\nLeave Request', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a2', 'Enter Leave Date\nand Reason', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a3', 'Validate Request', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('d1', 'Valid?', shape='diamond', style='filled', 
             fillcolor='#FFFACD')
    dot.node('a4', 'Save Request', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a5', 'HOD Reviews\nand Decides', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('d2', 'Approved?', shape='diamond', style='filled', 
             fillcolor='#FFFACD')
    dot.node('a6', 'Mark as Approved', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a7', 'Mark as Rejected', shape='box', style='rounded,filled', 
             fillcolor='#FFB6C6')
    dot.node('a8', 'Send Notification', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a9', 'Display Error', shape='box', style='rounded,filled', 
             fillcolor='#FFB6C6')
    
    # Transitions
    dot.edge('start', 'a1')
    dot.edge('a1', 'a2')
    dot.edge('a2', 'a3')
    dot.edge('a3', 'd1')
    dot.edge('d1', 'a9', label='No')
    dot.edge('d1', 'a4', label='Yes')
    dot.edge('a4', 'a5')
    dot.edge('a5', 'd2')
    dot.edge('d2', 'a6', label='Yes')
    dot.edge('d2', 'a7', label='No')
    dot.edge('a6', 'a8')
    dot.edge('a7', 'a8')
    dot.edge('a8', 'end')
    dot.edge('a9', 'end')
    
    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/activity_leave'
    dot.render(output_path, cleanup=True)
    print(f"Activity Diagram (Leave Request) generated: {output_path}.png")

def create_activity_diagram_feedback():
    """Activity Diagram for Feedback System"""
    dot = Digraph(comment='Activity Diagram - Feedback System', format='png')
    dot.attr(rankdir='TB', splines='curved', nodesep='0.5', ranksep='0.8')
    dot.attr('node', shape='box', style='rounded', fontname='Arial', fontsize='9')
    
    # Start and End
    dot.node('start', '', shape='circle', style='filled', fillcolor='black', width='0.3')
    dot.node('end', '', shape='circle', style='filled', fillcolor='black', width='0.3', 
             peripheries='2')
    
    # Activities
    dot.node('a1', 'User Submits\nFeedback', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a2', 'Enter Feedback\nMessage', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a3', 'Validate\nFeedback', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('d1', 'Valid?', shape='diamond', style='filled', 
             fillcolor='#FFFACD')
    dot.node('a4', 'Save Feedback', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a5', 'Notify HOD', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a6', 'HOD Reviews\nand Replies', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a7', 'Send Notification\nto User', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a8', 'Display Error', shape='box', style='rounded,filled', 
             fillcolor='#FFB6C6')
    
    # Transitions
    dot.edge('start', 'a1')
    dot.edge('a1', 'a2')
    dot.edge('a2', 'a3')
    dot.edge('a3', 'd1')
    dot.edge('d1', 'a8', label='No')
    dot.edge('d1', 'a4', label='Yes')
    dot.edge('a4', 'a5')
    dot.edge('a5', 'a6')
    dot.edge('a6', 'a7')
    dot.edge('a7', 'end')
    dot.edge('a8', 'end')
    
    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/activity_feedback'
    dot.render(output_path, cleanup=True)
    print(f"Activity Diagram (Feedback) generated: {output_path}.png")

def create_activity_diagram_course():
    """Activity Diagram for Course Management"""
    dot = Digraph(comment='Activity Diagram - Course Management', format='png')
    dot.attr(rankdir='TB', splines='curved', nodesep='0.5', ranksep='0.8')
    dot.attr('node', shape='box', style='rounded', fontname='Arial', fontsize='9')
    
    # Start and End
    dot.node('start', '', shape='circle', style='filled', fillcolor='black', width='0.3')
    dot.node('end', '', shape='circle', style='filled', fillcolor='black', width='0.3', 
             peripheries='2')
    
    # Activities
    dot.node('a1', 'HOD Opens Course\nManagement', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a2', 'Enter Course\nDetails', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a3', 'Validate\nCourse Data', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('d1', 'Valid?', shape='diamond', style='filled', 
             fillcolor='#FFFACD')
    dot.node('a4', 'Save Course', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a5', 'Assign Subjects', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a6', 'Assign Staff', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a7', 'Send Notification', shape='box', style='rounded,filled', 
             fillcolor='#FFE4B5')
    dot.node('a8', 'Display Error', shape='box', style='rounded,filled', 
             fillcolor='#FFB6C6')
    
    # Transitions
    dot.edge('start', 'a1')
    dot.edge('a1', 'a2')
    dot.edge('a2', 'a3')
    dot.edge('a3', 'd1')
    dot.edge('d1', 'a8', label='No')
    dot.edge('d1', 'a4', label='Yes')
    dot.edge('a4', 'a5')
    dot.edge('a5', 'a6')
    dot.edge('a6', 'a7')
    dot.edge('a7', 'end')
    dot.edge('a8', 'end')
    
    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/activity_course'
    dot.render(output_path, cleanup=True)
    print(f"Activity Diagram (Course Management) generated: {output_path}.png")

# Additional: per-user overview activity diagrams
def create_activity_diagram_user_student_overview():
    """Overview activity diagram showing typical student actions"""
    dot = Digraph(comment='Activity Diagram - Student Overview', format='png')
    dot.attr(rankdir='TB', splines='curved')
    dot.attr('node', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontname='Arial')

    dot.node('start', '', shape='circle', style='filled', fillcolor='black', width='0.25')
    dot.node('login', 'Login / Authenticate')
    dot.node('view_att', 'View Attendance')
    dot.node('view_marks', 'View Marks / Results')
    dot.node('submit_leave', 'Submit Leave Request')
    dot.node('submit_feedback', 'Submit Feedback')
    dot.node('notifications', 'Receive Notifications')
    dot.node('end', '', shape='circle', style='filled', fillcolor='black', width='0.25', peripheries='2')

    dot.edge('start', 'login')
    dot.edge('login', 'view_att')
    dot.edge('login', 'view_marks')
    dot.edge('login', 'submit_leave')
    dot.edge('login', 'submit_feedback')
    dot.edge('view_att', 'notifications', style='dashed')
    dot.edge('view_marks', 'notifications', style='dashed')
    dot.edge('submit_leave', 'notifications', style='dashed')
    dot.edge('submit_feedback', 'notifications', style='dashed')
    dot.edge('notifications', 'end')

    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/activity_user_student_overview'
    dot.render(output_path, cleanup=True)
    print(f"Activity Diagram (Student Overview) generated: {output_path}.png")


def create_activity_diagram_user_staff_overview():
    """Overview activity diagram showing typical staff actions"""
    dot = Digraph(comment='Activity Diagram - Staff Overview', format='png')
    dot.attr(rankdir='TB', splines='curved')
    dot.attr('node', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontname='Arial')

    dot.node('start', '', shape='circle', style='filled', fillcolor='black', width='0.25')
    dot.node('login', 'Login / Authenticate')
    dot.node('mark_att', 'Mark Attendance')
    dot.node('upload_marks', 'Upload Marks')
    dot.node('manage_subjects', 'Manage Subjects')
    dot.node('approve_leaves', 'Approve/Reject Leaves')
    dot.node('send_notifications', 'Send Notifications')
    dot.node('end', '', shape='circle', style='filled', fillcolor='black', width='0.25', peripheries='2')

    dot.edge('start', 'login')
    dot.edge('login', 'mark_att')
    dot.edge('login', 'upload_marks')
    dot.edge('login', 'manage_subjects')
    dot.edge('manage_subjects', 'upload_marks')
    dot.edge('mark_att', 'send_notifications', style='dashed')
    dot.edge('upload_marks', 'send_notifications', style='dashed')
    dot.edge('approve_leaves', 'send_notifications', style='dashed')
    dot.edge('login', 'approve_leaves')
    dot.edge('send_notifications', 'end')

    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/activity_user_staff_overview'
    dot.render(output_path, cleanup=True)
    print(f"Activity Diagram (Staff Overview) generated: {output_path}.png")


def create_activity_diagram_user_hod_overview():
    """Overview activity diagram showing typical HOD/Admin actions"""
    dot = Digraph(comment='Activity Diagram - HOD/Admin Overview', format='png')
    dot.attr(rankdir='TB', splines='curved')
    dot.attr('node', shape='box', style='rounded,filled', fillcolor='#FFE4B5', fontname='Arial')

    dot.node('start', '', shape='circle', style='filled', fillcolor='black', width='0.25')
    dot.node('login', 'Login / Authenticate')
    dot.node('create_course', 'Create / Manage Courses')
    dot.node('assign_staff', 'Assign Staff to Subjects')
    dot.node('approve_leaves', 'Approve/Reject Leaves')
    dot.node('generate_reports', 'Generate Reports')
    dot.node('manage_users', 'Manage Users (Staff/Students)')
    dot.node('end', '', shape='circle', style='filled', fillcolor='black', width='0.25', peripheries='2')

    dot.edge('start', 'login')
    dot.edge('login', 'create_course')
    dot.edge('create_course', 'assign_staff')
    dot.edge('login', 'approve_leaves')
    dot.edge('approve_leaves', 'manage_users')
    dot.edge('manage_users', 'generate_reports')
    dot.edge('generate_reports', 'end')

    output_path = '/home/shubham-kurkute/Documents/Django Proj/django-student-management-system/activity_user_hod_overview'
    dot.render(output_path, cleanup=True)
    print(f"Activity Diagram (HOD/Admin Overview) generated: {output_path}.png")


# Generate all activity diagrams (including per-user overviews)
print("Generating Activity Diagrams (including per-user overviews)...")
create_activity_diagram_student_login()
create_activity_diagram_attendance()
create_activity_diagram_marks()
create_activity_diagram_leave()
create_activity_diagram_feedback()
create_activity_diagram_course()
create_activity_diagram_user_student_overview()
create_activity_diagram_user_staff_overview()
create_activity_diagram_user_hod_overview()
print("\nAll Activity Diagrams generated successfully!")
