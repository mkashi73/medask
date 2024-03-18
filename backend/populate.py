import os
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'medask.settings')
import django
django.setup()
from django.utils import timezone
from api.models import User, Role, Permission, Center, Distt, Language, Profession, Province, QualType, Rank, Religion, Sect, EducationBoard, Tehsil, RollNo, Courses



sect = [
    
    {
        'id': 1, 'sect_name': 'Sunni', 'religion' : '1'
    },
    {
        'id': 2, 'sect_name': 'Shia', 'religion' : '1'
    },
    {
        'id': 3, 'sect_name': 'Ahl-e-Hadees', 'religion' : '1'
    },
    {
        'id': 4, 'sect_name': 'Brelvi', 'religion' : '1'
    },
    {
        'id': 5, 'sect_name': 'Deobandi', 'religion' : '1'
    },
    {
        'id': 6, 'sect_name': 'Ismaili', 'religion' : '8'
    },
    {
        'id': 7, 'sect_name': 'Sofia Noor Bakhshia', 'religion' : '1'
    },
    {
        'id': 8, 'sect_name': 'Catholic', 'religion' : '7'
    },
    {
        'id': 9, 'sect_name': 'Protestant', 'religion' : '7'
    },
    {
        'id': 10, 'sect_name': 'Roman Catholic', 'religion' : '7'
    },
    {
        'id': 11, 'sect_name': 'Kalash', 'religion' : '3'
    },
    {
        'id': 12, 'sect_name': 'Qadiani', 'religion' : '8'
    },
    {
        'id': 13, 'sect_name': 'Other', 'religion' : '8'
    },
    
]


religion = [
    
    {
        'id': 1, 'religion_name': 'Islam'
    },
    {
        'id': 2, 'religion_name': 'Jewish'
    },
    {
        'id': 3, 'religion_name': 'Kalash'
    },
    {
        'id': 4, 'religion_name': 'Sikh'
    },    
    {
        'id': 5, 'religion_name': 'Hindu'
    },
    {
        'id': 6, 'religion_name': 'Christian'
    },
    {
        'id': 7, 'religion_name': 'Buddhist'
    },
    {
        'id': 8, 'religion_name': 'Other'
    },
    
]



profession = [
    
    {
        'id': 1, 'profession_name': 'Bussinessman'
    },
    {
        'id': 2, 'profession_name': 'Business Women'
    },    
    {
        'id': 3, 'profession_name': 'Govt job'
    },
    {
        'id': 4, 'profession_name': 'Serving army'
    },
    {
        'id': 5, 'profession_name': 'Retd army'
    },
    {
        'id': 6, 'profession_name': 'Shaheed army'
    },
    {
        'id': 7, 'profession_name': 'In service death army'
    },
    {
        'id': 8, 'profession_name': 'war wounded army'
    },
    {
        'id': 9, 'profession_name': 'Serving air force'
    },
    {
        'id': 10, 'profession_name': 'Retd air force'
    },
    {
        'id': 11, 'profession_name': 'Shaheed air force'
    },
    {
        'id': 12, 'profession_name': 'In service death air force'
    },
    {
        'id': 13, 'profession_name': 'war wounded air force'
    },
    {
        'id': 14, 'profession_name': 'serving navy'
    },
    {
        'id': 15, 'profession_name': 'Retd navy'
    },
    {
        'id': 16, 'profession_name': 'Shaheed Navy'
    },
    {
        'id': 17, 'profession_name': 'In service death navy'
    },
    {
        'id': 18, 'profession_name': 'War wounded navy'
    },
    {
        'id': 19, 'profession_name': 'Other'
    },
    {
        'id': 20, 'profession_name': 'None'
    },
    {
        'id': 21, 'profession_name': 'House Wife'
    },
    {
        'id': 22, 'profession_name': 'AFNS army'
    },
    {
        'id': 23, 'profession_name': 'AFNS air force'
    },
    {
        'id': 24, 'profession_name': 'AFNS navy'
    },
    {
        'id': 25, 'profession_name': 'Private Job'
    },
]


rank = [
    
    {
        'id': 1, 'rank_name': 'General'
    },
    {
        'id': 2, 'rank_name': 'Lieutenant General'
    },
    {
        'id': 3, 'rank_name': 'Major General'
    },
    {
        'id': 4, 'rank_name': 'Brigadier'
    },
    {
        'id': 5, 'rank_name': 'Colonol'
    },
    {
        'id': 6, 'rank_name': 'Lieutenant Colonel'
    },
    {
        'id': 7, 'rank_name': 'Major'
    },
    {
        'id': 8, 'rank_name': 'Captain'
    },
    {
        'id': 9, 'rank_name': 'Lieutenant'
    },
    {
        'id': 10, 'rank_name': '2nd Lieutenant'
    },
    {
        'id': 11, 'rank_name': 'Honorary Captain'
    },
    {
        'id': 12, 'rank_name': 'Honorary Lieutenant'
    },
    {
        'id': 13, 'rank_name': 'Subedar Major'
    },
    {
        'id': 14, 'rank_name': 'Subedar'
    },
    {
        'id': 15, 'rank_name': 'Naib Subedar'
    },
    {
        'id': 16, 'rank_name': 'Havildar'
    },
    {
        'id': 17, 'rank_name': 'Lance Daffadar'
    },
    {
        'id': 18, 'rank_name': 'Naik'
    },
    {
        'id': 19, 'rank_name': 'Lance Naik'
    },
    {
        'id': 20, 'rank_name': 'Sepoy'
    },
    {
        'id': 21, 'rank_name': 'Admiral'
    },
    {
        'id': 22, 'rank_name': 'Vice Admiral'
    },
    {
        'id': 23, 'rank_name': 'Rear Admiral'
    },
    {
        'id': 24, 'rank_name': 'Commodore'
    },
    {
        'id': 25, 'rank_name': 'Captain(PN)'
    },
    {
        'id': 26, 'rank_name': 'Commander'
    },
    {
        'id': 27, 'rank_name': 'Lieutenant Commander'
    },
    {
        'id': 28, 'rank_name': 'Sub Lieutenant'
    },
    {
        'id': 29, 'rank_name': 'Acting Sub Lieutenant'
    },
    {
        'id': 30, 'rank_name': 'Miashipman'
    },
    {
        'id': 31, 'rank_name': 'Cadet'
    },
    {
        'id': 32, 'rank_name': 'Master Chief Petty Officer'
    },
    {
        'id': 33, 'rank_name': 'Chief Petty Officer'
    },
    {
        'id': 34, 'rank_name': 'Petty Officer'
    },
    {
        'id': 35, 'rank_name': 'Leading Seaman'
    },
    {
        'id': 36, 'rank_name': 'Able Seaman'
    },
    {
        'id': 37, 'rank_name': 'Ordinary Seaman'
    },
    {
        'id': 38, 'rank_name': 'Air Chief Marshal'
    },
    {
        'id': 39, 'rank_name': 'Air Marshal'
    },
    {
        'id': 40, 'rank_name': 'Air Vice Marshal'
    },
    {
        'id': 41, 'rank_name': 'Air Commodore'
    },
    {
        'id': 42, 'rank_name': 'Group Captain'
    },
    {
        'id': 43, 'rank_name': 'Wing Commander'
    },
    {
        'id': 44, 'rank_name': 'Squadren Leader'
    },
    {
        'id': 45, 'rank_name': 'Flight Lieutenant'
    },
    {
        'id': 46, 'rank_name': 'Flying Officer'
    },
    {
        'id': 47, 'rank_name': 'Pilot Officer'
    },
    {
        'id': 48, 'rank_name': 'Master Warrant Officer'
    },
    {
        'id': 49, 'rank_name': 'Warrant Officer'
    },
    {
        'id': 50, 'rank_name': 'Chief Technician'
    },
    {
        'id': 51, 'rank_name': 'Senior Technician'
    },
    {
        'id': 52, 'rank_name': 'Corporal'
    },
    {
        'id': 53, 'rank_name': 'Junior Technician'
    },
    {
        'id': 54, 'rank_name': 'Senior Technician'
    },
    {
        'id': 55, 'rank_name': 'Leading Aircraftman'
    },
    {
        'id': 56, 'rank_name': 'Aircraftman'
    },
    {
        'id': 57, 'rank_name': 'Other'
    },
    {
        'id': 58, 'rank_name': 'Fleet Chief Petty Officer'
    },
    {
        'id': 59, 'rank_name': 'Second Lieutenant'
    },

]

province = [

    {
        'id': 1, 'province_name': 'Federal Capital'
    },
    {
        'id': 2, 'province_name': 'AK'
    },
    {
        'id': 3, 'province_name': 'Balochistan'
    },
    {
        'id': 4, 'province_name': 'FATA'
    },
    {
        'id': 5, 'province_name': 'Gilgit Baltistan'
    },
    {
        'id': 6, 'province_name': 'KPK'
    },
    {
        'id': 7, 'province_name': 'Punjab'
    },
    {
        'id': 8, 'province_name': 'Sindh'
    },
]

