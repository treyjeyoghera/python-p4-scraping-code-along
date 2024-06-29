from socket import CAN_BCM_RX_ANNOUNCE_RESUME
from typing import Self


class Course:
     for course in Self.get_page().select('.post'):

        title = course.select("h2")[0].text if course.select("h2") else ''
        date = course.select(".date")[0].text if course.select(".date") else ''
        description = course.select("p")[0].text  if course.select("p") else ''

        new_course = CAN_BCM_RX_ANNOUNCE_RESUME(title, date, description)
        Self.courses.append(new_course)
     -  return Self.courses
