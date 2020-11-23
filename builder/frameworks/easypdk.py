# Copyright 2014-present PlatformIO <contact@platformio.org>
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

#
# Default flags for bare-metal programming (without any framework layers)
#

from os.path import join

from SCons.Script import DefaultEnvironment


env = DefaultEnvironment()
board_config = env.BoardConfig()
FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-easypdk")

env.Append(
    CFLAGS=[
        "-m%s" % board_config.get("build.cpu"),
        "--std-sdcc11",
        "--opt-code-size"
    ],
    CPPDEFINES=[
        "F_CPU=$BOARD_F_CPU",
        "TARGET_VDD_MV=$TARGET_VDD_MV",
        "$BOARD_MCU"
    ],
    LINKFLAGS=[
        "-m%s" % board_config.get("build.cpu"),
        "--out-fmt-ihx"
    ],
    CPPPATH=[
        join(FRAMEWORK_DIR, "includes")
    ]
)

