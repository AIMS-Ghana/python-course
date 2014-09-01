---
---

randInt = (max, min = 0) ->
  Math.floor(Math.random()*(max-min+1)+min)

window.pickStudent = (target) ->
  if !confirm(target.options[randInt(target.length-1)].text)
    pickStudent(target)
  else
    false
