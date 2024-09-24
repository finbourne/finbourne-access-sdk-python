# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import io
import json
import logging
import re
import ssl

from urllib.parse import urlencode, quote_plus
import urllib3

from finbourne_access.exceptions import ApiException, UnauthorizedException, ForbiddenException, NotFoundException, ServiceException, ApiValueError


logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.urllib3_response.headers

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.urllib3_response.headers.get(name, default)


class RESTClientObject(object):

    def __init__(self, configuration, pools_size=4, maxsize=None):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75  # noqa: E501
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680  # noqa: E501
        # maxsize is the number of requests to host that are allowed in parallel  # noqa: E501
        # Custom SSL certificates and client certificates: http://urllib3.readthedocs.io/en/latest/advanced-usage.html  # noqa: E501

        # cert_reqs
        if configuration.verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        addition_pool_args = {}
        if configuration.assert_hostname is not None:
            addition_pool_args['assert_hostname'] = configuration.assert_hostname  # noqa: E501

        if configuration.retries is not None:
            addition_pool_args['retries'] = configuration.retries

        if configuration.tls_server_name:
            addition_pool_args['server_hostname'] = configuration.tls_server_name


        if configuration.socket_options is not None:
            addition_pool_args['socket_options'] = configuration.socket_options

        if maxsize is None:
            if configuration.connection_pool_maxsize is not None:
                maxsize = configuration.connection_pool_maxsize
            else:
                maxsize = 4

        # https pool manager
        if configuration.proxy:
            self.pool_manager = urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=configuration.ssl_ca_cert,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=configuration.proxy,
                proxy_headers=configuration.proxy_headers,
                **addition_pool_args
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=configuration.ssl_ca_cert,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                **addition_pool_args
            )

        self.timeout = self.get_timeout(
            total=configuration.timeouts.total_timeout_ms / 1000.0,
            connect=configuration.timeouts.connect_timeout_ms / 1000.0,
            read=configuration.timeouts.read_timeout_ms / 1000.0,
        )

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None, opts=None):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT',
                          'PATCH', 'OPTIONS']

        if post_params and body:
            raise ApiValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}
        # url already contains the URL query string
        # so reset query_params to empty dict
        query_params = {}

        # _request_timeout param cannot be removed for backwards compatability
        # values from opts override values from _request_timeout
        # try to get values from opts first, then _request_timeout, then self.timeout, else set to None
        # timeout = _request_timeout or self.timeout
        timeout = None
        opts_total_timeout = opts.total_timeout_ms / 1000.0 if opts and opts.total_timeout_ms != None else None
        opts_connect_timeout = opts.connect_timeout_ms / 1000.0 if opts and opts.connect_timeout_ms != None else None
        opts_read_timeout = opts.read_timeout_ms / 1000.0 if opts and opts.read_timeout_ms != None else None
        if not _request_timeout:
            timeout = self.get_timeout(
                total=opts_total_timeout if opts_total_timeout != None
                    else self.timeout.total, 
                connect=opts_connect_timeout if opts_connect_timeout != None
                    else self.timeout._connect,
                read=opts_read_timeout if opts_read_timeout != None
                    else self.timeout._read)
        elif isinstance(_request_timeout, urllib3.Timeout):
            timeout = self.get_timeout(
                total=opts_total_timeout if opts_total_timeout != None
                    else _request_timeout.total if _request_timeout.total != None
                        else self.timeout.total, 
                connect=opts_connect_timeout if opts_connect_timeout != None
                    else _request_timeout._connect if _request_timeout._connect != None
                        else self.timeout._connect,
                read=opts_read_timeout if opts_read_timeout != None
                    else _request_timeout._read if _request_timeout._read != None
                        else self.timeout._read)
        elif isinstance(_request_timeout, (int, float)):
            timeout = self.get_timeout(
                total=opts_total_timeout if opts_total_timeout != None else _request_timeout, 
                connect=opts_connect_timeout if opts_connect_timeout != None else self.timeout._connect, 
                read=opts_read_timeout if opts_read_timeout != None else self.timeout._read)
        elif (isinstance(_request_timeout, tuple) and len(_request_timeout) == 2):
            timeout = self.get_timeout(
                total=opts_total_timeout if opts_total_timeout != None else self.timeout.total,
                connect=opts_connect_timeout if opts_connect_timeout != None else _request_timeout[0],
                read=opts_read_timeout if opts_read_timeout != None else _request_timeout[1])
        else:
            raise f"unexpected type '{type(_request_timeout)}' for _request_timeout"

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:

                # no content type provided or payload is json
                if not headers.get('Content-Type') or re.search('json', headers['Content-Type'], re.IGNORECASE):
                    request_body = None
                    if body is not None:
                        request_body = json.dumps(body)
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'application/x-www-form-urlencoded':  # noqa: E501
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=False,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers['Content-Type']
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=True,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is
                # provided in serialized form
                elif isinstance(body, str) or isinstance(body, bytes):
                    request_body = body
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(method, url,
                                              fields={},
                                              preload_content=_preload_content,
                                              timeout=timeout,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

            # log response body
            logger.debug("response body: %s", r.data)

        if not 200 <= r.status <= 299:
            if r.status == 401:
                raise UnauthorizedException(http_resp=r)

            if r.status == 403:
                raise ForbiddenException(http_resp=r)

            if r.status == 404:
                raise NotFoundException(http_resp=r)

            if 500 <= r.status <= 599:
                raise ServiceException(http_resp=r)

            raise ApiException(http_resp=r)

        return r

    def get_request(self, url, headers=None, query_params=None, _preload_content=True,
            _request_timeout=None, opts=None):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params,
                            opts=opts)

    def head_request(self, url, headers=None, query_params=None, _preload_content=True,
             _request_timeout=None, opts=None):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params,
                            opts=opts)

    def options_request(self, url, headers=None, query_params=None, post_params=None,
                body=None, _preload_content=True, _request_timeout=None, opts=None):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body,
                            opts=opts)

    def delete_request(self, url, headers=None, query_params=None, body=None,
               _preload_content=True, _request_timeout=None, opts=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body,
                            opts=opts)

    def post_request(self, url, headers=None, query_params=None, post_params=None,
             body=None, _preload_content=True, _request_timeout=None, opts=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body,
                            opts=opts)

    def put_request(self, url, headers=None, query_params=None, post_params=None,
            body=None, _preload_content=True, _request_timeout=None, opts=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body,
                            opts=opts)

    def patch_request(self, url, headers=None, query_params=None, post_params=None,
              body=None, _preload_content=True, _request_timeout=None, opts=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body,
                            opts=opts)

    def get_timeout(self, total: int, connect: int, read: int):
        # zero is used in the sdk config to explicitly set to infinity (and None is used to indicate the value has not been set)
        # but zero is not an allowed value for urllib3.Timeout so change any zeros to Nones
        return urllib3.Timeout(
            total=total if total != 0 else None,
            connect=connect if connect != 0 else None,
            read=read if read != 0 else None,
        )
