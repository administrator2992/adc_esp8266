from db import get_db

# menambahkan data adc
def insert_adc(adc):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO adc_table(adc) VALUES (?)"
    cursor.execute(query, [adc])
    db.commit()
    return True