districts = [
    
{ 'id':1, 'distt_name':'Islamabad', 'province':1 },
{ 'id':7, 'distt_name':'Attock', 'province':7 },
{ 'id':8, 'distt_name':'Bahawalnagar', 'province':7 },
{ 'id':9, 'distt_name':'Bahawalpur', 'province':7 },
{ 'id':10, 'distt_name':'Bhakkar', 'province':7 },
{ 'id':11, 'distt_name':'Chakwal', 'province':7 },
{ 'id':12, 'distt_name':'DG Khan', 'province':7 },
{ 'id':13, 'distt_name':'Faisalabad', 'province':7 },
{ 'id':14, 'distt_name':'Gujranwala', 'province':7 },
{ 'id':15, 'distt_name':'Gujrat', 'province':7 },
{ 'id':16, 'distt_name':'Hafizabad', 'province':7 },
{ 'id':17, 'distt_name':'Islamabad', 'province':7 },
{ 'id':18, 'distt_name':'Jhang', 'province':7 },
{ 'id':19, 'distt_name':'Jhelum', 'province':7 },
{ 'id':20, 'distt_name':'Kasur', 'province':7 },
{ 'id':21, 'distt_name':'Khanewal', 'province':7 },
{ 'id':22, 'distt_name':'Khushab', 'province':7 },
{ 'id':23, 'distt_name':'Lahore', 'province':7 },
{ 'id':24, 'distt_name':'Leiah', 'province':7 },
{ 'id':25, 'distt_name':'Lodhran', 'province':7 },
{ 'id':26, 'distt_name':'M B Din', 'province':7 },
{ 'id':27, 'distt_name':'Mianwali', 'province':7 },
{ 'id':28, 'distt_name':'Multan', 'province':7 },
{ 'id':29, 'distt_name':'Muzaffargarh', 'province':7 },
{ 'id':30, 'distt_name':'Narowal', 'province':7 },
{ 'id':31, 'distt_name':'Okara', 'province':7 },
{ 'id':32, 'distt_name':'Pakpattan', 'province':7 },
{ 'id':33, 'distt_name':'Rahim Yar Khan', 'province':7 },
{ 'id':34, 'distt_name':'Rajan Pur', 'province':7 },
{ 'id':35, 'distt_name':'Rawalpindi', 'province':7 },
{ 'id':36, 'distt_name':'Sahiwal', 'province':7 },
{ 'id':37, 'distt_name':'Sargodha', 'province':7 },
{ 'id':38, 'distt_name':'Sheikhupura', 'province':7 },
{ 'id':39, 'distt_name':'Sialkot', 'province':7 },
{ 'id':40, 'distt_name':'T T Sing', 'province':7 },
{ 'id':41, 'distt_name':'Vehari', 'province':7 },
{ 'id':42, 'distt_name':'Abbottabad', 'province':6 },
{ 'id':43, 'distt_name':'Bannu', 'province':6 },
{ 'id':44, 'distt_name':'Batgram', 'province':6 },
{ 'id':45, 'distt_name':'Buner', 'province':6 },
{ 'id':46, 'distt_name':'Charsadda', 'province':6 },
{ 'id':47, 'distt_name':'Chitral', 'province':6 },
{ 'id':48, 'distt_name':'Dir', 'province':6 },
{ 'id':49, 'distt_name':'D I Khan', 'province':6 },
{ 'id':50, 'distt_name':'Hangu', 'province':6 },
{ 'id':51, 'distt_name':'Haripur', 'province':6 },
{ 'id':52, 'distt_name':'Karak', 'province':6 },
{ 'id':53, 'distt_name':'Kohat', 'province':6 },
{ 'id':54, 'distt_name':'Kohistan', 'province':6 },
{ 'id':55, 'distt_name':'Lakki Marwat', 'province':6 },
{ 'id':56, 'distt_name':'Malakand', 'province':6 },
{ 'id':57, 'distt_name':'Mansehra', 'province':6 },
{ 'id':58, 'distt_name':'Mardan', 'province':6 },
{ 'id':59, 'distt_name':'Nowshera', 'province':6 },
{ 'id':60, 'distt_name':'Peshawar', 'province':6 },
{ 'id':61, 'distt_name':'Shangla', 'province':6 },
{ 'id':62, 'distt_name':'Swabi', 'province':6 },
{ 'id':63, 'distt_name':'Swat', 'province':6 },
{ 'id':64, 'distt_name':'Tank', 'province':6 },
{ 'id':65, 'distt_name':'Bajaur Agency', 'province':6 },
{ 'id':66, 'distt_name':'Baltistan', 'province':5 },
{ 'id':67, 'distt_name':'Khyber Agency', 'province':6 },
{ 'id':68, 'distt_name':'Kurram Agency', 'province':6 },
{ 'id':69, 'distt_name':'Mohemmend Agency', 'province':6 },
{ 'id':70, 'distt_name':'North Waziristan Agency', 'province':6 },
{ 'id':71, 'distt_name':'Orakzai Agency', 'province':6 },
{ 'id':72, 'distt_name':'South Waziristan Agency', 'province':6 },
{ 'id':73, 'distt_name':'Badin', 'province':8 },
{ 'id':74, 'distt_name':'Dadu', 'province':8 },
{ 'id':75, 'distt_name':'Ghotki', 'province':8 },
{ 'id':76, 'distt_name':'Hyderabad', 'province':8 },
{ 'id':77, 'distt_name':'Jacobabad', 'province':8 },
{ 'id':78, 'distt_name':'Karachi', 'province':8 },
{ 'id':79, 'distt_name':'Karachi East', 'province':8 },
{ 'id':80, 'distt_name':'Karachi South', 'province':8 },
{ 'id':81, 'distt_name':'Karachi West', 'province':8 },
{ 'id':82, 'distt_name':'Khairpur', 'province':8 },
{ 'id':83, 'distt_name':'Larkana', 'province':8 },
{ 'id':84, 'distt_name':'Malir', 'province':8 },
{ 'id':85, 'distt_name':'Mirpur Khas', 'province':8 },
{ 'id':86, 'distt_name':'Tarparker/Mithi', 'province':8 },
{ 'id':87, 'distt_name':'Naushahro Feroze', 'province':8 },
{ 'id':88, 'distt_name':'Nawab Shah', 'province':8 },
{ 'id':89, 'distt_name':'Sanghar', 'province':8 },
{ 'id':90, 'distt_name':'Shikarpur', 'province':8 },
{ 'id':91, 'distt_name':'Sukkur', 'province':8 },
{ 'id':92, 'distt_name':'Thatta', 'province':8 },
{ 'id':93, 'distt_name':'Umerkot', 'province':8 },
{ 'id':94, 'distt_name':'Bagh', 'province':2 },
{ 'id':96, 'distt_name':'Bhimber', 'province':2 },
{ 'id':97, 'distt_name':'Diamir', 'province':5 },
{ 'id':98, 'distt_name':'Ghanche', 'province':5 },
{ 'id':99, 'distt_name':'Ghizer', 'province':2 },
{ 'id':100, 'distt_name':'Gilgit', 'province':5 },
{ 'id':101, 'distt_name':'Kotli', 'province':2 },
{ 'id':102, 'distt_name':'Mirpur', 'province':2 },
{ 'id':103, 'distt_name':'Muzaffarabad', 'province':2 },
{ 'id':104, 'distt_name':'Poonch', 'province':2 },
{ 'id':105, 'distt_name':'Sudhnoti', 'province':2 },
{ 'id':106, 'distt_name':'Awaran', 'province':3 },
{ 'id':107, 'distt_name':'Barkhan', 'province':3 },
{ 'id':108, 'distt_name':'Bolan', 'province':3 },
{ 'id':109, 'distt_name':'Chagai', 'province':3 },
{ 'id':110, 'distt_name':'Dera Bugti', 'province':3 },
{ 'id':111, 'distt_name':'Gawadar', 'province':3 },
{ 'id':112, 'distt_name':'Jafarabad', 'province':3 },
{ 'id':113, 'distt_name':'Jhal Magsi', 'province':3 },
{ 'id':114, 'distt_name':'Kalat', 'province':3 },
{ 'id':115, 'distt_name':'Kech/Turbat', 'province':3 },
{ 'id':116, 'distt_name':'Kharan', 'province':3 },
{ 'id':117, 'distt_name':'Khuzdar', 'province':3 },
{ 'id':118, 'distt_name':'Killa Abdullah', 'province':3 },
{ 'id':119, 'distt_name':'Killa Saifullah', 'province':3 },
{ 'id':120, 'distt_name':'Kohlu', 'province':3 },
{ 'id':121, 'distt_name':'Lasbela', 'province':3 },
{ 'id':122, 'distt_name':'Loralai', 'province':3 },
{ 'id':123, 'distt_name':'Musa Khel', 'province':3 },
{ 'id':124, 'distt_name':'Mastung', 'province':3 },
{ 'id':125, 'distt_name':'Nasirabad', 'province':3 },
{ 'id':126, 'distt_name':'Panjgur', 'province':3 },
{ 'id':127, 'distt_name':'Pishin', 'province':3 },
{ 'id':128, 'distt_name':'Quetta', 'province':3 },
{ 'id':129, 'distt_name':'Sibbi', 'province':3 },
{ 'id':130, 'distt_name':'Zhob', 'province':3 },
{ 'id':131, 'distt_name':'Ziarat', 'province':3 },
{ 'id':132, 'distt_name':'Astore', 'province':5 },
{ 'id':133, 'distt_name':'Nankana Sahib', 'province':7 },
{ 'id':134, 'distt_name':'Tribal Areas adjoining Peshawar Dist', 'province':6 },
{ 'id':135, 'distt_name':'Tribal Areas adjoining Kohat Dist', 'province':6 },
{ 'id':136, 'distt_name':'Tribal Areas adjoining Bannu Dist', 'province':6 },
{ 'id':137, 'distt_name':'Tribal Areas adjoining Lakki Marwat Dist', 'province':6 },
{ 'id':138, 'distt_name':'Tribal Areas adjoining D.I.Khan Dist', 'province':6 },
{ 'id':139, 'distt_name':'Tribal Areas adjoining Tank Dist', 'province':6 },
{ 'id':140, 'distt_name':'Cholistan Desert', 'province':7 },
{ 'id':141, 'distt_name':'Drawer Fort', 'province':7 },
{ 'id':142, 'distt_name':'Salamsar', 'province':7 },
{ 'id':143, 'distt_name':'Mojgarh', 'province':7 },
{ 'id':144, 'distt_name':'Dingarh', 'province':7 },
{ 'id':145, 'distt_name':'Tando Muhammad Khan', 'province':8 },
{ 'id':146, 'distt_name':'Chiniot', 'province':7 },
{ 'id':147, 'distt_name':'Jamshoro', 'province':8 },
{ 'id':148, 'distt_name':'Pano Aqil', 'province':8 },
{ 'id':149, 'distt_name':'Lower Dir', 'province':6 },
{ 'id':150, 'distt_name':'Neelum', 'province':2 },
{ 'id':151, 'distt_name':'Hattian Bhala', 'province':2 },
{ 'id':152, 'distt_name':'Haveli', 'province':2 },
{ 'id':153, 'distt_name':'Skardu', 'province':5 },
{ 'id':154, 'distt_name':'Rondu', 'province':5 },
{ 'id':155, 'distt_name':'Shigar', 'province':5 },
{ 'id':156, 'distt_name':'Kharmang', 'province':5 },
{ 'id':157, 'distt_name':'Darel', 'province':5 },
{ 'id':158, 'distt_name':'Tangir', 'province':5 },
{ 'id':159, 'distt_name':'Ghizzer', 'province':5 },
{ 'id':160, 'distt_name':'Gupis-Yasin', 'province':5 },
{ 'id':161, 'distt_name':'Hunza', 'province':5 },
{ 'id':162, 'distt_name':'Nagar', 'province':5 },
]


