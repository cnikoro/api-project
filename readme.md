# Technical Interview (Employee API Creation)

### Problem Statement

Create an employee management system with the ability to:
* Create an employee
* Get all employees
* Update an employee (protect route)
* Delete an employee

Add an image of your database schema and send the link to the test added to your github repo to career@rimotechnology.com

### Solution Description

Created two models (Employee and Department) with the following exposed end points:

*Employee Endpoints:*

* 'employee_list/': get all employees
* 'employee_detail/<emp_id>': get information about a single employee
* 'employee_create/': create an employee
* 'employee_update/<emp_id>': update information about an employee
* 'employee_delete/<emp_id>': delete an employee

*Department Endpoints:*

* 'department_list/': get all departments
* 'department_detail/<dep_id>': get information about a single department
* 'department_create/': create an department
* 'department_update/<dep_id>': update information about an department
* 'department_delete/<dep_id>': delete an department


*Couldn't figure out a way of protecting the update route*
