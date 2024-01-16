def get_columns_from_query(query:str):
    query = query.lower()
    query.removeprefix("create table")
    table_name = query.split("(")[0]
    query.removeprefix(table_name)
    query.removeprefix("(")
