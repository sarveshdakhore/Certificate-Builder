import pandas as pd
import csv
import sys
import os
sys.path.append(os.getcwd())
column_for_messages=["msg_id","to","from","viaeb","message","replyid"]
column_for_username_host=["host_code","organization"]
column_for_username_join=["host_code","organization"]
column_for_request_gain=["username","name","host_code",]
column_for_rg_host=["username","host_code","organization"]
column_for_usr_pass=["username","password","name","email"]


def username_file(username):                                    # Working
    df=pd.DataFrame([],columns=column_for_username_host)
    df.to_csv(r'templates/username/'+username+r"/host.csv",index=False)

    df=pd.DataFrame([],columns=column_for_usr_pass)
    df.to_csv(r'templates/username/'+username+r"/pass.csv",index=False)

    df=pd.DataFrame([],columns=column_for_username_join)            
    df.to_csv(os.getcwd()+r'/templates/username/'+username+r"/join.csv",index=False)

def username_check(username):      # Working
    if username in os.listdir("templates/username"):
        return False
    else:
        return True


def user_list(host_code):
    df=pd.read_csv(r'templates/database/'+host_code+r"/user_data.csv")
    return df['usr_id'].tolist()

def username_data_creater(username):    # Working
    if username_check(username)==True:
        os.system('mkdir '+r'"templates/username/'+username+'"')
                

def username_setup(username,password,email,name):      # Working
    username_data_creater(username)
    username_file(username)
    row=[username,password,name,email]
    with open(r'templates/username/'+username+"/pass.csv","w",newline="") as f_object:
            writer_object = csv.writer(f_object)
            writer_object.writerow(row)
            f_object.close()






def host_code_check(host_code):  # Working
    if host_code in os.listdir("templates/database"):
        return False
    else:
        return True


def message_id_generator(host_code):            # Working
    file=open(r'templates/database/'+host_code+r"/messages.csv")
    reader = csv.reader(file)
    lines= len(list(reader))
    return lines



def host_csv_creater(host_code,column_for_messages):   # Working
    df=pd.DataFrame([],columns=column_for_messages)
    df.to_csv(r'templates/database/'+host_code+r"/messages.csv",index=False)
    
    df=pd.DataFrame([],columns=["usr_id","name","email","post"])
    df.to_csv(r'templates/database/'+host_code+r"/user_data.csv",index=False)
    


def host_code_setup(host_code,username,column_for_messages,organisation):    # Working
    if host_code_check(host_code)==True:
        os.system('mkdir '+r'"templates/database/'+host_code+'"')
        host_csv_creater(host_code,column_for_messages)
        

"""
        row=[username,host_code,organisation,]
        with open(r'templates/rg_host.csv',"a",newline="") as f_object:
            writer_object = csv.writer(f_object)
            writer_object.writerow(row)
            f_object.close()
        row=[host_code,organisation]
        with open(r'templates/username/'+username+"/host.csv","a",newline="") as f_object:
            writer_object = csv.writer(f_object)
            writer_object.writerow(row)
            f_object.close()
"""

def pass_extractor(username):                               # Working
    df=pd.read_csv(r'templates/username/'+username+'/pass.csv')
    filt =df['username']==username
    try:
        fnl=df.loc[filt,"password"].tolist()[0]
        return fnl
    except IndexError:
        return False


def message_adder(host_code,to,from_c,viaeb,message,replyid):            # Working
    row=[message_id_generator(host_code),to,from_c,viaeb,message,replyid]
    with open(r'templates/database/'+host_code+r"/messages.csv","a",newline="") as f_object:
        writer_object = csv.writer(f_object)
        writer_object.writerow(row)
        f_object.close()



def message_sorter_admin_rec(host_code,admin_country):      # Working
    df=pd.read_csv(r'templates/database/'+host_code+r"/messages.csv")
    filt = (df['to']==admin_country)
    filt= df[filt]
    filt= filt.values.tolist()
    return filt


'''host_code_setup("qw","qw",column_for_messages,"qwergcdc")
'''


