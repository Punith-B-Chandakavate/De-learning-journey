"""
You work as a data engineer for a top-tier technology company. 
You are given an employee_salaries table with the columns employee_id, employee_name, department, and salary. 
Your task is to find the third-highest salary in each department and return all employees who earn that salary.
Exclude departments that have fewer than three distinct salary values.


Return the following columns in the output: emp_id, name, department, salary.

Assumptions:
- The employees_salaries table includes emp_id, name, department, and salary.
- Departments with fewer than 3 distinct salary values should be excluded.
- Ranking is based on salary in descending order.

Sample Input:
employee_id	employee_name	department	salary
1014	Pooja	Support	37372
1023	Rohan	Marketing	56022
1032	Manish	Engineering	132653
1048	Sunita	Finance	70986
1061	Priya	HR	67750

Sample Output:
emp_id	name	department	salary
1107	Neha	Sales	78942
1128	Vikram	IT	111311
1137	Arjun	Finance	68916
1154	Sanjay	Engineering	115420
1199	Karan	Marketing	54695

Explanation:
Calculate the rank of every employee’s salary within their department in descending order.
All employees with the third-highest salary (rank = 3) in their department are selected.
Departments having fewer than 3 distinct salary values are excluded from results to ensure the third-highest-salary concept is meaningful.
The result includes multiple employees within the same department if there are salary ties.

"""
select 
    emp_id,
    name,
    department,
    salary
from(
select 
    employee_id as emp_id,
    employee_name as name,
    department,
    salary,
    dense_rank() over (partition by department order by salary desc) as rnk
from employee_salaries) as t
where rnk = 3



"""You are analyzing user login behavior for a software platform. 
The user_logins table records user_id and login_date. 
Your task is to find each user's longest consecutive login streak, returning its user_id, start_date, end_date, and streak_length.

Assumptions:
- The table user_logins stores daily login events per user.
- Consecutive logins are continuous days without gaps.
- The longest streak per user is the maximum number of consecutive login days.
- If multiple longest streaks exist, return any one.

Sample Input:
user_id	login_date
user_31	2025-09-18
user_4	2025-10-11
user_5	2025-10-01
user_41	2025-09-10
user_31	2025-09-09

Sample Output:
user_id	start_date	end_date	streak_length
user_31	2025-09-07	2025-09-15	9
user_4	2025-10-01	2025-10-06	6
user_5	2025-09-20	2025-09-28	9

Explanation:
Identify consecutive login days for each user.
Calculate the length of each consecutive streak.
Return the longest streak's start date, end date, and length per user.
If multiple longest streaks per user exist, return any one.

"""
WITH NumberedLogins AS (
    SELECT
        user_id,
        login_date,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) AS seq_num
    FROM user_logins
),
ConsecutiveGroups AS (
    SELECT
        user_id,
        login_date,
        DATE_SUB(login_date, INTERVAL seq_num DAY) AS grp
    FROM NumberedLogins
),
Streaks AS (
    SELECT
        user_id,
        MIN(login_date) AS start_date,
        MAX(login_date) AS end_date,
        COUNT(*) AS streak_length
    FROM ConsecutiveGroups
    GROUP BY user_id, grp
),
LongestStreaks AS (
    SELECT
        user_id,
        start_date,
        end_date,
        streak_length,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY streak_length DESC, start_date) AS rnk
    FROM Streaks
)
SELECT
    user_id,
    start_date,
    end_date,
    streak_length
FROM LongestStreaks
WHERE rnk = 1;

"""
You are a data engineer at a retail analytics company. 
Using the transactions table, which contains user_id, tx_date, and amount, identify user cohorts based on their first transaction month and calculate their weekly retention rate.For each cohort (signup month), show the percentage of active users per week since signup (Week 0, Week 1, Week 2, etc.). Return signup_month, W0, W1, W2, W3, W4, W5(with 2 decimals). 


Display the results ordered by signup_month Desc.

Assumptions:
- The transactions table contains user_id, tx_date, and amount.
- Each user’s first transaction month defines their cohort (signup month).
- Weeks are calculated relative to the signup month start date.
- Retention percentage shows the share of cohort users active in each week.
- Week 0 represents the signup week; later weeks increase sequentially.

Sample Input:
user_id	tx_date	amount
user_132	2025-06-14	265.34
user_27	2025-06-03	154.92
user_79	2025-07-30	48.17
user_105	2025-06-23	75.43
user_86	2025-06-15	210.88

Sample Output:
signup_month	W0	    W1	    W2	    W3	    W4	    W5
2025-09	        100.0	59.12	43.59	25.34	12.68	6.79
2025-08	        100.0	50.25	32.25	18.75	10.0	5.0
2025-07	        100.0	45.80	29.85	17.42	8.09	4.05
2025-06	        100.0	52.22	35.37	22.67	11.20	5.60
2025-05	        100.0	48.67	30.15	17.01	9.08	4.55

Explanation:
Assign each user to a signup month cohort based on their signup date.
Calculate the week number for each transaction relative to the signup month start.
Count unique active users per signup cohort per week.
Calculate retention percentages by dividing active users by cohort size.
Pivot retention percentages to form a cohort retention table with weeks as columns.
"""
WITH first_tx AS (
    SELECT
        user_id,
        MIN(tx_date) AS first_tx_date
    FROM transactions
    GROUP BY user_id
),
cohort_data AS (
    SELECT
        t.user_id,
        DATE_FORMAT(f.first_tx_date, '%Y-%m') AS signup_month,
        f.first_tx_date,
        t.tx_date,
        FLOOR(DATEDIFF(t.tx_date, f.first_tx_date) / 7) AS week_number
    FROM transactions t
    JOIN first_tx f ON t.user_id = f.user_id
    WHERE t.tx_date >= f.first_tx_date
),
cohort_counts AS (
    SELECT
        signup_month,
        COUNT(DISTINCT user_id) AS total_users
    FROM cohort_data
    WHERE week_number = 0
    GROUP BY signup_month
),
weekly_retention AS (
    SELECT
        signup_month,
        week_number,
        COUNT(DISTINCT user_id) AS active_users
    FROM cohort_data
    GROUP BY signup_month, week_number
)
SELECT
    w.signup_month,
    ROUND(100 * MAX(CASE WHEN week_number = 0 THEN active_users END) / c.total_users, 2) AS W0,
    ROUND(100 * MAX(CASE WHEN week_number = 1 THEN active_users END) / c.total_users, 2) AS W1,
    ROUND(100 * MAX(CASE WHEN week_number = 2 THEN active_users END) / c.total_users, 2) AS W2,
    ROUND(100 * MAX(CASE WHEN week_number = 3 THEN active_users END) / c.total_users, 2) AS W3,
    ROUND(100 * MAX(CASE WHEN week_number = 4 THEN active_users END) / c.total_users, 2) AS W4,
    ROUND(100 * MAX(CASE WHEN week_number = 5 THEN active_users END) / c.total_users, 2) AS W5
FROM weekly_retention w
JOIN cohort_counts c ON w.signup_month = c.signup_month
GROUP BY w.signup_month
ORDER BY w.signup_month DESC;