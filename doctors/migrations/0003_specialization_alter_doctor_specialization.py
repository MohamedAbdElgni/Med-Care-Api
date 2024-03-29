# Generated by Django 5.0.3 on 2024-03-18 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctor_area_doctor_fees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Dermatology', 'Dermatology (Skin)'), ('Dentistry', 'Dentistry (Teeth)'), ('Psychiatry', 'Psychiatry (Mental, Emotional or Behavioral Disorders)'), ('Pediatrics', 'Pediatrics and New Born (Child)'), ('Neurology', 'Neurology (Brain & Nerves)'), ('Orthopedics', 'Orthopedics (Bones)'), ('Gynaecology', 'Gynaecology and Infertility'), ('ENT', 'Ear, Nose and Throat'), ('Cardiology', 'Cardiology and Vascular Disease (Heart)'), ('Allergy', 'Allergy and Immunology (Sensitivity and Immunity)'), ('Andrology', 'Andrology and Male Infertility'), ('Audiology', 'Audiology'), ('Cardiology_Thoracic', 'Cardiology and Thoracic Surgery (Heart & Chest)'), ('Chest_Respiratory', 'Chest and Respiratory'), ('Diabetes_Endocrinology', 'Diabetes and Endocrinology'), ('Radiology', 'Diagnostic Radiology (Scan Centers)'), ('Dietitian', 'Dietitian and Nutrition'), ('Family_Medicine', 'Family Medicine'), ('Gastroenterology', 'Gastroenterology and Endoscopy'), ('General_Practice', 'General Practice'), ('General_Surgery', 'General Surgery'), ('Geriatrics', 'Geriatrics (Old People Health)'), ('Hematology', 'Hematology'), ('Hepatology', 'Hepatology (Liver Doctor)'), ('Internal_Medicine', 'Internal Medicine'), ('Interventional_Radiology', 'Interventional Radiology (Interventional Radiology)'), ('IVF', 'IVF and Infertility'), ('Laboratories', 'Laboratories'), ('Nephrology', 'Nephrology'), ('Neurosurgery', 'Neurosurgery (Brain & Nerves Surgery)'), ('Obesity_Laparoscopic', 'Obesity and Laparoscopic Surgery'), ('Oncology', 'Oncology (Tumor)'), ('Oncology_Surgery', 'Oncology Surgery (Tumor Surgery)'), ('Ophthalmology', 'Ophthalmology (Eyes)'), ('Osteopathy', 'Osteopathy (Osteopathic Medicine)'), ('Pain_Management', 'Pain Management'), ('Pediatric_Surgery', 'Pediatric Surgery'), ('Phoniatrics', 'Phoniatrics (Speech)'), ('Physiotherapy', 'Physiotherapy and Sport Injuries'), ('Plastic_Surgery', 'Plastic Surgery'), ('Rheumatology', 'Rheumatology'), ('Spinal_Surgery', 'Spinal Surgery'), ('Urology', 'Urology (Urinary System)'), ('Vascular_Surgery', 'Vascular Surgery (Arteries and Vein Surgery)')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctors.specialization'),
        ),
    ]
