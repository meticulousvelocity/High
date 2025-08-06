INSERT INTO ticket_staff (id, count)
VALUES (?, 1)
ON CONFLICT(id) DO UPDATE SET count = count + 1
