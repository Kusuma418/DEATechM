SELECT * FROM EXTERNAL_QUERY("projects/da-project-457709/locations/us/connections/bank-failed-transaction", "SELECT * FROM failed_transactions;");

-- Total Number of Failed Transactions
SELECT COUNT(*) AS total_failed_transactions
FROM EXTERNAL_QUERY("projects/da-project-457709/locations/us/connections/bank-failed-transaction", "SELECT * FROM failed_transactions;");

-- Failed Transactions by City
SELECT city, COUNT(*) AS failed_count
FROM EXTERNAL_QUERY("projects/da-project-457709/locations/us/connections/bank-failed-transaction", "SELECT * FROM failed_transactions;")
GROUP BY city
ORDER BY failed_count DESC;

-- Top 5 Branches with Most Failures
SELECT branch_name, city, COUNT(*) AS failed_count
FROM EXTERNAL_QUERY("projects/da-project-457709/locations/us/connections/bank-failed-transaction", "SELECT * FROM failed_transactions;")
GROUP BY branch_name, city
ORDER BY failed_count DESC
LIMIT 5;

-- common error messages and their frequencies
SELECT error_message, COUNT(*) AS count
FROM EXTERNAL_QUERY("projects/da-project-457709/locations/us/connections/bank-failed-transaction", "SELECT * FROM failed_transactions;")
WHERE error_message IS NOT NULL AND error_message != ''
GROUP BY error_message
ORDER BY count DESC;

-- Failed Transactions By Type
SELECT transaction_type, COUNT(*) AS failed_count
FROM EXTERNAL_QUERY("projects/da-project-457709/locations/us/connections/bank-failed-transaction", "SELECT * FROM failed_transactions;")
GROUP BY transaction_type
ORDER BY failed_count DESC;

-- Customers with Multiple Failures
SELECT customer_id, COUNT(*) AS failed_count
FROM EXTERNAL_QUERY("projects/da-project-457709/locations/us/connections/bank-failed-transaction", "SELECT * FROM failed_transactions;")
GROUP BY customer_id
HAVING failed_count > 1
ORDER BY failed_count DESC;

-- Failed Transactions Over Time(By Date)
SELECT transaction_date, COUNT(*) AS daily_failures
FROM EXTERNAL_QUERY("projects/da-project-457709/locations/us/connections/bank-failed-transaction", "SELECT * FROM failed_transactions;")
GROUP BY transaction_date
ORDER BY transaction_date;


-- Branch-Customer Error Correlation
-- Shows how many unique customers failed per branch — helpful in visual fraud hotspots.
SELECT 
  branch_name,
  COUNT(DISTINCT customer_id) AS unique_failed_customers
FROM EXTERNAL_QUERY("projects/da-project-457709/locations/us/connections/bank-failed-transaction", "SELECT * FROM failed_transactions;")
GROUP BY branch_name
ORDER BY unique_failed_customers DESC;

-- Error Message Clustering
-- Tells Which errors are most frequent
SELECT 
  error_message,
  COUNT(*) AS frequency
FROM EXTERNAL_QUERY("projects/da-project-457709/locations/us/connections/bank-failed-transaction", "SELECT * FROM failed_transactions;")
WHERE error_message IS NOT NULL AND error_message != ''
GROUP BY error_message
ORDER BY frequency DESC;









