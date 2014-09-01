{:.nav}
 - [![AIMS]({{ site.absoluteurl }}/logo.png "AIMS Program Home")](http://www.aims.edu.gh/)
 - [Course Home]({{ site.absoluteurl }}{{ site.baseurl }}/)
{% for day in site.days %} - {% if page.url contains day.url %}{:.{{ site.css.active }}}{% endif %}[{{ day.title }}]({{ site.absoluteurl }}{{ site.baseurl }}{{ day.url }})
{% endfor %} - [Students]({{ site.absoluteurl }}{{ site.baseurl }}/students)<input type="button" value="RANDOM DRAW" onclick="pickStudent(this.nextSibling);"/><select style="display:none">{% assign current_students = site.students | where: "status", "current" %}{% for student in current_students %}
<option>{{ student.name }}</option>{% endfor %}
</select>
 - [![Build Status](https://travis-ci.org/AIMS-Ghana/python-course.svg)](https://travis-ci.org/AIMS-Ghana/python-course)
