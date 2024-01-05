import time
import fade
import random
import threading
from pytermx import *
from requests import post
from urllib.parse import urlencode 

def Print(text: str):
    print(
        f"            {Color.BRIGHT_BLUE}->{Color.BRIGHT_PURPLE} {text} {Color.BRIGHT_BLUE}<- {Color.RESET}")


def Input(text: str):
    print(
        f"\r            {Color.BRIGHT_BLUE}->{Color.BRIGHT_PURPLE} {text} {Color.BRIGHT_BLUE}-> {Color.RESET}", end="")
    return input()

def get_ts():
    return time.time()

def send(item_id: int, device_id: int, install_id: int, cdid, openudid):
    for _ in range(2):
        actual_ts = get_ts()

        req_apis = [
            "api15-core-useast1a.tiktokv.com",
            "api16-core-useast1a.tiktokv.com",
            "api19-core-useast1a.tiktokv.com",
            "api22-core-c-alisg.tiktokv.com",
            "api22-normal-c-useast1a.tiktokv.com",
            "api31-core-useast1a.tiktokv.com",
        ]

        params = urlencode({
            "iid"                  : f"{install_id}",
            "device_id"            : f"{device_id}",
            "ac"                   : "wifi",
            "channel"              : "googleplay",
            "aid"                  : "1233",
            "app_name"             : "musical_ly",
            "version_code"         : "320503",
            "version_name"         : "32.5.3",
            "device_platform"      : "android",
            "os"                   : "android",
            "ab_version"           : "32.5.3",
            "ssmix"                : "a",
            "device_type"          : "SM-A405FN",
            "device_brand"         : "samsung",
            "language"             : "es-ES",
            "os_api"               : 720,
            "os_version"           : 9,
            "openudid"             : openudid,
            "manifest_version_code": 2023205030,
            "resolution"           : "1080*2110",
            "dpi"                  : 240,
            "update_version_code"  : 2023205030,
            "_rticket"             : actual_ts,
            "is_pad"               : 0,
            "app_type"             : "normal",
            "sys_region"           : "ES",
            "mcc_mnc"              : 45402,
            "timezone_name"        : "Europe/Madrid",
            "carrier_region_v2"    : 454,
            "app_language"         : "es-ES",
            "carrier_region"       : "ES",
            "ac2"                  : "wifi5g",
            "uoo"                  : 0,
            "op_region"            : "ES",
            "timezone_offset"      : 28800,
            "build_number"         : "32.5.3",
            "host_abi"             : "arm64-v8a",
            "locale"               : "es-ES",
            "region"               : "ES",
            "ts"                   : actual_ts,
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
            "session_id"              : actual_ts,
            "sync_origin"             : False,
            "follower_status"         : 0,
            "impr_order"              : 0,
            "action_time"             : actual_ts,
            "tab_type"                : 0,
            "item_distribute_source"  : "for_you_page",
            "pre_hot_sentence"        : "",
            "play_delta"              : 1,
            "aweme_type"              : 0,
            "order"                   : 0,
            "pre_item_id"             : ""
        })

        alg = get_al(
            params=params,
            payload=payload,
            sec_device_id=device_id
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
                "User-Agent"  : f"com.ss.android.ugc.trill/320503 (Linux; U; Android 11; fr_FR; SM-A405FN; Build/RP1A.200720.012; Cronet/58.0.2991.0)",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            } | alg,
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
