import csv      
# هنا هنستورد موديول csv

with open("./read.csv",'r') as f:
    # هنا هنفتح الملف بتاعنا و نديله صلاحية القراءة فقط و نديله اسم مستعار  
    render = csv.reader(f)
    # هنا بقوله من موديول csv هات method الي اسمها reader الي من خلالها اقدر اقراء ملفcsv
    for row in render:
        # دلوقتي احنا بقا عندنا object بيحتوي علي البيانات وهنعمله loop عشان نرججع البيانات 
        Name = row[0]
        Email = row[1]
        Phone = row[2]
        Job = row[3]
        print(Name)        
        print(Email)        
        print(Phone)        
        print(Job)        
