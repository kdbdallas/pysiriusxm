from __future__ import unicode_literals

import requests
#import json
import re
import logging

logger = logging.getLogger(__name__)


class API():

    def __init__(self, config):
        self.username = config.username
        self.password = config.password
        self.baseURL = config.baseURL
        self.authURL = config.authURL
        self.deviceMake = config.deviceMake
        self.oem = config.oem
        self.osVersion = config.osVersion
        self.platform = config.platform
        self.sxmAppVersion = config.sxmAppVersion
        self.carrier = config.carrier
        self.appRegion = config.appRegion
        self.deviceModel = config.deviceModel
        self.resultTemplate = config.resultTemplate
        self.deviceID = config.deviceID
        self.proxy = config.proxy
        self.proxy_username = config.proxy_username
        self.proxy_password = config.proxy_password

    def authenticate(self):
        pattern = re.compile('([0-9]+)$')
        sxmVersionPart = pattern.search(self.sxmAppVersion)

        headers = {'User-Agent': 'SXMLiveAudioPlayer/' + sxmVersionPart.group(),
                   'Accept-Encoding': 'gzip, deflate',
                   'Proxy-Connection': 'keep-alive',
                   'Connection': 'keep-alive',
                   'X-dynaTrace': 'MT2;5377067766218;17;K2US-mobile-ios;34;1;72'}

        payload = {
            "moduleList" : {
                "modules" : [
                    {
                        "moduleRequest" : {
                            "standardAuth" : {
                                "username" : self.username,
                                "password" : self.password
                            },
                            "deviceInfo" : {
                                "deviceMake" : self.deviceMake,
                                "oem" : self.oem,
                                "osVersion" : self.osVersion,
                                "platform" : self.platform,
                                "clientDeviceId" : self.deviceID,
                                "sxmAppVersion" : self.sxmAppVersion,
                                "mobileCarrier" : self.carrier,
                                "appRegion" : self.appRegion,
                                "deviceModel" : self.deviceModel
                            },
                            "resultTemplate" : self.resultTemplate
                        }
                    }
                ]
            }
        }

        request = requests.post(self.baseURL + self.authURL, json=payload, headers=headers)

        response = request.json()

        message = response["ModuleListResponse"]["messages"]["message"]
        print message
