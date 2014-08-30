---
layout: section
title: Current Students
---
## Current Students
{% assign current_students = site.students | where: "status", "current" %}
{% for student in current_students %}
{{ student.name }}, {{ student.country }} - [@{{ student.gh }}](http://github.com/{{ student.gh }})
{% endfor %}
* * *

## Past Students
{% assign past_students = site.students | where: "status", "past" %}
{% for student in past_students %}
## {{ student.name }}, {{ student.country }} - [@{{ student.gh }}](http://github.com/{{ student.gh }})
{% endfor %}
