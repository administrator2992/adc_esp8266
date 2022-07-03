from db import get_db

# ambil semua data adc
def get_adc():
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT * FROM adc_table"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row))) #konversi ke dictionary
        
    return result