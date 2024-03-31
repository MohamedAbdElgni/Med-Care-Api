# Med-Care-Api

## Description
This is a simple API for React.js MedCare [frontend](
      https://github.com/Ashryz/Med_Care
      ) project. It is built using Django Rest Framework.

## Features
#### We have 3 Main user roles:
1. Admin
2. Doctor
3. Patient

#### Admin
- Can control all the system through the admin panel.
- Can add, update, delete doctors.
- Can add, update, delete patients.
- Can add, update, delete appointments.

#### Doctor
- Add schedule for his appointments.
- View his appointments(approved, pending, rejected).
- approve or reject appointments.

#### Patient
- View all doctors.
- View doctor's profile.
- Book an appointment with a doctor.
- View his appointments(approved, pending, rejected).
- pay for the appointment via paymob.

### Related features
- Confirmation email for the registration.
- Email notification for the appointment status.

## Technologies
- Django
- Django Rest Framework
- Jazzmin
- Paymob api
- Postgresql

## Installation
1. Clone the repo
```sh
git clone git@github.com:MohamedAbdElgni/Med-Care-Api.git
```
2. Install requirements
```sh
pip install -r requirements.txt
```

3. Migration and create superuser

```sh
python manage.py makemigrations
python manage.py migrate
```

4. Run the server
```sh
python manage.py runserver
```

## API Endpoints
### Auth Endpoints '/auth/' Users App
- POST '/auth/register/' - Register a new user
- POST '/auth/login/' - Login user
- POST '/auth/logout/' - Logout user
- POST '/auth/activate/<uidb64>/<token>/ - Activate user account
- POST GET 'users/<int:id>/' - Get user by id - Update user 

### Doctor Endpoints '/doctors/' Doctors App

- GET '/doctors/' - Get all doctors
- GET PUT DELETE '/doctor/<int:pk>/' - Get doctor by id - Update doctor additonal info - Delete doctor

### Schedule Endpoints '/appointments/' Appointments App

- GET POST '/all_sch/' - Get all schedules - Add new schedule
- GET PUT DELETE '/schedule/<int:s_id>/' - Get schedule by id - Update schedule - Delete schedule
- GET POST '/all_app/' - Get all appointments - Add new appointment
- GET PUT DELETE '/appointment/<int:a_id>/' - Get appointment by id - Update appointment - Delete appointment
- GET '/all_app/doctor/<int:doctor_id>/' - Get all doctor appointments
- GET '/all_sch/doctor/<int:doctor_id>/' - Get all doctor schedules
- GET '/all_app/user/<int:user_id>/' - Get all user appointments
- PUT '/pay/<int:appointment_id>/' - Handle payment
- POST GET '/iframe/<int:appointment_id>/' - Get payment iframe url

### Rating Endpoints '/ratings/' Ratings App

- GET POST '/ratings/' - Get all ratings - Add new rating
- GET PUT DELETE '/rating/<int:rating_id>/' - Get rating by id - Update rating - Delete rating
- GET '/doctor/<int:doctor_id>/' - Get doctor ratings

### Offer Endpoints '/offers/' Offers App

- GET POST '/offers/' - Get all offers - Add new offer
- GET PUT DELETE '/offer/<int:offer_id>/' - Get offer by id - Update offer - Delete offer
- GET '/doctor/<int:doctor_id>/' - Get doctor offers

## Contributors
- [Mohamed AbdElgani](https://github.com/MohamedAbdElgni)
- [Tarek Ashry](https://github.com/Ashryz)
- [Israa Lotfy](https://github.com/serra24)
- [Yussef Abo Alam](https://github.com/yusufabualam)
- [Hager Serag](https://github.com/Eng-hager2000)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## This project is the final project of the [ITI](https://www.iti.gov.eg/) Full Stack Web Development Using Python Track

