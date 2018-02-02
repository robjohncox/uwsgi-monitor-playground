import os


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    response = list()
    response.append('Raw data:')
    for key in sorted(env.keys()):
        response.append('  {}: {}'.format(key, env[key]))
    response.append('')
    response.append('Input data: {}'.format(env['wsgi.input'].readline()))
    return os.linesep.join(response)
