#6. Principles of Data Manipulation and Management
## Data Models, Terminology
- how do we store data?
  - HDDs and SSDs - non-volatile storage
- What is the data model
  - how do we organize the data
    - tree like
    - rows and cols
    - spreadsheets - unstructured
- What is a data model?
  1. structures
  2. constraints
  3. operations
- Structures
  - rows/cols
  - nodes/edges
  - key-values
  - sequence of bytes - files
- Constraints
  - all rows have same number of cols
  - all vals in a col must be the same type
  - child cannot have two parents
- Operations
  - find the value x
  - find the rows where col x has val y
  - get the next N bytes, open/close
- What is a Database
  - collection of info organized to afford efficient retrieval
  - Another view by Jim Gray
    - data should be self-describing and it should have a schema

## From data models to databases
- Why would I want a database?
  - Sharing Data - support and interface for many users
  - Data Model Enforcement
    - ensure all application see clean, organized data
  - Scale
    - databases too large to fit into main memory
  - Flexibility
    - Use the data in new, unanticipated ways
- Questions to consider
  - how is the data physically organized on disk?
  - what kinds of queries are efficiently supported
    - reads vs writes - is the DB organized in a way to support the latency requirements
  - how to update or add new data
  - What happens if I encounter new queries that I didn't anticipate?

## Pre-Relational Databases
- Motivation of Relational Databases
- Historical Example: Network Database
    - file oriented 
    - allows for drill-down queries but not aggregated queries
      - adding fields requires reorganization of DB
    - different queries might need a duplicated but reorganized copy of the structure
- Hierarchical Database
  - IBM IMS system
  - Data organized as segments
  - you can change one segment without re-writing everything but the developer still needs to understand the Hierarchy
  - must anticipate the queries that will be asked

## Motivation Relational Databases
- build to use one set of data in multiple ways, including ways that we unforeseen at the time of creation
  - Everything is a table
  - Every row in the table has the same columns
  - relationships are implicit: no pointers
    - using shared ID
    - lookups of sharedID has worse performance over direct pointers but the time is consistent in either direction
  - everything is stored only once - not achieved with network DBs

## Relational Databases: key Ideas
- pre-relational: reorganization meant rebuilding application
- RDBMS were buggy and slow but required only 5% of the application code
- User/applications remain unaffected when the internal representation of the data is changed
- **Key Idea** Programs that manipulate tabular data exhibit and algebraic structure allowing reasoning and manipulation independently of the physical data representation
- Physical Data independence
  - we now manipulate the logical "table" as apposed to chasing pointers around
  - programs are more robust than without the rational model
- Algebra of Tables
  - Select, Project, join
  - queries written in terms of table operations
  - DB designers need only focus on implementing these operations

#7. Relational Algebra
## Algebraic Optimization Overview
- Algebraic laws (identity, distributive, commutative) can be use to simply expressions turing many operations into several.
- the same sort of optimization can be applied to tables increasing the query efficiency
- It is critical to not do things in the wrong order or un-needed work
- every query is rewritten using algebraic re-write rules
- attempt to minimize the cost of the expression
- conversely, optimizing map reduce is left up to the developer
- Algebraic Closure: every operation that applies to a table also returns a table
    - operations can be chained together

### Operators
  - union ∪   (222a)
  - intersection ∩ (2229)
  - difference - 
  - Selection σ (3c3)
  - Projection ∏ (220f)
  - Join ⋈ (22c8)
  - Extended RA
    - Duplicate elimination d
    - grouping and aggregation g
    - sorting t
  - Mainly: set operations + selection, projection, join

## RA Operators: Union, Difference, Selection
- Sets vs Bags
  - Sets - no duplicates
  - bags - duplicates allowed
- RA has 2 semantics
  - set semantics = standard RA
  - bag semantics = extended RA
- Rule of thumb
  - every paper will assume set semantics
  - every implementation will assume bag semantics

###Union
- R1 ∪ R2

```
SELECT * FROM R1
UNION
SELECT * FROM R2
```
- returns all data from R1 and R2 with duplicates between the 2 tables removed
- duplicates can be included by using ```UNION ALL```

###Difference
- R1 - R2

```
SELECT * FROM R1
EXCEPT
SELECT * FROM R2
```
- returns R1 with R2 values removed
- Intersection can be defined as difference
  - R1 ∩ R2 = R1 - (R1 - R2)
- Or as Join
  - R1 ∩ R2 = R1 ⋈ R2

###Selection
- Returns all tuples which satisfy a condition (c)
  - σ<sub>c</sub>(R)
- i.e.
  - σ<sub>Salary</sub> > 40000 (Employee)
  - σ<sub>Name</sub> = "Smith"(Employee)
- the condition c can be any equal/grater/less than condition, any boolean function, any arbitrary function that returns a boolean