tehsils = [    
{ 'id':1, 'tehsil_name':'Rawalpindi', 'distt':35 },
{ 'id':2, 'tehsil_name':'Taxila', 'distt':35 },
{ 'id':3, 'tehsil_name':'Kahuta', 'distt':35 },
{ 'id':4, 'tehsil_name':'Murree', 'distt':35 },
{ 'id':5, 'tehsil_name':'Kotli Sattian', 'distt':35 },
{ 'id':6, 'tehsil_name':'Gujar Khan', 'distt':35 },
{ 'id':7, 'tehsil_name':'Lahore City', 'distt':23 },
{ 'id':8, 'tehsil_name':'Lahore Cantt', 'distt':23 },
{ 'id':9, 'tehsil_name':'Attock', 'distt':7 },
{ 'id':10, 'tehsil_name':'Hassanabdal', 'distt':7 },
{ 'id':11, 'tehsil_name':'Fateh jang', 'distt':7 },
{ 'id':12, 'tehsil_name':'Pindi Gheb', 'distt':7 },
{ 'id':13, 'tehsil_name':'Jand', 'distt':7 },
{ 'id':14, 'tehsil_name':'Mankera', 'distt':10 },
{ 'id':15, 'tehsil_name':'Kalur Kot', 'distt':10 },
{ 'id':16, 'tehsil_name':'Bhakkar', 'distt':10 },
{ 'id':17, 'tehsil_name':'Darya khan', 'distt':10 },
{ 'id':18, 'tehsil_name':'Chakwal', 'distt':11 },
{ 'id':19, 'tehsil_name':'Talagang', 'distt':11 },
{ 'id':20, 'tehsil_name':'Choa Saidan Shah', 'distt':11 },
{ 'id':21, 'tehsil_name':'Faislabad City', 'distt':13 },
{ 'id':22, 'tehsil_name':'Faislabad Saddar', 'distt':13 },
{ 'id':23, 'tehsil_name':'Chak Jhumra', 'distt':13 },
{ 'id':24, 'tehsil_name':'Sammundri', 'distt':13 },
{ 'id':25, 'tehsil_name':'jaranwala', 'distt':13 },
{ 'id':26, 'tehsil_name':'Tandianwala', 'distt':13 },
{ 'id':27, 'tehsil_name':'Wazirabad', 'distt':14 },
{ 'id':28, 'tehsil_name':'Gujranwala city', 'distt':14 },
{ 'id':29, 'tehsil_name':'Gujranwala Saddar', 'distt':14 },
{ 'id':30, 'tehsil_name':'Nowshera vikran', 'distt':14 },
{ 'id':31, 'tehsil_name':'Kamoki', 'distt':14 },
{ 'id':32, 'tehsil_name':'Gujrat', 'distt':15 },
{ 'id':33, 'tehsil_name':'Kharian', 'distt':15 },
{ 'id':34, 'tehsil_name':'Lodhran', 'distt':25 },
{ 'id':35, 'tehsil_name':'Sarai Alamgir', 'distt':15 },
{ 'id':36, 'tehsil_name':'Kahror Pacca', 'distt':25 },
{ 'id':37, 'tehsil_name':'Hafizabad', 'distt':16 },
{ 'id':38, 'tehsil_name':'Duniyapur', 'distt':25 },
{ 'id':39, 'tehsil_name':' Pindi Bhattian', 'distt':16 },
{ 'id':40, 'tehsil_name':'chaubara', 'distt':24 },
{ 'id':41, 'tehsil_name':'Karor Lal Esan', 'distt':24 },
{ 'id':42, 'tehsil_name':'Chiniot ', 'distt':146 },
{ 'id':45, 'tehsil_name':'Jhang', 'distt':18 },
{ 'id':46, 'tehsil_name':'Lahore Cantt.', 'distt':23 },
{ 'id':50, 'tehsil_name':'Shorkot', 'distt':18 },
{ 'id':51, 'tehsil_name':'Jehlum', 'distt':19 },
{ 'id':52, 'tehsil_name':'Sohawa ', 'distt':19 },
{ 'id':53, 'tehsil_name':'Pind Dadan Khan ', 'distt':19 },
{ 'id':54, 'tehsil_name':'Dina', 'distt':19 },
{ 'id':55, 'tehsil_name':'Kasur', 'distt':20 },
{ 'id':56, 'tehsil_name':'Chunian ', 'distt':20 },
{ 'id':57, 'tehsil_name':'Pattoki', 'distt':20 },
{ 'id':58, 'tehsil_name':'Minchinabad', 'distt':8 },
{ 'id':59, 'tehsil_name':'Bahawalnagar ', 'distt':8 },
{ 'id':60, 'tehsil_name':'Fort Abbas ', 'distt':8 },
{ 'id':61, 'tehsil_name':'Haroonabad ', 'distt':8 },
{ 'id':62, 'tehsil_name':'Chishtian ', 'distt':8 },
{ 'id':63, 'tehsil_name':'Hasilpur ', 'distt':9 },
{ 'id':64, 'tehsil_name':'Bahawalpur ', 'distt':9 },
{ 'id':65, 'tehsil_name':'Yazman ', 'distt':9 },
{ 'id':66, 'tehsil_name':'Ahmadpur East ', 'distt':9 },
{ 'id':67, 'tehsil_name':'Khairpur Tamewali', 'distt':9 },
{ 'id':68, 'tehsil_name':'Khushab ', 'distt':22 },
{ 'id':69, 'tehsil_name':'Nurpur ', 'distt':22 },
{ 'id':70, 'tehsil_name':'Mianwali', 'distt':27 },
{ 'id':71, 'tehsil_name':'Isa Khel ', 'distt':27 },
{ 'id':72, 'tehsil_name':'Piplan', 'distt':27 },
{ 'id':73, 'tehsil_name':'Multan City', 'distt':28 },
{ 'id':74, 'tehsil_name':'ziarat', 'distt':131 },
{ 'id':75, 'tehsil_name':'Harnai', 'distt':131 },
{ 'id':76, 'tehsil_name':'sinjawi', 'distt':131 },
{ 'id':77, 'tehsil_name':'zhob', 'distt':130 },
{ 'id':78, 'tehsil_name':'sambaza', 'distt':130 },
{ 'id':79, 'tehsil_name':'sherani', 'distt':130 },
{ 'id':80, 'tehsil_name':'Qamar Din Karez', 'distt':130 },
{ 'id':81, 'tehsil_name':'Ashwat', 'distt':130 },
{ 'id':82, 'tehsil_name':'sibi', 'distt':129 },
{ 'id':83, 'tehsil_name':'kutmandai', 'distt':129 },
{ 'id':84, 'tehsil_name':'sangan', 'distt':129 },
{ 'id':85, 'tehsil_name':'Lehri', 'distt':129 },
{ 'id':86, 'tehsil_name':'quetta', 'distt':128 },
{ 'id':87, 'tehsil_name':'Panjpai', 'distt':128 },
{ 'id':88, 'tehsil_name':'Multan Saddar', 'distt':28 },
{ 'id':89, 'tehsil_name':'Shujabad ', 'distt':28 },
{ 'id':90, 'tehsil_name':'Jalalpur Pirwala', 'distt':28 },
{ 'id':91, 'tehsil_name':'Muzaffargarh', 'distt':29 },
{ 'id':92, 'tehsil_name':'Alipur', 'distt':29 },
{ 'id':93, 'tehsil_name':'jatoi', 'distt':29 },
{ 'id':94, 'tehsil_name':'Kot Addu', 'distt':29 },
{ 'id':95, 'tehsil_name':'Narowal', 'distt':30 },
{ 'id':96, 'tehsil_name':'Shakargarh ', 'distt':30 },
{ 'id':97, 'tehsil_name':'Okara', 'distt':31 },
{ 'id':98, 'tehsil_name':'Depalpur ', 'distt':31 },
{ 'id':99, 'tehsil_name':'Renala Khurd', 'distt':31 },
{ 'id':100, 'tehsil_name':'Pakpattan', 'distt':32 },
{ 'id':101, 'tehsil_name':'Arifwala ', 'distt':32 },
{ 'id':102, 'tehsil_name':'Liaquatpur ', 'distt':33 },
{ 'id':103, 'tehsil_name':'Khanpur ', 'distt':33 },
{ 'id':104, 'tehsil_name':'Rahim Yar Khan', 'distt':33 },
{ 'id':105, 'tehsil_name':'Sadiqabad ', 'distt':33 },
{ 'id':106, 'tehsil_name':'pishin', 'distt':127 },
{ 'id':107, 'tehsil_name':'Rajanpur', 'distt':34 },
{ 'id':108, 'tehsil_name':'Rojhan ', 'distt':34 },
{ 'id':109, 'tehsil_name':'Jampur', 'distt':34 },
{ 'id':110, 'tehsil_name':'Hurramzai', 'distt':127 },
{ 'id':111, 'tehsil_name':'De-Ex.Area of Rajanpur', 'distt':34 },
{ 'id':112, 'tehsil_name':'Sahiwal', 'distt':36 },
{ 'id':113, 'tehsil_name':'Chichawatni ', 'distt':36 },
{ 'id':114, 'tehsil_name':'Barshore', 'distt':127 },
{ 'id':115, 'tehsil_name':'Sargodha', 'distt':37 },
{ 'id':116, 'tehsil_name':'Karezat', 'distt':127 },
{ 'id':117, 'tehsil_name':'Sillanwali', 'distt':37 },
{ 'id':118, 'tehsil_name':'Bhalwal ', 'distt':37 },
{ 'id':119, 'tehsil_name':'Shahpur ', 'distt':37 },
{ 'id':121, 'tehsil_name':'Bostan', 'distt':127 },
{ 'id':123, 'tehsil_name':'Kot Momin', 'distt':37 },
{ 'id':124, 'tehsil_name':'Ferozewala ', 'distt':38 },
{ 'id':125, 'tehsil_name':'Nankana Sahib ', 'distt':133 },
{ 'id':126, 'tehsil_name':'Sheikhupura ', 'distt':38 },
{ 'id':127, 'tehsil_name':'Panjgur', 'distt':126 },
{ 'id':128, 'tehsil_name':'Parome', 'distt':126 },
{ 'id':129, 'tehsil_name':'Safdarabad', 'distt':133 },
{ 'id':130, 'tehsil_name':'Gichk', 'distt':126 },
{ 'id':131, 'tehsil_name':'Gowargo', 'distt':126 },
{ 'id':132, 'tehsil_name':'Sialkot', 'distt':39 },
{ 'id':133, 'tehsil_name':'Daska ', 'distt':39 },
{ 'id':134, 'tehsil_name':'Pasrur ', 'distt':39 },
{ 'id':135, 'tehsil_name':'chattar', 'distt':125 },
{ 'id':136, 'tehsil_name':'Tamboo', 'distt':125 },
{ 'id':137, 'tehsil_name':'Vehari', 'distt':41 },
{ 'id':138, 'tehsil_name':'D.M.jamali', 'distt':125 },
{ 'id':139, 'tehsil_name':'Burewala ', 'distt':41 },
{ 'id':140, 'tehsil_name':'Mailsi ', 'distt':41 },
{ 'id':141, 'tehsil_name':'Mastung', 'distt':124 },
{ 'id':142, 'tehsil_name':'Kirdgap', 'distt':124 },
{ 'id':143, 'tehsil_name':'Dasht', 'distt':124 },
{ 'id':144, 'tehsil_name':'Khad Koocha', 'distt':124 },
{ 'id':145, 'tehsil_name':'Dera Ghazi Khan', 'distt':12 },
{ 'id':146, 'tehsil_name':'Taunsa ', 'distt':12 },
{ 'id':147, 'tehsil_name':'Musakhel', 'distt':123 },
{ 'id':148, 'tehsil_name':'Kingri', 'distt':123 },
{ 'id':149, 'tehsil_name':'De-Ex.Area of D.G.Khan', 'distt':12 },
{ 'id':150, 'tehsil_name':'Loralai/Bori', 'distt':122 },
{ 'id':151, 'tehsil_name':'Mekhpar', 'distt':122 },
{ 'id':152, 'tehsil_name':'Duki', 'distt':122 },
{ 'id':153, 'tehsil_name':'Abbottabad', 'distt':42 },
{ 'id':154, 'tehsil_name':'Bannu', 'distt':43 },
{ 'id':155, 'tehsil_name':'Bela', 'distt':121 },
{ 'id':156, 'tehsil_name':'Batagram', 'distt':44 },
{ 'id':157, 'tehsil_name':'Uthal', 'distt':121 },
{ 'id':158, 'tehsil_name':'Lakhra', 'distt':121 },
{ 'id':159, 'tehsil_name':'Liari', 'distt':121 },
{ 'id':160, 'tehsil_name':'Hub', 'distt':121 },
{ 'id':161, 'tehsil_name':'Gadani', 'distt':121 },
{ 'id':162, 'tehsil_name':'Allai', 'distt':44 },
{ 'id':163, 'tehsil_name':'Sonmiani/Winder', 'distt':121 },
{ 'id':164, 'tehsil_name':'Duraji', 'distt':121 },
{ 'id':165, 'tehsil_name':'Kanraj', 'distt':121 },
{ 'id':166, 'tehsil_name':'Daggar/Buner ', 'distt':45 },
{ 'id':167, 'tehsil_name':'Kohlu', 'distt':120 },
{ 'id':168, 'tehsil_name':'Kahan', 'distt':120 },
{ 'id':169, 'tehsil_name':'Mawand', 'distt':120 },
{ 'id':170, 'tehsil_name':'', 'distt':119 },
{ 'id':171, 'tehsil_name':'Charsadda', 'distt':46 },
{ 'id':172, 'tehsil_name':'Tangi ', 'distt':46 },
{ 'id':173, 'tehsil_name':'Chitral', 'distt':47 },
{ 'id':174, 'tehsil_name':'Drosh', 'distt':47 },
{ 'id':175, 'tehsil_name':'Lutkoh', 'distt':47 },
{ 'id':179, 'tehsil_name':'Mastuj', 'distt':47 },
{ 'id':180, 'tehsil_name':'Turkoh', 'distt':47 },
{ 'id':181, 'tehsil_name':'Mulkoh', 'distt':47 },
{ 'id':182, 'tehsil_name':'Killa Saifullah', 'distt':119 },
{ 'id':183, 'tehsil_name':'Muslim Bagh', 'distt':119 },
{ 'id':184, 'tehsil_name':'Loiband', 'distt':119 },
{ 'id':185, 'tehsil_name':'Baddini', 'distt':119 },
{ 'id':186, 'tehsil_name':'Killa Abdullah', 'distt':118 },
{ 'id':187, 'tehsil_name':'Hangu', 'distt':50 },
{ 'id':188, 'tehsil_name':'Gulistan', 'distt':14 },
{ 'id':189, 'tehsil_name':'Chaman', 'distt':118 },
{ 'id':190, 'tehsil_name':'Haripur', 'distt':51 },
{ 'id':191, 'tehsil_name':'Dobandi', 'distt':118 },
{ 'id':192, 'tehsil_name':'Ghazi', 'distt':51 },
{ 'id':193, 'tehsil_name':'Karak', 'distt':52 },
{ 'id':194, 'tehsil_name':'Banda Daud Shah ', 'distt':52 },
{ 'id':195, 'tehsil_name':'Khuzdar', 'distt':117 },
{ 'id':196, 'tehsil_name':'Zehri', 'distt':117 },
{ 'id':197, 'tehsil_name':'Takht-E-Nasrati', 'distt':52 },
{ 'id':198, 'tehsil_name':'Moola', 'distt':117 },
{ 'id':199, 'tehsil_name':'Karakh', 'distt':118 },
{ 'id':200, 'tehsil_name':'Kohat', 'distt':53 },
{ 'id':201, 'tehsil_name':'Nal', 'distt':117 },
{ 'id':202, 'tehsil_name':'Wadh', 'distt':117 },
{ 'id':203, 'tehsil_name':'Lachi', 'distt':53 },
{ 'id':204, 'tehsil_name':'Oranch', 'distt':117 },
{ 'id':205, 'tehsil_name':'Saroona', 'distt':117 },
{ 'id':206, 'tehsil_name':'Aranji', 'distt':117 },
{ 'id':207, 'tehsil_name':'Kharan', 'distt':116 },
{ 'id':208, 'tehsil_name':'Besima', 'distt':116 },
{ 'id':209, 'tehsil_name':'Nag', 'distt':116 },
{ 'id':210, 'tehsil_name':'Wasuk', 'distt':116 },
{ 'id':211, 'tehsil_name':'Lakki Marwat', 'distt':55 },
{ 'id':212, 'tehsil_name':'Mashkhel', 'distt':116 },
{ 'id':213, 'tehsil_name':'Dera Ismail Khan', 'distt':49 },
{ 'id':214, 'tehsil_name':'Daraban', 'distt':49 },
{ 'id':215, 'tehsil_name':'Paharpur', 'distt':49 },
{ 'id':216, 'tehsil_name':'Kech', 'distt':115 },
{ 'id':217, 'tehsil_name':'Buleda', 'distt':115 },
{ 'id':218, 'tehsil_name':'Zamuran', 'distt':115 },
{ 'id':219, 'tehsil_name':'Kulachi', 'distt':49 },
{ 'id':220, 'tehsil_name':'Swat Ranizai', 'distt':56 },
{ 'id':221, 'tehsil_name':'Sam Ranizai ', 'distt':56 },
{ 'id':222, 'tehsil_name':'Hoshab', 'distt':115 },
{ 'id':223, 'tehsil_name':'Balnigor', 'distt':115 },
{ 'id':224, 'tehsil_name':'Mansehra', 'distt':57 },
{ 'id':226, 'tehsil_name':'Balakot ', 'distt':57 },
{ 'id':228, 'tehsil_name':'Oghi', 'distt':57 },
{ 'id':229, 'tehsil_name':'Tump', 'distt':115 },
{ 'id':230, 'tehsil_name':'Mand', 'distt':115 },
{ 'id':231, 'tehsil_name':'T.A.Adj.Mansehra Distt.', 'distt':57 },
{ 'id':232, 'tehsil_name':'Kalat', 'distt':114 },
{ 'id':233, 'tehsil_name':'Mangochar', 'distt':114 },
{ 'id':234, 'tehsil_name':'Johan', 'distt':114 },
{ 'id':235, 'tehsil_name':'Surab', 'distt':114 },
{ 'id':236, 'tehsil_name':'Gazg', 'distt':114 },
{ 'id':237, 'tehsil_name':'Mardan', 'distt':58 },
{ 'id':238, 'tehsil_name':'Takht Bhai ', 'distt':58 },
{ 'id':239, 'tehsil_name':'Nowshera', 'distt':59 },
{ 'id':240, 'tehsil_name':'Jhat pat', 'distt':112 },
{ 'id':241, 'tehsil_name':'Panhwar', 'distt':112 },
{ 'id':242, 'tehsil_name':'Peshawar', 'distt':60 },
{ 'id':243, 'tehsil_name':'Alpuri ', 'distt':61 },
{ 'id':244, 'tehsil_name':'Besham', 'distt':61 },
{ 'id':245, 'tehsil_name':'Chakesar', 'distt':61 },
{ 'id':246, 'tehsil_name':'Martung', 'distt':61 },
{ 'id':247, 'tehsil_name':'Usta Mohammad', 'distt':112 },
{ 'id':248, 'tehsil_name':' Gandaka', 'distt':112 },
{ 'id':249, 'tehsil_name':'Puran', 'distt':61 },
{ 'id':250, 'tehsil_name':'Gwadar', 'distt':111 },
# { 'id':251, 'tehsil_name':'Swabi', 'distt':63 },
{ 'id':252, 'tehsil_name':'Jiwani ', 'distt':111 },
{ 'id':253, 'tehsil_name':'Suntsar', 'distt':111 },
{ 'id':255, 'tehsil_name':'Lahor', 'distt':62 },
{ 'id':257, 'tehsil_name':'Pasni ', 'distt':111 },
{ 'id':259, 'tehsil_name':'Ormara', 'distt':111 },
{ 'id':262, 'tehsil_name':'Barang', 'distt':65 },
{ 'id':263, 'tehsil_name':'Charmang', 'distt':65 },
{ 'id':264, 'tehsil_name':'Khar Bajaur', 'distt':65 },
{ 'id':265, 'tehsil_name':'Mamund', 'distt':65 },
{ 'id':266, 'tehsil_name':'Salarzai ', 'distt':65 },
{ 'id':267, 'tehsil_name':'Utmankhel(Qzafi)', 'distt':65 },
{ 'id':268, 'tehsil_name':'Nawagai', 'distt':65 },
{ 'id':269, 'tehsil_name':'Dhadar', 'distt':108 },
{ 'id':270, 'tehsil_name':'Bhag', 'distt':108 },
{ 'id':271, 'tehsil_name':'Balanari', 'distt':108 },
{ 'id':272, 'tehsil_name':'Sani', 'distt':108 },
{ 'id':273, 'tehsil_name':'Khattan', 'distt':108 },
{ 'id':274, 'tehsil_name':'Mach', 'distt':108 },
{ 'id':275, 'tehsil_name':'Nushki', 'distt':109 },
{ 'id':276, 'tehsil_name':'Dalbandin ', 'distt':109 },
{ 'id':277, 'tehsil_name':'Chagai', 'distt':109 },
{ 'id':278, 'tehsil_name':'Nokundi', 'distt':109 },
{ 'id':279, 'tehsil_name':'Dak', 'distt':109 },
{ 'id':280, 'tehsil_name':'Taftan', 'distt':109 },
{ 'id':281, 'tehsil_name':'Mehar', 'distt':74 },
{ 'id':282, 'tehsil_name':'Khairpur Nathan Shah', 'distt':74 },
{ 'id':283, 'tehsil_name':'Sehwan', 'distt':74 },
{ 'id':284, 'tehsil_name':'Dadu', 'distt':74 },
{ 'id':285, 'tehsil_name':'Johi ', 'distt':74 },
{ 'id':286, 'tehsil_name':'Kotri', 'distt':74 },
{ 'id':287, 'tehsil_name':'Thano Bula Khan', 'distt':74 },
{ 'id':288, 'tehsil_name':'Faisalabad City', 'distt':13 },
{ 'id':290, 'tehsil_name':'Ghotki', 'distt':75 },
{ 'id':291, 'tehsil_name':'Khangarh', 'distt':75 },
{ 'id':292, 'tehsil_name':'Mirpur Mathelo', 'distt':75 },
{ 'id':293, 'tehsil_name':'Ubauro', 'distt':75 },
{ 'id':294, 'tehsil_name':'Daharki', 'distt':75 },
{ 'id':301, 'tehsil_name':'Umerkot', 'distt':93 },
{ 'id':302, 'tehsil_name':'Samaro', 'distt':93 },
{ 'id':303, 'tehsil_name':'Kunri', 'distt':93 },
{ 'id':304, 'tehsil_name':'pithoro', 'distt':93 },
{ 'id':305, 'tehsil_name':'Hala ', 'distt':76 },
{ 'id':306, 'tehsil_name':'Thatta', 'distt':92 },
{ 'id':307, 'tehsil_name':'Mirpur Sakro', 'distt':92 },
{ 'id':308, 'tehsil_name':'Matiari', 'distt':76 },
{ 'id':309, 'tehsil_name':'Keti Bunder', 'distt':92 },
{ 'id':310, 'tehsil_name':'Tando Allahyar', 'distt':76 },
{ 'id':312, 'tehsil_name':'Hyderabad City', 'distt':76 },
{ 'id':313, 'tehsil_name':'Latifabad', 'distt':76 },
{ 'id':314, 'tehsil_name':'Hyderabad', 'distt':76 },
{ 'id':316, 'tehsil_name':'Qasimabad', 'distt':76 },
{ 'id':317, 'tehsil_name':'Ghorabari', 'distt':92 },
{ 'id':318, 'tehsil_name':'Sujawal', 'distt':92 },
{ 'id':319, 'tehsil_name':'Mirpur Bathoro', 'distt':92 },
{ 'id':320, 'tehsil_name':'Jati', 'distt':92 },
{ 'id':321, 'tehsil_name':'Shah Bunder', 'distt':92 },
{ 'id':322, 'tehsil_name':'Kharo Chan', 'distt':92 },
{ 'id':323, 'tehsil_name':'Jacobabad ', 'distt':77 },
{ 'id':324, 'tehsil_name':'Garhi Khairo ', 'distt':77 },
{ 'id':325, 'tehsil_name':'Thul ', 'distt':77 },
{ 'id':326, 'tehsil_name':'Kandhkot ', 'distt':77 },
{ 'id':327, 'tehsil_name':'Kashmor ', 'distt':77 },
{ 'id':336, 'tehsil_name':'malir', 'distt':84 },
{ 'id':341, 'tehsil_name':'Chachro', 'distt':86 },
{ 'id':342, 'tehsil_name':'Nagar Parkar', 'distt':86 },
{ 'id':343, 'tehsil_name':'Diplo', 'distt':86 },
{ 'id':344, 'tehsil_name':'Mithi', 'distt':86 },
{ 'id':349, 'tehsil_name':'Khad Khocha', 'distt':124 },
{ 'id':351, 'tehsil_name':'Tank', 'distt':64 },
{ 'id':352, 'tehsil_name':'Toba Tek Singh', 'distt':40 },
{ 'id':353, 'tehsil_name':'Kamalia', 'distt':40 },
{ 'id':354, 'tehsil_name':'Gojra', 'distt':40 },
{ 'id':355, 'tehsil_name':'shikarpur', 'distt':90 },
{ 'id':356, 'tehsil_name':'Khanrpur', 'distt':90 },
{ 'id':357, 'tehsil_name':'Ghari Yasin', 'distt':90 },
{ 'id':358, 'tehsil_name':'Lakhi', 'distt':90 },
{ 'id':360, 'tehsil_name':'Pis', 'distt':127 },
{ 'id':362, 'tehsil_name':'Sudhnoti', 'distt':105 },
{ 'id':363, 'tehsil_name':'Central', 'distt':71 },
{ 'id':364, 'tehsil_name':'Lower', 'distt':71 },
{ 'id':365, 'tehsil_name':'Upper', 'distt':71 },
{ 'id':366, 'tehsil_name':'Poonch', 'distt':104 },
{ 'id':367, 'tehsil_name':'Ismailzai', 'distt':71 },
{ 'id':368, 'tehsil_name':'Muzaffarabad', 'distt':103 },
{ 'id':369, 'tehsil_name':'bagh', 'distt':105 },
{ 'id':371, 'tehsil_name':'Kotli', 'distt':101 },
{ 'id':376, 'tehsil_name':'Kandioro', 'distt':87 },
{ 'id':377, 'tehsil_name':'Naushrhro Feroze', 'distt':87 },
{ 'id':378, 'tehsil_name':'Bhiria', 'distt':87 },
{ 'id':379, 'tehsil_name':'Moro', 'distt':87 },
{ 'id':380, 'tehsil_name':'Sakrand', 'distt':88 },
{ 'id':381, 'tehsil_name':'Nawab Shah', 'distt':88 },
{ 'id':382, 'tehsil_name':'Daulatpur', 'distt':88 },
{ 'id':391, 'tehsil_name':'Khanewal ', 'distt':21 },
{ 'id':392, 'tehsil_name':'Jehanian', 'distt':21 },
{ 'id':393, 'tehsil_name':'Mian Channu ', 'distt':21 },
{ 'id':394, 'tehsil_name':'Kabirwala ', 'distt':21 },
{ 'id':395, 'tehsil_name':'Barkhan', 'distt':107 },
{ 'id':396, 'tehsil_name':'Mashkai', 'distt':106 },
{ 'id':397, 'tehsil_name':'Awaran', 'distt':106 },
{ 'id':398, 'tehsil_name':'Jhal Jao', 'distt':106 },
{ 'id':399, 'tehsil_name':'Golarchi ', 'distt':73 },
{ 'id':400, 'tehsil_name':'Badin ', 'distt':73 },
{ 'id':401, 'tehsil_name':'Matli', 'distt':73 },
{ 'id':402, 'tehsil_name':'Tando Bagho', 'distt':73 },
{ 'id':403, 'tehsil_name':'Talhar', 'distt':73 },
{ 'id':405, 'tehsil_name':'Dera Bugti', 'distt':110 },
{ 'id':406, 'tehsil_name':'Sangsillah', 'distt':110 },
{ 'id':407, 'tehsil_name':'Sui ', 'distt':110 },
{ 'id':408, 'tehsil_name':'Loti', 'distt':110 },
{ 'id':409, 'tehsil_name':'Phelawagh ', 'distt':110 },
{ 'id':410, 'tehsil_name':'Malam', 'distt':110 },
{ 'id':411, 'tehsil_name':'EntireUrban', 'distt':78 },
{ 'id':412, 'tehsil_name':'Entire Urban', 'distt':79 },
{ 'id':419, 'tehsil_name':'khairpur', 'distt':82 },
{ 'id':422, 'tehsil_name':'sobhodero', 'distt':82 },
{ 'id':424, 'tehsil_name':'Gambat', 'distt':82 },
{ 'id':425, 'tehsil_name':'kot Diji', 'distt':82 },
{ 'id':426, 'tehsil_name':'Mirwah', 'distt':82 },
{ 'id':427, 'tehsil_name':'Faiz Ganj', 'distt':82 },
{ 'id':428, 'tehsil_name':'Nara', 'distt':82 },
{ 'id':430, 'tehsil_name':'Bara', 'distt':67 },
{ 'id':431, 'tehsil_name':'Jamrud', 'distt':67 },
{ 'id':432, 'tehsil_name':'Landi Kotla', 'distt':67 },
{ 'id':433, 'tehsil_name':'Mula Ghori', 'distt':67 },
{ 'id':434, 'tehsil_name':'shahdadkot', 'distt':83 },
{ 'id':435, 'tehsil_name':'Miro khan', 'distt':83 },
{ 'id':436, 'tehsil_name':'Rato Dero', 'distt':83 },
{ 'id':437, 'tehsil_name':'Larkhana', 'distt':83 },
{ 'id':438, 'tehsil_name':'Dokri', 'distt':83 },
{ 'id':439, 'tehsil_name':'Kambar', 'distt':83 },
{ 'id':440, 'tehsil_name':'Warah', 'distt':83 },
{ 'id':441, 'tehsil_name':'Mirpur khas', 'distt':85 },
{ 'id':442, 'tehsil_name':'Digri', 'distt':85 },
{ 'id':443, 'tehsil_name':'Kot Ghulam Mohammad', 'distt':85 },
{ 'id':444, 'tehsil_name':'Sanghar', 'distt':89 },
{ 'id':445, 'tehsil_name':'Sinjhoro', 'distt':89 },
{ 'id':446, 'tehsil_name':'Khopro', 'distt':89 },
{ 'id':447, 'tehsil_name':'Shahdadpur', 'distt':89 },
{ 'id':448, 'tehsil_name':'Jam Nawaz Ali', 'distt':37 },
{ 'id':451, 'tehsil_name':'Tando Adam', 'distt':89 },
{ 'id':452, 'tehsil_name':'Sukkur', 'distt':91 },
{ 'id':453, 'tehsil_name':'Rohri', 'distt':91 },
{ 'id':454, 'tehsil_name':'Pano Aqil', 'distt':148 },
{ 'id':455, 'tehsil_name':'Salehpat', 'distt':91 },
{ 'id':456, 'tehsil_name':'Shah Kot', 'distt':133 },
{ 'id':457, 'tehsil_name':'Sangla Hill', 'distt':133 },
{ 'id':458, 'tehsil_name':'Bulri Shah Karim', 'distt':145 },
{ 'id':459, 'tehsil_name':'Tando Ghulam Hyder', 'distt':145 },
{ 'id':460, 'tehsil_name':'Tando Muhammad Khan', 'distt':145 },
{ 'id':461, 'tehsil_name':'M. B.Din', 'distt':26 },
{ 'id':462, 'tehsil_name':'Malikwal', 'distt':26 },
{ 'id':463, 'tehsil_name':'Phalia', 'distt':26 },
{ 'id':464, 'tehsil_name':'Athara Hazari', 'distt':18 },
{ 'id':465, 'tehsil_name':'Ahmad Pur Sial', 'distt':18 },
{ 'id':466, 'tehsil_name':'Lalian', 'distt':146 },
{ 'id':467, 'tehsil_name':'Bhowana', 'distt':146 },
{ 'id':469, 'tehsil_name':'Sehwan Sharif', 'distt':147 },
{ 'id':470, 'tehsil_name':'Thana Bulla Khan', 'distt':147 },
{ 'id':471, 'tehsil_name':'Manjhand', 'distt': 147 },
{ 'id':472, 'tehsil_name':'Islamabad', 'distt': 1 },
{ 'id':473, 'tehsil_name':'Bagh', 'distt': 94 },
{ 'id':474, 'tehsil_name':'Bhimber', 'distt':96 },
{ 'id':475, 'tehsil_name':'Ghizer', 'distt':99 },
{ 'id':476, 'tehsil_name':'Mirpur', 'distt':102 },
{ 'id':477, 'tehsil_name':'Muzaffarabad', 'distt':102 },
{ 'id':478, 'tehsil_name':'Jhal Magsi', 'distt':113 },
{ 'id':479, 'tehsil_name':'Baltistan', 'distt':66 },
{ 'id':480, 'tehsil_name':'Diamir', 'distt':97 },
{ 'id':481, 'tehsil_name':'Ghanche', 'distt':98 },
{ 'id':482, 'tehsil_name':'Gilgit', 'distt':100 },
{ 'id':483, 'tehsil_name':'Dir', 'distt':48 },
{ 'id':484, 'tehsil_name':'Kohistan', 'distt':54 },
{ 'id':485, 'tehsil_name':'Noushehra', 'distt':22 },
{ 'id':486, 'tehsil_name':'Karachi east', 'distt':79 },
{ 'id':487, 'tehsil_name':'Karachi west', 'distt':81 },
{ 'id':488, 'tehsil_name':'Karachi south', 'distt':80 },
{ 'id':489, 'tehsil_name':'Central Kurram', 'distt':68 },
{ 'id':490, 'tehsil_name':'Lower Kurram', 'distt':68 },
{ 'id':491, 'tehsil_name':'Upper Kurram', 'distt':68 },
{ 'id':492, 'tehsil_name':'Datta Khel', 'distt':70 },
{ 'id':493, 'tehsil_name':'Dossali', 'distt':70 },
{ 'id':494, 'tehsil_name':'Gharyum', 'distt':70 },
{ 'id':495, 'tehsil_name':'Ghulam Khan', 'distt':70 },
{ 'id':496, 'tehsil_name':'Mir Ali', 'distt':70 },
{ 'id':497, 'tehsil_name':'Miran Shah', 'distt':70 },
{ 'id':498, 'tehsil_name':'Razmak', 'distt':70 },
{ 'id':499, 'tehsil_name':'Shewa', 'distt':70 },
{ 'id':500, 'tehsil_name':'Spinwam', 'distt':70 },
{ 'id':501, 'tehsil_name':'Birmil', 'distt':72 },
{ 'id':502, 'tehsil_name':'Ladha', 'distt':72 },
{ 'id':503, 'tehsil_name':'Makin', 'distt':72 },
{ 'id':504, 'tehsil_name':'Sararogha', 'distt':72 },
{ 'id':505, 'tehsil_name':'Serwekai', 'distt':72 },
{ 'id':506, 'tehsil_name':'Tiarza', 'distt':72 },
{ 'id':507, 'tehsil_name':'Toi Khulla', 'distt':72 },
{ 'id':508, 'tehsil_name':'Wana', 'distt':72 },
{ 'id':509, 'tehsil_name':'Ambar Utman Khel', 'distt':69 },
{ 'id':510, 'tehsil_name':'Halim Zai', 'distt':69 },
{ 'id':511, 'tehsil_name':'Pindiali', 'distt':69 },
{ 'id':512, 'tehsil_name':'Pran Ghar', 'distt':69 },
{ 'id':513, 'tehsil_name':'Safi', 'distt':69 },
{ 'id':514, 'tehsil_name':'Upper Mohmand', 'distt':69 },
{ 'id':515, 'tehsil_name':'Ekka Ghund', 'distt':69 },
{ 'id':516, 'tehsil_name':'Lachi', 'distt':53 },
{ 'id':517, 'tehsil_name':'Domel', 'distt':43 },
{ 'id':518, 'tehsil_name':'Kaki', 'distt':43 },
{ 'id':519, 'tehsil_name':'Sari Naurang', 'distt':55 },
{ 'id':520, 'tehsil_name':'Paroa', 'distt':49 },
{ 'id':521, 'tehsil_name':'Astore', 'distt':132 },
{ 'id':522, 'tehsil_name':'Shounter', 'distt':132 },
{ 'id':523, 'tehsil_name':'Jahangira', 'distt':59 },
{ 'id':524, 'tehsil_name':'Pabbi', 'distt':59 },
{ 'id':525, 'tehsil_name':'Lund Khwar', 'distt':58 },
{ 'id':526, 'tehsil_name':'Rustam', 'distt':58 },
{ 'id':527, 'tehsil_name':'Katlang', 'distt':58 },
{ 'id':528, 'tehsil_name':'Baffa Pakhal', 'distt':57 },
{ 'id':529, 'tehsil_name':'Darband', 'distt':57 },
{ 'id':530, 'tehsil_name':'Havelian', 'distt':42 },
{ 'id':531, 'tehsil_name':'Ghara ', 'distt':45 },
{ 'id':532, 'tehsil_name':'Khudu Khel ', 'distt':45 },
{ 'id':533, 'tehsil_name':'Mandanr ', 'distt':45 },
{ 'id':534, 'tehsil_name':'Shabqadar', 'distt':46 },
{ 'id':535, 'tehsil_name':'Timergara', 'distt':149 },
{ 'id':536, 'tehsil_name':'Adenzai', 'distt':149 },
{ 'id':537, 'tehsil_name':'Lal Qilla', 'distt':149 },
{ 'id':538, 'tehsil_name':'Samarbagh', 'distt':149 },
{ 'id':539, 'tehsil_name':'Sharingal', 'distt':48 },
{ 'id':540, 'tehsil_name':'Wari', 'distt':48 },
{ 'id':541, 'tehsil_name':'Tall', 'distt':50 },
{ 'id':542, 'tehsil_name':'Ghazi', 'distt':51 },
{ 'id':543, 'tehsil_name':'Khanpur', 'distt':51 },
{ 'id':544, 'tehsil_name':'Kandia', 'distt':54 },
{ 'id':545, 'tehsil_name':'Bankad', 'distt':54 },
{ 'id':546, 'tehsil_name':'Pattan', 'distt':54 },
{ 'id':547, 'tehsil_name':'Model Town', 'distt':23 },
{ 'id':548, 'tehsil_name':'Raiwind', 'distt':23 },
{ 'id':549, 'tehsil_name':'Shalimar', 'distt':23 },
{ 'id':550, 'tehsil_name':'Kot Radha Kishan', 'distt':20 },
{ 'id':551, 'tehsil_name':'Murdike', 'distt':38 },
{ 'id':552, 'tehsil_name':'Safdrabad', 'distt':38 },
{ 'id':553, 'tehsil_name':'Sharqpur', 'distt':38 },
{ 'id':554, 'tehsil_name':'Zafarwal', 'distt':30 },
{ 'id':555, 'tehsil_name':'Sambrial', 'distt':39 },
{ 'id':556, 'tehsil_name':'Kallar Syedan', 'distt':35 },
{ 'id':557, 'tehsil_name':'Bhera', 'distt':37 },
{ 'id':558, 'tehsil_name':'Sahiwall', 'distt':37 },
{ 'id':559, 'tehsil_name':'Quaidabad', 'distt':22 },
# { 'id':560, 'tehsil_name':'Babuzai', 'distt':63 },
{ 'id':561, 'tehsil_name':'Barikot', 'distt':63 },
{ 'id':562, 'tehsil_name':'Bahrain', 'distt':63 },
# { 'id':563, 'tehsil_name':'Charbagh ', 'distt':63 },
# { 'id':564, 'tehsil_name':'Kabal ', 'distt':63 },
# { 'id':565, 'tehsil_name':'Khwaza Khela ', 'distt':63 },
{ 'id':566, 'tehsil_name':'Razzar', 'distt':62 },
{ 'id':567, 'tehsil_name':'Topi', 'distt':62 },
{ 'id':568, 'tehsil_name':'Hazro', 'distt':7 },
{ 'id':569, 'tehsil_name':'Kot Chutta', 'distt':12 },
{ 'id':570, 'tehsil_name':'Jalalpur Jatan', 'distt':15 },
{ 'id':571, 'tehsil_name':'Samahni', 'distt':96 },
{ 'id':572, 'tehsil_name':'Barnala', 'distt':96 },
{ 'id':573, 'tehsil_name':'Dhirkot', 'distt': 94 },
{ 'id':574, 'tehsil_name':'Hari Ghel', 'distt': 94 },
{ 'id':575, 'tehsil_name':'Rera', 'distt': 94 },
{ 'id':576, 'tehsil_name':'Birpani', 'distt': 94 },
{ 'id':577, 'tehsil_name':'Char Hoi', 'distt':101 },
{ 'id':578, 'tehsil_name':'Sehnsa', 'distt':101 },
{ 'id':579, 'tehsil_name':'Fatehpur Nakyal', 'distt':101 },
{ 'id':580, 'tehsil_name':'Khuiratta', 'distt':101 },
{ 'id':581, 'tehsil_name':'Dilyan Jattan', 'distt':101 },
{ 'id':582, 'tehsil_name':'Dadyal', 'distt':102 },
{ 'id':583, 'tehsil_name':'Nasirbbad', 'distt':103 },
{ 'id':584, 'tehsil_name':'Neelum', 'distt':150 },
{ 'id':585, 'tehsil_name':'Athmuqam', 'distt':150 },
{ 'id':586, 'tehsil_name':'Sharda', 'distt':150 },
{ 'id':587, 'tehsil_name':'Abbaspur', 'distt':104 },
{ 'id':588, 'tehsil_name':'Hajira', 'distt':104 },
{ 'id':589, 'tehsil_name':'Rawalakot', 'distt':104 },
{ 'id':590, 'tehsil_name':'Thorar', 'distt':104 },
{ 'id':591, 'tehsil_name':'Balouch', 'distt':105 },
{ 'id':592, 'tehsil_name':'Mang', 'distt':105 },
{ 'id':593, 'tehsil_name':'Palandri', 'distt':105 },
{ 'id':594, 'tehsil_name':'Tarar Khal', 'distt':105 },
{ 'id':595, 'tehsil_name':'Hattian Bhala', 'distt':151 },
{ 'id':596, 'tehsil_name':'Chikkar', 'distt':151 },
{ 'id':597, 'tehsil_name':'Leepa', 'distt':151 },
{ 'id':598, 'tehsil_name':'Haveli', 'distt':152 },
{ 'id':599, 'tehsil_name':'Khurshidabad', 'distt':152 },
{ 'id':600, 'tehsil_name':'Mumtazabad', 'distt':152 },
{ 'id':601, 'tehsil_name':'Babusar', 'distt':97 },
{ 'id':602, 'tehsil_name':'Chilas', 'distt':97 },
{ 'id':603, 'tehsil_name':'Daghoni', 'distt':98 },
{ 'id':604, 'tehsil_name':'Khaplu', 'distt':98 },
{ 'id':605, 'tehsil_name':'Mashabrum', 'distt':98 },
{ 'id':606, 'tehsil_name':'Chorbut', 'distt':98 },
{ 'id':607, 'tehsil_name':'Keris', 'distt':98 },
{ 'id':608, 'tehsil_name':'Haldi', 'distt':98 },
{ 'id':609, 'tehsil_name':'Danyor', 'distt':100 },
{ 'id':610, 'tehsil_name':'Juglot', 'distt':100 },
{ 'id':611, 'tehsil_name':'Gultari', 'distt':153 },
{ 'id':612, 'tehsil_name':'Skardu', 'distt':153 },
{ 'id':613, 'tehsil_name':'Gamba', 'distt':153 },
{ 'id':614, 'tehsil_name':'Rodu', 'distt':153 },
{ 'id':615, 'tehsil_name':'Rondu', 'distt':154 },
{ 'id':616, 'tehsil_name':'Shigar', 'distt':155 },
{ 'id':617, 'tehsil_name':'Gulabpur', 'distt':155 },
{ 'id':618, 'tehsil_name':'Kharmang', 'distt':156 },
{ 'id':619, 'tehsil_name':'Darel', 'distt':157 },
{ 'id':620, 'tehsil_name':'Tangir', 'distt':158 },
{ 'id':621, 'tehsil_name':'Punial', 'distt':159 },
{ 'id':622, 'tehsil_name':'Ishkoman', 'distt':159 },
{ 'id':623, 'tehsil_name':'Gopis', 'distt':160 },
{ 'id':624, 'tehsil_name':'Yasin', 'distt':160 },
{ 'id':625, 'tehsil_name':'Phander', 'distt':160 },
{ 'id':626, 'tehsil_name':'Hunza', 'distt':161 },
{ 'id':627, 'tehsil_name':'Aliabad', 'distt':161 },
{ 'id':628, 'tehsil_name':'Gojal', 'distt':161 },
{ 'id':629, 'tehsil_name':'Nagar-1', 'distt':162 },
{ 'id':630, 'tehsil_name':'Nagar-2', 'distt':162 },
{ 'id':631, 'tehsil_name':'Chalt', 'distt':162 },
]