def message_sorter_admin_sent(host_code,admin_country):     # Woring
    df=pd.read_csv(r'templates/database/'+host_code+r"/messages.csv")
    filt = (df['from']==admin_country)
    filt= df[filt]
    filt= filt.values.tolist()
    return filt
'''print(message_sorter_admin_sent('qw',"china"))
'''

def msg_process(host_code,admin_country):                                  # Woring
    msg_sent=message_sorter_admin_sent(host_code,admin_country)
    msg_rec=message_sorter_admin_rec(host_code,admin_country)
    
    msg_f_sent=[]
    msg_f_rec=[]
    for i in msg_sent:
        if i[-1]=='None':
            msg_f_sent.append(i)
            print(msg_f_sent)
        elif i[-1].isnumeric():
            df=pd.read_csv(r'templates/database/'+host_code+r"/messages.csv")
            filt = (df['msg_id']==int(i[-1]))
            try:
                fnl=df.loc[filt,"message"].tolist()[0]
                i.pop()
                i.append(fnl)
                msg_f_sent.append(i)
            except:
                pass

    for i in msg_rec:
        if i[-1]=="None":    
            msg_f_rec.append(i)
            
        elif i[-1].isnumeric():
            df=pd.read_csv(r'templates/database/'+host_code+r"/messages.csv")
            filt = ((df['msg_id'])==int(i[-1]))
            try:
                fnl=df.loc[filt,"message"].tolist()[0]
                i.pop()
                i.append(fnl)
                msg_f_rec.append(i)
            except IndexError:
                pass

    return msg_f_rec, msg_f_sent


msg_rec= msg_process("qw","china")[0]
msg_sent=msg_process("qw","china")[1]

def message_sort_wc(host_code,sort_c):
    pass




def msg_for_eb(host_code):
    df=pd.read_csv(r'templates/database/'+host_code+r"/messages.csv")
    filt = ((df['viaeb'])=='Yes')
    filt= df[filt]
    filt= filt.values.tolist()
    finl=[]
    for i in filt:
        if i[-1]=='None':
            finl.append(i)
            
        elif i[-1].isnumeric():
            df=pd.read_csv(r'templates/database/'+host_code+r"/messages.csv")
            filt1 = (df['msg_id']==int(i[-1]))
            try:
                fnl=df.loc[filt1,"message"].tolist()[0]
                i.pop()
                i.append(fnl)
                finl.append(i)
            except:
                pass
    return finl


def to_c_v_mg(host_code,msg_id):
    df=pd.read_csv(r'templates/database/'+host_code+r"/messages.csv")
    filt1 = (df['msg_id']==int(msg_id))
    try:
        fnl=df.loc[filt1,"from"].tolist()[0]
    except:
        fnl=''
    return fnl

print(to_c_v_mg('qw',3))

def msg_sort_rec(host_code,admin_country,sort_country_name):
    msg_rec=msg_process(host_code,admin_country)[0]
    df= pd.DataFrame(msg_rec,columns=column_for_messages)
    filt = (df['from'])==sort_country_name
    return (df[filt].values.tolist())

def msg_sort_sent(host_code,admin_country,sort_country_name):
    msg_sent=msg_process(host_code,admin_country)[1]
    df= pd.DataFrame(msg_sent,columns=column_for_messages)
    filt = (df['to'])==sort_country_name
    return (df[filt].values.tolist())


def user_exist_yes_than_country(host_code,user_id):
    df=pd.read_csv(r'templates/database/'+host_code+r"/user_data.csv")
    usr_id_list=df['usr_id'].tolist()
    lp=[]
    for i in usr_id_list:
        lp.append(str(i))
    usr_id_list=lp
    try:
        if user_id in usr_id_list:
            filt = (df['usr_id'])==(user_id)
            return (df[filt].values.tolist())[0][-1]
    except:
        pass
    else:
        return False

def country_li(host_code):
    df=pd.read_csv(r'templates/database/'+host_code+r"/user_data.csv")
    return df['post'].tolist()

