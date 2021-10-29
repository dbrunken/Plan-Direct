#Plan-Direct
>Conquer Your Days

##Project Overview
- Journal to record daily life (MVP)
- Planner to chart to-do's (MVP)
- When user needs to go to location, embedded Geolocator can fetch directions

##Features
Upon opening the app, user sees a monthly calendar and a blank journal page. Typing in the journal auto records the entry date. After writing, the user clicks on 'save entry' button, and a new button appears: 'create new entry'.
Clicking on a specific day on the calendar brings up the day and a blank to do list. A plain list can be created, random entries in a non-specific order. User can also organize by location, which geolocator can give directions.
User can also click on 'notes' button above list page, to add notes such as numbers, things of interest, etc.

###User Stories
>As a user, I want to record my thoughts in a simple, straight-forward journal because I want to be able to better plan my days and organize my thoughts.
- journal function
- daily planner
- note taker

>As a user, I want all my tasks to properly be organized and the option to know where i'm going in one app because I can't find an app that combines all these features.
- daily planner
- Geo function to give directions

##Data Model
1. User
    - basic import function
    - basic user information
    - goal setting (6 month, 1 year, 5 year goal)
2. Journal Input
    - user input text space
    - auto add date-time
    - add multiple entries
    - store and show old entries on history page
3. Calendar
    - show monthly Calendar
    - select day for tasks and notes
4. To-Do
    - add tasks
    - delete tasks
    - check off as complete
    - importance ranking
5. Note Input
    - user input text space (500 char max)
    - auto add date-time
    - multiple entries
6. GeoLocator Api

##Schedule
###Week 1
- base model index
- save and display user entry into journal
- display calendar function

###Week 2
- functional to-do model
- functional daily note taker
- User Login function

###Week 3
- CSS
- Finish Calendar functionality
- Add history page
- clean bugs

###Week 4
- CSS
- clean bugs