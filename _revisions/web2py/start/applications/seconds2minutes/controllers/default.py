def index():
  form=FORM('# of seconds: ',
      INPUT(_type='integer', _name='seconds', requires=IS_INT_IN_RANGE(0,1000000)),
      INPUT(_type='submit')).process()
  if form.accepted:
      redirect(URL('convert',args=form.vars.seconds))
  return dict(form=form)

def convert():
   seconds = request.args(0,cast=int)
   return dict(seconds=seconds, minutes=seconds/60, new_seconds=seconds%60)
