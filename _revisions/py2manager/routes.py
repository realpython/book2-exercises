routers = dict( 
    BASE = dict( 
        default_application='py2manager', 
    ) 
) 

routes_onerror = [
  ('*/*', '/py2manager/static/error.html')
]
