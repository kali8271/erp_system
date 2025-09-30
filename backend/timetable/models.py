from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (Capacity: {self.capacity})"


class Timetable(models.Model):
    course = models.ForeignKey("academics.Course", on_delete=models.CASCADE, related_name="timetables")
    section = models.ForeignKey("academics.Section", on_delete=models.CASCADE, related_name="timetables")
    teacher = models.ForeignKey("accounts.TeacherProfile", on_delete=models.CASCADE, related_name="timetables")
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name="timetables")
    day_of_week = models.CharField(
        max_length=10,
        choices=[
            ("Monday", "Monday"),
            ("Tuesday", "Tuesday"),
            ("Wednesday", "Wednesday"),
            ("Thursday", "Thursday"),
            ("Friday", "Friday"),
            ("Saturday", "Saturday"),
        ]
    )
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course.code} ({self.section.name}) - {self.day_of_week} {self.start_time}-{self.end_time}"
