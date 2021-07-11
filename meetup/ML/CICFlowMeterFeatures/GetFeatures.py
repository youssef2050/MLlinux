from meetup.ML.BGTs import BGTs
from csv import reader

from meetup.models import ResultML


def convertToCSV(path):
    with open(path, 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            ip_src = (row[1])
            port_src = (row[2])
            ip_des = (row[3])
            port_des = (row[4])
            #
            row.pop(0)
            row.pop(0)
            row.pop(0)
            row.pop(0)
            row.pop(0)
            row.pop(0)
            row.pop(0)
            row.pop(len(row) - 1)
            print(row)
            classification = BGTs.predict([row])
            res = ResultML(ip_src=ip_src, port_src=port_src, ip_des=ip_des, port_des=port_des,
                           classification=classification)
            res.save()
    return 'is finished'
