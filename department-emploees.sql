SELECT DEPARTMENT.NAME, COUNT(EMPLOYEE.ID) as employee_count
FROM DEPARTMENT
LEFT JOIN EMPLOYEE ON DEPARTMENT.ID = EMPLOYEE.DEPT_ID
GROUP BY DEPARTMENT.NAME
ORDER BY COUNT(EMPLOYEE.ID) DESC, DEPARTMENT.NAME ASC;


SELECT DEPARTMENT.NAME, COUNT(EMPLOYEE.ID) as employee_count
FROM DEPARTMENT
LEFT OUTER JOIN EMPLOYEE ON DEPARTMENT.ID = EMPLOYEE.DEPT_ID
GROUP BY DEPARTMENT.NAME
ORDER BY COUNT(EMPLOYEE.ID) DESC, DEPARTMENT.NAME ASC;
