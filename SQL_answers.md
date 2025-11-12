1) Return all orders for customer `C001`:

```sql
SELECT *
FROM Orders
WHERE CustomerId = 'C001';
```

2) Total order amount per customer:

```sql
SELECT CustomerId,
       SUM(Amount) AS TotalAmount
FROM Orders
GROUP BY CustomerId;
```
