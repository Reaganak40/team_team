-- Update 'numCheckins'
UPDATE Business
SET y_checkin_count = (SELECT COUNT(y_business_id) FROM Check_In WHERE Check_In.y_business_id = Business.y_business_id)
;

-- Update 'totalLikes'
UPDATE Users
SET y_tip_like_count = (SELECT u2.total_like_count
FROM
(SELECT Users.y_user_id, coalesce(u1.total_like_count, 0) as total_like_count
FROM Users
LEFT OUTER JOIN
(SELECT y_user_id, SUM(y_like_count) as total_like_count
FROM Tip
GROUP BY y_user_id) as u1
ON Users.y_user_id = u1.y_user_id) as u2 WHERE Users.y_user_id = u2.y_user_id)
;

-- Update 'tipCount'
UPDATE Users
SET y_tip_count = (SELECT COUNT(y_user_id) FROM Tip WHERE Tip.y_user_id = Users.y_user_id)
;


