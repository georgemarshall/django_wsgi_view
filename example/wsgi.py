def application(environ, start_response):

   response_body = str(environ)

   status = '200 OK'

   # Now content type is text/html
   response_headers = [('Content-Type', 'text/plain'),
                  ('Content-Length', str(len(response_body)))]
   start_response(status, response_headers)

   return [response_body]