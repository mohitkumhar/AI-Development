-- DISTINCT
-- ==========
SELECT location FROM student;  -- this will print all the location column data from the table

SELECT DISTINCT location FROM student;  -- this will remove the duplicate data and then print data

SELECT DISTINCT source_of_joining;


-- ORDER BY
-- ==========
 -- use to print data in any specific order
 
 SELECT student_id, enrollment_date, selected_course, student_fname, years_of_exp, student_company, batch_date, source_of_joining, location FROM student ORDER BY years_of_exp;
 
 SELECT student_fname FROM student ORDER BY student_fname;

-- to sort data in descending order ise desc
SELECT student_fname FROM student ORDER BY student_fname DESC;

-- sort according to number of column that is goinf to be printed
SELECT student_fname, years_of_exp FROM student ORDER BY 1 DESC;   -- this will sort accordint o student_fname

SELECT student_fname, years_of_exp FROM student ORDER BY student_fname, location;   -- this will first sort according to student_fname and then location 


-- LIMIT
-- ========

SELECT * FROM student LIMIT 3;

-- get 3 candidate with least experience
SELECT * FROM student ORDER BY years_of_exp LIMIT 3;


-- from which sources last 5 candidate have enrolled
SELECT source_of_joining FROM student ORDER BY enrollment_date LIMIT 5;

-- last student who enrolled
SELECT student_fname FROM student ORDER BY enrollment_date DESC LIMIT 0,3;
SELECT student_fname FROM student ORDER BY enrollment_date DESC LIMIT 3,2;



-- LIKE
-- =======
SELECT student_fname FROM student WHERE student_fname LIKE '%ra%'; -- print all the name where ra in present in their name
SELECT student_fname FROM student WHERE student_fname LIKE 'ra%'; -- print all the name is starting from ra
SELECT student_fname FROM student WHERE student_fname LIKE '%ha'; -- print all the name which ends with ha

-- what if student name has percentage character
SELECT student_fname FROM student WHERE student_fname LIKE '%\%it'; -- this will print any name which ends with %it

-- % is a wildcard character


SELECT student_fname FROM student WHERE student_fname LIKE '_____'; -- print all the name which has 5 letters (it depends on the number of underscore(_) )
-- _ is also a wildcard character













INSERT INTO student (student_fname, student_lname, student_mname, student_email, student_phone, student_alternate_phone, enrollment_date, selected_course, years_of_exp, student_company, batch_date, source_of_joining, location)
VALUES
('Moh%it', 'Kumhar', 'A', 'mohitmolela#gmail.com', '1234567890', '0987654321', '2024-01-01 10:00:00', 1, 2, 'Tech Solutions India', '2024-05-01', 'Website', 'Mumbai');
('Priya', 'Sharma', 'B', 'priya.sharma@example.com', '2345678901', '9876543210', '2024-01-02 11:00:00', 2, 3, 'Indian IT Innovations', '2024-05-01', 'Referral', 'Bangalore'),
('Amit', 'Singh', 'C', 'amit.singh@example.com', '3456789012', '8765432109', '2024-01-03 12:00:00', 3, 1, 'TechCorp India', '2024-05-01', 'Advertisement', 'New Delhi'),
('Sneha', 'Gupta', 'D', 'sneha.gupta@example.com', '4567890123', '7654321098', '2024-01-04 13:00:00', 1, 4, 'Software Solutions India', '2024-05-01', 'Friend', 'Hyderabad'),
('Vikram', 'Yadav', 'E', 'vikram.yadav@example.com', '5678901234', '6543210987', '2024-01-05 14:00:00', 2, 2, 'Indian Tech Services', '2024-05-01', 'Advertisement', 'Chennai'),
('Ananya', 'Das', 'F', 'ananya.das@example.com', '6789012345', '5432109876', '2024-01-06 15:00:00', 3, 3, 'IndiaSoft', '2024-05-01', 'Website', 'Kolkata'),
('Aarav', 'Jain', 'G', 'aarav.jain@example.com', '7890123456', '4321098765', '2024-01-07 16:00:00', 1, 1, 'TechGenius India', '2024-05-01', 'Advertisement', 'Pune'),
('Riya', 'Choudhury', 'H', 'riya.choudhury@example.com', '8901234567', '3210987654', '2024-01-08 17:00:00', 2, 2, 'Indian IT Solutions', '2024-05-01', 'Friend', 'Ahmedabad'),
('Rahul', 'Mishra', 'I', 'rahul.mishra@example.com', '9012345678', '2109876543', '2024-01-09 18:00:00', 3, 3, 'TechWorld India', '2024-05-01', 'Referral', 'Jaipur'),
('Neha', 'Gandhi', 'J', 'neha.gandhi@example.com', '0123456789', '1098765432', '2024-01-10 19:00:00', 1, 4, 'Indian Innovations', '2024-05-01', 'Advertisement', 'Lucknow'),
('Aarav', 'Patil', 'K', 'aarav.patil@example.com', '1234509876', '5432198760', '2024-01-20 20:00:00', 3, 2, 'India IT Solutions', '2024-05-01', 'Advertisement', 'Nagpur'),
('Isha', 'Reddy', 'L', 'isha.reddy@example.com', '2345610987', '6543219870', '2024-01-21 21:00:00', 1, 3, 'TechIndia', '2024-05-01', 'Website', 'Indore'),
('Arjun', 'Kumar', 'M', 'arjun.kumar@example.com', '3456721098', '7654320981', '2024-01-22 22:00:00', 2, 1, 'Indian IT Hub', '2024-05-01', 'Referral', 'Chandigarh'),
('Sanvi', 'Shah', 'N', 'sanvi.shah@example.com', '4567832109', '8765432101', '2024-01-23 23:00:00', 3, 4, 'TechIndia Solutions', '2024-05-01', 'Friend', 'Visakhapatnam'),
('Advik', 'Joshi', 'O', 'advik.joshi@example.com', '5678943210', '9876543210', '2024-01-24 00:00:00', 1, 2, 'Indian Tech Innovations', '2024-05-01', 'Advertisement', 'Surat'),
('Prisha', 'Verma', 'P', 'prisha.verma@example.com', '6789054321', '0987654321', '2024-01-25 01:00:00', 2, 3, 'TechGenius India', '2024-05-01', 'Website', 'Bhopal'),
('Kabir', 'Sharma', 'Q', 'kabir.sharma@example.com', '7890165432', '1098765432', '2024-01-26 02:00:00', 3, 1, 'Indian Innovations', '2024-05-01', 'Referral', 'Patna')