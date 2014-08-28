{:.nav}
 - [![AIMS]({{ site.absoluteurl }}{{ site.baseurl }}/assets/logo.png "AIMS Program Home")](http://www.aims.edu.gh/)
 - [Course Home]({{ site.absoluteurl }}{{ site.baseurl }}/)
{% for day in site.days %} - {% if page.url contains day.url %}{:.{{ site.css.active }}}{% endif %}[{{ day.title }}]({{ site.absoluteurl }}{{ site.baseurl }}{{ day.url }})
{% endfor %} - [Students]({{ site.absoluteurl }}{{ site.baseurl }}/students)<select>
<option>A</option>
<option>B</option>
</select><input type="button" value="ROLL" />
