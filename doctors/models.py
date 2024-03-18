from django.db import models
from users.models import User

    
SPECIALIZATIONS = [
    ('Dermatology', 'Dermatology (Skin)'),
    ('Dentistry', 'Dentistry (Teeth)'),
    ('Psychiatry', 'Psychiatry (Mental, Emotional or Behavioral Disorders)'),
    ('Pediatrics', 'Pediatrics and New Born (Child)'),
    ('Neurology', 'Neurology (Brain & Nerves)'),
    ('Orthopedics', 'Orthopedics (Bones)'),
    ('Gynaecology', 'Gynaecology and Infertility'),
    ('ENT', 'Ear, Nose and Throat'),
    ('Cardiology', 'Cardiology and Vascular Disease (Heart)'),
    ('Allergy', 'Allergy and Immunology (Sensitivity and Immunity)'),
    ('Andrology', 'Andrology and Male Infertility'),
    ('Audiology', 'Audiology'),
    ('Cardiology_Thoracic', 'Cardiology and Thoracic Surgery (Heart & Chest)'),
    ('Chest_Respiratory', 'Chest and Respiratory'),
    ('Diabetes_Endocrinology', 'Diabetes and Endocrinology'),
    ('Radiology', 'Diagnostic Radiology (Scan Centers)'),
    ('Dietitian', 'Dietitian and Nutrition'),
    ('Family_Medicine', 'Family Medicine'),
    ('Gastroenterology', 'Gastroenterology and Endoscopy'),
    ('General_Practice', 'General Practice'),
    ('General_Surgery', 'General Surgery'),
    ('Geriatrics', 'Geriatrics (Old People Health)'),
    ('Hematology', 'Hematology'),
    ('Hepatology', 'Hepatology (Liver Doctor)'),
    ('Internal_Medicine', 'Internal Medicine'),
    ('Interventional_Radiology', 'Interventional Radiology (Interventional Radiology)'),
    ('IVF', 'IVF and Infertility'),
    ('Laboratories', 'Laboratories'),
    ('Nephrology', 'Nephrology'),
    ('Neurosurgery', 'Neurosurgery (Brain & Nerves Surgery)'),
    ('Obesity_Laparoscopic', 'Obesity and Laparoscopic Surgery'),
    ('Oncology', 'Oncology (Tumor)'),
    ('Oncology_Surgery', 'Oncology Surgery (Tumor Surgery)'),
    ('Ophthalmology', 'Ophthalmology (Eyes)'),
    ('Osteopathy', 'Osteopathy (Osteopathic Medicine)'),
    ('Pain_Management', 'Pain Management'),
    ('Pediatric_Surgery', 'Pediatric Surgery'),
    ('Phoniatrics', 'Phoniatrics (Speech)'),
    ('Physiotherapy', 'Physiotherapy and Sport Injuries'),
    ('Plastic_Surgery', 'Plastic Surgery'),
    ('Rheumatology', 'Rheumatology'),
    ('Spinal_Surgery', 'Spinal Surgery'),
    ('Urology', 'Urology (Urinary System)'),
    ('Vascular_Surgery', 'Vascular Surgery (Arteries and Vein Surgery)'),
]

class Specialization(models.Model):
    name = models.CharField(max_length=100, choices=SPECIALIZATIONS)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)    
    degree = models.CharField(max_length=100, blank=True, null=True)
    #experience = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    fees = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
