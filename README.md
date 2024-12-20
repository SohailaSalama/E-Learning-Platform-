# E-Learning-Platform-


A comprehensive online learning management system inspired by Moodle, designed for both students and educators.

## Project Problem Statement
The problem this project aims to address is the lack of an efficient, scalable online learning platform for both students and educators. Current solutions like Moodle and others are often difficult to use, lack flexibility, and don't scale well to larger user bases. Students face challenges in accessing their coursework, submitting assignments, and interacting with instructors, while educators struggle to manage course materials, assignments, and student progress.

This project seeks to build an intuitive, feature-rich, and scalable online learning platform that allows students to access courses, interact with instructors, and submit assignments seamlessly, while providing educators with tools to create courses, grade assignments, and manage the learning experience.

## Project Idea
The idea is to develop an e-learning platform that supports both students and educators. The platform will allow students to access courses, participate in online discussions, view grades, and submit assignments. Educators will have the ability to create and manage courses, upload assignments, grade submissions, and provide feedback to students.

### Key Features:
- **User Authentication and Role Management**: Students and teachers will have different roles with access to different features.
- **Course Management**: Educators can create, update, and delete courses.
- **Assignments**: Students can submit assignments, and educators can grade them.
- **Forum/Discussion Board**: A space for students to interact with each other and ask questions to the instructor.

The platform will be scalable, allowing a large number of students and educators to use it simultaneously while maintaining high performance and usability.

## Requirements

### Functional Requirements
1. **User Authentication**:
   - Students and teachers should be able to log in and access their roles and permissions.
   - Role-based access control should be in place, where students can view and submit assignments, while teachers can create/manage courses and grade submissions.

2. **Course Management**:
   - Teachers can create new courses, update existing courses, and delete courses.
   - Students should be able to view available courses and enroll in them.

3. **Assignments**:
   - Students can submit assignments for a given course.
   - Teachers can grade assignments and provide feedback.

4. **Discussion Forums**:
   - A forum for each course should be available for students to ask questions and interact with instructors and peers.

5. **Grade Tracking**:
   - Students can view their grades for assignments and courses.
   - Teachers can provide feedback on assignments.

6. **Notifications**:
   - Students and teachers should receive notifications for important events like assignment deadlines, grades, and new course materials.

### Non-Functional Requirements
1. **Scalability**:
   - The platform should be able to support up to 5000 concurrent users without performance degradation.

2. **Security**:
   - User data (including login credentials) should be securely stored using encryption.
   - Use of HTTPS for secure communication.

3. **Performance**:
   - Pages should load in under 2 seconds, even when the platform is under heavy load.

4. **Usability**:
   - The platform should have an intuitive, user-friendly interface.
   - Accessible design for all users, including those with disabilities.

5. **Maintainability**:
   - The system should be modular and easy to update, with clear separation between front-end and back-end components.

## User Personas

### Student Persona
- **Name**: John Doe
- **Age**: 21
- **Occupation**: Full-time student at a university
- **Technology Proficiency**: Moderate (comfortable using technology for learning)
- **Goals**:
  - Access courses online
  - Submit assignments
  - Participate in discussions
  - Track grades and progress
- **Pain Points**:
  - Difficulty navigating current online platforms
  - Slow response times when submitting assignments
  - Lack of engagement with course content

### Teacher Persona
- **Name**: Dr. Jane Smith
- **Age**: 45
- **Occupation**: Professor at a university
- **Technology Proficiency**: Moderate (comfortable using online tools for teaching)
- **Goals**:
  - Create and manage courses
  - Assign and grade assignments
  - Interact with students and provide feedback
- **Pain Points**:
  - Inability to track student progress effectively
  - Complicated interfaces that slow down course management
  - Limited interaction with students in current systems

## Features
- User Authentication (Registration/Login)
- Course Management (Create, Manage, Enroll)
- Assignment Submission and Grading
- Notification System for Updates and Deadlines
- Admin and Instructor Dashboards

## Technologies
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Tools**: GitHub for version control, Heroku for deployment

## How to Run Locally
1. Clone this repository.
2. Navigate to the backend folder and install dependencies:
   ```bash
   pip install -r requirements.txt
