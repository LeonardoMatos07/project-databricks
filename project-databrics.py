import psycopg2
import re
from dotenv import load_dotenv
from collections import Counter

def get_country():
    """! Método conectar banco de dados
    """    
    load_dotenv()
    try:
        conn = psycopg2.connect(
            host='psql-mock-database-cloud.postgres.database.azure.com',
            database='ecom1689951132216tjuxokympmxdoryr',
            user='lairioimrapffuvvvemlellb@psql-mock-database-cloud',
            password='lflazvwgonwctugymsgyegmb'
        )
        sql = """select
                c.country
                from orders o
                inner join customers c on c.customer_number = o.customer_number
                where o.status = 'Cancelled'
            """ 
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()

        countrys = []
        for i in rows:
            countrys.append(i[0])

        contador = Counter(countrys)
        country, frequencia = contador.most_common(1)[0]    
        return country 
     
    except Exception as error:
        print("Erro ao conectar banco de dados.")


def get_line():
    """! Método conectar banco de dados
    """    
    load_dotenv()
    try:
        conn = psycopg2.connect(
            host='psql-mock-database-cloud.postgres.database.azure.com',
            database='ecom1689951132216tjuxokympmxdoryr',
            user='lairioimrapffuvvvemlellb@psql-mock-database-cloud',
            password='lflazvwgonwctugymsgyegmb'
        )
        sql = """select
                pd.product_line,
                p.buy_price
                from orders o
                inner join orderdetails od on o.order_number = od.order_number
                inner join products p on od.product_code = p.product_code
                inner join product_lines pd on pd.product_line = p.product_line
                where o.status = 'Shipped' and o.order_date::TEXT like '2005%'
            """ 
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        lines = []
        for i in rows:
            lines.append(i[0])

        contador = Counter(lines)
        line, frequencia = contador.most_common(1)[0]  

        value = 0
        for n in rows:
            if n[0] == line:
                value += float(n[1])  
        return line, value 
     
    except Exception as error:
        print("Erro ao conectar banco de dados.")
        
        
def get_employee():
    """! Método conectar banco de dados
    """    
    load_dotenv()
    try:
        conn = psycopg2.connect(
            host='psql-mock-database-cloud.postgres.database.azure.com',
            database='ecom1689951132216tjuxokympmxdoryr',
            user='lairioimrapffuvvvemlellb@psql-mock-database-cloud',
            password='lflazvwgonwctugymsgyegmb'
        )
        sql = """select 
                e.first_name,
                e.last_name,
                e.email
                from employees e
                inner join offices o on o.office_code = e.office_code
                where o.country = 'Japan'
            """ 
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()

        employees = []
        for i in rows:
        
            local_part, domain = re.match(r'(.+)@(.+)', i[2]).groups()
            masked_local_part = local_part[0] + '*' * (len(local_part) - 1)
            email = masked_local_part + domain

            employees.append(
                {   
                    "first_name": i[0],
                    "last_name": i[1],
                    "email": email
                }
            )
        return employees
     
    except Exception as error:
        print("Erro ao conectar banco de dados.")



employee = get_employee()
print(employee)    

line = get_line()
print("A linha mais vendida foi a " + line[0] + " com faturamento total de: $" + str(line[1]))    

country_repeat = get_country()
print("The country that had the most canceled orders was " + country_repeat)    
