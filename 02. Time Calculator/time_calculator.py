def add_time(start, duration, starting_day=None):
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    start_time, start_period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    if start_period == "PM":
        start_hour += 12

    total_minutes = start_minute + duration_minute
    end_minute = total_minutes % 60
    carry_hour = total_minutes // 60

    total_hours = start_hour + duration_hour + carry_hour
    end_hour = total_hours % 24

    days_later = total_hours // 24

    if end_hour < 12:
        end_period = "AM"
    else:
        end_period = "PM"
        end_hour -= 12

    if end_hour == 0:
        end_hour = 12

    result = f"{end_hour}:{end_minute:02d} {end_period}"

    if starting_day:
        start_day_index = days_of_week.index(starting_day.title())
        end_day_index = (start_day_index + days_later) % 7
        result += f", {days_of_week[end_day_index]}"

    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result