qual_type = [
    
    {
        'id': 1, 'qual_name': 'Matriculation', 'qual_years' : '1000'
    },
    {
        'id': 2, 'qual_name': 'O Levels', 'qual_years' : '1000'
    },
    {
        'id': 3, 'qual_name': 'Intermediate', 'qual_years' : '1000'
    },
    {
        'id': 4, 'qual_name': 'A Levels', 'qual_years' : '1000'
    },
    {
        'id': 5, 'qual_name': 'I.Com', 'qual_years' : '1000'
    },
    {
        'id': 6, 'qual_name': 'FCS', 'qual_years' : '1000'
    },
    {
        'id': 7, 'qual_name': 'FA', 'qual_years' : '1000'
    },
    {
        'id': 8, 'qual_name': 'F.Sc', 'qual_years' : '1000'
    },
    {
        'id': 9, 'qual_name': 'F.Com', 'qual_years' : '1000'
    },
    {
        'id': 10, 'qual_name': 'ICS', 'qual_years' : '1000'
    },
    {
        'id': 11, 'qual_name': 'D.Com', 'qual_years' : '1000'
    },
    {
        'id': 12, 'qual_name': 'DAE', 'qual_years' : '1000'
    },
    {
        'id': 13, 'qual_name': 'BA', 'qual_years' : '1000'
    },
    {
        'id': 14, 'qual_name': 'B.Com', 'qual_years' : '1000'
    },
    {
        'id': 15, 'qual_name': 'B.Ed', 'qual_years' : '1000'
    },
    {
        'id': 16, 'qual_name': 'B.Sc.', 'qual_years' : '1000'
    },
    {
        'id': 17, 'qual_name': 'BDS', 'qual_years' : '1000'
    },
    {
        'id': 18, 'qual_name': 'Bachelor of Engineering(BE)', 'qual_years' : '1000'
    },
    {
        'id': 19, 'qual_name': 'MBBS', 'qual_years' : '1000'
    },
    {
        'id': 20, 'qual_name': 'B.TECH', 'qual_years' : '1000'
    },
    {
        'id': 21, 'qual_name': 'BBA', 'qual_years' : '1000'
    },
    {
        'id': 22, 'qual_name': 'BS', 'qual_years' : '1000'
    },
    {
        'id': 23, 'qual_name': 'BS Hons', 'qual_years' : '1000'
    },
    {
        'id': 24, 'qual_name': 'LLB', 'qual_years' : '1000'
    },
    {
        'id': 25, 'qual_name': 'BCS', 'qual_years' : '1000'
    },
    {
        'id': 26, 'qual_name': 'BA Hons', 'qual_years' : '1000'
    },
    {
        'id': 27, 'qual_name': 'MA', 'qual_years' : '1000'
    },
    
    {
        'id': 28, 'qual_name': 'M.Sc.', 'qual_years' : '1000'
    },
    {
        'id': 29, 'qual_name': 'MBA', 'qual_years' : '1000'
    },
    {
        'id': 30, 'qual_name': 'M.Ed', 'qual_years' : '1000'
    },
    {
        'id': 31, 'qual_name': 'MS', 'qual_years' : '1000'
    },
    {
        'id': 32, 'qual_name': 'M. Phil', 'qual_years' : '1000'
    },
    {
        'id': 33, 'qual_name': 'FCPS', 'qual_years' : '1000'
    },
    {
        'id': 34, 'qual_name': 'M.Com', 'qual_years' : '1000'
    },
    {
        'id': 35, 'qual_name': 'MCS', 'qual_years' : '1000'
    },
    {
        'id': 36, 'qual_name': 'PHD', 'qual_years' : '1000'
    },
    {
        'id': 37, 'qual_name': 'Hafiz-e-Quran', 'qual_years' : '1000'
    },

]

