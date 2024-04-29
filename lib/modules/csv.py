from csv import writer
import os

def delete_old_report(path:str):
    try:
        os.remove(path)
    except OSError:
        pass

def write_csv_bulk(data:list[list[str]], path:str):
    with open(path, 'a', newline='') as f_object:
        writer_object = writer(f_object)
        for x in data:
            writer_object.writerow(x)
        f_object.close()

def write_csv_line(data:list, path:str):
    with open(path, 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(data)
        f_object.close()
        