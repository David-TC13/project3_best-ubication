import pandas as pd


def prof_data_frame():
    dict_prof= {
    'group_name': ['Designers','UI/UX Engineers','Frontend Developers',
                   'Data Engineers','Backend Developers','Account Managers','Maintenance guy','Executives', 'CEO'],
    'number_prof': [20,5,10,15,5,20,1,10,1]
    
    
    }
    df= pd.DataFrame(dict_prof)
    df['percentage']= [(df.number_prof[i]/df.number_prof.sum())*100 for i in range(len(df.number_prof))]
    df.sort_values( by= 'percentage', ascending= False, inplace= True)
    df.reset_index(inplace= True)
    return  df

