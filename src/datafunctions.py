import re

def typeeffect(df):
    """
    This functions creates a column that indicates the type of mutation based in tha variation description. It also creates a column indicating the effect of the mutation
    """
    df['Type'] = 'unknown'
    df['Effect'] = 'unknown'
    for i,r in df.iterrows():
        if re.match('.*Fusion.*',r['Variation']):
            df['Effect'][i] = 'fusion'
            df['Type'][i] = 'Deletion'
            
        elif re.match('.*\*.*',r['Variation']):
            df['Type'][i] = 'Substitution'
            df['Effect'][i] = 'nonsense'
            
        elif re.match('.*\?.*',r['Variation']):
            df['Type'][i] = 'Substitution'
            
        elif re.match('.*Truncating.*',r['Variation']):
            df['Effect'][i] = 'nonsense'
        
        elif re.match('.*missense.*',r['Variation']):
            df['Effect'][i] = 'missense'
            
        elif re.match('.*ins.*|.*Ins.*',r['Variation']):
            df['Type'][i] = 'Insertion'
            
        elif re.match('.*del.*|.*Del.*',r['Variation']):
            df['Type'][i] = 'Deletion'
        
        elif re.match('[A-Z]\d*[A-Z]',r['Variation']):
            df['Type'][i] = 'Substitution'
            df['Effect'][i] = 'missense'
    return df

stop_words = set(stopwords.words('english'))

def nlp_preprocessing(total_text, index, column):
    if type(total_text) is not int:
        string = ""
        # Replace every special char with space
        total_text = re.sub('[^a-zA-Z0-9\n]', ' ', total_text)
        # Replace multiple spaces with single space
        total_text = re.sub('\s+',' ', total_text)
        # Converting all the chars into lower-case
        total_text = total_text.lower()