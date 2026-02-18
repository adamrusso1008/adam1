def generate_weekly_plan(user, workouts, oura, week_start_date=None):
    if week_start_date:
        start = datetime.fromisoformat(week_start_date)
    else:
        today = datetime.now()
        start = today + timedelta(days=(7 - today.weekday()))
        start = start.replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(days=7)
