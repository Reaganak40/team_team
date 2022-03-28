-- Update 'numCheckins'
UPDATE Business
SET y_checkin_count = (SELECT COUNT(y_business_id) FROM Check_In WHERE Check_In.y_business_id = Business.y_business_id)
;

-- Update 'totalLikes'
UPDATE Users
SET y_tip_like_count = (SELECT COUNT(y_like_count) FROM Tip WHERE Tip.y_user_id = Users.y_user_id)
;

-- Update 'tipCount'
UPDATE Business
SET y_tip_count = (SELECT COUNT(y_business_id) FROM Tip WHERE Tip.y_business_id = Business.y_business_id)
;
