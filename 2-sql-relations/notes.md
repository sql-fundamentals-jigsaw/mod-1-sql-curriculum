Joining tables
  - how does a join/sql work and make queries
  - inner join
  - outer join

- Complex data model
  - Bar wants to keep track of the customers that bring in the most revenue, and the bartenders that bring in the most revenue.  It also wants to keep track of the cost of each drink - which will be calculated by adding each drink's ingredients.
  As a bonus, also consider how we would structure the tables if we want to keep track of what orders are on what receipt.
  How do we model these tables?


bart simpson ordered a milk shake (vanilla ice) from patty
lisa simpson ordered a rootbeer float (vanilla ice) from moe

Remembering the relationships strategies
School

Teacher

Students

Course

Classrooms

1. Describe the relationships
  a. start with the belongs to
  b. then do the inverse
  - Teacher has many students, through the course
  - Teacher belongs_to school
  - School has many teachers
  - Student belongs_to a course
  - course has_many students
  - teacher has many classrooms
  - classroom has many teachers
  - teacher belongs to a course
  - course has many teachers

2. Make a visual representation

 - Unified Modeling Language
  ____
  |  course | --<
  _____


3. Translate to excel

Rules
  1. Belongs to always gets the foreign key
  2. has many never gets the foreign key
  3. many to many -> separate joins table

II.






- has many through
- aggregate functions
  - sum, count
  - group by
  - order by and having


INNER Join followed by, and then have a secondary join
GROUP BY multiple arguments


Feedback
  In the code along, indicate how many files you need
