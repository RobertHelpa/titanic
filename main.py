import pandas as pd

df = pd.read_csv('titanic.csv')

#df.info()
#print(df.head(10))

df.drop(["PassengerId", "Name", "Ticket", "Cabin"], 
        axis=1, inplace=True
        )

df['Embarked'].fillna('S', inplace=True)

age_1 = df[df['Pclass']==1]['Age'].median()
age_2 = df[df['Pclass']==1]['Age'].median()
age_3 = df[df['Pclass']==1]['Age'].median()

def set_age(row):
    if pd.insull(row['Age']):
        if row ["Pclass"] == 1:
            return age_1
        elif row ['Pclass'] == 2:
            return age_2
        elif row ['Pclass'] == 3:
            return age_3
    return row['Age']

df['Age'] = df.apply(set_age, axis=1)

def set_sex(sex):
    if sex == 'male':
        return 1
    elif sex == 'female':
        return 0
    
df['sex'] = df['sex'].apply(set_sex)

df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])

df.drop('Embarked', axis=1, inplace=True)