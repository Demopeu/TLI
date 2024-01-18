from pprint import pprint as print
user_data = [
    {
        'blood_group': 'AB',
        'company': 'Stone Inc',
        'mail': 'ian17@yahoo.com',
        'name': 'Kathryn Jenkins',
        'website': [
            'https://www.boyd-herrera.com/',
            'https://watson.com/',
            'http://www.mitchell.com/',
            'http://irwin-cline.biz/',
        ],
    },
    {
        'blood_group': 'AB+',
        'company': 'Fleming Ltd',
        'mail': 'patricianelson@yahoo.com',
        'name': 'Angel Williamson',
        'website': [
            'https://wilson-johnson.com/',
            'https://santiago-hammond.com/',
            'https://morales.com/',
            'https://fry-fleming.com/',
        ],
    },
    {
        'blood_group': 'A+',
        'company': 'Scott PLC',
        'mail': 'lisajones@gmail.com',
        'name': 'Stephanie Herman MD',
        'website': [
            'https://www.boyer-stevens.org/',
            'http://www.johnson.com/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Warren-Stewart',
        'mail': 'allisonjennifer@gmail.com',
        'name': 'Jon Martinez',
        'website': ['https://www.berg.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Fisher Inc',
        'mail': 'mross@yahoo.com',
        'name': 'Justin Brown',
        'website': [
            'https://www.gray.com/',
            'https://jones.com/',
            'http://williams.biz/',
            'https://hammond.net/',
        ],
    },
    {
        'blood_group': 'B-',
        'company': 'Pearson Group',
        'mail': 'gravesbarbara@hotmail.com',
        'name': 'Bobby Patterson',
        'website': ['https://www.cunningham.biz/', 'https://johnson.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'White, Andrade and Howard',
        'mail': 'mcole@gmail.com',
        'name': 'Michelle Strickland',
        'website': ['http://www.rose-gomez.com/', 'https://reilly.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Brown-Young',
        'mail': 'tmorales@hotmail.com',
        'name': 'Stephanie Moore',
        'website': ['https://schmidt.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Brooks PLC',
        'mail': 'wellsmatthew@hotmail.com',
        'name': 'Dr. David Johnson',
        'website': [
            'http://ford-dean.com/',
            'http://www.petersen.com/',
            'https://thompson-cooley.info/',
            'http://ryan-gay.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Stewart Group',
        'mail': 'sean37@hotmail.com',
        'name': 'Veronica Webb',
        'website': ['http://www.holmes.info/', 'http://www.morris.biz/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Cabrera, Perry and Harris',
        'mail': 'bgonzales@yahoo.com',
        'name': 'Lisa Wilcox',
        'website': ['https://www.small.com/', 'http://martin-petersen.com/'],
    },
    {
        'blood_group': 'B+',
        'company': 'Thomas, Lozano and Lopez',
        'mail': 'bperry@yahoo.com',
        'name': 'Brian Simmons',
        'website': [
            'http://reid.com/',
            'http://www.roman-neal.biz/',
            'https://www.hoover.org/',
            'https://www.lynn.com/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Baker-Leach',
        'mail': 'johnlucas@yahoo.com',
        'name': 'Carlos Robinson',
        'website': ['https://martin.com/', 'http://montgomery-cline.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Higgins, Higgins and Garcia',
        'mail': 'chris66@gmail.com',
        'name': 'Gabriel Collins',
        'website': ['https://www.cole-pugh.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Tanner, Wheeler and Weaver',
        'mail': 'leonardtammy@gmail.com',
        'name': 'Christopher Cook',
        'website': [
            'https://www.myers-reynolds.com/',
            'https://dunlap-rogers.com/',
            'https://luna.net/',
            'http://smith-miller.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Schaefer-Hunter',
        'mail': 'nsummers@gmail.com',
        'name': 'Daniel Monroe',
        'website': [
            'https://cook.net/',
            'http://carpenter.com/',
            'http://morris-terrell.com/',
        ],
    },
    {
        'blood_group': 'B+',
        'company': 'Stephens Group',
        'mail': 'rolson@gmail.com',
        'name': 'Molly Parks',
        'website': [
            'https://wright-vincent.biz/',
            'http://www.cruz.com/',
            'http://olson.org/',
            'http://gomez.com/',
        ],
    },
    {
        'blood_group': 'O-',
        'company': 'Fitzgerald, Costa and Hobbs',
        'mail': 'jennifervang@hotmail.com',
        'name': 'Jill Patterson',
        'website': [
            'https://www.brewer.com/',
            'https://malone-murray.info/',
            'http://evans.com/',
            'https://ortiz.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Frazier Ltd',
        'mail': 'vsolis@hotmail.com',
        'name': 'Marie May',
        'website': [
            'http://pratt.info/',
            'http://www.ortega.com/',
            'http://www.smith.net/',
            'https://nichols.biz/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Rodriguez and Sons',
        'mail': 'michael09@yahoo.com',
        'name': 'Julia Gonzalez',
        'website': [
            'https://www.cantrell.com/',
            'https://www.smith.net/',
            'http://delgado.com/',
            'http://stevens.com/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Brown-Arnold',
        'mail': 'christopher79@hotmail.com',
        'name': 'David Garza',
        'website': ['https://price.net/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Butler-Hernandez',
        'mail': 'angiechoi@yahoo.com',
        'name': 'Leslie Kemp',
        'website': ['http://www.martin-thompson.org/', 'http://martin.org/'],
    },
    {
        'blood_group': 'A-',
        'company': 'Schneider-Hensley',
        'mail': 'cesarsantos@hotmail.com',
        'name': 'Brandon Peterson',
        'website': [
            'https://www.owens-gay.com/',
            'https://www.santiago.org/',
            'https://www.singleton.com/',
        ],
    },
    {
        'blood_group': 'O-',
        'company': 'Hunter, Alvarado and Stewart',
        'mail': 'thomas16@gmail.com',
        'name': 'Matthew Stanley',
        'website': ['https://nelson.com/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Elliott, Mullins and Michael',
        'mail': 'smithedward@hotmail.com',
        'name': 'Robert Brown',
        'website': [
            'http://montgomery-rogers.biz/',
            'http://www.williams-nixon.com/',
        ],
    },
    {
        'blood_group': 'AB+',
        'company': 'Velasquez-Garcia',
        'mail': 'samanthawilson@yahoo.com',
        'name': 'Stephanie Cohen',
        'website': ['http://jackson-harris.com/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Mccoy-Hopkins',
        'mail': 'lli@yahoo.com',
        'name': 'Michael Clark',
        'website': [
            'https://www.harding.info/',
            'https://www.jones.biz/',
            'http://knight-adkins.org/',
            'http://www.alvarado-mendoza.org/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Kerr Ltd',
        'mail': 'georgebrittany@yahoo.com',
        'name': 'Brandon White',
        'website': [
            'https://flowers-parker.info/',
            'http://oliver-rice.info/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Villarreal, Wood and Smith',
        'mail': 'denise73@yahoo.com',
        'name': 'Kevin Blevins',
        'website': [
            'http://www.ramirez.info/',
            'https://mckay.net/',
            'http://duran.com/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Jenkins-Garcia',
        'mail': 'kwoodward@hotmail.com',
        'name': 'Michelle Dixon',
        'website': [
            'http://www.taylor.com/',
            'https://bates-trujillo.org/',
            'https://www.thomas-boyer.org/',
        ],
    },
]

blood_types = ['A-', 'A+', 'B-', 'B+', 'O-', 'O+', 'AB-', 'AB+']
black_list = [
    'Jenkins-Garcia',
    'Stephens Group',
    'White, Andrade and Howard',
    'Warren-Stewart',
]
def create_user(list):
    lst = is_validation(list)
    global long_user
    if lst != True:
        long_user += 1
        if lst == 'blocked':
            return False
        else:
            for i in range(len(lst[1])):
                list[lst[1][i]] = None
            return list
    else:
        return list
        



def is_validation(list):
    TF = True
    False_list = []
    if list['company'] in black_list:
        return 'blocked'
    if list['blood_group'] not in blood_types:
        TF = False
        False_list.append('blood_group')
    if list['mail'].find('@') == -1:
        TF = False
        False_list.append('mail')
    if len(list['name'])<2 and len(list['name'])>30:
        TF = False
        False_list.append('name')

    if 1>len(list['website']):
        TF = False
        False_list.append('website')
    if TF == False:
        return (TF,False_list)
    else:
        return True

long_user = 0
New_user_list = []
for i in range(len(user_data)):
    New_user_data = create_user(user_data[i]) 
    if New_user_data != False:
        New_user_list.append(New_user_data)
print(f'잘못된 데이터로 구성된 유저의 수는 {long_user} 입니다.') 
print(New_user_list) 
