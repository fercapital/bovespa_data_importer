
raw_data = open("COTAHIST_D18102018.txt","r")
formatted_data = open("bovespa_cotacao_diaria_18102018.txt","w")

header_list = [ ("TIPREG", 0, 2),
                ("DATA", 2, 10),
                ("CODBDI", 10, 12),
                ("CODNEG", 12, 24),
                ("TPMERC", 24, 27),
                ("NOMRES", 27, 39),
                ("ESPECI", 39, 49),
                ("PRAZOT", 49, 52),
                ("MODREF", 52, 56),
                ("PREABE", 56, 69),
                ("PREMAX", 69, 82),
                ("PREMIN", 82, 95),
                ("PREMED", 95, 108),
                ("PREULT", 108, 121),
                ("PREOFC", 121, 134),
                ("PREOFV", 134, 147),
                ("TOTNEG", 147, 152),
                ("QUATOT", 152, 170),
                ("VOLTOT", 170, 188),
                ("PREEXE", 188, 201),
                ("INDOPC", 201, 202),
                ("DATVEN", 202, 210),
                ("FATCOT", 210, 217),
                ("PTOEXE", 217, 230),
                ("CODISI", 230, 242),
                ("DISMES", 242, 245) ]

line_list = [] 
line = raw_data.readline()

#this can be faster if we process each line as we read 
#and use: with open('filename') as f: ... lines = f.readlines()
while line:
    line_list.append(line)
    line = raw_data.readline()

#Discart Registro-00 and Registro-99 (Check .pdf for info)
del line_list[0]
del line_list[-1] 

for line in line_list:
    line_data = ""
    #Read Registro-01 
    for column in header_list:
        column_data = line[column[1] : column[2]]
        line_data += column_data + " "
    formatted_data.write(line_data + '\n')

raw_data.close()