education_board = [
    
    {
        'id': 1, 'board_name': 'Agha Khan Uoniversity Examination Board '
    },
    {
        'id': 2, 'board_name': 'Allama Iqbal Open Uiniversity'
    },
    {
        'id': 3, 'board_name': 'Balochistan Board of intermediate & Secondary education Quetta'
    },
    {
        'id': 4, 'board_name': 'Board of intermediate & Secondary Board of Hyderebad(Sindh)'
    },
    {
        'id': 5, 'board_name': 'Federal Board of intermediate & Secondary education Islamabad'
    },
    {
        'id': 6, 'board_name': 'The AJ&K Board of intermediate & Secondary education Mirpur(AK)'
    },
    {
        'id': 7, 'board_name': 'The Armed Forces Board for higher education GHQ, Rawalpindi'
    },
    {
        'id': 8, 'board_name': 'The Board of intermediate & Secondary Education Abbotabad'
    },
    {
        'id': 9, 'board_name': 'The Board of intermediate & Secondary Education Bahawalpur'
    },
    {
        'id': 10, 'board_name': 'The Board of intermediate & Secondary Education Bannu'
    },
    {
        'id': 11, 'board_name': 'The Board of intermediate & Secondary Education Dera Khazi Khan'
    },
    {
        'id': 12, 'board_name': 'The Board of intermediate & Secondary Education Dera Ismail Khan'
    },
    {
        'id': 13, 'board_name': 'The Board of intermediate & Secondary Education Faisalabad'
    },
    {
        'id': 14, 'board_name': 'The Board of intermediate & Secondary Education Gujranwala'
    },
    {
        'id': 15, 'board_name': 'The Board of intermediate & Secondary Education Karachi'
    },
    {
        'id': 16, 'board_name': 'The Board of intermediate & Secondary Education Kohat'
    },
    {
        'id': 17, 'board_name': 'The Board of intermediate & Secondary Education Lahore'
    },
    {
        'id': 18, 'board_name': 'The Board of intermediate & Secondary Education Larkana'
    },
    {
        'id': 19, 'board_name': 'The Board of intermediate & Secondary Education Malakand'
    },
    {
        'id': 20, 'board_name': 'The Board of intermediate & Secondary Education Mardan'
    },
    {
        'id': 21, 'board_name': 'The Board of intermediate & Secondary Education Mirpur Khas(Sind)'
    },
    {
        'id': 22, 'board_name': 'The Board of intermediate & Secondary Education Multan'
    },
    {
        'id': 23, 'board_name': 'The Board of intermediate & Secondary Education Peshawar'
    },
    {
        'id': 24, 'board_name': 'The Board of intermediate & Secondary Education Rawalpindi'
    },
    {
        'id': 25, 'board_name': 'The Board of intermediate & Secondary Education Saidu Sharif Swat'
    },
    {
        'id': 26, 'board_name': 'The Board of intermediate & Secondary Education Sargodha'
    },
    {
        'id': 27, 'board_name': 'The Board of intermediate & Secondary Education Sukkur(Sind)'
    },
    
    {
        'id': 28, 'board_name': 'The Board of intermediate & Secondary Education Sahiwal'
    },
    {
        'id': 29, 'board_name': 'The Board of technical Education Peshaewar(BTE)'
    },
    {
        'id': 30, 'board_name': 'The Inter Bord of Committee of Chairman Government of Pakistan'
    },
    {
        'id': 31, 'board_name': 'The Karakurum intermediate University Gilgit'
    },
    {
        'id': 32, 'board_name': 'The Punjab Board of Technical Education Lahore'
    },
    {
        'id': 33, 'board_name': 'The School of Electronics, Pakistan Air Force Korrangi Karachi'
    },
    {
        'id': 34, 'board_name': 'The Sind Board of Technical Eduction, Karachi'
    },
    {
        'id': 35, 'board_name': 'Zia ud Din University Examination board, Karachi'
    },
    {
        'id': 36, 'board_name': 'Board of Intermediate and Secondary Education SBA'
    },

]





