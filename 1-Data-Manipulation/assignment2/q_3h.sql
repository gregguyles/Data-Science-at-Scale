SELECT sum(term_prod) AS similarity
FROM (
    SELECT a.docid AS docid_a, 
           b.docid AS docid_b,
           a.term AS term, 
           a.count * b.count AS term_prod
    FROM (
        SELECT docid, term, count
        FROM Frequency
        ) AS a
        , (
        SELECT docid, term, count
        FROM Frequency
        ) AS b
    WHERE a.term = b.term 
    AND a.docid = '10080_txt_crude'
    AND b.docid = '17035_txt_earn'
)
GROUP BY docid_a, docid_b
;
