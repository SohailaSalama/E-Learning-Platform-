-- Users table (for students, instructors, and admins)
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL CHECK (role IN ('student', 'instructor', 'admin')),
    name VARCHAR(255) NOT NULL
);

-- Courses table
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    instructor_id INT REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Assignments table
CREATE TABLE Assignments (
    assignment_id SERIAL PRIMARY KEY,
    course_id INT REFERENCES Courses(course_id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    due_date DATE NOT NULL
);

-- Submissions table
CREATE TABLE Submissions (
    submission_id SERIAL PRIMARY KEY,
    assignment_id INT REFERENCES Assignments(assignment_id) ON DELETE CASCADE,
    student_id INT REFERENCES Users(user_id) ON DELETE CASCADE,
    file_path VARCHAR(255) NOT NULL,
    submission_date TIMESTAMP NOT NULL,
    grade INT,
    feedback TEXT
);

-- Enrollments table
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES Users(user_id) ON DELETE CASCADE,
    course_id INT REFERENCES Courses(course_id) ON DELETE CASCADE,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Notifications table
CREATE TABLE Notifications (
    notification_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(user_id) ON DELETE CASCADE,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- progressTracker table
CREATE TABLE ProgressTracker (
    progress_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES Users(user_id) ON DELETE CASCADE,
    course_id INT REFERENCES Courses(course_id) ON DELETE CASCADE,
    completion_percentage INT CHECK (completion_percentage BETWEEN 0 AND 100)
);
