SELECT c.login,
       COUNT(o.id) AS deliveryCount
FROM "Couriers" c
JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = TRUE
GROUP BY c.login;