from config.app import *
import pandas as pd

def GenerateReportVentas(app:App):
    conn=app.bd.getConection()
    query="""
        SELECT 
            p.pais,
            v.product_id,
            SUM(v.quantity) AS total_vendido
        FROM 
            VENTAS v
        JOIN 
            POSTALCODE p
        ON 
            v.postal_code = p.code
        GROUP BY 
            p.pais, v.product_id
        ORDER BY 
            total_vendido ASC;
    """
    df=pd.read_sql_query(query,conn)
    fecha="16-Febrero"
    path=f"/workspaces/PRACTICAS/Proyecto/files/Data-{fecha}.csv"
    df.to_csv(path)
    sendMail(app,path)

def sendMail(app:App,data):
    app.mail.send_email('from@example.com','Reporte - Datux','Reporte - Datux',data)