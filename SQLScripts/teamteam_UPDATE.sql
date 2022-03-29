-- Update 'numCheckins'
UPDATE Business
SET y_checkin_count = (SELECT COUNT(y_business_id) FROM Check_In WHERE Check_In.y_business_id = Business.y_business_id)
;

-- Update 'numTips'
UPDATE Business
SET y_tip_count = (SELECT b2.t_count FROM (SELECT Business.y_business_id, coalesce(b1.t_count, 0) as t_count
FROM Business 
LEFT OUTER JOIN 
(SELECT y_business_id, COUNT(y_business_id) as t_count
FROM Tip 
GROUP BY y_business_id ) AS b1 
ON Business.y_business_id = b1.y_business_id) AS b2 WHERE b2.y_business_id = Business.y_business_id)
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