centers = [    
    {
        'id': 1, 'center_name': 'ASRC Rawalpindi', 'center_located' : 'Rawalpindi', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '202.147.161.19', 'abbrv' : 'RWP'
    },
    {
        'id': 2, 'center_name': 'ASRO Jehlum', 'center_located' : 'Jhelum', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asro', 'static_ip' : '0.0.0.0', 'abbrv' : 'JMR'
    },
    {
        'id': 3, 'center_name': 'ASRC Muzaffarabad', 'center_located' : 'Muzaffarabad', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '118.107.130.209', 'abbrv' : 'MZD'
    },
    {
        'id': 4, 'center_name': 'ASRC Lahore', 'center_located' : 'Lahore', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '202.83.170.86', 'abbrv' : 'LHR'
    },
    {
        'id': 5, 'center_name': 'ASRO Sialkot', 'center_located' : 'Sialkot', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asro', 'static_ip' : '0.0.0.0', 'abbrv' : 'SLK'
    },
    {
        'id': 6, 'center_name': 'ASRC Faisalabad', 'center_located' : 'Faisalabad', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '182.180.100.52', 'abbrv' : 'FSD'
    },
    {
        'id': 7, 'center_name': 'ASRC Peshawer', 'center_located' : 'Peshawar', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '202.83.167.238', 'abbrv' : 'PSH'
    },
    {
        'id': 8, 'center_name': 'ASRO D.I.Khan', 'center_located' : 'D I Khan', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asro', 'static_ip' : '0.0.0.0', 'abbrv' : 'DIK'
    },
    {
        'id': 9, 'center_name': 'ASRO Kohat', 'center_located' : 'Kohat', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asro', 'static_ip' : '0.0.0.0', 'abbrv' : 'KHT'
    },
    {
        'id': 10, 'center_name': 'ASRC Quetta', 'center_located' : 'Quetta', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '58.65.192.72', 'abbrv' : 'QTA'
    },
    {
        'id': 11, 'center_name': 'ASRO Turbat', 'center_located' : 'Kech/Turbat', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asro', 'static_ip' : '0.0.0.0', 'abbrv' : 'TBT'
    },
    {
        'id': 12, 'center_name': 'ASRO Loralai', 'center_located' : 'Loralai', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asro', 'static_ip' : '0.0.0.0', 'abbrv' : 'LLI'
    },
    {
        'id': 13, 'center_name': 'ASRO Khuzdar', 'center_located' : 'Khuzdar', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asro', 'static_ip' : '0.0.0.0', 'abbrv' : 'KZD'
    },
    {
        'id': 14, 'center_name': 'ASRC Karachi', 'center_located' : 'Karachi', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '202.147.160.141', 'abbrv' : 'KHI'
    },
    {
        'id': 15, 'center_name': 'ASRC Multan', 'center_located' : 'Multan', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '58.65.192.57', 'abbrv' : 'MTN'
    },
    {
        'id': 16, 'center_name': 'ASRO Sargodha', 'center_located' : 'Sargodha', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asro', 'static_ip' : '0.0.0.0', 'abbrv' : 'SGD'
    },
    {
        'id': 17, 'center_name': 'ASRO Bhawalpur', 'center_located' : 'Bahawalpur', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asro', 'static_ip' : '0.0.0.0', 'abbrv' : 'BWP'
    },
    {
        'id': 18, 'center_name': 'ASRC Hyderabad', 'center_located' : 'Hyderabad', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '159.209.105.18', 'abbrv' : 'HYD'
    },
    {
        'id': 19, 'center_name': 'ASRO Larkana', 'center_located' : 'Larkana', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asro', 'static_ip' : '0.0.0.0', 'abbrv' : 'LKR'
    },
    {
        'id': 20, 'center_name': 'ASRO Sukkur', 'center_located' : 'Sukkur', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asro', 'static_ip' : '0.0.0.0', 'abbrv' : 'SKR'
    },
    {
        'id': 21, 'center_name': 'ASRC Gilgit', 'center_located' : 'Gilgit', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '0.0.0.0', 'abbrv' : 'GLT'
    },
    {
        'id': 22, 'center_name': 'ASRC Dera Ismail Khan', 'center_located' : 'D I Khan', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '202.83.169.24', 'abbrv' : 'DIK'
    },
    {
        'id': 23, 'center_name': 'ASRC PanoAqil', 'center_located' : 'Pano Aqil', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '182.184.109.38', 'abbrv' : 'PNL'
    },
    {
        'id': 24, 'center_name': 'ASRC Khuzdar', 'center_located' : 'Khuzdar', 'email': 'webmaster@joinpakarmy.gov.pk', 'center_type' : 'asrc', 'static_ip' : '182.184.127.188', 'abbrv' : 'KZD'
    }
]


