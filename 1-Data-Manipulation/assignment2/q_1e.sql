SELECT count(*) FROM (
    SELECT docid, count(term)
    FROM frequency
    GROUP BY docid
    HAVING count(term) > 300
)    
;
