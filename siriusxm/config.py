from __future__ import unicode_literals

class config(object):

    def __init__(self):
        # Defaults
        self.cache_location = b'tmp'
        self.settings_location = b'tmp'
        self.baseURL = "https://streamingapi.mountain.siriusxm.com"
        self.authURL = "/rest/v1/experience/modules/modify/authentication"
        self.deviceMake = "Apple"
        self.oem = "Apple"
        self.osVersion = "IOS_9.1"
        self.platform = "Phone"
        self.sxmAppVersion = "3.0.40.1446870927"
        self.carrier = "AT&T"
        self.appRegion = "US"
        self.deviceModel = "iPhone8,1"
        self.resultTemplate = "mobile"
        self.deviceID = None
        self.username = None
        self.password = None
        self.proxy = None
        self.proxy_username = None
        self.proxy_password = None

    @property
    def cache_location(self):
        """A location for siriusxm to cache files.

        Defaults to ``tmp`` in the current working directory.

        Must be a bytestring. Cannot be shared with other Sirius XM apps. Can
        only be used by one session at the time. Optimally, you should use a
        lock file or similar to ensure this.
        """
        return self.cache_location.encode('utf_8')

    @cache_location.setter
    def cache_location(self, value):
        self.cache_location = value

    def set_cache_size(self, size):
        """Set maximum size in MB for siriusxm's cache.

        If set to 0 (the default), up to 10% of the free disk space will be used."""
        pass

    def flush_caches(self):
        """Write all cached data to disk.

        siriusxm does this regularly and on logout, so you should never need
        to call this method yourself.
        """
        pass

    @property
    def baseURL(self):
        """The Base URL of the Sirius XM internet radio API to use"""
        return self.baseURL

    @baseURL.setter
    def baseURL(self, value):
        self.baseURL = value

    @property
    def authURL(self):
        """The Authentication URL (segment) of the Sirius XM internet radio API to use"""
        return self.authURL

    @authURL.setter
    def authURL(self, value):
        self.authURL = value

    @property
    def deviceMake(self):
        """The Device Make (values set by the API) to which you belong.
        'Apple' is the only supported device by this library currently."""
        return self.deviceMake

    @deviceMake.setter
    def deviceMake(self, value):
        self.deviceMake = value

    @property
    def oem(self):
        """The OEM (values set by the API) to which your device belongs.
        'Apple' is the only supported OEM by this library currently."""
        return self.oem

    @oem.setter
    def oem(self, value):
        self.oem = value

    @property
    def osVersion(self):
        """OS Version of your device (note: formatting set by API)."""
        return self.osVersion

    @osVersion.setter
    def osVersion(self, value):
        self.osVersion = value

    @property
    def platform(self):
        """The type of device you are running (types are set by the API).
        Currently the only supported value is 'Phone'"""
        return self.platform

    @platform.setter
    def platform(self, value):
        self.platform = value

    @property
    def sxmAppVersion(self):
        """The API version of Sirius XM we're using."""
        return self.sxmAppVersion

    @sxmAppVersion.setter
    def sxmAppVersion(self, value):
        """Must be in the format of X.X.X.X"""
        self.sxmAppVersion = value

    @property
    def carrier(self):
        """The Carrier of the device you are using (or pretending to be using).
        Currently the only supported value is 'AT&T'"""
        return self.carrier

    @carrier.setter
    def carrier(self, value):
        self.carrier = value

    @property
    def appRegion(self):
        """The Application Region.
        Currently the only supported value is 'US'"""
        return self.appRegion

    @appRegion.setter
    def appRegion(self, value):
        self.appRegion = value

    @property
    def deviceModel(self):
        """Your Device's Model.
        Currently the only supported value is 'iPhone8,1'"""
        return self.deviceModel

    @deviceModel.setter
    def deviceModel(self, value):
        self.deviceModel = value

    @property
    def resultTemplate(self):
        """Intended Result Template.
        Currently the only supported value is 'mobile'"""
        return self.resultTemplate

    @resultTemplate.setter
    def resultTemplate(self, value):
        self.resultTemplate = value

    @property
    def deviceID(self):
        """Device ID.
        How this value is generated in currently unknown but can be found by sniffing an iOS device using the Sirius XM app."""
        return self.deviceID

    @deviceID.setter
    def deviceID(self, value):
        self.deviceID = value

    @property
    def username(self):
        """Sirius XM Internet Radio Username."""
        return self.username

    @username.setter
    def username(self, value):
        self.username = value

    @property
    def password(self):
        """Sirius XM Internet Radio Password."""
        return self.password

    @password.setter
    def password(self, value):
        self.password = value

    @property
    def proxy(self):
        """URL to the proxy server that should be used.

        Defaults to :class:`None`.

        The format is protocol://host:port where protocol is
        http/https/socks4/socks5."""
        return self.proxy.encode('utf_8') or None

    @proxy.setter
    def proxy(self, value):
        self.proxy = value

    @property
    def proxy_username(self):
        """Username to authenticate with proxy server.

        Defaults to :class:`None`"""
        return self.proxy_username.encode('utf_8') or None

    @proxy_username.setter
    def proxy_username(self, value):
        self.proxy_username = value

    @property
    def proxy_password(self):
        """Password to authenticate with proxy server.

        Defaults to :class:`None`."""
        return self.proxy_password.encode('utf_8') or None

    @proxy_password.setter
    def proxy_password(self, value):
        self.proxy_password = value
