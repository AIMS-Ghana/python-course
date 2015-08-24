---
---

randInt = (max, min = 0) ->
  Math.floor(Math.random()*(max-min+1)+min)

window.pickStudent = (target) ->
  if !confirm(target.options[randInt(target.length-1)].text)
    pickStudent(target)
  else
    false

window.randomQuestion = (event) ->
  tar = event.target
  par = tar.parentElement
  newTar = randInt(par.childElementCount-1)
  tar.classList.remove("shown")
  par.children[newTar].classList.add("shown")
  false

window.onload = ( ->
  # get all the hs
  for hele in document.getElementsByTagName('h2')
    hele.onclick = ( ->
      if 'minimize' in this.classList
        this.classList.remove('minimize')
      else
        this.classList.add('minimize')
    )

  for draw in document.getElementsByClassName('random')
    draw.onclick = ( ->
      alert('heyo!')
      false
    )
)