# Copyright (C) 2021-present CompatibL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from attrs import define
from cl.enterprise_python.mocks.storage.other_record_mock_key import OtherRecordMockKey
from cl.enterprise_python.mocks.storage.simple_record_mock_key import SimpleRecordMockKey


@define
class OtherRecordMock(OtherRecordMockKey):
    """Record that contains a foreign key."""

    foreign_key: SimpleRecordMockKey = None
    """Foreign key to SimpleRecordMock table."""