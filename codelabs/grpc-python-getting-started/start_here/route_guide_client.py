# Copyright 2024 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide client."""

import logging

import grpc
import route_guide_pb2
import route_guide_pb2_grpc

def format_point(point):
    # not delegating in point.__str__ because it is an empty string when its
    # values are zero. In addition, it puts a newline between the fields.
    return "latitude: %d, longitude: %d" % (point.latitude, point.longitude)

def run():
    """
    Codelab Hint: Logic for your gRPC Client will be added here.
    Steps include:
     1. Create a connection to the gRPC server using grpc.insecure_channel()
     2. Call service methods on the client to interact with the server.
    """

if __name__ == "__main__":
    logging.basicConfig()
    run()
