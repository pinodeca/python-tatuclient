#   Copyright 2018 Huawei, Inc. All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

from tatuclient.v1.base import V1Controller
from tatuclient.v1 import utils as v1_utils


class UserCertController(V1Controller):

    def create(self, user_id, auth_id, pub_key):
        data = {
            'user_id': user_id,
            'auth_id': auth_id,
            'pub_key': pub_key,
        }
        return self._post('/noauth/usercerts', data=data)

    def list(self, criterion=None, marker=None, limit=None):
        url = self.build_url('/noauth/usercerts', criterion, marker, limit)
        return self._get(url, response_key='users')

    def get(self, serial):
        return self._get('/noauth/usercerts/%s' % serial)

    def revoke(self, auth_id, serial):
        url = '/noauth/revokeduserkeys/%s' % auth_id
        data = { 'serial': serial }
        return self._post(url, data=data)