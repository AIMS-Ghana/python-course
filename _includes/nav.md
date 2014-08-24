{:.nav}
 - [![AIMS](/assets/logo.png "AIMS Program Home")](http://www.aims.edu.gh/)
 - [Course Home]({{ site.absoluteurl }}{{ site.baseurl }}/)
{% for day in site.days %} - {% if page.url contains day.url %}{:.{{ site.css.active }}}{% endif %}[{{ day.title }}]({{ day.url }})
{% endfor %}
