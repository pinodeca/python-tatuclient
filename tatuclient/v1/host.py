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


class HostController(V1Controller):

    def list(self, criterion=None, marker=None, limit=None):
        url = self.build_url('/hosts', criterion, marker, limit)
        return self._get(url, response_key='hosts')

    def get(self, host_id):
        return self._get('/hosts/%s' % (host_id))
