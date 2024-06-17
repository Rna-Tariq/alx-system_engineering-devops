Postmortem: June 15, 2024, Web Application Outage
Issue Summary

Duration:
June 15, 2024, from 10:00 AM to 12:30 PM UTC

Impact:
Our e-commerce platform experienced a significant slowdown, with page load times increasing from an average of 1.2 seconds to over 15 seconds. Approximately 75% of users were affected, leading to a 60% drop in transactions during the outage period.

Root Cause:
The root cause was an unoptimized database query that resulted in a sudden spike in CPU and memory usage on the primary database server.

Timeline

10:00 AM UTC - Issue detected via monitoring alert indicating high database CPU usage.
10:05 AM UTC - Initial investigation by on-call engineer who confirmed the high CPU usage on the primary database server.
10:15 AM UTC - Misleading debugging path: suspected DDoS attack due to unusual traffic patterns.
10:30 AM UTC - Network team engaged to investigate potential DDoS attack.
10:45 AM UTC - Determined traffic was normal; focus shifted back to the database.
11:00 AM UTC - Database team identified a slow-running query introduced in the latest deployment.
11:15 AM UTC - Escalated to development team responsible for the latest deployment.
11:30 AM UTC - Code rollback initiated to previous stable version.
12:00 PM UTC - Rollback completed; database performance began to stabilize.
12:30 PM UTC - Monitoring confirmed that system performance returned to normal.
Root Cause and Resolution

Root Cause:
The issue was caused by an unoptimized database query introduced during a code deployment the previous night. The query involved multiple complex joins and lacked proper indexing, causing a significant increase in CPU and memory usage on the primary database server when executed.

Resolution:
The incident was resolved by rolling back the deployment to the previous stable version of the application. This rollback removed the problematic query, allowing the database performance to return to normal. A follow-up investigation identified the specific query, and it was optimized by adding appropriate indexes and simplifying the join operations.

Corrective and Preventative Measures

Improvements/Fixes:

Enhance code review process to include database query optimization checks.
Implement additional monitoring to detect and alert on slow queries.
Improve deployment procedures to include performance testing for database queries.
Tasks:

Patch Database Server: Update database indexing and optimize existing queries.
Enhance Monitoring: Implement monitoring for slow queries and high CPU usage on the database server.
Review Code Deployment Procedures: Ensure performance testing for database queries is part of the deployment pipeline.
Training: Conduct training sessions for developers on writing optimized database queries.
Create Incident Response Playbook: Develop a detailed incident response plan for database performance issues.
By implementing these measures, we aim to prevent similar issues in the future and ensure a more robust and reliable e-commerce platform.
