class Column:
    def __init__(self,name,initial_position,final_position):
        self.name = name
        self.initial_position = initial_position
        self.final_position = final_position
    def __str__(self):
        return "name: %s, initial_postion: %i, final_position: %i" \
          % (self.name,self.initial_position,self.final_position) 

raw_data = open("COTAHIST_D18102018.txt","r")
formatted_data = open("bovespa_cotacao_diaria_18102018.txt","w")

columns_list = [ Column("TIPREG", 0, 2),
                 Column("DATA", 2, 10),
                 Column("CODBDI", 10, 12),
                 Column("CODNEG", 12, 24),
                 Column("TPMERC", 24, 27),
                 Column("NOMRES", 27, 39),
                 Column("ESPECI", 39, 49),
                 Column("PRAZOT", 49, 52),
                 Column("MODREF", 52, 56),
                 Column("PREABE", 56, 69),
                 Column("PREMAX", 69, 82),
                 Column("PREMIN", 82, 95),
                 Column("PREMED", 95, 108),
                 Column("PREULT", 108, 121),
                 Column("PREOFC", 121, 134),
                 Column("PREOFV", 134, 147),
                 Column("TOTNEG", 147, 152),
                 Column("QUATOT", 152, 170),
                 Column("VOLTOT", 170, 188),
                 Column("PREEXE", 188, 201),
                 Column("INDOPC", 201, 202),
                 Column("DATVEN", 202, 210),
                 Column("FATCOT", 210, 217),
                 Column("PTOEXE", 217, 230),
                 Column("CODISI", 230, 242),
                 Column("DISMES", 242, 245) ]

line_list = [] 
line = raw_data.readline()

#this can be faster if we process each line as we read 
#and use: with open('filename') as f: ... lines = f.readlines()
while line:
    line_list.append(line)
    line = raw_data.readline()

#Discart Registro-00 and Registro-99 
del line_list[0]
del line_list[-1] 

for line in line_list:
    line_data = ""
    #Read Registro-01 
    for column in columns_list:
        column_data = line[column.initial_position : column.final_position]
        line_data += column_data + " "
    formatted_data.write(line_data + '\n')

raw_data.close()
