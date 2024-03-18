import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'medask.settings')

import django
django.setup()

from api.models import Permission

permissions = [

    Permission(name='Show Dashboard', code_name='show_dashboard', module_name='Dashboard', description='User can show dashboard'),

    Permission(name='Create User', code_name='create_user', module_name='User', description='User can create user'),
    Permission(name='Read User', code_name='read_user', module_name='User', description='User can read user'),
    Permission(name='Update User', code_name='update_user', module_name='User', description='User can update user'),
    Permission(name='Show User', code_name='show_user', module_name='User', description='User can view user'),

    Permission(name='Read Organization', code_name='read_organization', module_name='Organization', description='User can read organization'),
    Permission(name='Show Organization', code_name='show_organization', module_name='Organization', description='User can show organization'),

    Permission(name='Create Role', code_name='create_role', module_name='Role', description='User can create role'),
    Permission(name='Read Role', code_name='read_role', module_name='Role', description='User can read role'),
    Permission(name='Update Role', code_name='update_role', module_name='Role', description='User can update role'),
    Permission(name='Delete Role', code_name='delete_role', module_name='Role', description='User can delete role'),
    Permission(name='Show Role', code_name='show_role', module_name='Role', description='User can view role'),

    Permission(name='Show City', code_name='show_city', module_name='City', description='User can view City'),
    Permission(name='Read City', code_name='read_city', module_name='City', description='User can read City'),
    Permission(name='Create City', code_name='create_city', module_name='City', description='User can create City'),
    Permission(name='Update City', code_name='update_city', module_name='City', description='User can update City'),
    Permission(name='Delete City', code_name='delete_city', module_name='City', description='User can delete City'),
    
    Permission(name='Show Document', code_name='show_document', module_name='Document', description='User can view Document'),
    Permission(name='Read Document', code_name='read_document', module_name='Document', description='User can read Document'),
    Permission(name='Create Document', code_name='create_document', module_name='Document', description='User can create Document'),
    Permission(name='Update Document', code_name='update_document', module_name='Document', description='User can update Document'),
    Permission(name='Delete Document', code_name='delete_document', module_name='Document', description='User can delete Document'),

    Permission(name='Show Candidate', code_name='show_candidate', module_name='Candidate', description='User can view Candidate'),
    Permission(name='Read Candidate', code_name='read_candidate', module_name='Candidate', description='User can read Candidate'),
    Permission(name='Create Candidate', code_name='create_candidate', module_name='Candidate', description='User can create Candidate'),
    Permission(name='Update Candidate', code_name='update_candidate', module_name='Candidate', description='User can update Candidate'),
    Permission(name='Delete Candidate', code_name='delete_candidate', module_name='Candidate', description='User can delete Candidate'),
    

    Permission(name='Show Batch', code_name='show_batches', module_name='Batches', description='User can view Batch'),
    Permission(name='Read Batch', code_name='read_batches', module_name='Batches', description='User can read Batch'),
    Permission(name='Create Batch', code_name='create_batches', module_name='Batches', description='User can create Batch'),
    Permission(name='Update Batch', code_name='update_batches', module_name='Batches', description='User can update Batch'),
    Permission(name='Delete Batch', code_name='delete_batches', module_name='Batches', description='User can delete Batch'),


    Permission(name='Show Center', code_name='show_centers', module_name='Center', description='User can view Center'),
    Permission(name='Read Center', code_name='read_centers', module_name='Center', description='User can read Center'),
    Permission(name='Create Center', code_name='create_centers', module_name='Center', description='User can create Center'),
    Permission(name='Update Center', code_name='update_centers', module_name='Center', description='User can update Center'),
    Permission(name='Delete Center', code_name='delete_centers', module_name='Center', description='User can delete Center'),


    Permission(name='Show Course', code_name='show_courses', module_name='Courses', description='User can view Course'),
    Permission(name='Read Course', code_name='read_courses', module_name='Courses', description='User can read Course'),
    Permission(name='Create Course', code_name='create_courses', module_name='Courses', description='User can create Course'),
    Permission(name='Update Course', code_name='update_courses', module_name='Courses', description='User can update Course'),
    Permission(name='Delete Course', code_name='delete_courses', module_name='Courses', description='User can delete Course'),

    Permission(name='Show Discipline', code_name='show_disciplines', module_name='Discipline', description='User can view Discipline'),
    Permission(name='Read Discipline', code_name='read_disciplines', module_name='Discipline', description='User can read Discipline'),
    Permission(name='Create Discipline', code_name='create_disciplines', module_name='Discipline', description='User can create Discipline'),
    Permission(name='Update Discipline', code_name='update_disciplines', module_name='Discipline', description='User can update Discipline'),
    Permission(name='Delete Discipline', code_name='delete_disciplines', module_name='Discipline', description='User can delete Discipline'),

    Permission(name='Show Option', code_name='show_options', module_name='QuestionOption', description='User can view Option'),
    Permission(name='Read Option', code_name='read_options', module_name='QuestionOption', description='User can read Option'),
    Permission(name='Create Option', code_name='create_options', module_name='QuestionOption', description='User can create Option'),
    Permission(name='Update Option', code_name='update_options', module_name='QuestionOption', description='User can update Option'),
    Permission(name='Delete Option', code_name='delete_options', module_name='QuestionOption', description='User can delete Option'),
    
    Permission(name='Show Question', code_name='show_questions', module_name='Question', description='User can view Question'),
    Permission(name='Read Question', code_name='read_questions', module_name='Question', description='User can read Question'),
    Permission(name='Create Question', code_name='create_questions', module_name='Question', description='User can create Question'),
    Permission(name='Update Question', code_name='update_questions', module_name='Question', description='User can update Question'),
    Permission(name='Delete Question', code_name='delete_questions', module_name='Question', description='User can delete Question'),

    Permission(name='Show District', code_name='show_distt', module_name='Distt', description='User can view Ditrict'),
    Permission(name='Read District', code_name='read_distt', module_name='Distt', description='User can read Ditrict'),
    Permission(name='Create District', code_name='create_distt', module_name='Distt', description='User can create Ditrict'),
    Permission(name='Update District', code_name='update_distt', module_name='Distt', description='User can update Ditrict'),
    Permission(name='Delete District', code_name='delete_distt', module_name='Distt', description='User can delete Ditrict'),

    Permission(name='Show Province', code_name='show_province', module_name='Province', description='User can view Province'),
    Permission(name='Read Province', code_name='read_province', module_name='Province', description='User can read Province'),
    Permission(name='Create Province', code_name='create_province', module_name='Province', description='User can create Province'),
    Permission(name='Update Province', code_name='update_province', module_name='Province', description='User can update Province'),
    Permission(name='Delete Province', code_name='delete_province', module_name='Province', description='User can delete Province'),

    Permission(name='Show Language', code_name='show_lang', module_name='Language', description='User can view Language'),
    Permission(name='Read Language', code_name='read_lang', module_name='Language', description='User can read Language'),
    Permission(name='Create Language', code_name='create_lang', module_name='Language', description='User can create Language'),
    Permission(name='Update Language', code_name='update_lang', module_name='Language', description='User can update Language'),
    Permission(name='Delete Language', code_name='delete_lang', module_name='Language', description='User can delete Language'),

    Permission(name='Show Profession', code_name='show_profession', module_name='Profession', description='User can view Profession'),
    Permission(name='Read Profession', code_name='read_profession', module_name='Profession', description='User can read Profession'),
    Permission(name='Create Profession', code_name='create_profession', module_name='Profession', description='User can create Profession'),
    Permission(name='Update Profession', code_name='update_profession', module_name='Profession', description='User can update Profession'),
    Permission(name='Delete Profession', code_name='delete_profession', module_name='Profession', description='User can delete Profession'),


    Permission(name='Show Qualitifcation Type', code_name='show_qualtype', module_name='QualType', description='User can view Qualitifcation Type'),
    Permission(name='Read Qualitifcation Type', code_name='read_qualtype', module_name='QualType', description='User can read Qualitifcation Type'),
    Permission(name='Create Qualitifcation Type', code_name='create_qualtype', module_name='QualType', description='User can create Qualitifcation Type'),
    Permission(name='Update Qualitifcation Type', code_name='update_qualtype', module_name='QualType', description='User can update Qualitifcation Type'),
    Permission(name='Delete Qualitifcation Type', code_name='delete_qualtype', module_name='QualType', description='User can delete Qualitifcation Type'),

    Permission(name='Show Rank', code_name='show_rank', module_name='Rank', description='User can view Rank'),
    Permission(name='Read Rank', code_name='read_rank', module_name='Rank', description='User can read Rank'),
    Permission(name='Create Rank', code_name='create_rank', module_name='Rank', description='User can create Rank'),
    Permission(name='Update Rank', code_name='update_rank', module_name='Rank', description='User can update Rank'),
    Permission(name='Delete Rank', code_name='delete_rank', module_name='Rank', description='User can delete Rank'),


    Permission(name='Show Religion', code_name='show_religion', module_name='Religion', description='User can view Religion'),
    Permission(name='Read Religion', code_name='read_religion', module_name='Religion', description='User can read Religion'),
    Permission(name='Create Religion', code_name='create_religion', module_name='Religion', description='User can create Religion'),
    Permission(name='Update Religion', code_name='update_religion', module_name='Religion', description='User can update Religion'),
    Permission(name='Delete Religion', code_name='delete_religion', module_name='Religion', description='User can delete Religion'),

    Permission(name='Show Sect', code_name='show_sect', module_name='Sect', description='User can view Sect'),
    Permission(name='Read Sect', code_name='read_sect', module_name='Sect', description='User can read Sect'),
    Permission(name='Create Sect', code_name='create_sect', module_name='Sect', description='User can create Sect'),
    Permission(name='Update Sect', code_name='update_sect', module_name='Sect', description='User can update Sect'),
    Permission(name='Delete Sect', code_name='delete_sect', module_name='Sect', description='User can delete Sect'),


    Permission(name='Show Roll No', code_name='show_roll_no', module_name='RollNo', description='User can view Roll No'),
    Permission(name='Read Roll No', code_name='read_roll_no', module_name='RollNo', description='User can read Roll No'),
    Permission(name='Create Roll No', code_name='create_roll_no', module_name='RollNo', description='User can create Roll No'),
    Permission(name='Update Roll No', code_name='update_roll_no', module_name='RollNo', description='User can update Roll No'),
    Permission(name='Delete Roll No', code_name='delete_roll_no', module_name='RollNo', description='User can delete Roll No'),

    Permission(name='Show Tehsil', code_name='show_tehsil', module_name='Tehsil', description='User can view Tehsil'),
    Permission(name='Read Tehsil', code_name='read_tehsil', module_name='Tehsil', description='User can read Tehsil'),
    Permission(name='Create Tehsil', code_name='create_tehsil', module_name='Tehsil', description='User can create Tehsil'),
    Permission(name='Update Tehsil', code_name='update_tehsil', module_name='Tehsil', description='User can update Tehsil'),
    Permission(name='Delete Tehsil', code_name='delete_tehsil', module_name='Tehsil', description='User can delete Tehsil'),

    Permission(name='Show Change Status', code_name='show_change_status', module_name='Change Status', description='User can view change status'),

]


def add_permission():
    for permission in permissions:
        try:
            Permission.objects.get(code_name=permission.code_name)
        except Permission.DoesNotExist:
            permission.save()


if __name__ == '__main__':
    print("Adding permissions...")
    add_permission()
    print("permissions Added...")
