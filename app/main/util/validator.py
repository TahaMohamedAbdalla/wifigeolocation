from marshmallow import Schema, fields , ValidationError
from marshmallow.validate import Length
from datetime import datetime
class SignupSchema(Schema):
    class Meta:
            fields = ('first_name', 'last_name', 'email' , 'password', 'alternative_email', 'cell_phone', 'date_of_birth',
                    'country', 'province', 'area', 'area_code', 'id_type', 'id_number', 'gender','race','religion',
                    'first_language', 'second_language', 'employment_status', 'marital_status', 'number_of_siblings', 'spouse',
                    'spouse_contact', 'spouse_employment','guardian', 'guardian_employment' )   
    first_name = fields.Str(required=True,  validate=Length(1))
    last_name = fields.Str(required=True,  validate=Length(1))
    email = fields.Email(required=True,  validate=Length(1))
    password = fields.Str(required=False,  validate=Length(8))
    alternative_email = fields.Email(required=False,  validate=Length(0))
    cell_phone = fields.Integer(required=False,  validate=Length(0))
    date_of_birth = fields.DateTime(format='%y-%m-%d')
    country = fields.Integer(required=False,  validate=Length(0))
    province = fields.Integer(required=False,  validate=Length(0))
    physical_address = fields.Str(required=False,  validate=Length(0))
    area =  fields.Str(required=False,  validate=Length(0))
    area_code = fields.Integer(required=False,  validate=Length(0))
    id_type = fields.Integer(required=False,  validate=Length(0))
    id_number = fields.Str(required=False,  validate=Length(0))
    gender =  fields.Integer(required=False,  validate=Length(0))
    race = fields.Integer(required=False,  validate=Length(0))
    religion = fields.Integer(required=False,  validate=Length(0))
    first_language = fields.Integer(required=False,  validate=Length(0))
    second_language =  fields.Integer(required=False,  validate=Length(0))
    employment_status = fields.Integer(required=False,  validate=Length(0))
    marital_status = fields.Integer(required=False,  validate=Length(0))
    number_of_siblings = fields.Integer(required=False,  validate=Length(0))
    spouse = fields.Str(required=False,  validate=Length(0))
    spouse_contact = fields.Str(required=False,  validate=Length(0))
    spouse_employment = fields.Str(required=False,  validate=Length(0))
    guardian =  fields.Str(required=False,  validate=Length(0))
    guardian_employment =  fields.Str(required=False,  validate=Length(0))
     



class SigninSchema(Schema):
    class Meta:
        fields = ('email' , 'password' )
   
    email =  fields.Email(required=True,  validate=Length(1))
    password = fields.Str(required=True,  validate=Length(1))


class SignoutSchema(Schema):
    class Meta:
        fields = ('token' , )
   
    token = fields.Str()


class EmailPasswordSchema(Schema):
    class Meta:
        fields = ( 'email', )
           
    email =  fields.Email(required=True,  validate=Length(1))
 


class PasswordSchema(Schema):
    class Meta:
        fields = ( 'password', 'token' )
           
    password = fields.Str(required=True,  validate=Length(1))
    token = fields.Str(required=True,  validate=Length(1))


class ApplicantSchema(Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'email' , 'password', 'alternative_email', 'cell_phone', 'date_of_birth',
                  'country', 'province', 'area', 'area_code', 'id_type', 'id_number', 'gender','race','religion',
                   'first_language', 'second_language', 'employment_status', 'marital_status', 'number_of_siblings', 'spouse',
                    'spouse_contact', 'spouse_employment','guardian', 'guardian_employment' )   
    first_name = fields.Str(required=True,  validate=Length(1))
    last_name = fields.Str(required=True,  validate=Length(1))
    email = fields.Email(required=True,  validate=Length(1))
    password = fields.Str(required=False,  validate=Length(8))
    alternative_email = fields.Email(required=False,  validate=Length(0))
    cell_phone = fields.Integer(required=False,  validate=Length(0))
    date_of_birth = fields.DateTime(format='%y-%m-%d')
    country = fields.Integer(required=False,  validate=Length(0))
    province = fields.Integer(required=False,  validate=Length(0))
    physical_address = fields.Str(required=False,  validate=Length(0))
    area =  fields.Str(required=False,  validate=Length(0))
    area_code = fields.Integer(required=False,  validate=Length(0))
    id_type = fields.Integer(required=False,  validate=Length(0))
    id_number = fields.Str(required=False,  validate=Length(0))
    gender =  fields.Integer(required=False,  validate=Length(0))
    race = fields.Integer(required=False,  validate=Length(0))
    religion = fields.Integer(required=False,  validate=Length(0))
    first_language = fields.Integer(required=False,  validate=Length(0))
    second_language =  fields.Integer(required=False,  validate=Length(0))
    employment_status = fields.Integer(required=False,  validate=Length(0))
    marital_status = fields.Integer(required=False,  validate=Length(0))
    number_of_siblings = fields.Integer(required=False,  validate=Length(0))
    spouse = fields.Str(required=False,  validate=Length(0))
    spouse_contact = fields.Str(required=False,  validate=Length(0))
    spouse_employment = fields.Str(required=False,  validate=Length(0))
    guardian =  fields.Str(required=False,  validate=Length(0))
    guardian_employment =  fields.Str(required=False,  validate=Length(0))
    


