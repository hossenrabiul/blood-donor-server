# Data.Doner-Backend

## API Endpoints

### Authentication APIs
- **Register API:** [http://127.0.0.1:8000/accounts/](http://127.0.0.1:8000/accounts/)
- **Login API:** [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/)
- **Logout API:** [http://127.0.0.1:8000/accounts/logout/](http://127.0.0.1:8000/accounts/logout/)
- **All User List:** [http://127.0.0.1:8000/accounts/users/](http://127.0.0.1:8000/accounts/users/)

### User Profile APIs
- **All Profile List:** [http://127.0.0.1:8000/accounts/profiles/](http://127.0.0.1:8000/accounts/profiles/)
  
  **Filters:**
  - `?user_id=<int>`

  **PUT Requests:**
  - `/profiles/<int>/update-image/` - Update profile image with `{'image': <file>}`
  - `/profiles/<int>/update-profile/` - Update profile with the following fields:
    - **User:** `{'first_name', 'last_name', 'email'}`
    - **Profile:** `{'phone', 'age', 'gender', 'blood', 'division', 'country'}`

### Event Management APIs
- **All Events List:** [http://127.0.0.1:8000/event/events/](http://127.0.0.1:8000/event/events/)

  **GET Requests:**
  - `?user=<int>`
  - `?doner=<int>`

  **PUT Requests:**
  - `/events/<int>/accepted/` - Accept an event request with `{'doner_id', 'doner_message'}`
  - `/events/<int>/received/` - Mark the event creator as having received blood with `{}`

  **Example:**
  ```json
  {
      "user": 14,
      "title": "Blood Donation Event",
      "description": "A description of the blood donation event",
      "event_date": "2025-06-19",
      "event_time": "14:00",
      "blood": "A+"
  }
  ```

- **Create Event:** [http://127.0.0.1:8000/event/events/create/](http://127.0.0.1:8000/event/events/create/)

  **POST Request Body:**
  ```json
  {
      "user": 1,
      "title": "Emergency Blood Donation",
      "description": "Description of the event",
      "event_date": "2025-01-25",
      "event_time": "14:30:00"
  }
  ```

  **Filters:**
  - `?user=<int>`
  - `?status=Completed`
  - `?event_id=<int>`
  - `?doner=<int>`
  - `?event_date=<YYYY-MM-DD>`
  - `?blood=<blood_type>`
  - `?last_donate=<int>`




##### data.doner-backend
##### data.doner-123
 


# DataDonor-webapp
# DataDonor-webapp
