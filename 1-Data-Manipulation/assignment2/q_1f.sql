SELECT count(*) FROM(
    SELECT * FROM
        (SELECT docid, term
        FROM frequency
        WHERE term = 'transactions') AS t
    JOIN 
        (SELECT docid, term
        FROM frequency
        WHERE term = 'world') AS w
    ON  t.docid = w.docid
)
;
