import psycopg2
import psycopg2.extras



class pg_connect():
    def dict_gen(self,curs):
        ''' From Python Essential Reference by David Beazley
        '''
        import itertools
        field_names = [d[0].lower() for d in curs.description]
        while True:
            rows = curs.fetchmany()
            if not rows: return
            for row in rows:
                yield dict(itertools.izip(field_names, row))
    
    def __init__(self,host,port,username,password,database):
        self.conn = psycopg2.connect(database=database, user=username,
                                password=password, host=host,
                                port=port)
        self.cursor = self.conn.cursor()

    def get_all_table(self):
        
        self.cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        self.tables = []
        for table in self.cursor.fetchall():
            self.tables.append(table[0])
            
        return self.tables

    def get_table_coulumns(self,table_name):
        self.cursor.execute("Select * FROM %s" % (table_name))
        colnames = [desc[0] for desc in self.cursor.description]
        return colnames
    
    
    def get_table_values(self,table_name,query=None):
        
        cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if query:
            pass
        else:
            cur.execute("Select * FROM %s" % (table_name))
        ans =cur.fetchall()
        ans1 = []
        for row in ans:
            ans1.append(dict(row))
        
        print ans1  #act\ally it's return
        


    
        
