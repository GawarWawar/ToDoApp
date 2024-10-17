-- 1. get all statuses, not repeating, alphabetically ordered
SELECT DISTINCT status
FROM tasks
ORDER BY status ASC;

SELECT '';
-- 2. Get the count of all tasks in each project, order by tasks count descending
SELECT projects.name, COUNT(tasks.id) AS task_count
FROM projects
LEFT JOIN tasks ON projects.id = tasks.project_id
GROUP BY projects.name
ORDER BY task_count DESC;

SELECT '';
-- 3. get the count of all tasks in each project, order by projects names
SELECT projects.name, COUNT(tasks.id) AS task_count
FROM projects
LEFT JOIN tasks ON projects.id = tasks.project_id
GROUP BY projects.name
ORDER BY projects.name ASC;

SELECT '';
-- 4. get the tasks for all projects having the name beginning with "N" letter
SELECT tasks.*
FROM tasks
JOIN projects ON tasks.project_id = projects.id
WHERE projects.name LIKE 'N%';

-- 5. get the list of al projects containing the 'a' letter in the middle of the name, and show the tasks count near each project. 
-- Mention that there can exist projects without tasks and tasks with project_id= NULL
SELECT projects.name, COUNT(tasks.id) AS task_count
FROM projects
LEFT JOIN tasks ON projects.id = tasks.project_id
WHERE projects.name LIKE '%a%'
GROUP BY projects.name;

-- 6. get the list of tasks with duplicate names. Order alphabetically
SELECT name
FROM tasks
GROUP BY name
HAVING COUNT(*) > 1
ORDER BY name ASC;

SELECT '';
-- 7. get the list of tasks having several exact matches of both name and status, from the project 'Delivery’. Order by matches count
SELECT tasks.name, tasks.status, COUNT(*) AS match_count
FROM tasks
JOIN projects ON tasks.project_id = projects.id
WHERE projects.name = 'Delivery'
GROUP BY tasks.name, tasks.status
HAVING COUNT(*) > 1
ORDER BY match_count DESC;

SELECT '';
-- 8. get the list of project names having more than 10 tasks in status 'completed'. Order by project_id
SELECT projects.name
FROM projects
JOIN tasks ON projects.id = tasks.project_id
WHERE tasks.status = 'completed'
GROUP BY projects.id, projects.name
HAVING COUNT(tasks.id) > 10
ORDER BY projects.id ASC;

SELECT '';