users = [    
    {
        'id' : 2 ,'username' : 'asrcfsd', 'center' : 6, 'password' : 'asrcfsd321'
    },
    {
        'id' : 3 ,'username' : 'asrcglt', 'center' : 21, 'password' : 'asrcglt654'
    },
    {
        'id' : 4 ,'username' : 'asrchyd', 'center' : 18, 'password' : 'asrchyd456'
    },
    {
        'id' : 5 ,'username' : 'asrckhi', 'center' : 14, 'password' : 'asrckhi987'
    },
    {
        'id' : 6 ,'username' : 'asrclhr', 'center' : 4, 'password' : 'asrclhr789'
    },
    {
        'id' : 7 ,'username' : 'asrcmtn', 'center' : 15, 'password' : 'asrcmtn147'
    },
    {
        'id' : 8 ,'username' : 'asrcmzd', 'center' : 3, 'password' : 'asrcmzd741'
    },
    {
        'id' : 9 ,'username' : 'asrcpsh', 'center' : 7, 'password' : 'asrcpsh258'
    },
    {
        'id' : 10 ,'username' : 'asrcqta', 'center' : 10, 'password' : 'asrcqta852'
    },
    {
        'id' : 11 ,'username' : 'asrcrwp', 'center' : 1, 'password' : 'asrcrwp369'
    },
    {
        'id' : 12 ,'username' : 'asrcdik', 'center' : 8, 'password' : 'asrcdik963'
    },
    {
        'id' : 13 ,'username' : 'asrcpnl', 'center' : 23, 'password' : 'asrcpnl159'
    },
    {
        'id' : 14 ,'username' : 'asrckzd', 'center' : 13, 'password' : 'asrckzd123'
    }
]

