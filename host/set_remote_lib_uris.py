# Creating variables dynamically.
# To be able to pass arguments to variable file, we must define
# and use "get_variables" in a similar manner as follows:

def get_variables(server_uri, start_port):

    # Note that the order in which the libraries are listed here must match
    # that in 'server.py'.
    port            = int(start_port)
    target_uri      =  "%s:%d" % (server_uri, port)

    port            += 1
    common_uri      =  "%s:%d" % (server_uri, port)

    port            += 1
    security_uri    =  "%s:%d" % (server_uri, port)

    # The following variables will be available in the caller's
    # file.
    return { "target_uri"   : target_uri,
             "common_uri"   : common_uri,
             "security_uri" : security_uri }

