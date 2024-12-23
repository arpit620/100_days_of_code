mean_volume AS (

    SELECT 
        user_id,
        (email_volume_day_minus_1 + email_volume_day_minus_2) / 2.0 AS mean_volume_last_2_days,

                    (ARRAY_SLICE(ARRAY_SORT(ARRAY_CONSTRUCT(email_volume_day_minus_1 , email_volume_day_minus_2 , email_volume_day_minus_3 , 
         email_volume_day_minus_4 , email_volume_day_minus_5 , email_volume_day_minus_6 , 
         email_volume_day_minus_7 , email_volume_day_minus_8 , email_volume_day_minus_9 , 
         email_volume_day_minus_10 , email_volume_day_minus_11 , email_volume_day_minus_12 , 
         email_volume_day_minus_13 , email_volume_day_minus_14)), 
                        (ARRAY_SIZE(ARRAY_CONSTRUCT(email_volume_day_minus_1 , email_volume_day_minus_2 , email_volume_day_minus_3 , 
         email_volume_day_minus_4 , email_volume_day_minus_5 , email_volume_day_minus_6 , 
         email_volume_day_minus_7 , email_volume_day_minus_8 , email_volume_day_minus_9 , 
         email_volume_day_minus_10 , email_volume_day_minus_11 , email_volume_day_minus_12 , 
         email_volume_day_minus_13 , email_volume_day_minus_14)) / 2) - 1, 
                        1)[0] + 
             ARRAY_SLICE(ARRAY_SORT(ARRAY_CONSTRUCT(email_volume_day_minus_1 , email_volume_day_minus_2 , email_volume_day_minus_3 , 
         email_volume_day_minus_4 , email_volume_day_minus_5 , email_volume_day_minus_6 , 
         email_volume_day_minus_7 , email_volume_day_minus_8 , email_volume_day_minus_9 , 
         email_volume_day_minus_10 , email_volume_day_minus_11 , email_volume_day_minus_12 , 
         email_volume_day_minus_13 , email_volume_day_minus_14)), 
                        (ARRAY_SIZE(ARRAY_CONSTRUCT(email_volume_day_minus_1 , email_volume_day_minus_2 , email_volume_day_minus_3 , 
         email_volume_day_minus_4 , email_volume_day_minus_5 , email_volume_day_minus_6 , 
         email_volume_day_minus_7 , email_volume_day_minus_8 , email_volume_day_minus_9 , 
         email_volume_day_minus_10 , email_volume_day_minus_11 , email_volume_day_minus_12 , 
         email_volume_day_minus_13 , email_volume_day_minus_14)) / 2), 
                        1)[0]) / 2 as mean_volume_14_days
  
    FROM grouped_counts