roll_numbers = [
     { "id" : 1, "center_id" : 1, "course_id" : 2, "start" : 10000, "end" : 30000 },
     { "id" : 2, "center_id" : 4, "course_id" : 2, "start" : 30001, "end" : 50000 },
     { "id" : 3, "center_id" : 14, "course_id" : 2, "start" : 50001, "end" : 70000 },
     { "id" : 4, "center_id" : 7, "course_id" : 2, "start" : 70001, "end" : 100000 },
     { "id" : 5, "center_id" : 15, "course_id" : 2, "start" : 100001, "end" : 120000 },
     { "id" : 6, "center_id" : 6, "course_id" : 2, "start" : 120001, "end" : 140000 },
     { "id" : 7, "center_id" : 10, "course_id" : 2, "start" : 140001, "end" : 150000 },
     { "id" : 8, "center_id" : 3, "course_id" : 2, "start" : 150001, "end" : 160000 },
     { "id" : 9, "center_id" : 22, "course_id" : 2, "start" : 160001, "end" : 170000 },
     { "id" : 10, "center_id" : 18, "course_id" : 2, "start" : 170001, "end" : 180000 },
     { "id" : 11, "center_id" : 24, "course_id" : 2, "start" : 180001, "end" : 190000 },
     { "id" : 12, "center_id" : 23, "course_id" : 2, "start" : 190001, "end" : 200000 },
     { "id" : 13, "center_id" : 21, "course_id" : 2, "start" : 200001, "end" : 210000 },
]

def populate():
    # permissions = Permission.objects.all()

    # role = None
    # try:
    #     role = Role.objects.get(code_name='su')
    #     role.permissions.clear()
    # except Role.DoesNotExist:
    #     role = Role.objects.create(name='SuperUser', code_name='su')

    # role.permissions.add(*permissions)
    # role.save()

    # carole = None
    # try:
    #     carole = Role.objects.get(code_name='ca')
    # except Role.DoesNotExist:
    #     carole = Role.objects.create(name='CenterAdmin', code_name='ca')
    # carole.save()

    # try:
    #     user = User.objects.get(username='superuser')
    # except User.DoesNotExist:
    #     user = User.objects.create_superuser(
    #         id=1,
    #         username="superuser",
    #         password="C!$@well123",
    #     )
    #     user.role = Role.objects.get(code_name='su')
    #     user.save()
    # print("**** Super Admin Inserted ****")


    # for profess in profession:
    #         try:
    #             Profession.objects.get(profession_name=profess['profession_name'])
    #         except Profession.DoesNotExist:
    #             Profession.objects.create(
    #                 id=profess['id'],
    #                 profession_name=profess['profession_name'],
    #                 created_by = User.objects.get(id=1),
    #                 updated_by = User.objects.get(id=1)
    #             )

    # print("**** Profession Inserted ****")
    

    # for prov in province:
    #         try:
    #             Province.objects.get(province_name=prov['province_name'])
    #         except Province.DoesNotExist:
    #             Province.objects.create(
    #                 id=prov['id'],
    #                 province_name=prov['province_name'],
    #                 created_by = User.objects.get(id=1),
    #                 updated_by = User.objects.get(id=1)
    #             )
    # print("**** Province Inserted ****")


    for distt in districts:
            try:
                Distt.objects.get(distt_name=distt['distt_name'])
            except Distt.DoesNotExist:
                Distt.objects.create(
                    id=distt['id'],
                    distt_name=distt['distt_name'],
                    province=Province.objects.get(id=distt['province']),
                    created_by=User.objects.get(id=1),
                    updated_by=User.objects.get(id=1)
                )
    print("**** Districts Inserted ****")


    for tehsil in tehsils:
            try:
                Tehsil.objects.get(tehsil_name=tehsil['tehsil_name'])
            except Tehsil.DoesNotExist:
                Tehsil.objects.create(
                    id=tehsil['id'],
                    tehsil_name=tehsil['tehsil_name'],
                    distt=Distt.objects.get(id=tehsil['distt']),
                    created_by=User.objects.get(id=1),
                    updated_by=User.objects.get(id=1)
                )
    print("**** Tehsils Inserted ****")


    # for qual in qual_type:
    #         try:
    #             QualType.objects.get(qual_name=qual['qual_name'])
    #         except QualType.DoesNotExist:
    #             QualType.objects.create(
    #                 id=qual['id'],
    #                 qual_name=qual['qual_name'],
    #                 qual_years=qual['qual_years'],
    #                 created_by = User.objects.get(id=1),
    #                 updated_by = User.objects.get(id=1)
    #             )
    # print("**** Qualification Type Inserted ****")


    # for rnk in rank:
    #         try:
    #             Rank.objects.get(rank_name=rnk['rank_name'])
    #         except Rank.DoesNotExist:
    #             Rank.objects.create(
    #                 id=rnk['id'],
    #                 rank_name=rnk['rank_name'],
    #                 created_by = User.objects.get(id=1),
    #                 updated_by = User.objects.get(id=1)
    #             )
    # print("**** Rank Inserted ****")
         

    # for relig in religion:
    #         try:
    #             Religion.objects.get(religion_name=relig['religion_name'])
    #         except Religion.DoesNotExist:
    #             Religion.objects.create(
    #                 id=relig['id'],
    #                 religion_name=relig['religion_name'],
    #                 created_by = User.objects.get(id=1),
    #                 updated_by = User.objects.get(id=1)
    #             )
    # print("**** Religion Inserted ****")


    # for st in sect:
    #         try:
    #             Sect.objects.get(sect_name=st['sect_name'])
    #         except Sect.DoesNotExist:
    #             Sect.objects.create(
    #                 id=st['id'],
    #                 sect_name=st['sect_name'],
    #                 religion= Religion.objects.get(id=st['religion']),
    #                 created_by = User.objects.get(id=1),
    #                 updated_by = User.objects.get(id=1)
    #             )
    # print("**** Sect Inserted ****")


    # for eb in education_board:
    #         try:
    #             EducationBoard.objects.get(board_name=eb['board_name'])
    #         except EducationBoard.DoesNotExist:
    #             EducationBoard.objects.create(
    #                 id=eb['id'],
    #                 board_name=eb['board_name'],
    #                 created_by = User.objects.get(id=1),
    #                 updated_by = User.objects.get(id=1)
    #             )
    # print("**** Board Inserted ****")


    # for centr in centers:
    #         try:
    #             Center.objects.get(center_name=centr['center_name'])
    #         except Center.DoesNotExist:
    #             Center.objects.create(
    #                 id=centr['id'],
    #                 center_name=centr['center_name'],
    #                 center_located=Distt.objects.get(distt_name=centr['center_located']),
    #                 email=centr['email'],
    #                 center_type=centr['center_type'],
    #                 static_ip=centr['static_ip'],
    #                 created_by = User.objects.get(id=1),
    #                 updated_by = User.objects.get(id=1)
    #             )
    # print("**** Center Inserted ****")



    # for usr in users:
    #     try:
    #         user = User.objects.get(username=usr['username'])
    #     except User.DoesNotExist:
    #         user = User.objects.create(
    #             id=usr['id'],
    #             username=usr['username'],
    #             password=usr['password'],
    #             center=Center.objects.get(id=usr['center']),
    #             staff= True,
    #             superuser= False,
    #         )
    #         user.role = Role.objects.get(code_name='ca')
    #         user.save()
    # print("**** Center Admins created ****")



    # for rollno in roll_numbers:
            
    #     RollNo.objects.create(
    #         id=rollno['id'],
    #         center_id=Center.objects.get(id=rollno['center_id']),
    #         course_id=Courses.objects.get(id=rollno['course_id']),
    #         start=rollno['start'],
    #         end=rollno['end'],
    #         created_by = User.objects.get(id=1),
    #         updated_by = User.objects.get(id=1)
    #     )
    # print("**** Roll No Inserted ****")


   
if __name__ == '__main__':
    print("Populating medask...")
    populate()