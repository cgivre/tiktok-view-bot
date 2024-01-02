import fade
import random
import urllib3
import threading
from pytermx import *
from requests import post
from urllib.parse import urlencode

urllib3.disable_warnings()

def Print(text: str):
    print(
        f"            {Color.BRIGHT_BLUE}->{Color.BRIGHT_PURPLE} {text} {Color.BRIGHT_BLUE}<- {Color.RESET}")


def Input(text: str):
    print(
        f"\r            {Color.BRIGHT_BLUE}->{Color.BRIGHT_PURPLE} {text} {Color.BRIGHT_BLUE}-> {Color.RESET}", end="")
    return input()

def get_al(params: str, payload: str = None, sectoken: str = ""):
    """
        'Difficulties are things that show a person what they are.' - Epictetus
    """

def send(item_id: int, device_id: int, install_id: int, cdid, openudid):
    for _ in range(2):
        req_apis = [
            "api15-core-useast1a.tiktokv.com",
            "api16-core-useast1a.tiktokv.com",
            "api19-core-useast1a.tiktokv.com",
            "api22-core-c-alisg.tiktokv.com",
            "api22-normal-c-useast1a.tiktokv.com",
            "api31-core-useast1a.tiktokv.com",
        ]

        version = random.choice(
                    [247, 312, 322, 357, 358, 415, 422, 444, 466]
        )

        device = random.choice(
                    ["SM-G9900", "sm-g950f", "SM-A136U1", "SM-M225FV", "SM-E426B", "SM-M526BR", "SM-M326B", "SM-A528B", "SM-F711B", "SM-F926B", "SM-A037G", "SM-A225F", "SM-M325FV", "SM-A226B", "SM-M426B", "SM-A525F"]
        )

        params = urlencode({
            "iid"                  : f"{install_id}",
            "device_id"            : f"{device_id}",
            "ac"                   : "5g",
            "channel"              : "googleplay",
            "aid"                  : "1233",
            "app_name"             : "musical_ly",
            "version_code"         : "250304",
            "version_name"         : "25.3.4",
            "device_platform"      : "android",
            "os"                   : "android",
            "ab_version"           : "25.3.4",
            "ssmix"                : "a",
            "device_type"          : "SM-A405FN",
            "device_brand"         : "samsung",
            "language"             : "zh-Hant",
            "os_api"               : 28,
            "os_version"           : 9,
            "openudid"             : openudid,
            "manifest_version_code": 2022503040,
            "resolution"           : "1080*2110",
            "dpi"                  : 240,
            "update_version_code"  : 2022503040,
            "_rticket"             : 1704110807522,
            "is_pad"               : 0,
            "app_type"             : "normal",
            "sys_region"           : "TW",
            "mcc_mnc"              : 45402,
            "timezone_name"        : "Asia/Taipei",
            "carrier_region_v2"    : 454,
            "app_language"         : "zh-Hant",
            "carrier_region"       : "HK",
            "ac2"                  : "wifi",
            "uoo"                  : 0,
            "op_region"            : "HK",
            "timezone_offset"      : 28800,
            "build_number"         : "25.3.4",
            "host_abi"             : "arm64-v8a",
            "locale"               : "zh-Hant-TW",
            "region"               : "TW",
            "ts"                   : 1704110807,
            "cdid"                 : cdid
        })

        payload = urlencode({
            "pre_item_playtime"       : "",
            "user_algo_refresh_status": False,
            "first_install_time"      : 0,
            "enter_from"              : "homepage_hot",
            "item_id"                 : f"{item_id}",
            "is_ad"                   : 0,
            "follow_status"           : 0,
            "session_id"              : 1704110807,
            "sync_origin"             : False,
            "follower_status"         : 0,
            "impr_order"              : 0,
            "action_time"             : 1704110807,
            "tab_type"                : 0,
            "item_distribute_source"  : "for_you_page",
            "pre_hot_sentence"        : "",
            "play_delta"              : 1,
            "aweme_type"              : 0,
            "order"                   : 0,
            "pre_item_id"             : ""
        })

        xargus, xladon = get_al(
            params  = params,
            payload = payload,
        )

        tiktok_res = post(
            url     = (
                "https://"
                    + random.choice(req_apis)
                    + "/aweme/v1/aweme/stats/?"
                    + params
            ),
            data    = payload,
            headers = {
                "User-Agent"  : f"com.ss.android.ugc.trill/{version} (Linux; U; Android 11; fr_FR; {device}; Build/RP1A.200720.012; Cronet/58.0.2991.0)",
                "X-Argus"     : xargus,
                "X-Ladon"     : xladon,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            }
        )

        if tiktok_res.text == "":
            pass
        else:
            Print(tiktok_res.text)

banner = """
       __               
      / /_  ______  ___ 
 __  / / / / / __ \/ _ \\
/ /_/ / /_/ / / / /  __/
\____/\__,_/_/ /_/\___/ 
                        
"""

if __name__ == "__main__":
    print(fade.purpleblue(Center.center_x(banner)))

    video_id = int(Input("Video Id> "))

    with open("devices.txt", "r") as f:
        devices = f.read().splitlines()

    while True:
        device = random.choice(devices)

        if threading.active_count() < 100:
            did, iid, cdid, openudid = device.split(":")

            threading.Thread(
                target = send,
                args   = [
                    video_id,
                    did,
                    iid,
                    cdid,
                    openudid
                ]
            ).start()
