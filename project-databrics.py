import psycopg2
import re
from collections import Counter
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

def get_country():
    """! Método para obter país com maior quantidade de pedidos cancelados
    """    
    try:
        sql = """select
                c.country
                from orders o
                inner join customers c on c.customer_number = o.customer_number
                where o.status = 'Cancelled'
            """ 
        cur = connect()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()

        countrys = []
        for i in rows:
            countrys.append(i[0])

        contador = Counter(countrys)
        country, frequencia = contador.most_common(1)[0]

        data = [(country,)]
        schema = StructType([
            StructField("country", StringType(), True)
        ])
        save_delta(data=data, schema=schema)  

        return country 
     
    except Exception as error:
        print("Erro ao obter informações.")

def get_line():
    """! Método para obter informações de linha de produto
    """    
    try:
        sql = """select
                pd.product_line,
                p.buy_price
                from orders o
                inner join orderdetails od on o.order_number = od.order_number
                inner join products p on od.product_code = p.product_code
                inner join product_lines pd on pd.product_line = p.product_line
                where o.status = 'Shipped' and o.order_date::TEXT like '2005%'
            """ 
        cur = connect()
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

        data = [(line, value)]
        schema = StructType([
            StructField("linha", StringType(), True),
            StructField("faturamento", StringType(), True)
        ])
        save_delta(data=data, schema=schema)  
        
        return line, value 
     
    except Exception as error:
        print("Erro ao obter informações")

def get_employees():
    """! Método para obter informações de vendedores
    """    
    try:
    
        sql = """select 
                e.first_name,
                e.last_name,
                e.email
                from employees e
                inner join offices o on o.office_code = e.office_code
                where o.country = 'Japan'
            """ 
        cur = connect()
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()

        employees = []
        values = []
        for i in rows:
        
            local_part, domain = re.match(r'(.+)@(.+)', i[2]).groups()
            masked_local_part = local_part[0] + '*' * (len(local_part) - 1)
            email = masked_local_part + domain
            values.append((i[0], i[1], email))

            employees.append(
                {   
                    "first_name": i[0],
                    "last_name": i[1],
                    "email": email
                }
            )
        data = values
        schema = StructType([
            StructField("first_name", StringType(), True),
            StructField("last_name", StringType(), True),
            StructField("email", StringType(), True)
        ])
        save_delta(data=data, schema=schema)      
        return employees
     
    except Exception as error:
        print("Erro ao obter informações de vendedores.")

def connect():
    """! Método para conectar banco de dados
    """    
    try:
        conn = psycopg2.connect(
            host='psql-mock-database-cloud.postgres.database.azure.com',
            database='ecom1689951132216tjuxokympmxdoryr',
            user='lairioimrapffuvvvemlellb@psql-mock-database-cloud',
            password='lflazvwgonwctugymsgyegmb'
        )

        cur = conn.cursor()
        return cur
     
    except Exception as error:
        print("Erro ao conectar banco de dados.")

def save_delta(data, schema):
    """! Método para salvar dados
    """    
    try:
        spark = SparkSession.builder.appName("Salvando em Delta").getOrCreate()
        df = spark.createDataFrame(data, schema)
        caminho_delta = "/delta-table"
        spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")
        df.write.format("delta").mode("append").save(caminho_delta)

    except Exception as error:
        print("Erro ao salvar dados. " + str(error))

country_repeat = get_country()
print("O país com maior número de itens cancelados foi: " + country_repeat)    

line = get_line()
print("A linha mais vendida foi a " + line[0] + " com faturamento total de: $" + str(line[1]))   

employees = get_employees()
print("Informações de vendedores do Japão: ")
for i in employees:
    print(i)
 
print("Os valores foram salvos em formato Delta.")

